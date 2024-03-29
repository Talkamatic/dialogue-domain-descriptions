# Findout
## Definition
```xml
<findout question_type="type" predicate="p">
```

The element defines a question that should be answered, either by the
user, or by some service connected to TDM capable of answering it.


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


## Examples
### A findout to ask the user what they want to do

```xml
  <findout type="goal"/>
```

### A findout for a WH question, "which colour would you like?"

```xml
  <findout type="wh_question" predicate="colour"/>
```

### A findout for a Yes/No question, "Would you like some fries with that?"

```xml
  <findout type="yn_question" predicate="side_order_fries"/>
```

### A findout for a WH question, "What is your destination?", where the answer can be recycled from old answers

```xml
  <findout type="wh_question" predicate="destination" allow_answer_from_pcom="true"/>
```

### A findout for an alt question, "Would you like to calculate the monthly payment or would you like to know the interest rate?"

```xml
<findout type="alt_question">
    <alt>
        <resolve type="wh_question" predicate="monthly_payment"/>
    </alt>
    <alt>
        <resolve type="wh_question" predicate="interest_rate"/>
    </alt>
</findout>
```

### A findout for a yes/no question, "Should I connect you?"

```xml
<findout type="yn_question">
    <perform action="do_call_contact_from_history"/>
</findout>
```
