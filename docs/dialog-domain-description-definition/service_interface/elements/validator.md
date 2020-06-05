# Validator

## Definition
```xml
<validator name="ValidatorName">
```

Checks the validity of some predicate in an http_service or a device module.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the validator class. Names are written according to the PascalCase convention, e.g. 'CityRecognizer'. |


## Children

- [<parameters\>](/tdm_documentation/service_interface/children/parameters)
    - [<parameter\>](/tdm_documentation/service_interface/children/parameters)
- [<target\>](/tdm_documentation/service_interface/children/target)
    - [<http\>](/tdm_documentation/service_interface/children/target)
    - [<device_module\>](/tdm_documentation/service_interface/children/target)


## Behaviour

The <validator\> element in the service interface checks the validity of a parameter using the specified module in [<target\>](/tdm_documentation/service_interface/children/target). The target service must be either an http_service or a device module, which would return either `true` or `false` as the value for `"is_valid"` inside a validator response.

<!-- Include a link to action response in the HTTP service API doc? -->

If the target module returns a `"is_valid": false`, that will trigger the system to reject the user utterance, and explain to the user why the parameter was rejected. The rejecting utterance will need to be defined in the [grammar](/tdm_documentation/grammar/children/validity).


## Examples

### Check in an http_service if the value and grammar entry for the destination city are valid

```xml
  <validator name="CityValidity">
    <parameters>
      <parameter predicate="dest_city" format="value"/>
      <parameter predicate="dest_city" format="grammar_entry"/>
    </parameters>
    <target>
      <http endpoint="http://127.0.0.1:10100/city_validity"/>
    </target>
  </validator>
```
