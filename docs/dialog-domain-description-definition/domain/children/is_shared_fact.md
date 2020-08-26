# Is Shared Fact
## Definition
```xml
<is_shared_fact>
```

The condition that evaluates to true if there is a shared fact that is identical to the proposition that is the child of this element.

Attribute | Type | Description |
--- | --- | --- |
None.

## Parents
- [<downdate\_condition\>](/dialog-domain-description-definition/domain/children/downdate_condition)

## Children
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)

## Behaviour
The condition that evaluates to true if there is a shared fact that is identical to the proposition that is the child of this element and false otherwise. It is the child element of the `downdate_condition` element.

## Examples

### is_shared_fact which will evaluate to true if the departure is late:

```xml
<is_shared_fact>
     <proposition predicate="flight_departure" value="late"/>
</is_shared_fact>
```
