# Individual
## Definition
```xml
<individual name="i" sort="s"/>
```

The `individual` element describes a thing that one can talk about.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the individual. |
sort | string | Required. The sort of the individual. |



## Parents

- [<ontology\>](/dialog-domain-description-definition/ontology/ontology.md)


## Children

None.


## Behaviour



The `individual` element describes a thing that one can talk about -  an entity in the domain that the ontology is describing.

All individuals are of a sort, and all predicates take individuals (of a specific sort) as arguments.

Known limitations: Note that individuals cannot be numbers.



## Examples
### Months

```xml
  <individual name="january" sort="month"/>
  <individual name="february" sort="month"/>
  <individual name="march" sort="month"/>
...
  <individual name="december" sort="month"/>
```

