# Crimson Ray Security Playbooks

A company-maintained starter library for evidence-led security work in **Crimson Ray → Skills → Company Skills**.

The library contains **16 portable skills** in **8 collections**. Every skill includes a procedure, a report template, and an interpretation checklist. The workflows help analysts, engineers, assurance teams, and leaders turn supplied evidence into reviewable decisions. They do not configure connectors, grant access, execute changes, or provide certification.

## Start here

- **Company administrators and users:** [Company Skills handbook](docs/HANDBOOK.md).
- **Skill maintainers:** [Authoring and contribution guide](CONTRIBUTING.md).
- **PDF handbook:** download the PDF attached to [release v0.1.0](https://github.com/crimsonray-ai/company-skills/releases/tag/v0.1.0).
- **Skill template:** [new-skill template](docs/new-skill-template.md).

### Application prerequisite

Company Skills is introduced by [Crimson Ray PR #794](https://github.com/crimsonray-ai/crimsonray/pull/794). This repository does not install or upgrade Crimson Ray. Use an approved application build containing that feature, and confirm that **Skills → Company Skills** is available. A library release is not a Desktop release; do not infer application availability from this repository's version tag.

The first Company Skills implementation supports **github.com and local gateways**. Private repositories use the existing GitHub authentication on the machine running the gateway. There is no new in-app GitHub sign-in wizard or shared-secret service.

## Install as a user

1. Obtain read access to this repository and complete company-approved GitHub authentication.
2. Open the intended local Crimson Ray profile, then **Skills → Company Skills**.
3. Enter `https://github.com/crimsonray-ai/company-skills`. Enter `v0.1.0` for the starter release, or leave the ref blank to follow the repository's default branch.
4. Select **Preview library**. Start with `essentials`; add the collection(s) for your role and preview again.
5. Review the commit, file changes, skill instructions, and security scan results. Approve **Apply reviewed changes** only after review.
6. Open the **Skills** tab, find the installed `cr-…` skills, and enable or disable individual skills for that profile.
7. Start a new conversation. Invoke a skill by its slash command, such as `/cr-incident-triage`, and supply the required evidence.

**Collections install files; enabled switches control skill availability. Neither grants permission to business systems.** Selecting multiple collections installs overlapping skills only once. Repository access allows users to read the whole repository, not just the collections they selected.

## Choose a collection

| Collection | Intended users | What it contains |
| --- | --- | --- |
| `essentials` | New users and cross-functional security teams | Evidence brief, incident triage, remediation plan, executive brief |
| `soc` | SOC analysts and incident responders | Evidence brief, triage, timeline, detection gaps, hunt planning |
| `exposure-management` | Vulnerability and exposure teams | Prioritization, asset coverage, cloud posture, remediation planning |
| `cloud-identity` | Cloud, IAM, and IT security owners | Cloud posture, identity review, SaaS exposure, asset coverage |
| `application-security` | AppSec and platform change reviewers | Secure change review, supply-chain review, prioritization, remediation |
| `assurance` | GRC and third-party-risk teams | Supplier review, control/evidence mapping, evidence brief |
| `leadership` | Security leaders and decision owners | Executive brief, evidence brief, remediation planning |
| `all` | Maintainers and deliberate full-library users | Every skill in the library; not the default |

See [`company-skills.json`](company-skills.json) for the exact membership. Collection IDs are selection conveniences, **not access-control boundaries**.

## Skill catalog

| Skill / slash command | Deliverable |
| --- | --- |
| [`cr-evidence-brief`](skills/cr-evidence-brief/SKILL.md) | Source-linked claims, contradictions, gaps, and the next decision |
| [`cr-incident-triage`](skills/cr-incident-triage/SKILL.md) | Triage disposition, evidence, bounded next reads, and response options |
| [`cr-incident-timeline`](skills/cr-incident-timeline/SKILL.md) | Chronology with original timestamps, uncertainty, and source references |
| [`cr-vulnerability-prioritization`](skills/cr-vulnerability-prioritization/SKILL.md) | Explainable remediation queue with ownership and verification |
| [`cr-cloud-posture-review`](skills/cr-cloud-posture-review/SKILL.md) | Cloud-control risk register with explicit coverage limitations |
| [`cr-identity-access-review`](skills/cr-identity-access-review/SKILL.md) | Identity/entitlement review decisions and owner follow-up |
| [`cr-saas-exposure-review`](skills/cr-saas-exposure-review/SKILL.md) | Sharing, privilege, and application-grant exposure review |
| [`cr-detection-gap-analysis`](skills/cr-detection-gap-analysis/SKILL.md) | Behavior-to-telemetry coverage matrix and validation backlog |
| [`cr-threat-hunting-plan`](skills/cr-threat-hunting-plan/SKILL.md) | Testable hypotheses, bounded read-only query plans, and stop conditions |
| [`cr-third-party-risk-review`](skills/cr-third-party-risk-review/SKILL.md) | Supplier evidence assessment and risk-decision options |
| [`cr-compliance-evidence-map`](skills/cr-compliance-evidence-map/SKILL.md) | Versioned control/evidence map and missing-proof requests |
| [`cr-secure-change-review`](skills/cr-secure-change-review/SKILL.md) | Concrete security-review findings and required validation |
| [`cr-remediation-plan`](skills/cr-remediation-plan/SKILL.md) | Approval-ready targets, steps, dependencies, verification, and recovery |
| [`cr-executive-security-brief`](skills/cr-executive-security-brief/SKILL.md) | Decision-oriented leadership update with traceable metrics |
| [`cr-asset-coverage-review`](skills/cr-asset-coverage-review/SKILL.md) | Inventory reconciliation and monitoring-coverage gaps |
| [`cr-software-supply-chain-review`](skills/cr-software-supply-chain-review/SKILL.md) | Dependency/artifact discrepancies and provenance-verification backlog |

## Maintain the library

- Change skill content through a reviewed pull request, not by editing installed copies.
- Keep a skill's folder and frontmatter `name` aligned. Names use the `cr-` prefix to reduce collisions with bundled or personal skills.
- Update collection membership when adding or retiring a skill.
- Publish reviewed releases as tags. Do not move existing release tags; use a full commit SHA when a strict immutable source pin is required.
- Employees explicitly preview and apply updates. A pinned release does not advance itself to a newer tag.
- Local modifications block replacement or removal. Preserve a separately named personal variant or restore the managed copy before updating.
- No credentials, completed customer reports, raw investigation evidence, or personal conversations belong in this repository.

## Validate changes

Maintainer validation uses Python and a pinned YAML parser; these are **not** dependencies for using the installed skills.

```bash
python3 -m pip install -r requirements-dev.txt
bash scripts/run_tests.sh
```

On Windows PowerShell, after installing the requirements with the intended Python interpreter:

```powershell
py -3 scripts/validate_library.py
py -3 -m unittest discover -s tests -v
```

The GitHub workflow runs the same structural validation and regression tests. Before a release, also preview the candidate commit through the actual Crimson Ray Company Skills implementation and inspect its security results. Structural validation and a clean scan do not prove that a security conclusion is correct; pilot representative, sanitized examples with the relevant domain owner.

## Repository layout

```text
company-skills.json       Collection definitions; format version 1
skills/<name>/SKILL.md    Installed skill instructions
skills/<name>/templates/  Installed output templates
skills/<name>/references/ Installed interpretation checklists
docs/HANDBOOK.md          Source for the company/user PDF handbook
scripts/                 Maintainer validation, not installed skills
tests/                   Library-contract tests
```

The `version: 1` in `company-skills.json` is the manifest **format version**. Skill versions such as `0.1.0`, repository release tags such as `v0.1.0`, and Crimson Ray application versions are separate concepts.
