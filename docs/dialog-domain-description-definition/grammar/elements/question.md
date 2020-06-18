# Question
## Definition
```xml
<question speaker="speaker" predicate="predicate_name" type="type">
```

The grammar entry of a question asked by the system or the user.

| Attributes | Type | Description |
| --- | --- | --- |
| speaker | string | Required. Specifies the speaker of the utterance. Available options: <ul><li>system</li><li>user</li><li>all</li></ul> |
| predicate | string | Required. Specifies the name of the predicate to which the grammar entry refers. Predicate names are written using lowercase separated by underscores, e.g. 'current_temperature'. |
| type | string |  Required only when speaker is system. Specifies which type of question is asked by the system. Available options: <ul><li>wh_question</li></ul> |

<!-- The other options to type?? -->

## Children

- [<one-of\>](/dialog-domain-description-definition/grammar/children/one-of)
    - [<item\>](/dialog-domain-description-definition/grammar/children/item)
        - [<slot\>](/dialog-domain-description-definition/grammar/children/slot)
        - [<vp\>](/dialog-domain-description-definition/grammar/children/vp)
            - [<infinitive\>](/dialog-domain-description-definition/grammar/children/vp)
            - [<imperative\>](/dialog-domain-description-definition/grammar/children/vp)
            - [<ing-form\>](/dialog-domain-description-definition/grammar/children/vp)
            - [<object\>](/dialog-domain-description-definition/grammar/children/vp)

## Behaviour

The <question\> element in the grammar defines the way in which the system and users can speak about a given question. The attribute `predicate` indicates which predicate in the ontology that the grammar entry is for, the attribute `speaker` specifies the speaker of the question, and the attribute `type` specifies the type of question when `speaker` is set to `system`.

### `speaker` attribute choices:

#### User

Indicates that the <question\> element contains possible questions that the user can ask the system in order to **resolve** a [<goal\>](path/to/domain/goal) in [domain.xml](/domain).

#### System

Indicates that the <question\> element contains a phrase used by the system to ask about the `predicate` specified. It is prompted by a [<findout\>](path/to/domain/findout) in [domain.xml](/domain).

#### All

Indicates that the <question\> element contains a phrase used by both system and user in questions. Regardless of who is speaking, when asking or talking about a question of the specified `predicate`, they can use this phrase.

### `type` attribute choices:

#### Wh-question

Type of question that starts with or contains wh-words such as 'what', 'when', 'which', 'who', etc..

<!--#### Yes/No-question

???

#### Alt-question

??? -->

## Examples

### User

The user can ask for a phone number as following.

```xml
<question speaker="user" predicate="phone_number_of_contact">
  <one-of>
    <item>tell me a phone number</item>
    <item>what is <slot predicate="selected_contact" type="individual"/>'s number</item>
    <item>tell me <slot predicate="selected_contact" type="individual"/>'s number</item>
  </one-of>
</question>
```

### System

The system can ask for the name of the individual if the user has not specified it in the question above.

```xml
<question speaker="system" predicate="selected_contact" type="wh_question">whose number</question>
```

### All

Both the user and the system can use this phrase to ask about a phone number.

For example, to ask for a phone number, the user can say "What is the phone number?". When returning to discussing this question after talking about something else, the system can say "Returning to the phone number".

```xml
<question speaker="all" predicate="selected_contact">the phone number</question>
```
