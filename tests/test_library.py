import json
from pathlib import Path
import shutil
import tempfile
import unittest

from scripts.validate_library import ROOT, ValidationError, validate


class LibraryContractTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / 'company-skills.json', self.root / 'company-skills.json')
        shutil.copytree(ROOT / 'skills', self.root / 'skills')
        self.skill = next((self.root / 'skills').glob('*/SKILL.md'))

    def manifest(self):
        return json.loads((self.root / 'company-skills.json').read_text(encoding='utf-8'))

    def save_manifest(self, value):
        (self.root / 'company-skills.json').write_text(json.dumps(value), encoding='utf-8')

    def test_repository_is_installable_and_defaults_are_a_subset(self):
        report = validate(self.root)
        names = {p.parent.name for p in (self.root / 'skills').glob('*/SKILL.md')}
        self.assertTrue(set(report['default_skills']) <= names)
        self.assertEqual(report['skills'], len(names))
        self.assertGreater(report['files'], report['skills'])

    def test_unknown_collection_member_is_rejected(self):
        manifest = self.manifest()
        manifest['collections']['essentials'].append('does-not-exist')
        self.save_manifest(manifest)
        with self.assertRaisesRegex(ValidationError, 'Unknown skill'):
            validate(self.root)

    def test_default_collection_must_exist(self):
        manifest = self.manifest()
        manifest['defaults'] = ['does-not-exist']
        self.save_manifest(manifest)
        with self.assertRaisesRegex(ValidationError, 'Defaults'):
            validate(self.root)

    def test_long_description_is_rejected(self):
        content = self.skill.read_text(encoding='utf-8')
        start = content.index('description:')
        end = content.index('\n', start)
        self.skill.write_text(content[:start] + 'description: "' + 'x' * 61 + '."' + content[end:], encoding='utf-8')
        with self.assertRaisesRegex(ValidationError, 'Description'):
            validate(self.root)

    def test_missing_support_file_is_rejected(self):
        (self.skill.parent / 'templates/report.md').unlink()
        with self.assertRaisesRegex(ValidationError, 'Missing support'):
            validate(self.root)

    def test_name_must_match_folder(self):
        content = self.skill.read_text(encoding='utf-8').replace(f'name: {self.skill.parent.name}', 'name: another-skill', 1)
        self.skill.write_text(content, encoding='utf-8')
        with self.assertRaisesRegex(ValidationError, 'name must match'):
            validate(self.root)

    def test_hidden_file_is_rejected(self):
        (self.skill.parent / '.env').write_text('EXAMPLE_ONLY=not-a-credential', encoding='utf-8')
        with self.assertRaisesRegex(ValidationError, 'Hidden'):
            validate(self.root)

    def test_unicode_collision_is_rejected(self):
        refs = self.skill.parent / 'references'
        (refs / 'café.md').write_text('first', encoding='utf-8')
        (refs / 'cafe\u0301.md').write_text('second', encoding='utf-8')
        if len(list(refs.glob('caf*.md'))) != 2:
            self.skipTest('Filesystem normalizes equivalent names before validation')
        with self.assertRaisesRegex(ValidationError, 'collision'):
            validate(self.root)

    def test_symlinks_are_rejected(self):
        link = self.skill.parent / 'references/link.md'
        try:
            link.symlink_to(self.skill)
        except OSError:
            self.skipTest('This account cannot create symlinks')
        with self.assertRaisesRegex(ValidationError, 'Symlink'):
            validate(self.root)


if __name__ == '__main__':
    unittest.main()
