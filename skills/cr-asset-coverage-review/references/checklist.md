# Asset Coverage Review: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Inventory presence | The source reports that the asset exists within its scope. |
| Enrollment | A control or agent has a registration associated with the asset. |
| Freshness | The latest relevant observation falls within the supplied threshold. |
| Operating evidence | Records demonstrate the relevant control performing its intended function. |
| Unassessed | The source set cannot determine coverage for that population. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

Two inventories share a hostname but show different cloud instance identifiers and lifecycle dates. Treat them as distinct or unresolved entities rather than count a single protected asset.

## Reviewer questions

- The denominator and exclusions are explicit for each reported metric.
- Joins use stable identifiers or are labelled ambiguous.
- Enrollment, freshness, and operating evidence remain separate.
- Gap-remediation tasks identify the confirmation evidence and owner.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
