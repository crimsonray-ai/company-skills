---
name: cr-incident-timeline
description: "Build a source-linked incident timeline."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, IncidentResponse, Timeline]
---
# Incident Timeline Skill

Reconstruct a timeline from supplied event records while preserving time uncertainty and source provenance. This skill orders observations; it does not manufacture causal links or infer events from gaps in logging.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Build a timeline from these incident records.
- Reconcile these conflicting timestamps.
- Show which events are observed and which links are hypotheses.

Primary audience: Incident responders and forensic analysts.

## Prerequisites

- Event records with original timestamps and source identifiers.
- Known timezones, clock offsets, and ingestion timestamps where available.
- The incident window and relevant entity identifiers.
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

1. Inventory the sources, their collection windows, timestamp fields, precision, and known clock behavior.
2. Retain each original timestamp. Convert to a common timezone only when its timezone or offset is known.
3. Separate event time, ingestion time, and analyst observation time. Place unknown-timezone events in a distinct uncertain-time section.
4. Deduplicate repeated observations using source record identifiers or an explained composite key, without discarding independent corroboration.
5. Order events within the precision the sources support. Use an interval or an explicit ordering uncertainty when clocks disagree.
6. Attach an evidence reference to each timeline row and identify which entity relationship supports any cross-source join.
7. Describe causal hypotheses separately from the chronology. Explain which additional evidence would test each hypothesis.
8. Mark coverage gaps and the collection request needed to close them; finish with a handoff that preserves unresolved ordering questions.

## Pitfalls

- A log’s ingestion timestamp may be hours later than the underlying event.
- Sorting timestamps does not prove causation.
- Removing duplicate-looking records can discard independent evidence.
- Timezone guesses create a false chronology.

## Verification

Before delivering the report, check all of the following:

- [ ] Every event retains its original timestamp and reference.
- [ ] Normalized times have a known timezone or offset.
- [ ] Unknown ordering and collection gaps are explicitly represented.
- [ ] Causal statements are separately labelled and evidence-linked.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
