# Detection Gap Analysis: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Validated | A relevant test or observed case demonstrates the rule and data path together. |
| Configured, unvalidated | Logic exists but end-to-end behavior is not established. |
| Telemetry gap | Required data or fields are absent from the evidenced collection path. |
| Unknown | Configuration, collection, or validation evidence is missing. |
| False-positive check | A legitimate comparison case that tests a stated exclusion or discriminator. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

A rule is tagged for suspicious authentication but its required device field is absent from the supplied events. Record a telemetry/schema dependency, not validated coverage.

## Reviewer questions

- Each behavior maps to required telemetry and available evidence.
- Validated coverage cites an actual test or observation.
- Unknown coverage is not counted as absent or complete.
- Each proposed validation has expected results and a safe scope.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
