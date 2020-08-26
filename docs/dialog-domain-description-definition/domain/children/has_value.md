# Has Value
## Definition
```xml
<has_value predicate="p">
```

The condition that evaluates to true if there is a shared fact that is a proposition using the predicate `p`, and false otherwise.

Attribute | Type | Description |
--- | --- | --- |
predicate | string | Required. This attribute specifies the predicate of the proposition.|

## Parents
- [<downdate_condition\>](/dialog-domain-description-definition/domain/children/downdate_condition)

## Children
None.


## Behaviour
The condition that evaluates to true if there is a shared fact that is a proposition using the predicate `p`, and false otherwise. It is a child element of the `downdate_condition` element.

### has_value element for defining the condition that evaluates to true once the departure of a flight is known:

```xml
<has_value predicate="flight_departure"/>
```
