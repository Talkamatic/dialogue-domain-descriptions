<span style="font-size: 2em">**Preconfirm**</span>
## Definition
```xml
<preconfirm action="ActionName">
```

The grammar entry of preconfirmations for actions. Defines how the system can ask the user for confirmation about performing an action.

| Attributes | Type | Description |
| --- | --- | --- |
| action | string |  Required. Specifies which action the preconfirmation is for. This name should match the corresponding action name in service_interface. The action names in <preconfirm\> tags are written according to the PascalCase convention, e.g. 'SetTemperature'. |

## Children

- [<slot\>](/tdm_documentation/grammar/children/slot)

## Behaviour

The <preconfirm\> element in the grammar ... The attribute `action` specifies the action for which this entry makes preconfirmation possible. 

<!--What does this entry do? Marta mentioned that it was like a report before an action happens but isn't that was reports with status started are for? Is it more for checking whether the user wants to perform the action before performing it?-->

A preconfirm entry in the grammar has one phrase which the system uses to preconfirm with the user whether an action should be performed. Said phrase can contain [<slot\>](/tdm_documentation/grammar/children/slot) tags.

## Examples

```xml
<preconfirm action="RemoveAlarm">remove the alarm</preconfirm>
```
```xml
<preconfirm action="BookHousing">book this hotel</preconfirm>
```