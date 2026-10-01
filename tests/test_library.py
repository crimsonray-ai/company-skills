import contextlib
import io
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

from scripts.manage import manage, parser
from scripts.validate_library import ROOT, ValidationError, load_manifest, validate


class LibraryTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        shutil.copy2(ROOT / "company-skills.json", self.root)
        shutil.copytree(ROOT / "skills", self.root / "skills")
        self.skill = self.root / "skills/hello-world/SKILL.md"

    def run_helper(self, *argv):
        with contextlib.redirect_stdout(io.StringIO()):
            manage(parser().parse_args(argv), self.root)

    def snapshot(self):
        return {p.relative_to(self.root): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def test_cli_lifecycle_and_hello_world(self):
        shutil.copytree(ROOT / "scripts", self.root / "scripts", ignore=shutil.ignore_patterns("__pycache__"))
        def cli(script, *args):
            return subprocess.run([sys.executable, str(self.root / script), *args], cwd=self.root,
                                  text=True, capture_output=True, check=True).stdout
        self.assertEqual(cli("skills/hello-world/scripts/hello.py"), "Hello, world!\n")
        self.assertIn("hello-world", cli("scripts/manage.py", "list"))
        cli("scripts/manage.py", "add-skill", "notes", "--collection", "example", "--description", "Summarize notes.")
        cli("scripts/manage.py", "add-collection", "writing", "notes")
        self.assertIn("writing", cli("scripts/manage.py", "list"))
        cli("scripts/validate_library.py")
        cli("scripts/manage.py", "remove-collection", "writing", "--yes")
        cli("scripts/manage.py", "remove-skill", "notes", "--yes")
        self.assertEqual(load_manifest(self.root), load_manifest(ROOT))
        self.assertFalse((self.root / "skills/notes").exists())
        self.assertEqual(validate(self.root), validate(ROOT))

    def test_invalid_operations_leave_files_untouched(self):
        before = self.snapshot()
        for args in [
            ("add-skill", "../escape", "--collection", "example", "--description", "Example."),
            ("add-skill", "con", "--collection", "example", "--description", "Example."),
            ("add-skill", "hello-world", "--collection", "example", "--description", "Example."),
            ("add-skill", "notes", "--collection", "missing", "--description", "Example."),
            ("add-skill", "notes", "--collection", "example", "--description", "x" * 61),
            ("add-collection", "broken", "missing"),
            ("add-collection", "broken", "hello-world", "hello-world"),
            ("remove-skill", "hello-world"),
            ("remove-skill", "hello-world", "--yes"),
            ("remove-collection", "example", "--yes"),
        ]:
            with self.subTest(args=args), self.assertRaises(ValidationError):
                self.run_helper(*args)
            self.assertEqual(before, self.snapshot())

    def test_removal_cannot_empty_a_collection_or_orphan_a_skill(self):
        self.run_helper("add-skill", "notes", "--collection", "example", "--description", "Summarize notes.")
        self.run_helper("add-collection", "writing", "notes")
        before = self.snapshot()
        with self.assertRaisesRegex(ValidationError, "empty"):
            self.run_helper("remove-skill", "notes", "--yes")
        self.assertEqual(before, self.snapshot())
        manifest = load_manifest(self.root)
        manifest["collections"]["example"].remove("notes")
        (self.root / "company-skills.json").write_text(json.dumps(manifest), encoding="utf-8")
        before = self.snapshot()
        with self.assertRaisesRegex(ValidationError, "belong"):
            self.run_helper("remove-collection", "writing", "--yes")
        self.assertEqual(before, self.snapshot())

    def test_manifest_write_failure_restores_files(self):
        before = self.snapshot()
        with patch("scripts.manage.os.replace", side_effect=OSError("write failed")):
            with self.assertRaises(OSError):
                self.run_helper("add-skill", "notes", "--collection", "example", "--description", "Notes.")
        self.assertEqual(before, self.snapshot())
        self.run_helper("add-skill", "notes", "--collection", "example", "--description", "Notes.")
        before = self.snapshot()
        with patch("scripts.manage.os.replace", side_effect=OSError("write failed")):
            with self.assertRaises(OSError):
                self.run_helper("remove-skill", "notes", "--yes")
        self.assertEqual(before, self.snapshot())
        self.assertFalse(list(self.root.glob(".removed-skill-*")))
        self.assertFalse(list(self.root.glob(".manifest-*")))

    def test_invalid_manifests_are_rejected(self):
        original = load_manifest(self.root)
        for change in [
            {"version": True}, {"name": "bad\nname"}, {"collections": {"example": ["missing"]}},
            {"collections": {"example": []}}, {"defaults": ["missing"]}, {"defaults": [[]]},
        ]:
            with self.subTest(change=change):
                (self.root / "company-skills.json").write_text(json.dumps(original | change), encoding="utf-8")
                with self.assertRaises(ValidationError):
                    validate(self.root)
        (self.root / "company-skills.json").write_text('{"version":1,"version":1}', encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "Duplicate"):
            validate(self.root)

    def test_metadata_and_paths_are_checked(self):
        original = self.skill.read_text(encoding="utf-8")
        for content in [original.replace("name: hello-world", "name: wrong"),
                        original.replace("Print a friendly hello-world greeting.", "x" * 61),
                        "---\nname: [\n---\nInstructions"]:
            self.skill.write_text(content, encoding="utf-8")
            with self.assertRaises(ValidationError):
                validate(self.root)
        self.skill.write_text(original, encoding="utf-8")
        hidden = self.skill.parent / ".env"
        hidden.write_text("", encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "Hidden"):
            validate(self.root)
        hidden.unlink()
        nested = self.skill.parent / "scripts/SKILL.md"
        nested.write_text(original, encoding="utf-8")
        with self.assertRaisesRegex(ValidationError, "Nested"):
            validate(self.root)
        nested.unlink()
        link = self.skill.parent / "link.md"
        try:
            link.symlink_to(self.skill)
        except OSError:
            self.skipTest("Symlinks unavailable on this platform")
        with self.assertRaisesRegex(ValidationError, "Symlink"):
            validate(self.root)

    def test_unicode_path_collisions_are_rejected(self):
        folder = self.skill.parent
        (folder / "café.md").write_text("one", encoding="utf-8")
        (folder / "cafe\u0301.md").write_text("two", encoding="utf-8")
        if len(list(folder.glob("caf*.md"))) != 2:
            self.skipTest("Filesystem normalizes equivalent names")
        with self.assertRaisesRegex(ValidationError, "collision"):
            validate(self.root)


if __name__ == "__main__":
    unittest.main()
