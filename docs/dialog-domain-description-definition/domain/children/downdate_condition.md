# Downdate Condition
## Definition
```xml
<downdate_condition>
```

The element that specifies the conditions for downdating a particular perform goal. Downdating in TDM lingo means that the goal has been fulfilled, and that the plan can be stopped from executing.

Attribute | Type | Description |
--- | --- | --- |

## Parents
- [<goal\>](/dialog-domain-description-definition/domain/elements/goal)

## Children
- [<has\_value\>](/dialog-domain-description-definition/domain/children/has_value)
- [<is\_shared\_fact\>](/dialog-domain-description-definition/domain/children/is_shared_fact)
    - [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)

## Behaviour
If the condition embedded in a downdate\_condition element evaluates to true, the goal is considered to be fulfilled, and the goal is downdated -- which means that the plan associated with the goal will no longer be running. More than one downdate\_condition can be specified for each goal. If more than one condition is present, they will be treated as a logical or: any condition evaluated to true is enough for downdating the goal.

## Examples
### Downdate Condition for defining that once the departure time of a flight is known, the goal is considered to be fulfilled:

```xml
<downdate_condition>
    <has_value predicate="flight_departure"/>
</downdate_condition>
```

**Downdate_condition for defining that if the flight departure is late, the goal is considered to be fulfilled:**

```xml
<downdate_condition>
    <is_shared_fact>
          <proposition predicate="flight_departure" value="late"/>
    </is_shared_fact>
</downdate_condition>
```
