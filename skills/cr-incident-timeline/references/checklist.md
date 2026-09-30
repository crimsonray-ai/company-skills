# Incident Timeline: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Event time | When the source says the activity occurred. |
| Ingestion time | When a collector received or indexed the record. |
| Clock offset | A measured or supplied difference from a reference clock, with its applicable interval. |
| Time precision | The smallest unit the source reliably distinguishes. |
| Ordering uncertainty | More than one sequence remains consistent with the available timestamps. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

A device event has a timestamp without an offset and a cloud event uses UTC. Preserve the device’s original time and mark its relative ordering unknown until the device timezone or clock offset is supplied.

## Reviewer questions

- Every event retains its original timestamp and reference.
- Normalized times have a known timezone or offset.
- Unknown ordering and collection gaps are explicitly represented.
- Causal statements are separately labelled and evidence-linked.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
