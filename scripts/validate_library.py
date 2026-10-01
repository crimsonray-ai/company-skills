#!/usr/bin/env python3
"""Check the Company Skills file/manifest contract; no network or execution."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unicodedata

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(10)), *(f"lpt{i}" for i in range(10))}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def check_name(name: str) -> None:
    require(isinstance(name, str) and bool(NAME.fullmatch(name)) and name not in RESERVED,
            f"Invalid name: {name!r}; use 1–64 lowercase letters, numbers or hyphens, not device names")


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate manifest key: {key}")
        result[key] = value
    return result


def load_manifest(root: Path) -> dict:
    path = root / "company-skills.json"
    require(path.is_file() and not path.is_symlink(), "company-skills.json must be a regular file")
    try:
        return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    except (OSError, ValueError) as exc:
        raise ValidationError(f"Cannot read company-skills.json: {exc}") from exc


def validate_manifest(manifest: dict, names: set[str]) -> None:
    require(isinstance(manifest, dict), "Manifest must be an object")
    require(set(manifest) <= {"version", "name", "collections", "defaults"}, "Unsupported manifest field")
    require(type(manifest.get("version")) is int and manifest["version"] == 1, "Manifest format version must be 1")
    title = manifest.get("name")
    require(isinstance(title, str) and bool(title.strip()) and len(title) <= 120
            and not any(ord(c) < 32 for c in title), "Library name must be 1–120 printable characters")
    require(1 <= len(names) <= 64, "Library must contain 1–64 skills")
    collections = manifest.get("collections")
    if not isinstance(collections, dict):
        raise ValidationError("Collections must be an object")
    require(1 <= len(collections) <= 32, "Provide 1–32 collections")
    covered = set()
    for name, members in collections.items():
        check_name(name)
        require(isinstance(members, list) and 1 <= len(members) <= 64, f"Collection must not be empty: {name}")
        require(all(isinstance(member, str) and member in names for member in members), f"Unknown skill in collection: {name}")
        require(len(set(members)) == len(members), f"Duplicate member in collection: {name}")
        covered.update(members)
    require(covered == names, "Every skill must belong to a collection")
    defaults = manifest.get("defaults")
    if not isinstance(defaults, list):
        raise ValidationError("Defaults must be a list")
    require(bool(defaults) and all(isinstance(name, str) and name in collections for name in defaults),
            "Defaults must select existing collections")
    require(len(set(defaults)) == len(defaults), "Duplicate default collection")


def validate(root: Path = ROOT) -> dict:
    manifest = load_manifest(root)
    skills_root = root / "skills"
    require(skills_root.is_dir() and not skills_root.is_symlink(), "skills/ must be a real directory")
    keys = set()
    files = []
    total = 0
    for path in sorted(skills_root.rglob("*")):
        rel = path.relative_to(skills_root)
        require(not path.is_symlink(), f"Symlink not allowed: {rel}")
        require(len(rel.as_posix()) <= 240, f"Path is too long: {rel}")
        for part in rel.parts:
            require(not part.startswith(".") and not part.endswith((".", " ")), f"Hidden/non-portable path: {rel}")
            require(part.split(".")[0].lower() not in RESERVED, f"Reserved path: {rel}")
            require(not any(ord(c) < 32 or c in '\\:*?"<>|' for c in part), f"Non-portable path: {rel}")
        key = unicodedata.normalize("NFC", rel.as_posix()).casefold()
        require(key not in keys, f"Case/Unicode-equivalent path collision: {rel}")
        keys.add(key)
        if path.is_dir():
            continue
        require(path.is_file(), f"Only regular files are allowed: {rel}")
        require(len(rel.parts) >= 2, f"Files belong inside a skill folder: {rel}")
        size = path.stat().st_size
        require(size <= 2 * 1024 * 1024, f"File exceeds 2 MiB: {rel}")
        if path.name == "SKILL.md":
            require(len(rel.parts) == 2, f"Nested skill not allowed: {rel}")
            require(size <= 64 * 1024, f"SKILL.md exceeds 64 KiB: {rel}")
        total += size
        files.append(path)
    require(len(files) <= 512 and total <= 20 * 1024 * 1024, "Library exceeds download limits")
    names = set()
    for folder in sorted(skills_root.iterdir()):
        require(folder.is_dir(), f"Unexpected file at skills root: {folder.name}")
        check_name(folder.name)
        skill_file = folder / "SKILL.md"
        require(skill_file.is_file(), f"Missing SKILL.md: {folder.name}")
        content = skill_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        require(bool(lines) and lines[0] == "---", f"Missing YAML frontmatter: {folder.name}")
        require("---" in lines[1:], f"Unclosed YAML frontmatter: {folder.name}")
        end = lines.index("---", 1)
        try:
            metadata = yaml.safe_load("\n".join(lines[1:end]))
        except yaml.YAMLError:
            raise ValidationError(f"Invalid YAML frontmatter: {folder.name}") from None
        require(isinstance(metadata, dict), f"Frontmatter must be a mapping: {folder.name}")
        require(metadata.get("name") == folder.name, f"Frontmatter name must match folder: {folder.name}")
        description = metadata.get("description")
        require(isinstance(description, str) and bool(description.strip()) and len(description) <= 60
                and not any(ord(c) < 32 for c in description), f"Description must be one line, 1–60 characters: {folder.name}")
        require(bool("\n".join(lines[end + 1:]).strip()), f"Skill instructions are empty: {folder.name}")
        names.add(folder.name)
    validate_manifest(manifest, names)
    return {"name": manifest["name"], "skills": len(names), "collections": len(manifest["collections"]),
            "files": len(files), "bytes": total}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), indent=2))
    except (ValueError, TypeError, OSError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
