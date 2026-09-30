---
name: cr-asset-coverage-review
description: "Find inventory and security-monitoring coverage gaps."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Assets, Coverage]
---
# Asset Coverage Review Skill

Compare supplied asset inventories with security-control and telemetry records to identify coverage gaps. This skill reconciles observations; it does not assume that an absent record proves an asset or control is absent.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Which assets are missing security-monitoring coverage?
- Reconcile these inventories and explain the mismatches.
- Assess how complete this security data set is.

Primary audience: Security operations, exposure-management, and platform owners.

## Prerequisites

- The intended asset population and independent inventory sources, where available.
- Control/agent enrollment, telemetry, and last-seen records with identifiers and collection windows.
- Asset lifecycle, ownership, and freshness criteria.
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

1. Define the intended population and the scope/collection limitations of each source before comparing counts.
2. Normalize asset types and join records using stable identifiers plus account/tenant boundaries.
3. Treat ambiguous joins as unresolved rather than merging similar hostnames or recycled addresses.
4. Separate inventory presence, control enrollment, recent telemetry, and demonstrated control operation.
5. Apply supplied freshness thresholds and lifecycle context, including ephemeral or intentionally retired assets.
6. Classify mismatches as potential inventory gaps, enrollment gaps, stale telemetry, ambiguous identity, or unassessed coverage.
7. Calculate coverage only for a defined, evidenced denominator, preserving excluded or unknown populations.
8. Prepare owner-specific reconciliation tasks and the evidence needed to confirm each gap.

## Pitfalls

- Hostnames and IP addresses can be reused.
- An enrolled agent is not necessarily producing current telemetry.
- Ephemeral and serverless assets may need different coverage criteria.
- A percentage without a trustworthy denominator is not coverage evidence.

## Verification

Before delivering the report, check all of the following:

- [ ] The denominator and exclusions are explicit for each reported metric.
- [ ] Joins use stable identifiers or are labelled ambiguous.
- [ ] Enrollment, freshness, and operating evidence remain separate.
- [ ] Gap-remediation tasks identify the confirmation evidence and owner.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
