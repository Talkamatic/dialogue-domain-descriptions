# Validity
## Definition
```xml
<validity name="ValidityName">
```

The grammar entry specifying how the system reports to the user that one or more of their given parameters are invalid. .

| Attributes | Type | Description |
| --- | --- | --- |
| name | string |  Required. Specifies the name of the Validity, which should match the corresponding validator in service_interface. The validity names in <validity\> tags are written according to the PascalCase convention, e.g. 'SetTemperature'. |

## Children

- [<slot\>](/tdm_documentation/grammar/children/slot)

## Behaviour

The <validity\> element in the grammar defines the way in which the system informs users about the parameters they have given being invalid. The attribute `name` specifies the name of the validator and needs to match the name of the corresponding validator in service_interface.

A validity entry in the grammar contains one phrase which the system can use to inform the user of invalid parameters. This phrase can contain [<slot\>](/tdm_documentation/grammar/children/slot) tags.

## Examples

```xml
<validity name="HourValidity">cannot set the hour to <slot predicate="hour_to_set"/>.</validity>
<validity name="MinuteValidity">cannot set the minute to <slot predicate="minute_to_set"/>.</validity>
```
