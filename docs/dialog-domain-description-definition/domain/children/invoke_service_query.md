# Invoke Service Query
## Definition
```xml
<invoke_service_query type="wh_question" predicate="p"/>
```

```xml
<invoke_service_query type="yn_question">
  <proposition predicate="p">
</invoke_service_query>
```



Calls for an query to be sent to a service.


Attribute | Type | Description |
--- | --- | --- |
type | string | Required. The value is one of "yn_question" and "wh_question".|
predicate | string | Required if type="wh_question". This attribute specifies the predicate of the question sent to the service. |


## Parents

- [<plan\>](/dialog-domain-description-definition/domain/children/plan)


## Children

- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition/)


## Behaviour
An <invoke_service_query/> element calls for a query to be sent to a service, which (if successful) returns an answer.

The answer first becomes known to the system, and if the system knows the answer and the question is a goal question, this will trigger the system providing the answer to the user.


## Examples
### Invoke service query for getting the price of a trip.

```xml
<invoke_service_query type="wh_question" predicate="price"/>
```

### Invoke service query for checking if a person needs a visa.

```xml
<invoke_service_query type="yn_question">
  <proposition predicate="need_visa"/>
</invoke_service_query>
```
