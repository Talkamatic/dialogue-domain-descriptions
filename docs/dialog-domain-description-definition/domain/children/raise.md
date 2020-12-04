# Raise
## Definition
```xml
<raise question_type="type" predicate="p">
```

Defines a question that should be asked. In contrast with [findout](/dialog-domain-description-definition/domain/children/findout), the question does not have to be answered. In contrast with [bind](/dialog-domain-description-definition/domain/children/bind), the question is explicitly asked.


Attribute | Type | Description |
--- | --- | --- |
question\_type | string | Optional. Defaults to `wh_question`, but can be one of `goal`, `wh_question`, `alt_question` or `yn_question`. |
predicate | string | Optional. Required if question\_type is `wh_question` or `yn_question`.|
allow\_answer\_from\_pcom | string | Optional. Defaults to `false`. If set to `true`, this allows TDM to recycle an old answer that the user has previously provided. |

## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

## Children
- [<alt\>](/dialog-domain-description-definition/domain/children/alt)


## Behaviour

Defines a question that should be asked by the system, but not necessarily answered. Can be used for optional parameters.

## Examples
### A raise to ask the user what they want to do

```xml
  <raise type="goal"/>
```

### A raise about a WH question, "which colour would you like?"

```xml
  <raise type="wh_question" predicate="colour"/>
```

### A raise about a Yes/No question, "Would you like some fries with that?"

```xml
  <raise type="yn_question" predicate="side_order_fries"/>
```


### A raise about an alt question, "Would you like to calculate the monthly payment or would you like to know the interest rate?"

```xml
<raise type="alt_question">
    <alt>
        <resolve type="wh_question" predicate="monthly_payment"/>
    </alt>
    <alt>
        <resolve type="wh_question" predicate="interest_rate"/>
    </alt>
</findout>
```
