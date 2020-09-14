# Parameters
## Definition
```xml
<goal type="..." ...>
```

Attribute | Type | Description |
--- | --- | --- |
type | string | Required. Needs to be one of `resolve` or `perform` .|
action | string | Optional. Needed if the type is `perform`. The action needs to be declared in `ontology.xml`. |
question_type | string | Optional. Needed if the type is `resolve`. Needs to be one of `wh_question` or `yn_question`. In case of an `yn_question` the goal needs a `proposition` child. |
predicate | string | Optional. Needed if the type is `wh_question`. The predicate needs to be declared in `ontology.xml`. |
accommodate\_without\_feedback | boolean | Optional.  Indicates whether the default system behavior to give feedback when accommodating the goal, e.g. uttering "Book a travel" in response to "From London to Paris tomorrow", should be disabled.
reraise\_on\_resume | boolean | Optional. Indicates whether the default system behavior to give feedback when reraising the goal, e.g. "Returning to booking a travel", should be disabled.
restart\_on\_completion | boolean | Optional. Indicates if the goal should be restarted immediately after completion. This can be handy when a dialogue system is designed to perform a single task again and again.
max\_answers | integer | Optional. Defines the maximum number of answers that the system can give, when the user asks a question about several alternatives at once, e.g. "How old are they?" By default, max\_answers has the value 1, meaning that user questions about several alternatives are not supported.
alternatives\_predicate | string | Optional. If max\_answers>1, alternatives_predicate is required and provides the name of predicate that distinguishes the alternatives, e.g. "person" if the question concerns several persons.


## Parents
- [<domain\>](/dialog-domain-description-definition/domain/elements/domain)

## Children
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<downdate\_condition\>](/dialog-domain-description-definition/domain/children/downdate_condition)
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)
- [<preferred\>](/dialog-domain-description-definition/domain/children/preferred)
- [<superaction\>](/dialog-domain-description-definition/domain/children/superaction)


## Behaviour

The element defines a goal, including the plan to achieve the goal. This is the
basic building block of a DDD. It defines a goal, which must be of one
of the types _perform_ or _resolve_. A perform goal indicates that
something should be performed, while a resolve goal indicates that a
question should be answered. Although there is nothing preventing the
plan of a perform goal to actually answer a question, it is considered
good practice to leave that to resolve goals.

## Examples
### A perform goal that will quietly be restarted

```xml
  <goal type="perform" action="adjust_temperature" reraise_on_resume="false">
    <plan>
      <findout type="wh_question" predicate="desired_temperature"/>
      <invoke_service_query type="wh_question" predicate="current_temperature"/>
      <invoke_service_action name="SetTemperature" postconfirm="true"/>
    </plan>
  </goal>

```
