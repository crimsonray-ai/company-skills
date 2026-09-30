# Identity Access Review: interpretation checklist

Use this glossary to interpret the supplied records. It is not a vendor specification, a substitute for the customer's policy, or evidence about a real environment.

## Terms and evidence expectations

| Term or control area | Meaning |
| --- | --- |
| Assigned entitlement | The role or membership directly present in the supplied record. |
| Effective access | The resulting resource access after relevant inheritance and boundary rules. |
| Dormant within window | No qualifying activity observed in a stated, sufficiently covered interval. |
| Owner confirmation needed | Purpose or continuing need cannot be established from available evidence. |
| Emergency identity | An explicitly designated recovery identity requiring its own review criteria. |

## Synthetic example

The following is an invented training example, not a finding to copy into a report:

An application identity has not signed in interactively for 90 days but has current workload activity. It is not a dormant human account; review its workload purpose, owner, and effective permissions separately.

## Reviewer questions

- Identity joins preserve tenant and immutable identifiers.
- Inactivity conclusions state the observation window and threshold.
- Workload dependencies and emergency accounts are considered before proposing removal.
- Each proposed change is distinguishable from a completed action.

## Handoff record

When another analyst continues the work, preserve the assessed scope, observation window, source references, unresolved questions, and the decision owner. Keep this library's files unchanged; working evidence and completed reports belong in the user's approved workspace.
