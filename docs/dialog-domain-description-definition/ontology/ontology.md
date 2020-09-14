# Ontology
## Definition
```xml
<ontology name="n">
...
</ontology>
```

An ontology is an inventory of the things one can talk about in an application, consisting of (semantic) sorts, individuals, predicates and actions.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the ontology. |


## Parents

None.

## Elements

- [<sort\>](/dialog-domain-description-definition/ontology/elements/sort/)
- [<individual\>](/dialog-domain-description-definition/ontology/elements/individual/)
- [<predicate\>](/dialog-domain-description-definition/ontology/elements/predicate/)
- [<action\>](/dialog-domain-description-definition/domain/elements/action/)

## Children

None.


## Behaviour

The ontology element is the root element of the ontology file.



## Examples
### Partial ontology for a phone application

```xml
<ontology name="phone">
  <sort name="number_type"/>

  <predicate name="number_type_to_call" sort="number_type"/>

  <action name="make_call"/>

  <individual name="mobile" sort="number_type"/>
  <individual name="home" sort="number_type"/>
  <individual name="work" sort="number_type"/>
</ontology>

```
