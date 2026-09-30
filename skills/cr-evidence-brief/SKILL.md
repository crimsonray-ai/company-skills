---
name: cr-evidence-brief
description: "Turn source records into a cited security brief."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, Evidence, Reporting]
---
# Evidence Brief Skill

Turn a bounded evidence set into a decision-ready account of what is known, disputed, and missing. This skill synthesizes records; it does not collect credentials, make changes, or turn unsupported assertions into findings.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Summarize the evidence for this security question.
- Explain what these findings actually establish.
- Prepare a handoff without overstating certainty.

Primary audience: Security analysts, solution engineers, and service leads.

## Prerequisites

- The decision or question the reader must answer.
- Source records or exports with identifiers, capture times, and scope.
- The intended audience and any confidentiality restrictions.
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

1. Define the question, reporting period, covered systems, and excluded systems before interpreting records.
2. Build the evidence register in the template. Reuse supplied record identifiers; give unlabelled records local references that map back to their file and location.
3. Separate direct observations, source-owner assertions, analytical inferences, and unanswered questions.
4. Group evidence by claim rather than by vendor. For each claim, record the strongest supporting evidence and any counter-evidence.
5. Compare source scope and freshness before resolving contradictions. Preserve a conflict if the available records cannot resolve it.
6. Explain the decision impact of each uncertainty. Identify the smallest additional observation that would change the conclusion.
7. Produce a handoff using the report template, retaining the evidence register and explicit exclusions.

## Pitfalls

- A successful connection is not proof that a source covers the entire environment.
- Two exports derived from the same original record are not independent corroboration.
- An empty result does not establish absence when filters, permissions, or retention are unknown.
- A summary must not strengthen the source claim: suspected is not confirmed.

## Verification

Before delivering the report, check all of the following:

- [ ] Every substantive claim resolves to an evidence reference or is labelled as an inference.
- [ ] The covered scope and excluded scope are explicit.
- [ ] Contradictions and missing information are visible beside their decision impact.
- [ ] The handoff distinguishes a recommended next step from a completed action.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
