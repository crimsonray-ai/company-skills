---
name: cr-detection-gap-analysis
description: "Map threat scenarios to detection coverage gaps."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Detection, Telemetry]
---
# Detection Gap Analysis Skill

Compare a defined threat scenario with supplied telemetry and detection evidence. This skill produces a coverage assessment and validation plan; it does not deploy rules or equate an enabled rule with proven detection.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Can our current detections observe this scenario?
- Find the telemetry gaps behind these detection gaps.
- Prepare a detection-validation backlog.

Primary audience: Detection engineers and SOC content owners.

## Prerequisites

- A bounded threat scenario or observed behavior set.
- Detection logic/version, enablement state, and validation evidence where available.
- Telemetry schema, collection scope, retention, and sample events.
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

1. Decompose the scenario into observable behaviors without assuming a particular vendor schema.
2. Identify the data source, fields, time coverage, and entity context required for each behavior.
3. Map supplied detection logic to those behaviors, distinguishing directly covered behavior from indirect indicators.
4. Check field availability, parser assumptions, filter exclusions, collection freshness, and retention constraints.
5. Classify coverage as validated, configured but unvalidated, unsupported by current telemetry, or unknown.
6. Attach external framework technique identifiers only when the supplied behavior and framework version justify the mapping.
7. Design a safe validation case with expected positive and negative observations. Use synthetic or explicitly authorized evidence, not a live attack.
8. Prioritize the backlog by decision impact and dependency: missing telemetry may precede detection tuning.

## Pitfalls

- A rule name or technique tag is not proof of coverage.
- An enabled rule with missing fields may never match.
- A positive test alone does not show acceptable false-positive behavior.
- Coverage percentages need an explicit denominator and evidence for every counted item.

## Verification

Before delivering the report, check all of the following:

- [ ] Each behavior maps to required telemetry and available evidence.
- [ ] Validated coverage cites an actual test or observation.
- [ ] Unknown coverage is not counted as absent or complete.
- [ ] Each proposed validation has expected results and a safe scope.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
