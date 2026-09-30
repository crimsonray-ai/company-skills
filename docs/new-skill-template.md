# New skill authoring template

Copy the content below into `skills/cr-your-workflow/SKILL.md`, then replace every `REPLACE_ME` value. Add the referenced support files and collection membership before validation. This document is an authoring aid, not an installed skill.

````markdown
---
name: REPLACE_ME
description: "REPLACE_ME with one sentence of at most 60 characters."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Evidence]
---

# REPLACE_ME Skill

REPLACE_ME with what the workflow produces and what it does not do.
State whether it needs software beyond the existing harness.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- REPLACE_ME with a concrete user request.

## Prerequisites

- REPLACE_ME with the minimum evidence, scope, and policy inputs.
- State missing inputs as gaps rather than assuming values.

## How to Run

1. Confirm the prerequisites.
2. If `skill_view` is loaded, open `templates/report.md` and `references/checklist.md` with this skill's name and the relative `file_path`. Otherwise request their text.
3. If `read_file` is loaded, use it for supplied artifacts; otherwise work from pasted evidence.
4. Follow the Procedure and deliver the template's information using the platform's rendering rules.

## Quick Reference

| Item | Location |
| --- | --- |
| Deliverable | `templates/report.md` |
| Interpretation guide | `references/checklist.md` |

## Procedure

1. REPLACE_ME with a concrete analysis step.
2. REPLACE_ME with an evidence-based decision criterion.
3. REPLACE_ME with a bounded handoff or completion condition.

## Pitfalls

- REPLACE_ME with a domain-specific interpretation trap.

## Verification

- [ ] REPLACE_ME with an observable result check.
- [ ] Every substantive conclusion has an evidence reference or an explicit uncertainty label.
````

The folder name and frontmatter name must match. Do not publish this template unchanged. See [CONTRIBUTING.md](../CONTRIBUTING.md) for review and release requirements.
