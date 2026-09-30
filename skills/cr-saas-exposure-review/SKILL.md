---
name: cr-saas-exposure-review
description: "Assess risky SaaS access and sharing settings."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, SaaS, Exposure]
---
# SaaS Exposure Review Skill

Review supplied SaaS configuration and access evidence for unnecessary exposure. This skill assesses sharing, privileges, and application grants; it does not change tenant settings or assume access from a product edition alone.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review external sharing in this SaaS workspace.
- Assess risky app grants and administrator access.
- Explain the exposure in these collaboration-platform exports.

Primary audience: SaaS-security, IT, and collaboration-platform owners.

## Prerequisites

- Workspace/tenant scope and relevant sharing, privilege, application-grant, and audit exports.
- Capture dates, license/edition constraints, and known collection omissions.
- Data classification and the company’s sharing or collaboration policy.
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

1. Map the supplied workspaces, populations, and settings to the intended review scope.
2. Classify each sharing mechanism: named recipient, organization-wide, external guest, or anonymous/public access.
3. Assess the effective audience using inheritance, membership, and applicable restrictions where evidence is available.
4. Review administrator roles and application grants separately from document-sharing settings.
5. Compare authentication and audit settings with the company’s stated policy and observed evidence, noting edition limitations.
6. Identify affected content or workflows without inferring data sensitivity from titles alone.
7. Produce a prioritized review register with evidence gaps, owner decisions, and proposed bounded verification.
8. Separate recommended setting changes from changes actually performed.

## Pitfalls

- An organization-wide link is not automatically an anonymous internet link.
- A guest invitation is not proof that the guest accessed the resource.
- Available controls differ by edition and tenant configuration.
- Removing an application grant can interrupt a business workflow.

## Verification

Before delivering the report, check all of the following:

- [ ] Each exposure claim identifies its sharing/access mechanism.
- [ ] Effective audience and data sensitivity are supported or marked unknown.
- [ ] Application-grant findings include scope and workflow ownership.
- [ ] Proposed changes identify affected users and a validation method.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
