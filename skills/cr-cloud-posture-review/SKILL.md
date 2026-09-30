---
name: cr-cloud-posture-review
description: "Review cloud risks and control gaps from evidence."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Cloud, Posture]
---
# Cloud Posture Review Skill

Review a bounded cloud inventory and configuration evidence set for risk and control gaps. This skill produces a posture assessment; it does not enumerate unapproved accounts or change cloud resources.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review the security posture of this cloud scope.
- Explain the highest-impact issues in these cloud exports.
- Distinguish configuration findings from proven exposure.

Primary audience: Cloud-security and platform engineering teams.

## Prerequisites

- The exact accounts, subscriptions, projects, regions, and resource classes in scope.
- Inventory/configuration exports with capture times and collection coverage.
- Business ownership, environment labels, and applicable control requirements.
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

1. Define the cloud boundaries and compare the supplied inventory with the intended scope. Mark missing regions or resource classes.
2. Review identity permissions, external network paths, data access, logging, and recovery evidence as separate control areas.
3. For each candidate issue, assemble the relevant configuration chain. For reachability, include routes and boundary controls rather than a single permissive rule.
4. Distinguish intended configuration from observed effective state. Record source disagreement or collection age.
5. Assess the plausible impact using affected data, workload purpose, and owner context, without inferring sensitivity from a resource name alone.
6. Identify control dependencies and exceptions that require an owner decision.
7. Produce an evidence-linked risk register with proposed validation and remediation options.
8. Explain what the review cannot conclude because of absent scope, permissions, or telemetry.

## Pitfalls

- One security-group rule is not a complete reachability assessment.
- Encryption at rest does not establish appropriate access control.
- A control supported by the provider may not be enabled on the resource.
- A clean export is not proof that unqueried regions are clean.

## Verification

Before delivering the report, check all of the following:

- [ ] Every issue names an in-scope resource identifier and source reference.
- [ ] Exposure claims include the relevant access-path evidence or are labelled unverified.
- [ ] Missing coverage is separated from confirmed control failures.
- [ ] Proposed remediation includes an owner and a validation criterion.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
