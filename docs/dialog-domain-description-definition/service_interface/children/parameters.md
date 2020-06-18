# Parameters

## Definition
```xml
  <parameters>
    <parameter predicate="predicate_name" format="format" default="default"/>
  </parameters>
```

Specifies the parameters to be used as arguments by the target service.


Attribute | Type | Description |
--- | --- | --- |
predicate | string | Required. The name of the predicate that is used as a parameter. Should match the name of the corresponding predicate declared in the Ontology. Predicate names are written using lowercase separated by underscores, e.g. 'current_temperature'. |
format | string | Required. Specifies the field in the request from which the parameter should be taken. Available options: <ul><li>value</li><li>grammar_entry</li></ul> |
default | string | Optional. Default 'value' or 'grammar_entry' for the predicate used as a parameter. |


## Children

- [<parameter\>](/dialog-domain-description-definition/service_interface/children/parameters)


## Behaviour

The <parameters\> element in the service interface contains all the parameters sent as arguments to the [<target\>](/dialog-domain-description-definition/service_interface/children/target) service.

Each of the parameters used by the specified target must be passed in a <parameter\> child.

### Format attribute

The `format` attribute specifies if the parameter passed to the target service has to be taken from the 'value' or 'grammar_entry' field of the request. <!-- Link to the API for HTTP services doc? -->

### Default attribute

The `default` attribute contains a string that is used as a 'value' or 'grammar_entry' if the predicate in the <parameter\> doesn't have any content in that 'value' or 'grammar_entry' (the one specified in the `format` attribute).

This attribute is necessary when the parameter is resolved in the Domain with a [<bind\>](/dialog-domain-description-definition/domain/children/bind) or a [<raise\>](/dialog-domain-description-definition/domain/children/raise) element since the user doesn't need to answer to these. If the user didn't answer those and a `default` value hasn't been specified, the predicate would be empty.


## Examples

### Forward a Call to a frontend with a selected contact and phone

```xml
<action name="Call">
  <parameters>
    <parameter predicate="selected_contact" format="value"/>
    <parameter predicate="selected_phone" format="grammar_entry" default="mobile"/>
  </parameters>
  <failure_reasons/>
  <target>
    <frontend/>
  </target>
</action>
```
