# Maintaining and creating Company Skills

This repository contains skill content, not the Crimson Ray application. Changes should improve a concrete security workflow without adding credentials, broadening permissions, or changing the agent's core behavior.

For the company and employee setup process, see [the handbook](docs/HANDBOOK.md).

## 1. Decide whether a new skill is needed

Start with a real user question and a distinct deliverable. Extend an existing skill when the input, procedure, and output are substantially the same. Do not create a routing skill whose only job is to point to other skills.

Write down:

- Who will use it?
- What evidence must they provide?
- What decision or artifact should result?
- What will the skill explicitly not do?
- What would demonstrate that the result is correct?

## 2. Create a complete skill folder

Use the [new-skill template](docs/new-skill-template.md) as a starting point:

```text
skills/cr-your-workflow/
├── SKILL.md
├── templates/
│   └── report.md
└── references/
    └── checklist.md
```

Keep the folder name and frontmatter `name` identical. Use lowercase letters, numbers, and hyphens; avoid spaces, reserved Windows device names, and names longer than 64 characters. The `cr-` prefix reduces collisions, but the installer still checks for existing skill names.

The repository template contains `REPLACE_ME` placeholders. Replace them before submitting a change. It is outside `skills/` so it is not itself installed.

## 3. Write frontmatter that routes correctly

```yaml
---
name: cr-your-workflow
description: "Explain the capability in one short sentence."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Evidence]
---
```

- The description must be one sentence, at most **60 characters**, ending in a period. It is the routing hint users and the model see—not a marketing paragraph.
- Generated starter skills use the fixed author value `Hermes`, following the harness's generated-skill convention. Do not derive an author from a machine username or credential. Credit human contributors when their identity has been explicitly provided and approved; preserve authorship in Git history and reviews.
- Use semantic skill versions, such as `0.1.1`, for content revisions. Do not confuse these with the manifest format number or the application version.
- These starter skills are portable Markdown workflows and omit `platforms`. If a future skill uses genuinely platform-specific scripts, declare the supported platforms and test them. Prefer a portable implementation first.
- Keep metadata non-secret. Do not include API keys, tokens, account exports, or customer evidence.

## 4. Keep the body operational

Use this section order:

1. Human-readable title and a short introduction.
2. `## When to Use`
3. `## Prerequisites`
4. `## How to Run`
5. `## Quick Reference`
6. `## Procedure`
7. `## Pitfalls`
8. `## Verification`

Declare **Policy: extend**. The skill inherits the active harness's approval, access, and rendering rules; it must not silently replace them.

Good instructions identify concrete inputs, decision criteria, uncertainty, and completion evidence. Avoid undefined assurances such as “ensure everything is secure.” Do not invent vendor APIs, tool names, query fields, control IDs, completed tests, or evidence.

### Tools and scripts

- Name native tools only in an availability-gated instruction: for example, “If `read_file` is loaded, use it for the supplied artifact; otherwise request pasted evidence.”
- Use `skill_view` for supporting files when that tool is available, with the skill name and the relative `file_path`.
- Do not present shell utilities as substitutes for native tools in `SKILL.md` prose.
- Do not add installation hooks or scripts that run on import or installation.
- If a workflow genuinely needs a helper script, keep it in `scripts/` inside that skill, frame execution through an available `terminal` tool, document inputs and limits, and add runnable tests. A helper must not acquire permissions merely because the skill was installed.
- Keep provider authentication and business-system access separate from skill distribution.

## 5. Add supporting material

The output template should name the information the analyst must deliver, including evidence references and limitations. It should not contain pre-filled real findings.

The interpretation checklist should add useful domain definitions, evidence expectations, or a clearly labelled synthetic example. Avoid copying the Procedure word for word.

Keep every referenced file inside the skill folder. Symlinks, hidden files, nested `SKILL.md` files, and case/Unicode-equivalent paths are not supported. Do not depend on a shared root-level reference file: the installer distributes selected skill folders, not the entire repository.

## 6. Make it discoverable

Add the exact skill name to the appropriate collection(s) in `company-skills.json`, and keep the `all` collection complete. Update the README catalog and the handbook when the user-facing workflow changes.

Collections may overlap. Do not rename an existing collection ID casually: installed profiles remember that ID. Prefer adding a replacement and announcing a migration.

## 7. Validate before review

Install the maintainer-only dependency, then use the repository runner:

```bash
python3 -m pip install -r requirements-dev.txt
bash scripts/run_tests.sh
```

On Windows, the equivalent validation commands are documented in the README. Checks cover metadata, collection membership, file limits, support references, and representative invalid inputs. They do not prove the reasoning quality of a skill.

Before publishing, also:

1. Preview the candidate branch or commit using **Company Skills** in a clean local profile.
2. Inspect the existing Crimson Ray security scanner's result. Fix the cause of a blocked skill; do not weaken the scanner to ship it.
3. Install the selected collection and confirm the skill appears in discovery and slash commands.
4. Test with sanitized, representative evidence and with missing or contradictory evidence.
5. Check that the output cites its sources, preserves uncertainty, and does not claim unperformed actions.
6. Ask the domain owner to review the skill's usefulness and boundaries.

## 8. Review and publish

Use a pull request that explains the user need, changed skill IDs, collection changes, validation performed, and migration impact. Have a maintainer or domain owner review the content. Automated checks are not a substitute for that review.

After approval:

1. Merge the reviewed change.
2. Publish a new repository release tag. Never move an existing release tag to different content.
3. Include release notes listing added, changed, renamed, and removed skills.
4. Regenerate the handbook PDF from `docs/HANDBOOK.md` when needed and attach it to the release, rather than committing a generated PDF.
5. Tell users which ref and collections to select. Users pinned to an older tag must deliberately change their ref and preview again.

## Retirement and customization

- Removing a skill from one collection does not remove it when another selected collection still includes it.
- Removing the folder and its memberships causes a later update preview to propose removal of the managed copy. Locally modified copies block replacement/removal.
- A renamed skill is a new identity. Users must review its enabled state; old per-skill preferences do not automatically transfer.
- For a personal variant, create a separately named skill or propose an upstream change. Do not edit a managed copy and expect future updates to overwrite it safely.
- Never commit completed customer reports, working investigation evidence, `.env`, `auth.json`, or credentials. Keep them in the user's authorized workspace.
