# Postplan
## Definition
```xml
<postplan>
...
</postplan>
```

A sequence of plan elements for bookeeping actions after a goal has been resolved, performed or downdated.


## Parents

- [<goal\>](/dialog-domain-description-definition/domain/elements/goal)


## Children

- [<assume_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
- [<assume_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
- [<assume_system_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
- [<bind\>](/dialog-domain-description-definition/domain/children/bind)
- [<findout\>](/dialog-domain-description-definition/domain/children/findout)
- [<forget\>](/dialog-domain-description-definition/domain/children/forget)
- [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
- [<get_done\>](/dialog-domain-description-definition/domain/children/get_done)
- [<if\>](/dialog-domain-description-definition/domain/children/if)
- [<inform\>](/dialog-domain-description-definition/domain/children/inform)
- [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
- [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
- [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
- [<log\>](/dialog-domain-description-definition/domain/children/log)
- [<raise\>](/dialog-domain-description-definition/domain/children/raise)
- [<signal_action_completion/>\>](/dialog-domain-description-definition/domain/children/signal_action_completion)
- [<signal_action_failure/>\>](/dialog-domain-description-definition/domain/children/signal_action_failure)


## Behaviour

Immediately after a system goal has been fulfilled, the contents of a
potential `postplan` element will be added to the plan in TDM. This is
intended for bookkeeping tasks like assuming and forgetting
propositions, possibly jumping to other plans etc.




## Examples
### Postplan for forgetting all propositions of the predicate `attraction`
```xml
<postplan>
    <forget predicate="attraction"/>
</postplan>
```

### Postplan for keeping track of that a certain plan has been executed
```xml
<postplan>
    <assume_system_belief predicate="enrollment_done" value="true"/>
</postplan>
```
