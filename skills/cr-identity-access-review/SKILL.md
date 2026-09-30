---
name: cr-identity-access-review
description: "Review privileged access and dormant identities."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Identity, AccessReview]
---
# Identity Access Review Skill

Review human and workload access using supplied identity, entitlement, and activity records. This skill prepares review decisions; it does not revoke permissions, disable accounts, or equate inactivity with compromise.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review privileged identities in this scope.
- Find access assignments that need owner confirmation.
- Assess dormant accounts without breaking service identities.

Primary audience: IAM teams, security operations, and access-review owners.

## Prerequisites

- Identity and entitlement records with stable identifiers and account/workspace scope.
- Activity windows, ownership data, and human-versus-workload classifications.
- Approved access policy and inactivity thresholds, if available.
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

1. Separate human, workload, service, emergency, and external identities; record unknown classifications rather than guessing.
2. Join identities and entitlements with immutable identifiers and explicit tenant boundaries.
3. Distinguish assigned roles from effective permissions, including group membership, delegation, and resource scope when evidenced.
4. Assess privilege against documented business purpose and owner approval, not against role-name similarity across systems.
5. Interpret inactivity only within the available activity window and the supplied policy threshold. Identify telemetry limitations.
6. Review authentication-control evidence separately from access grants; a configured policy and an observed sign-in are different evidence types.
7. Classify each review item as retain, investigate, or propose change, with owner, rationale, and operational dependency.
8. Prepare proposed removals or privilege reductions for the organization’s existing approval process, including a rollback and validation question.

## Pitfalls

- Identical display names can identify different accounts.
- A service identity can be critical despite having no interactive sign-ins.
- A disabled user may still have separately managed application grants.
- An assigned role does not always describe the full effective permission set.

## Verification

Before delivering the report, check all of the following:

- [ ] Identity joins preserve tenant and immutable identifiers.
- [ ] Inactivity conclusions state the observation window and threshold.
- [ ] Workload dependencies and emergency accounts are considered before proposing removal.
- [ ] Each proposed change is distinguishable from a completed action.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
