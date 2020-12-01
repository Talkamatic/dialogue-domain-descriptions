# Bind
## Definition
```xml
<bind question_type="type" predicate="p">
```

The element defines a question that can be answered by the user, but will not be asked by the system.


Attribute | Type | Description |
--- | --- | --- |
question\_type | string | Optional. Defaults to `wh_question`, but can be one of `goal`, `wh_question`, `alt_question` or `yn_question`. |
predicate | string | Optional. Required if question_type is `wh_question` or `yn_question`.|


## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

## Children
- [<alt\>](/dialog-domain-description-definition/domain/children/alt)


## Behaviour

The element defines a question that can be answered by the user, but will not be asked by the system, thereby `binding' that answer to the goal in question. This makes it possible to take into consideration optional and unrequested parameters.

This is only valid **as long as the plan element is still in the plan**. When executed, the plan element **is removed from the plan**. This means that the element **should always be placed last in the plan**, unless the developer wishes to remove the `bind` element during execution of the plan.



## Examples


### Binding a WH question about price range (e.g. in a travel booking application)

```xml
  <bind type="wh_question" predicate="price-class"/>
```
