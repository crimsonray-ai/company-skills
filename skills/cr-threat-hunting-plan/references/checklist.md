# Threat Hunting Plan: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Hypothesis | A proposition whose supporting and disconfirming observations can be stated. |
| Population | The explicit identities, devices, services, or accounts included in the hunt. |
| Baseline | A justified comparison population or period; not an assumed universal norm. |
| Stop condition | A clear evidence, volume, time, cost, or authorization boundary. |
| Escalation trigger | An observed discriminator that would warrant incident triage, not a pre-declared incident. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

A hunt for unusual administrative activity specifies the identity population, a seven-day window supplied by the user, the available audit schema, and a legitimate maintenance comparison. Missing audit retention is a blocker, not a negative result.

## Reviewer questions

- The hypothesis can be tested with the identified observations.
- Every query stage has a source, time bound, and stop condition.
- Unavailable schemas produce a stated blocker or pseudocode, not invented fields.
- The plan includes disconfirming evidence and legitimate alternatives.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
