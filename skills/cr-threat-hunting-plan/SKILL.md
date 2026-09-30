---
name: cr-threat-hunting-plan
description: "Design hypothesis-led, read-only threat hunts."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, ThreatHunting, Planning]
---
# Threat Hunting Plan Skill

Turn a threat question into a bounded hunting plan using the telemetry and schema the user actually has. This skill plans an investigation; it does not launch scans, execute payloads, or run queries automatically.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Create a hunt plan for this threat hypothesis.
- Turn this intelligence into bounded evidence requests.
- Define what would confirm or reject this hunt hypothesis.

Primary audience: Threat hunters and senior SOC analysts.

## Prerequisites

- A testable hypothesis and the systems or population in scope.
- Available telemetry schemas, retention windows, and query constraints.
- An approved investigation window and any cost, privacy, or volume limits.
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

1. Write the hypothesis as an observable proposition, not a conclusion that the environment is compromised.
2. Define the population, time range, business context, and relevant exclusion criteria.
3. List the observations that would support, weaken, or leave the hypothesis unresolved.
4. Map each observation to an available source and actual field schema. Mark missing fields as blockers.
5. Draft a read-only query plan. If exact syntax cannot be grounded in supplied schema and documentation, label the logic as pseudocode rather than executable syntax.
6. Specify row/time limits, expected volume, privacy constraints, and a stop condition before proposing execution.
7. Include baseline comparisons and legitimate alternatives to avoid treating rare activity as malicious by definition.
8. Deliver the hunt plan with evidence-capture requirements and the point at which escalation would be justified.

## Pitfalls

- An intelligence report describes an external pattern, not local compromise.
- No matches are inconclusive when the relevant telemetry was not retained.
- Rare activity is not automatically malicious.
- An unbounded query can exceed cost, privacy, or operational limits.

## Verification

Before delivering the report, check all of the following:

- [ ] The hypothesis can be tested with the identified observations.
- [ ] Every query stage has a source, time bound, and stop condition.
- [ ] Unavailable schemas produce a stated blocker or pseudocode, not invented fields.
- [ ] The plan includes disconfirming evidence and legitimate alternatives.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
