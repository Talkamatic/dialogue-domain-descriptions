# Signal\_Action\_Failure
## Definition
```xml
<signal_action_failure reason="failure_reason"/>
```

The plan item that will make a perform plan stop running, indicating failure through the output of a
`"report(action_status(some_action, aborted(failure_reason)))"` move.


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
The `<signal_action_failure/>` will make TDM treat the perform goal of the current plan as failed. This means that the remains of the plan (if any) will not be executed, and that a report move indicating failure (see above) will be output.



## Examples
### Signal\_Action\_Failure element indicating the failure reason of "no\_money"

```xml
<signal_action_failure reason="no_money"/>
```
