---
name: cr-third-party-risk-review
description: "Assess supplier risk and evidence gaps."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, ThirdPartyRisk, Assurance]
---
# Third-Party Risk Review Skill

Assess a supplier against a defined service scope and the company’s risk criteria using supplied evidence. This skill supports a review decision; it does not certify the supplier or treat a questionnaire answer as independently verified.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review this supplier’s security evidence.
- Identify the follow-up questions that matter for this vendor.
- Prepare a risk decision for a proposed service.

Primary audience: Third-party-risk, procurement, and security-assurance teams.

## Prerequisites

- The service being purchased, data flows, access, and business criticality.
- Supplier questionnaires, reports, contracts, and operational evidence with dates and scope.
- The company’s acceptance criteria and the decision owner.
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

1. Define the purchased service and its access/data boundary; avoid generalizing from the supplier’s entire brand.
2. Inventory the evidence and classify it as supplier assertion, policy, independent assessment, contract commitment, or operational observation.
3. Check dates, assessed service scope, exceptions, and report limitations before using an assurance claim.
4. Map the evidence to the company’s relevant risk criteria, separating contractual promises from observed operation.
5. Identify material gaps and write focused questions whose answers could change the decision.
6. Assess concentration, dependency, exit, and incident-notification considerations using the provided service context.
7. Present decision options, residual risk, proposed conditions, and the accountable acceptance owner.
8. Leave final commercial, legal, and risk acceptance decisions with their designated owners.

## Pitfalls

- A report covering one service may not cover the purchased product.
- A supplier assertion and an independent assessment are not equivalent evidence.
- An expired document may support historical claims but not current operation.
- A numerical score is misleading without an approved scoring policy and complete inputs.

## Verification

Before delivering the report, check all of the following:

- [ ] The assessed service and evidence scope match or their differences are stated.
- [ ] Each risk finding identifies its evidence type and limitations.
- [ ] Follow-up questions are tied to a decision, not a generic questionnaire dump.
- [ ] Residual-risk acceptance has a named role or an explicit ownership gap.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
