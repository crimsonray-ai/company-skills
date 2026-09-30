---
name: cr-software-supply-chain-review
description: "Review dependencies and build provenance risks."
version: 0.1.0
author: Hermes
metadata:
  hermes:
    category: security
    tags: [Security, SupplyChain, ApplicationSecurity]
---
# Software Supply-Chain Review Skill

Review supplied dependency and build evidence for provenance and integrity gaps. This skill assesses artifacts and process evidence; it does not execute packages, change dependencies, or treat a signature as a guarantee of safety.
The workflow is portable and requires no additional software package.

**Policy: extend.** Inherit the active Crimson Ray harness rules; this skill adds only its analysis workflow and deliverable.

## When to Use

- Review the supply-chain risk in this release.
- Compare this SBOM, lockfile, and deployed artifact evidence.
- Assess dependency pinning and build provenance.

Primary audience: Application-security, build-platform, and software owners.

## Prerequisites

- The release/artifact scope and relevant manifests, lockfiles, SBOMs, and build records.
- Artifact digests, signing or attestation evidence, and verification results where available.
- Applicable dependency, publisher, and build-security policies.
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

1. Identify the exact release and artifact being assessed; distinguish source, resolved dependencies, built output, and deployed output.
2. Compare component identities and versions across the supplied manifests, lockfiles, SBOMs, and deployment evidence.
3. Identify unpinned or unexpected dependency sources and explain their effect on reproducibility and reviewability.
4. Assess provenance and signature evidence against the actual artifact digest and expected publisher or builder identity.
5. Review supplied build permissions, secret exposure boundaries, and untrusted-input handling without executing the build.
6. Keep vulnerability, provenance, integrity, and licensing questions separate; refer legal determinations to the accountable owner.
7. Prioritize discrepancies by affected artifact and supported impact, without labelling a package malicious from its name alone.
8. Produce a verification backlog with the exact missing artifact, record, or check needed to close each gap.

## Pitfalls

- A signed artifact is not automatically a safe artifact.
- A source manifest does not prove the dependencies present in a deployed binary.
- Mutable tags can point at different bytes over time.
- A suspicious package name is a lead, not proof of compromise.

## Verification

Before delivering the report, check all of the following:

- [ ] Conclusions bind to the exact artifact or explicitly state that its identity is missing.
- [ ] Cross-artifact comparisons preserve version and digest mismatches.
- [ ] Signature or provenance claims cite actual verification results or remain unverified.
- [ ] No package, build step, or downloaded artifact was executed by this workflow.
- [ ] Template placeholders are replaced with supplied facts or explicit unknowns, not invented values.
- [ ] The report distinguishes completed observations from recommendations for future work.
