# Proposition
## Definition
```xml
<proposition predicate="p" value="a">
```

The element that represents a proposition, consisting of a predicate on an individual.

Attribute | Type | Description |
--- | --- | --- |
predicate | string | Required. The value must be enumerated in the ontology.|
value | string | Required. The value must be known to TDM e.g. by being a static individual enumerated in the ontology.|

## Parents
- [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
- [<assume\_system\_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
- [<condition\>](/dialog-domain-description-definition/domain/children/if)
- [<has\_shared\_value\>] (/dialog-domain-description-definition/domain/children/conditions)
- [<has\_private\_value\>] (/dialog-domain-description-definition/domain/children/conditions)
- [<has\_shared\_or\_private\_value\>] (/dialog-domain-description-definition/domain/children/conditions)
- [<is\_shared\_commitment\>] (/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\>] (/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\_or\_shared\_commitment\>] (/dialog-domain-description-definition/domain/children/conditions)

## Children
None.


## Behaviour
The proposition is used in conditional constructs in the domain language, in conditions, for assuming etc.


## Examples
### Proposition for the colour blue:

```xml
<proposition predicate="color" value="blue"/>
```
