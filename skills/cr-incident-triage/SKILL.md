---
name: cr-incident-triage
description: "Assess an alert and propose a bounded response."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, IncidentResponse, Triage]
---
# Incident Triage Skill

Assess an alert using the supplied events, asset context, and investigation window. This skill produces a triage assessment and response options; it does not contain hosts, disable accounts, or declare a breach from an alert alone.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Triage this alert and explain what to investigate next.
- Is this activity confirmed, suspicious, or inconclusive?
- Prepare an incident-response handoff.

Primary audience: SOC analysts and incident responders.

## Prerequisites

- The original alert and underlying event records, not just its title.
- Affected asset and identity identifiers, business context, and investigation time window.
- The organization’s incident severity and escalation policy, if available.
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

1. Record the alert identifier, observed times, detector rationale, and the exact entities implicated by the source.
2. Check whether the records describe actual behavior, a configuration risk, or a detector hypothesis. Keep those categories separate.
3. Correlate entities using stable identifiers and time bounds. Do not join users or devices only because display names resemble one another.
4. Look for evidence that supports the detector and evidence that could explain legitimate activity, such as an approved change or known service identity.
5. Assess potential impact using supplied business criticality and observed reach. Distinguish the observed set of entities from a possible wider scope.
6. Assign a triage disposition with a rationale. Use the organization’s severity definitions; otherwise label the proposed severity as provisional.
7. Identify the next bounded read or evidence request for each important uncertainty. Specify entity, time window, expected discriminator, and stop condition.
8. Prepare response options and escalation ownership. Mark each operational action as proposed and leave execution to the existing approval workflow.

## Pitfalls

- Detector severity and incident severity answer different questions.
- A privileged account in an event is not proof that its credentials were stolen.
- Missing telemetry cannot clear an alert when collection coverage is unknown.
- A proposed containment step is not evidence that containment occurred.

## Verification

Before delivering the report, check all of the following:

- [ ] Disposition and severity each have an evidence-backed rationale.
- [ ] All affected identities and assets can be traced to supplied identifiers.
- [ ] At least one alternative explanation is considered or explicitly ruled out with evidence.
- [ ] The next investigative step has a scope and a stop condition.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
