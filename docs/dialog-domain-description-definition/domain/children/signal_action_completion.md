# Signal_Action_Completion
## Definition
```xml
<signal_action_completion/>
```

The plan item that will make a perform plan stop running, indicating a successful result through the output of a
`"report(action_status(some_action, done))"` move.


Attribute | Type | Description |
--- | --- | --- |
None. | - | -|


## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

## Children
None.

## Behaviour
The `<signal_action_completion/>` will make TDM treat the perform goal of the current plan as fulfilled. This means that the remains of the plan (if any) will not be executed, and that a report move indicating success (see above) will be output.



## Examples
### Signal\_Action\_Completion element for telling the user that the first name is "Charlie"

```xml
<signal_action_completion/>
```
