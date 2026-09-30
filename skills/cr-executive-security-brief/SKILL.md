---
name: cr-executive-security-brief
description: "Summarize evidence-backed risks for decision-makers."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Leadership, Reporting]
---
# Executive Security Brief Skill

Convert a supplied security assessment into a leadership brief organized around decisions and business impact. This skill explains evidence and uncertainty; it does not invent financial estimates, trend improvements, or risk acceptance.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Prepare an executive update from this assessment.
- Explain the decisions needed from leadership.
- Summarize the security posture without overstating the data.

Primary audience: CISOs, security leaders, and executive stakeholders.

## Prerequisites

- The assessment, evidence references, and reporting period.
- The intended audience, business context, and decisions being requested.
- Comparable prior-period metrics and financial assumptions only if supplied.
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

1. Identify the audience, reporting period, and concrete decisions leadership needs to make.
2. Select the decision-relevant risks and explain their business implications without adding unsupported affected populations or loss estimates.
3. Separate current exposure, observed incidents, delivery progress, and unresolved evidence gaps.
4. Use metrics only with a stated definition, denominator, scope, and observation period.
5. Present a trend only when the prior and current measures are comparable; otherwise explain the change in measurement.
6. State decision options, accountable owners, dependencies, and the consequences of deferring a decision.
7. Keep uncertainty visible in the main brief and retain supporting evidence in the appendix.
8. Use the template to deliver an executive summary and a traceable decision register.

## Pitfalls

- A smaller finding count may reflect reduced coverage rather than improvement.
- A technical severity label is not a financial-loss estimate.
- A roadmap item is not a completed risk reduction.
- A recommendation does not mean leadership accepted the residual risk.

## Verification

Before delivering the report, check all of the following:

- [ ] Every headline claim is traceable to the underlying assessment.
- [ ] Metrics include their denominator and time/scope definition.
- [ ] Financial or trend claims use supplied assumptions and comparable evidence.
- [ ] Each requested decision names an owner or states that ownership is unresolved.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
