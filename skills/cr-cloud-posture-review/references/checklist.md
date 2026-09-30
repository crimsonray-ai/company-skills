# Cloud Posture Review: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Identity | Effective permission path, workload/human identity, scope, and privilege boundary. |
| Network | Addressability, routes, filtering boundaries, service exposure, and relevant ingress context. |
| Data | Classification evidence, access policy, sharing, encryption, and retention context. |
| Audit | Enabled log sources, collection window, retention, and demonstrated event delivery. |
| Recovery | Backup scope, restoration evidence, ownership, and dependency assumptions. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

A storage policy grants broad access, but the supplied export omits an organization-level restriction. Report the risky resource policy and unresolved effective exposure; do not assert that anonymous access has been demonstrated.

## Reviewer questions

- Every issue names an in-scope resource identifier and source reference.
- Exposure claims include the relevant access-path evidence or are labelled unverified.
- Missing coverage is separated from confirmed control failures.
- Proposed remediation includes an owner and a validation criterion.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
