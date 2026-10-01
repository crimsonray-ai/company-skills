# Author a skill

A skill is a folder containing `SKILL.md` and any files it needs. Start with a real task; extend an existing skill when that is enough.

## Create a draft

From the repository root, with the maintainer environment activated:

```sh
python3 scripts/manage.py add-skill summarize-notes --collection example --description "Summarize supplied meeting notes."
```

This creates `skills/summarize-notes/SKILL.md` and adds it to the selected collection. It refuses to overwrite an existing skill. Replace the draft body with clear instructions, for example:

```markdown
---
name: summarize-notes
description: Summarize supplied meeting notes.
---

# Summarize notes

**Policy: extend.** Follow the active agent's access and approval rules.

## When to use

When the user supplies meeting notes and requests a summary.

## Procedure

1. Read the supplied notes. Ask for them if none were provided.
2. Summarize the decisions and action items. Preserve stated owners and dates.
3. Mark missing owners or dates as unspecified; do not invent them.

## Expected result

A concise summary followed by action items with their stated owners and dates.
```

No fixed set of headings, author metadata, or per-skill version number is required. The folder name and frontmatter `name` must match; the description must be one line of at most 60 characters. Use a distinctive name if it might collide with an installed skill.

## Add files only when useful

Put a script in `skills/<name>/scripts/`, a template in `templates/`, or supporting notes in `references/`. Link to files relative to the skill directory. Do not rely on repository-root files: they are not installed with the skill.

Scripts should have clear inputs and outputs, avoid dependencies where practical, and never run during installation. Describe any required access; a skill does not grant it. Test the script and reference the actual output, not a claimed success.

See [`hello-world`](../skills/hello-world/SKILL.md) for a runnable example.

## Check the change

```sh
python3 scripts/validate_library.py
python3 -m unittest discover -s tests -v
git diff
```

The validator checks structure, frontmatter, collection references, and installer file limits. It does not prove that instructions are correct, detect every secret, or replace Crimson Ray's installation security review. Try the actual skill before publishing it.
