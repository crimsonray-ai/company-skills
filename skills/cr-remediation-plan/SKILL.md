---
name: cr-remediation-plan
description: "Build approval-ready, testable remediation plans."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Remediation, Planning]
---
# Remediation Plan Skill

Turn an evidence-backed finding into a scoped remediation proposal with ownership and verification. This skill prepares plan content; it does not grant execution authority, perform changes, or treat a proposed rollback as already tested.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Create a remediation plan for these findings.
- Prepare a safe change proposal with rollback criteria.
- Turn this security review into an actionable backlog.

Primary audience: Security engineers, incident owners, and change approvers.

## Prerequisites

- The finding and supporting evidence, including affected entity identifiers.
- Desired outcome, business constraints, maintenance windows, and accountable owners.
- Available validation and rollback information.
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

1. Define the security outcome and identify the exact affected entities; separate confirmed targets from candidates needing confirmation.
2. Explain the root cause supported by the evidence and the reason the proposed treatment addresses it.
3. List dependencies, prerequisite evidence, approvals, and operational constraints before sequencing work.
4. Break the proposal into bounded steps with an accountable owner and an observable completion criterion.
5. State expected impact and failure modes for each change, including affected users or workloads.
6. Define pre-change checks, post-change verification, and the evidence needed to claim the finding is resolved.
7. Specify rollback triggers and the known rollback procedure; mark any untested recovery assumption.
8. Submit the plan through the existing human approval process. Keep proposed actions, approved actions, and completed actions distinct.

## Pitfalls

- A plan is not an execution grant.
- A resource name without a stable identifier can target the wrong object.
- A completed change is not proof that the underlying risk was removed.
- Rollback may be unavailable or require a separate decision; do not invent it.

## Verification

Before delivering the report, check all of the following:

- [ ] Every change has a concrete target, owner, and success criterion.
- [ ] Prerequisites and approvals are explicit.
- [ ] Verification tests the security outcome, not just completion of a command.
- [ ] Rollback assumptions and residual risk are visible.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
