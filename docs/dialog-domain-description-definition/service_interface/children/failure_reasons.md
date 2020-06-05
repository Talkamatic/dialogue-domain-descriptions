# Failure Reasons

## Definition
```xml
<failure_reasons>
  <failure_reason name="failure_reason_name"/>
</failure_reasons>
```

Specifies the reasons for an [<action\>](/tdm_documentation/service_interface/elements/action) to return a failure.


Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the failure reason. The names are written using lowercase separated by underscores, e.g. 'temperature_too_high'. |


## Children

- [<failure_reason\>](/tdm_documentation/service_interface/children/failure_reasons)


## Behaviour

The <failure_reasons\> element in the service interface contains all the possible reasons for the [<target\>](/tdm_documentation/service_interface/children/target) service inside an [<action\>](/tdm_documentation/service_interface/elements/action) to return a `fail` status in its response. <!-- Link to the API for HTTP services doc (action response)? -->

Each of the reasons must be passed in a <failure_reason\> child. For each <failure_reason\>, the response from the target service must also contain a reason that matches the name of the <failure_reason\>.

It is possible for an <action\> to not contain any <failure_reason\>, in which case the <action\> is expected to always return a `"status": "success"`.

The `"status": "fail"` (and the <failure_reason\>) is meant for action failures expected by the DDD developer. Such a failure could be, for instance, an action receiving a parameter with an invalid value (see the [example](/tdm_documentation/service_interface/children/failure_reasons/#examples) below). This will trigger the system to report to the user why the action has failed. The failure utterance will need to be defined in the [grammar](/tdm_documentation/grammar/children/report).


## Examples

### Set temperature with a failure reason

If the action in the target http_service receives a value for the parameter `degrees` above a specific threshold (e.g. "27 degrees"), the http_service sends back a response with `"status": "fail"` and the `"reason": "temperature_too_high"`.

```xml
<action name="SetTemperature">
  <parameters>
    <parameter predicate="degrees" format="value"/>
  </parameters>
  <failure_reasons>
    <failure_reason name="temperature_too_high"/>
  </failure_reasons>
  <target>
    <http endpoint="http://127.0.0.1:10100/set_temperature"/>
  </target>
</action>
```
