---
name: cr-compliance-evidence-map
description: "Map evidence to controls without claiming certification."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Compliance, Evidence]
---
# Compliance Evidence Map Skill

Map supplied evidence to an explicitly identified control set and assessment period. This skill supports audit preparation; it does not provide certification, a legal opinion, or an auditor’s final conclusion.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Map these artifacts to our control requirements.
- Show which audit evidence is missing or stale.
- Separate policy evidence from evidence of operation.

Primary audience: GRC, control owners, and audit-readiness teams.

## Prerequisites

- The exact framework/control text, version, assessment scope, and period.
- Evidence artifacts with ownership, source references, and observation dates.
- The organization’s applicability decisions and assessment criteria, if available.
- Supplied evidence must be within the user's authorized scope. Missing inputs remain explicit gaps.
- Live connectors are optional, separately configured capabilities; installing this skill does not provide them.

## How to Run

1. Load this skill, then establish the prerequisites with the user.
2. If `skill_view` is loaded, use it with this skill's name and `file_path` to open `templates/report.md` and `references/checklist.md`. Otherwise request the supporting text from the user.
3. If `read_file` is loaded, use it for the supplied local artifacts. Otherwise work from pasted evidence or request an export.
4. Follow the Procedure and deliver the template's information using the current platform's rendering rules.
5. If the user asks for a saved report and `write_file` is loaded, use it for an agreed output location outside this installed skill. Otherwise return the report in the conversation.

## Quick Reference

| Item | Location or meaning |
| --- | --- |
| Deliverable | `templates/report.md` |
| Interpretation guide | `references/checklist.md` |
| Evidence reference | A supplied record ID, or a local label mapped to a source file and location |
| Missing input | State what is missing and how it limits the conclusion |
| Operational handoff | Proposed actions remain distinct from execution evidence |

## Procedure

1. Confirm the exact control identifiers and version from the supplied control set. Do not invent identifiers from a framework name.
2. Record applicability and assessment-period boundaries; unresolved applicability remains a question for the control owner.
3. Classify evidence as control design, implementation, operation, or exception handling.
4. Map each artifact to the specific requirement it supports and explain the relationship rather than matching keywords alone.
5. Check scope, period, ownership, sample limitations, and whether the artifact establishes the claimed operation.
6. Classify the mapping as supported, partially supported, missing, conflicting, or not applicable with an evidenced rationale.
7. Create focused evidence requests for the remaining gaps, with owner and the criterion that would satisfy the request.
8. Present the mapping as preparation for accountable review, preserving assessment limits and unresolved questions.

## Pitfalls

- A policy document does not prove that the control operated.
- One sample does not establish population-wide effectiveness.
- Framework versions and assessment periods must not be mixed silently.
- Not applicable requires a rationale; it is not a synonym for missing evidence.

## Verification

Before delivering the report, check all of the following:

- [ ] Every control identifier comes from the supplied versioned control set.
- [ ] Each mapping explains what the evidence supports and what it does not.
- [ ] Evidence freshness and sample limitations are recorded.
- [ ] No preparation status is presented as certification or a final audit opinion.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
