# Target

## Definition
```xml
  <target>
    <http endpoint="http://127.0.0.1:10100/function_name"/>
  </target>
```
```xml
  <target>
    <frontend/>
  </target>
```
```xml
  <target>
    <device_module device="NameDevice"/>
  </target>
```

Specifies the target service.

### <http>

Attribute | Type | Description
--- | --- | ---
endpoint | string | Required. The url of the http_service endpoint followed by the name of the function it should run in that endpoint, e.g. 'http://127.0.0.1:10100/set_temperature'.

### <device_module>

Attribute | Type | Description |
--- | --- | --- |
device | string | Required. The name of the device module to run. |


## Children

- [<http\>](#http)
- [<frontend\>](#frontend)
- [<device_module\>](#device_module)


## Behaviour

The <target\> element in the service interface specifies the target service that will handle its parent [<action\>](/tdm_documentation/service_interface/elements/action), [<query\>](/tdm_documentation/service_interface/elements/query), [<validator\>](/tdm_documentation/service_interface/elements/validator) or [<entity_recognizer\>](/tdm_documentation/service_interface/elements/entity_recognizer).

### <http>

Points the parent element to a function of an http_service served on a Flask instance. The DDD sends a request to the http_service, performs the function in it and returns a response. <!--LINK to API docs-->

### <frontend>

Points the parent [<action\>](/tdm_documentation/service_interface/elements/action) to an integrated frontend service such as Twilio or Alexa. This allows for performing actions like forwarding a call using a frontend service.

<!-- I think it would be good to point (or have it here) to some list of the frontend actions already implemented in TDM. There is one in the Taiga wiki. -->

### <device_module>

Points the parent element to a device module. This will run a class inside the device module which must have the same name as the parent [<action\>](/tdm_documentation/service_interface/elements/action), [<query\>](/tdm_documentation/service_interface/elements/action), etc.


## Examples

### Set the temperature to a specific value using an http_service

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

### Forward a Call action to a frontend service

```xml
<action name="Call">
  <parameters>
    <parameter predicate="phone_number" format="grammar_entry"/>
  </parameters>
  <failure_reasons/>
  <target>
    <frontend/>
  </target>
</action>
```

### Query a device module about the current temperature in a location

```xml
<query name="current_temperature">
  <parameters>
    <parameter predicate="location" format="grammar_entry"/>
  </parameters>
  <target>
    <device_module device="ClimateDevice"/>
  </target>
</query>
```
