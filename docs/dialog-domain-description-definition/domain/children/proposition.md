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
- [<is_shared_fact\>](/dialog-domain-description-definition/domain/children/is_shared_fact)

## Children
None.


## Behaviour
The proposition is used in conditional constructs in the domain language.


## Examples
### Proposition for the colour blue:

```xml
<proposition predicate="color" value="blue"/>
```
