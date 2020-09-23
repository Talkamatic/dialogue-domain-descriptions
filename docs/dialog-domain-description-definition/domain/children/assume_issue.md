# Assume Issue
## Definition
```xml
<assume_issue type="question_type" predicate="p">
```

The plan item that assumes that a question is relevant to the user. Defines a question that should be assumed.

Attribute | Type | Description |
--- | --- | --- |
type | string | Required. The type can take one of the values "wh_question" or "yn_question".|
predicate | string | Required. This attribute specifies the predicate of the raised question.|

## Parents

- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)


## Children
None.


## Behaviour
Using the <assume_issue/> element has exactly the same effect as if the user would have asked the question. The element defines a question through its attributes. The issue (or question) that is assumed, must have a resolve-goal in the domain file.


## Examples
### Assume-issue entry for assuming the issue about the departure time (which is the resolve goal of another plan):

```xml
<assume_issue type="wh_question" predicate="flight_departure"/>
```
