# Software Supply-Chain Review: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Manifest | Declared dependency intent; not necessarily the final resolved or deployed set. |
| Lockfile | Resolved dependency versions and, where recorded, integrity data. |
| SBOM | A component inventory whose generation scope and artifact relationship must be established. |
| Attestation | A statement about an artifact or build; identity and binding require verification. |
| Artifact digest | A content identifier for the specific bytes assessed, using the relevant trusted verification process. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

An SBOM describes one artifact digest while the deployed release reports another. Preserve the mismatch and request the correct binding evidence before concluding that the deployed artifact was assessed.

## Reviewer questions

- Conclusions bind to the exact artifact or explicitly state that its identity is missing.
- Cross-artifact comparisons preserve version and digest mismatches.
- Signature or provenance claims cite actual verification results or remain unverified.
- No package, build step, or downloaded artifact was executed by this workflow.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
