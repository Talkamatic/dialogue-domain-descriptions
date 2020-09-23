# Forget All
## Definition
```xml
<forget_all/>
```

The plan item that makes the system forget all and start from the beginning.

Attribute | Type | Description |
--- | --- | --- |
None.

## Parents

- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)


## Children
None.


## Behaviour
Forget All makes the system forget all and restart.
- The plan is cleared
- The system beliefs are cleared
- The shared commitments (what the system thinks that the system and the user have agreed upon) are cleared
- The goals stack is emptied
- The "top" goal is pushed on the goals stack
- Any traces of previous utterances are cleared


## Examples
### Forget All

```xml
<forget_all/>
```
