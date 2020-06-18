# Query

## Definition
```xml
<query name="query_name">
```

Requests information from an http_service or a device module.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the predicate that is requesting the information. Should match the name of the corresponding predicate of the invoke_service_query in the domain. Query names are written using lowercase separated by underscores, e.g. 'current_temperature'. |


## Children

- [<parameters\>](/dialog-domain-description-definition/service_interface/children/parameters)
    - [<parameter\>](/dialog-domain-description-definition/service_interface/children/parameters)
- [<target\>](/dialog-domain-description-definition/service_interface/children/target)
    - [<http\>](/dialog-domain-description-definition/service_interface/children/target)
    - [<device_module\>](/dialog-domain-description-definition/service_interface/children/target)


## Behaviour

The <query\> element in the service interface connects the corresponding [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query) element in the domain to a specific service query inside [<target\>](/dialog-domain-description-definition/service_interface/children/target). The target service must be either a http_service or a device module which returns a query response.

<!-- Include a link to query response in the API documentation? -->

Each of the parameters used by the specified [<target\>](/dialog-domain-description-definition/service_interface/children/target) must be passed under [<parameters\>](/dialog-domain-description-definition/service_interface/children/parameters).


## Examples

### Query a device module about the current temperature in a location

```xml
<query name="current_temperature">
  <parameters>
    <parameter predicate="location" format="grammar_entry"/>
  </parameters>
  <target>
    <http endpoint="http://127.0.0.1:10100/current_temperature"/>
  </target>
</query>
```
