---
name: cr-secure-change-review
description: "Review proposed changes for security regressions."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, ApplicationSecurity, ChangeReview]
---
# Secure Change Review Skill

Review a supplied code, infrastructure, or policy change against its stated intent and trust boundaries. This skill produces review findings; it does not modify the repository, approve a deployment, or claim tests ran without results.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review this proposed change for security regressions.
- Assess this infrastructure or access-policy diff.
- Identify the tests needed before this change is approved.

Primary audience: Application-security and platform change reviewers.

## Prerequisites

- The change description, diff, and enough surrounding context to understand the affected path.
- Trust boundaries, deployment scope, and relevant security requirements.
- Test results or validation evidence, if available.
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

1. State the intended behavior change and identify the concrete entry points, callers, and affected deployment scope.
2. Trace the relevant input data, authorization decisions, and response handling in the supplied code.
3. Compare old and new behavior at each changed trust boundary, including failure and fallback paths.
4. Identify reproducible security findings with a location, triggering condition, plausible impact, and evidence.
5. Separate confirmed defects from questions that require missing code or environment context.
6. Review test evidence for the affected behavior; distinguish executed results from suggested tests or an unexecuted test file.
7. Propose the smallest corrective change or additional validation that addresses the underlying issue.
8. Deliver a review summary with blocking findings, non-blocking questions, and explicit limits.

## Pitfalls

- A suspicious keyword is not a demonstrated vulnerability.
- A safe caller does not establish safety for every caller of a shared function.
- A green unrelated test suite does not validate the changed boundary.
- Removing the feature’s purpose is not automatically an acceptable mitigation.

## Verification

Before delivering the report, check all of the following:

- [ ] Each blocking finding has a concrete trigger and affected location.
- [ ] Assertions about execution refer to actual supplied test results.
- [ ] Missing context is labelled rather than invented.
- [ ] Recommended fixes address the shared cause without widening the requested scope.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
