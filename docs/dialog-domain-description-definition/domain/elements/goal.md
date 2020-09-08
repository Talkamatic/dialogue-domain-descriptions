# Parameters
## Definition
```xml
<goal type="..." ...>
```

Attribute | Type | Description |
--- | --- | --- |
type | string | Required. Needs to be one of ```resolve``` or ```perform``` .|
action | string | Optional. Needed if the type is ```perform```. The action needs to be declared in ```ontology.xml```. |
question_type | string | Optional. Needed if the type is ```resolve```. Needs to be one of ```wh_question``` or ```yn_question```. In case of an ```yn_question``` the goal needs a ```proposition``` child. |
predicate | string | Optional. Needed if the type is ```wh_question```. The predicate needs to be declared in ```ontology.xml```. |
accommodate\_without\_feedback | boolean | Optional. Indicates wether the goal should be _accommodated_ (inferred as a goal by TDM) without feedback.
reraise\_on\_resume | boolean | Optional. Indicates wether the goal can be reraised by TDM without feedback ("Returning to ...").
restart\_on\_completion | boolean | Optional. Indicates if the goal should be restarted immediately after completion. This can be handy when a dialogue system is designed to perform a single task again and again.
max\_answers | integer | Optional. Decides the maximum number of answers that TDM can give, when the user asks about the possible alternatives during incremental search.
alternatives\_predicate | string | Optional. The predicate that is used for querying a service for possible answers to a question in the plan.


## Parents
- [<domain\>](/dialog-domain-description-definition/domain/elements/domain)

## Children
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<postcond\>](/dialog-domain-description-definition/domain/children/postcond)
- [<downdate\_condition\>](/dialog-domain-description-definition/domain/children/downdate_condition)
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)
- [<preferred\>](/dialog-domain-description-definition/domain/children/preferred)
- [<superaction\>](/dialog-domain-description-definition/domain/children/superaction)


## Behaviour

The element defines a goal element, including a plan. This is the
basic building block of a DDD. It defines a goal, which must be of one
of the types _perform_ or _resolve_. A perform goal indicates that
something should be performed, a resolve goal indicates that a
question should be answered. Although there is nothing preventing the
plan of a perform goal to actually answer a question, it is considered
good practice to leave that to resolve goals.

The attributes that need to be specified are dependent on the type of
the goal. In the case of a resolve goal, the developer needs to
specify the question that the system should get as goal to answer,
using the ```question_type``` and ```predicate``` attributes (only
custom predicate questions can be answered by the system). In the case of a perform goal, the developer needs to use the ```action``` attribute to give name the action that is performed by the contained ```plan```.


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
