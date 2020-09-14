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

- [<forget\>]
- [<forget_all\>]
- [<log\>](/dialog-domain-description-definition/domain/children/log)
- [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
- [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
- [<findout\>](/dialog-domain-description-definition/domain/children/findout)
- [<raise\>]
- [<bind\>]
- [<get_done\>]
- [<assume_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
- [<assume_shared\>]
- [<assume_system_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
- [<if\>]
- [<jumpto\>]



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
