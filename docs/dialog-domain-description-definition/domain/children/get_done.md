# Get Done
## Definition
```xml
<get_done action="alpha">
```

The element defines an action that the system should request the user to carry out. 


Attribute | Type | Description |
--- | --- | --- |
action | string | Required. The action that is requested from the user. |

## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)

## Children
- [<alt\>](/dialog-domain-description-definition/domain/children/alt)


## Behaviour

This plan item is considered as finished when the user has reported that the action is done.

## Examples
### A get_done to request that the user adds water

```xml
  <get_done action="add_water"/>
```
