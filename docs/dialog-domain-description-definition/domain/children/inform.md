# Inform
## Definition
```xml
<inform>
  <proposition predicate="p" value="a"/>
</inform>
```

The plan item that informs the user about a proposition.


Attribute | Type | Description |
--- | --- | --- |
None. | - | -|


## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

## Children
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)

## Behaviour
The `<inform/>` element makes the system believe a proposition `p(a)`, and then also assume that the issue of `?X.p(X)` is under discussion. This means that the system will try to inform the user that `p(a)`, unless this is already known by the user. It is required that the proposition is of a predicate defined in the ontology (i.e. goal propositions etc... are not supported).

The same behaviour can be obtained by the following code:
```xml
<assume_system_belief>
    <proposition predicate="p" value="a"/>
</assume_system_belief>
<assume_issue predicate="p" type="wh_question"/>
```


## Examples
### Inform element for telling the user that the first name is "Charlie"

```xml
<inform>
    <proposition predicate="first_name" value="Charlie"/>
</inform>
```
