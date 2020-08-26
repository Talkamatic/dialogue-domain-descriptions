# Assume System Belief
## Definition
```xml
<assume_system_belief>
  <proposition predicate="p" value="a"/>
</assume_system_belief>
```

The plan item that assumes a proposition. The proposition will be a part of the system's private beliefs.

Attribute | Type | Description |
--- | --- | --- |
None. | - | -|


## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)

## Children
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)

## Behaviour
Using the <assume_system_belief/> element has the effect of adding the assumed proposition to the private beliefs of the system. This means that it is available as an answer to a question, or as a parameter to a service call. Assumptions will not be validated by user defined validators, and only propositions over individuals already known to the system can be made (e.g. static individuals).


## Examples
### Assume_System_Belief element for assuming that the user is an adult

```xml
<assume_system_belief>
  <proposition predicate="user_age_category" value="adult"/>
</assume_system_belief>
```
