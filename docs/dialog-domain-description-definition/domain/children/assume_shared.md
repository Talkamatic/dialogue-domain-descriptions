# Assume Shared
## Definition
```xml
<assume_shared>
  <proposition predicate="p" value="a"/>
</assume_shared>
```

Assumes the common knowledge between the system and the user of a predicate and assigns to it a specific value.

Attribute | Type | Description |
--- | --- | --- |
None. | - | -|

## Parents

- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)


## Children

- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)


## Behaviour
The <assume_shared/\> element adds the proposition to the facts that the system believe are shared between the user and the system. Any <findout\> with this predicate in <proposition\> will be considered as answered by the system with the specified value.


## Examples
### Assume Shared entry for assuming the fact that the "current_recipe" is "sourdough_starter":

```xml
<assume_shared>
  <proposition predicate="current_recipe" value="sourdough_starter"/>
</assume_shared>
```
