# Background
## Definition
```xml
<service_query predicate="p"/>
```

Defining that a service query to be used for incremental search.

Attribute | Type | Description |
--- | --- | --- |
Predicate| String | The predicate for the query that will provide the incremental search with results.|

## Parents
- [<parameters\>](/dialog-domain-description-definition/domain/elements/parameters)

## Children
None

## Behaviour
If the parent parameter set is configured for incremental search, and if the "source" attribute of that parameter set is set to "service", then this element defines the service query that will provide the incremental search with results.

## Examples
### Service query:

Service query for `available_contact_from_api`:

```xml
    <service_query predicate="available_contact_from_api"/>
```

### Parameter set with service query:
```xml
    <parameters question_type="wh_question" predicate="contact_retrieved_from_api" graphical_type="list"
              source="service" incremental="true" max_spoken_alts="5" max_reported_hit_count="15"
              on_zero_hits_action="mitigate_zero_hits_from_api"
              on_too_many_hits_action="mitigate_too_many_hits_from_api">
    <service_query predicate="available_contact_from_api"/>
    <ask_feature predicate="name_of_contact"/>
    <ask_feature predicate="postal_area_of_contact" kpq="true"/>
    <ask_feature predicate="street_name_of_contact" kpq="true"/>
    <ask_feature predicate="age_of_contact" kpq="true"/>
  </parameters>
```
