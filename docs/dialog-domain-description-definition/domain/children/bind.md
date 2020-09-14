# Bind
## Definition
```xml
<bind question_type="type" predicate="p">
```

The element defines a question that can be answered by the user, but will not be asked by the system.




Attribute | Type | Description |
--- | --- | --- |
question\_type | string | Required. Must be one of `goal`, `wh_question`, `alt_question` or `yn_question`. |
predicate | string | Optional. Required if question_type is `wh_question` or `yn_question`.|


## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)

## Children
- [<alt\>](/dialog-domain-description-definition/domain/children/alt)


## Behaviour

The element defines a question that can be answered by the user, but will not be asked by the system, thereby `binding' that answer to the goal in question. This makes it possible to take into consideration optional and unrequested parameters.



## Examples


### Binding a WH question about price range (e.g. in a travel booking application)

```xml
  <bind type="wh_question" predicate="price-class"/>
```
