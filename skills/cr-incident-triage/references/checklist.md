# Incident Triage: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Confirmed malicious activity | Observed behavior and context support the malicious interpretation; cite the specific discriminator. |
| Suspicious | Evidence warrants investigation but does not resolve the malicious-versus-legitimate question. |
| Inconclusive | The available evidence is insufficient or contradictory. |
| Benign explanation | A supported legitimate explanation fits the observed activity; do not infer it from missing events. |
| Potential scope | A hypothesis to investigate, not an additional confirmed affected entity. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

A sign-in alert shows a new location. A verified travel record and a familiar managed device may explain it; neither a country name alone nor the alert title settles the disposition.

## Reviewer questions

- Disposition and severity each have an evidence-backed rationale.
- All affected identities and assets can be traced to supplied identifiers.
- At least one alternative explanation is considered or explicitly ruled out with evidence.
- The next investigative step has a scope and a stop condition.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
