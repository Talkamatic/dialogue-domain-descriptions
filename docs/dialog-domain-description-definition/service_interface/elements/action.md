# Action

## Definition
```xml
<action name="ActionName">
```

Performs an action in http_service, device module or frontend service.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the action. Action names are written according to the PascalCase convention, e.g. 'SetTemperature'. |


## Children

- [<parameters\>](/dialog-domain-description-definition/service_interface/children/parameters)
    - [<parameter\>](/dialog-domain-description-definition/service_interface/children/parameters)
- [<failure_reasons\>](/dialog-domain-description-definition/service_interface/children/failure_reasons)
    - [<failure_reason\>](/dialog-domain-description-definition/service_interface/children/failure_reasons)
- [<target\>](/dialog-domain-description-definition/service_interface/children/target)
    - [<http\>](/dialog-domain-description-definition/service_interface/children/target)
    - [<device_module\>](/dialog-domain-description-definition/service_interface/children/target)
    - [<frontend\>](/dialog-domain-description-definition/service_interface/children/target)


## Behaviour

The <action\> element in the service interface connects the corresponding [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action) element in the domain to a specific service action inside [<target\>](/dialog-domain-description-definition/service_interface/children/target). The target service must be either an http_service, device module or frontend service, which would return either `success` or `fail` status inside an action response.

<!-- Include a link to action response in the HTTP service API doc? -->

Each of the parameters used by the specified [<target\>](/dialog-domain-description-definition/service_interface/children/target) must be passed under [<parameters\>](/dialog-domain-description-definition/service_interface/children/parameters).

If the <action\> contains a [<failure_reason\>](/dialog-domain-description-definition/service_interface/children/failure_reasons), the target service must be able to return a `fail` status with the reason name in the response. Check the documentation of this child element for more information.


## Examples

### Set temperature

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

### Forward a Call

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
