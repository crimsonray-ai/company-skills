#!/usr/bin/env python3
"""Local file helpers. Edit content directly; review and publish with Git."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile

import yaml

if __package__:
    from .validate_library import ROOT, check_name, load_manifest, require, validate, validate_manifest
else:
    from validate_library import ROOT, check_name, load_manifest, require, validate, validate_manifest


def save_manifest(root: Path, manifest: dict) -> None:
    """Replace the manifest only after a complete write on the same filesystem."""
    fd, name = tempfile.mkstemp(prefix=".manifest-", suffix=".tmp", dir=root)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            stream.write(json.dumps(manifest, indent=2) + "\n")
        os.replace(name, root / "company-skills.json")
    finally:
        Path(name).unlink(missing_ok=True)


def manage(args: argparse.Namespace, root: Path = ROOT) -> None:
    validate(root)
    manifest = load_manifest(root)
    collections = manifest["collections"]
    names = {p.name for p in (root / "skills").iterdir()}
    if args.command == "list":
        print(manifest["name"])
        for name, members in collections.items():
            default = " (default)" if name in manifest["defaults"] else ""
            print(f"  {name}{default}: {', '.join(members)}")
        return

    check_name(args.name)
    target = root / "skills" / args.name
    if args.command == "add-skill":
        require(args.name not in names, "Skill already exists; edit its SKILL.md directly")
        require(args.collection in collections, "Choose an existing collection")
        description = args.description
        require(bool(description.strip()) and len(description) <= 60
                and not any(ord(c) < 32 for c in description), "Description must be one line, 1–60 characters")
        collections[args.collection].append(args.name)
        names.add(args.name)
    elif args.command == "remove-skill":
        require(args.yes, "Removal deletes the whole skill folder; review git diff, then pass --yes")
        require(args.name in names, "Skill does not exist")
        names.remove(args.name)
        for members in collections.values():
            if args.name in members:
                members.remove(args.name)
    elif args.command == "add-collection":
        require(args.name not in collections, "Collection already exists; edit membership in company-skills.json")
        collections[args.name] = args.skills
    elif args.command == "remove-collection":
        require(args.yes, "Removal changes the available collections; pass --yes to confirm")
        require(args.name in collections, "Collection does not exist")
        del collections[args.name]
        manifest["defaults"] = [name for name in manifest["defaults"] if name != args.name]

    # Refuse empty collections/defaults and orphaned skills before touching disk.
    validate_manifest(manifest, names)
    if args.command == "add-skill":
        target.mkdir()
        try:
            metadata = yaml.safe_dump({"name": args.name, "description": args.description}, sort_keys=False)
            (target / "SKILL.md").write_text(
                f"---\n{metadata}---\n\n# {args.name}\n\n"
                "**Policy: extend.** Follow the active agent's access and approval rules.\n\n"
                "Draft skill: not ready for use. Ask the maintainer to write its procedure and expected result.\n",
                encoding="utf-8",
            )
            save_manifest(root, manifest)
        except BaseException:
            shutil.rmtree(target)
            raise
    elif args.command == "remove-skill":
        # Keep a recoverable copy until the manifest write succeeds.
        backup = Path(tempfile.mkdtemp(prefix=".removed-skill-", dir=root))
        saved = backup / args.name
        try:
            target.rename(saved)
            try:
                save_manifest(root, manifest)
            except BaseException:
                saved.rename(target)
                raise
            shutil.rmtree(saved)
        finally:
            # If restore/cleanup failed, leave the backup rather than delete data.
            if not any(backup.iterdir()):
                backup.rmdir()
            else:
                print(f"Recovery copy retained at {backup}", file=sys.stderr)
    else:
        save_manifest(root, manifest)
    print("Updated local files. Review git diff and finish any draft instructions before publishing.")


def parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(description=__doc__)
    commands = cli.add_subparsers(dest="command", required=True)
    commands.add_parser("list", help="List collections and their skills")
    add = commands.add_parser("add-skill", help="Create a draft skill in an existing collection")
    add.add_argument("name")
    add.add_argument("--collection", required=True)
    add.add_argument("--description", required=True)
    add = commands.add_parser("add-collection", help="Group existing skills")
    add.add_argument("name")
    add.add_argument("skills", nargs="+")
    for command in ("remove-skill", "remove-collection"):
        remove = commands.add_parser(command, help="Remove after explicit confirmation")
        remove.add_argument("name")
        remove.add_argument("--yes", action="store_true")
    return cli


if __name__ == "__main__":
    try:
        manage(parser().parse_args())
    except (ValueError, TypeError, OSError) as exc:
        print(f"No successful update: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
