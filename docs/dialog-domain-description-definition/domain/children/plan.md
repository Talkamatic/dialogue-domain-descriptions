# Plan
## Definition
```xml
<plan>
...
</plan>
```

A dialogue plan, consisting of a sequence of plan items.


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

To resolve questions, or perform actions, TDM executes a dialogue plan. In some cases the plan is equivalent to a form with slots and values that need to be filled, after which the requested action can be carried out, or the asked question can be answered by the system. However, dialogue plans are more powerful than forms in the kinds of dialogue behaviours they can produce.




## Examples
### Plan for asking a sequence of questions and getting the price of a trip.

```xml
<plan>
  <findout type="wh_question" predicate="means_of_transport"/>
  <findout type="wh_question" predicate="dest_city"/>
  <findout type="wh_question" predicate="dept_city"/>
  <findout type="wh_question" predicate="dept_month"/>
  <findout type="wh_question" predicate="dept_day"/>
  <findout type="wh_question" predicate="class"/>
  <invoke_service_query type="wh_question" predicate="price"/>
</plan>
```
