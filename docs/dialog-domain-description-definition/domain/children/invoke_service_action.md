# Invoke Service Action
## Definition
```xml
<invoke-service-action name="alpha">
```

Calls for an action to be performed by a service.


Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the [Action](/dialog-domain-description-definition/service_interface/elements/action) as defined in the Service Interface. |
preconfirm | string | Optional. Can be set to  "assertive" or "interrogative". If defined, causes system to ask for a  confirmation from the user before performing the action.   |
postconfirm | boolean | Optional. If set to `True', causes the system to report on the status of the action  |
downdate_plan | boolean | Optional. If set to `True', causes the system to regard the action as done once the device has been called to carry out the action. |


## Parents

- [<plan\>](/dialog-domain-description-definition/domain/children/plan)


## Children
None.


## Behaviour
An <invoke_service_action/> element calls for an action to be performed by a service. The action needs to be defined by the [Service Interface](/dialog-domain-description-definition/service_interface/elements/action).


If defined, the  `preconfirm' attribute causes system to give the user the opportunity to confirm (or abort) an action before  it is performed. Can be set to  "assertive" (e.g., "Do you want to call John") or "interrogative" (e.g. "I will call John"), depending on whether the preconfirmation should take the form of an assertion (which the user can respond, but if they do not, the system will go ahead and perform the action) or a question (requiring an answer from the user). The natural language form of the preconfirmation is defined in the grammar, see [Preconfirm](/dialog-domain-description-definition/grammar/elements/preconfirm/). The natural language form can be configured to include parameters of the action.

If set to `True', the `postconfirm' attribute causes the system to report on the status of the action after calling on the device to carry out the action. The natural language form of the postconfirmation is defined in the grammar, see [Report](dialog-domain-description-definition/grammar/elements/report/).

If set to `True', the 'downdate_plan' element causes the system to regard the action as done once the device has been called to carry out the action. Otherwise, it will not regard the action as done until it has been explicitly reported to be done. The latter may be useful for actions that need to succeed.

## Examples
### Invoke service action entry for calling a person, first confirming that the parameters are correct, and reporting again when the call has been made:

```xml
<invoke_service_action name="Call" preconfirm=interrogative postconfirm=True downdate_plan=False/>
```
