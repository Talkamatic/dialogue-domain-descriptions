# Report
## Definition
```xml
<report action="ActionName" status="status">
```

The grammar entry of a report given by the system.

| Attributes | Type | Description |
| --- | --- | --- |
| action | string | Required. Specifies the name of the action the report entry is for. This name should match the corresponding action name in service_interface. The action names in <report\> tags are written according to the PascalCase convention, e.g. 'SetTemperature'. |
| status | string | Required. Specifies the status of the action the report entry is for. Available options: <ul><li>started</li><li>ended</li><li>failed</li></ul> |
| reason | string | Optional, used together with status="failed". Specifies the reason for the failure to perform an action. |

## Children

- [<one-of selection="..."\>](/tdm_documentation/grammar/children/one-of)
    - [<item\>](/tdm_documentation/grammar/children/item)
        - [<slot\>](/tdm_documentation/grammar/children/slot)

## Behaviour

The <report\> element in the grammar defines the way in which the system makes reports about actions before or after performing them. The attribute `action` specifies which action the report is for, and the attribute `status` specifies the outcome of the performed action.

A report action can contain one of more phrases which are used by the system to report the result of the report's specified action. These phrases can also contain [<slot\>](/tdm_documentation/grammar/children/slot) tags. When a <report\> element contains multiple phrases, these are specified in [<item\>](/tdm_documentation/grammar/children/item) tags inside a [<one-of\>](/tdm_documentation/grammar/children/one-of) tag. In the case of <report\>, these <one-of\> tags have an attribute called 'selection' which specifies the order in which the contained items are used.

Reports can make use of the attribute `reason` in situations where the system reports on an action failure that could be due to multiple different reasons. An example of this is a situation where the action "CancelReservation" fails as the user is trying to cancel their booking of a hotel room. The reasons could for instance be that the user has no booked hotel room to cancel, or that the user is trying to cancel the reservation less than 24 hours before when this is not allowed.

### `status` attribute choices:

#### Started

Indicates that the report's specified action has been initialized. The report phrase should inform the user about this.

#### Ended

Indicates that the report's specified action was successfully completed and has been finalized. The report phrase should inform the user about this.

#### Failed

Indicates that the report's specified action was failed and was not completed. The report phrase should inform the user about the action failure and the reasons for said failure.

## Examples

### Started

This <report\> entry contains the phrase the system would use to report to the user that it has started the process of cancelling a booking. In this case, the system lets the user know that it is looking for reservations to cancel.

```xml
<report action="CancelReservation" status="started">checking for reservations.</report>
```

### Ended

This <report\> entry contains the phrase the system would use to report to the user that it has successfully cancelled the user's hotel room reservation.

```xml
<report action="CancelReservation" status="ended">your reservation has been cancelled.</report>
```

### Failed

The following <report\> entries show two examples of reports for cases where the system failed to perform the cancellation of the user's hotel room reservation. The two examples have different reasons for failure, the first being that the user has no booked hotel room to cancel and the second being that the user is trying to cancel a reservation less than 24 hours before the booking begins, when this is not allowed.
```xml
<report action="CancelReservation" status="failed" reason="no_reservation_exists">there is no reservation to cancel.</report>

<report action="CancelReservation" status="failed" reason="too_late_to_cancel">you cannot cancel your reservation less than 24 hours before your booking begins.</report>
```

### With <one-of\>

This <report\> entry shows an example of a report with multiple phrases that the system can use. In this case, the report is the result of the user asking the system to tell a joke.

```xml
<report action="Jokes" status="ended">
  <one-of selection="cyclic">
    <item>Why don't teddy bears ever order dessert? Because they're always stuffed</item>
    <item>What's the difference between snowmen and snow-women? Snowballs</item>
    <item>Why can't you trust an atom? Because they make up literally everything</item>
    <item>Why did the robot cross the road? It was programmed to be a chicken</item>
    <item>Why did the robot go to the shopping mall? It had hardware and software, but it needed underware</item>
  </one-of>
</report>
```
