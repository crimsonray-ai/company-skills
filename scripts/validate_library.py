#!/usr/bin/env python3
"""Validate the publishable skill-library contract; no network or execution."""
from __future__ import annotations

import json
from pathlib import Path
import re
import sys
import unicodedata

import yaml

ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r"[a-z0-9][a-z0-9-]{0,63}\Z")
SECTIONS = (
    "When to Use", "Prerequisites", "How to Run", "Quick Reference",
    "Procedure", "Pitfalls", "Verification",
)
RESERVED = {"con", "prn", "aux", "nul", *(f"com{i}" for i in range(10)), *(f"lpt{i}" for i in range(10))}


class ValidationError(ValueError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate manifest key: {key}")
        result[key] = value
    return result


def validate(root: Path = ROOT) -> dict:
    manifest = json.loads((root / "company-skills.json").read_text(encoding="utf-8"), object_pairs_hook=unique_object)
    require(isinstance(manifest, dict), "Manifest must be an object")
    require(set(manifest) <= {"version", "name", "collections", "defaults"}, "Unsupported manifest field")
    require(type(manifest.get("version")) is int and manifest["version"] == 1, "Manifest format version must be 1")
    title = manifest.get("name")
    require(isinstance(title, str) and 0 < len(title.strip()) <= 120, "Manifest name must be 1–120 characters")
    skills_root = root / "skills"
    require(skills_root.is_dir() and not skills_root.is_symlink(), "skills/ must be a real directory")
    files = []
    keys = set()
    total = 0
    for path in sorted(skills_root.rglob("*")):
        rel = path.relative_to(skills_root)
        require(not path.is_symlink(), f"Symlink not allowed: {rel}")
        if path.is_dir():
            continue
        require(path.is_file(), f"Only regular files are allowed: {rel}")
        require(len(rel.parts) >= 2, f"Files belong inside a skill folder: {rel}")
        require(len(rel.as_posix()) <= 240, f"Path is too long: {rel}")
        for part in rel.parts:
            require(not part.startswith(".") and not part.endswith((".", " ")), f"Hidden/non-portable path: {rel}")
            require(part.split(".")[0].lower() not in RESERVED, f"Reserved path: {rel}")
            require(not any(ord(c) < 32 or c in '\\:*?"<>|' for c in part), f"Non-portable path: {rel}")
        key = unicodedata.normalize("NFC", rel.as_posix()).casefold()
        require(key not in keys, f"Case/Unicode-equivalent file collision: {rel}")
        keys.add(key)
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
        require(bool(NAME.fullmatch(folder.name)) and folder.name not in RESERVED, f"Invalid skill folder: {folder.name}")
        skill_file = folder / "SKILL.md"
        require(skill_file.is_file(), f"Missing SKILL.md: {folder.name}")
        content = skill_file.read_text(encoding="utf-8")
        require(content.startswith("---\n"), f"Missing YAML frontmatter: {folder.name}")
        parts = content.split("---\n", 2)
        require(len(parts) == 3, f"Unclosed YAML frontmatter: {folder.name}")
        try:
            metadata = yaml.safe_load(parts[1])
        except yaml.YAMLError:
            raise ValidationError(f"Invalid YAML frontmatter: {folder.name}") from None
        require(isinstance(metadata, dict), f"Frontmatter must be a mapping: {folder.name}")
        require(metadata.get("name") == folder.name, f"Frontmatter name must match folder: {folder.name}")
        description = metadata.get("description")
        require(isinstance(description, str) and 1 <= len(description) <= 60 and description.endswith(".") and "\n" not in description,
                f"Description must be one line, <=60 characters, ending in a period: {folder.name}")
        require(bool(re.fullmatch(r"\d+\.\d+\.\d+", str(metadata.get("version", "")))), f"Missing semantic skill version: {folder.name}")
        require(isinstance(metadata.get("author"), str) and bool(metadata["author"].strip()), f"Missing author: {folder.name}")
        body = parts[2]
        require("REPLACE_ME" not in content, f"Unfinished authoring placeholder: {folder.name}")
        offsets = [body.find(f"## {section}\n") for section in SECTIONS]
        require(all(index >= 0 for index in offsets) and offsets == sorted(offsets), f"Missing or misordered skill sections: {folder.name}")
        require("**Policy: extend.**" in body, f"Declare the inherited-policy relationship: {folder.name}")
        for relative in set(re.findall(r"`((?:templates|references|scripts|assets)/[^`]+)`", body)):
            require(".." not in Path(relative).parts and not Path(relative).is_absolute(), f"Unsafe support reference: {folder.name}")
            require((folder / relative).is_file(), f"Missing support file: {folder.name}/{relative}")
        names.add(folder.name)
    require(1 <= len(names) <= 64, "Library must contain 1–64 skills")
    collections = manifest.get("collections")
    require(isinstance(collections, dict) and 1 <= len(collections) <= 32, "Provide 1–32 collections")
    covered = set()
    for name, members in collections.items():
        require(bool(NAME.fullmatch(name)) and name not in RESERVED, f"Invalid collection name: {name}")
        require(isinstance(members, list) and bool(members), f"Empty or invalid collection: {name}")
        require(all(isinstance(member, str) and member in names for member in members), f"Unknown skill in collection: {name}")
        require(len(set(members)) == len(members), f"Duplicate member in collection: {name}")
        covered.update(members)
    require(covered == names, "Every skill must be reachable through a collection")
    if "all" in collections:
        require(set(collections["all"]) == names, "The all collection must cover every skill")
    defaults = manifest.get("defaults")
    require(isinstance(defaults, list) and bool(defaults) and all(isinstance(name, str) and name in collections for name in defaults),
            "Defaults must select existing collections")
    return {"name": title, "skills": len(names), "collections": len(collections), "files": len(files), "bytes": total,
            "default_skills": sorted({name for group in defaults for name in collections[group]})}


if __name__ == "__main__":
    try:
        print(json.dumps(validate(), indent=2))
    except (ValidationError, ValueError, TypeError, OSError, yaml.YAMLError) as exc:
        print(f"Library validation failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from None
