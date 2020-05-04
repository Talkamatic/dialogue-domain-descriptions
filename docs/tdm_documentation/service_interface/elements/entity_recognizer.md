<span style="font-size: 2em">**Entity Recognizer**</span>

## Definition
```xml
<entity_recognizer name="EntityRecognizerName">
```

Requests entities from an http_service or a device module.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the entity recognizer. Names are written according to the PascalCase convention, e.g. 'CityRecognizer'. |


## Children

- [<target\>](/tdm_documentation/service_interface/children/target)
    - [<http\>](/tdm_documentation/service_interface/children/target)
    - [<device_module\>](/tdm_documentation/service_interface/children/target)


## Behaviour

The <entity_recognizer\> element in the service interface requests entities from the [<target\>](/tdm_documentation/service_interface/children/target) http_service or device module. The endpoint function will collect the entities and return each of the entities' `value`, `grammar_entry` and `sort` in the response. <!-- Include a LINK to entity_recognizer response in the API documentation -->


## Examples

**Request for cities to an http_service**

```xml
  <entity_recognizer name="CityRecognizer">
    <target>
      <http endpoint="http://127.0.0.1:10100/city_recognizer"/>
    </target>
  </entity_recognizer>
```
