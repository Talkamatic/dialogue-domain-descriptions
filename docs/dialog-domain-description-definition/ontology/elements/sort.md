# Sort
## Definition
```xml
<sort name="s"/>
```

The `sort` element describes a kind of thing that one can talk about. One can also think of it as a datatype declaration. All individuals are of a sort, and all predicates take arguments (individuals) of a specific sort.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the sort. |
dynamic | boolean | Optional. If set to `"True"`, new individuals of the sort can be added during runtime. |


## Parents

- [<ontology\>](/dialog-domain-description-definition/ontology/ontology.md)


## Children

None.


## Behaviour

Sorts can be dynamic or static. For dynamic sorts,  new individuals of the sort can be added during runtime.

Sorts can be user-defined or pre-defined. Only user-defined sorts need to be declared in the ontology.

Pre-defined sorts in TDM are:

- `Boolean`: `True` or `False`
- `Integer`
- `Real`: Real numbers represented as floats
- `String`: Strings of characters.This is primarily used for literal answers dictated by the user, e.g. messages or names.
- `Image`: String representing a URL of an image
- `Webview`: String representing the URL of a webview
- `Domain`:  The name of an other domain. This allows one to talk explicitly about domains, and can be thus used for meta dialogues, e.g. switching between domains.




## Examples
### Sort for telephone number type

```xml
  <sort name="number_type"/>
```

### Sort for album title in music playing app

```xml
  <sort name="album_name" dynamic="True"/>
```
