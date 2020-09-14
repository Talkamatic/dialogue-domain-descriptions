# Action
## Definition
```xml
<action name="alpha"/>
```

The `action` element describes an action in the domain of the application. 


Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the action. |


## Parents

- [<ontology\>](/dialog-domain-description-definition/ontology/ontology.md)


## Children

None.


## Behaviour

The `action` element describes an action in the domain of the application. An action could be to show a particular menu, or to carry out a device action.

Actions are part of perform goals.


## Examples

### Action to make a call

```xml
<action name="make_call"/>
```
