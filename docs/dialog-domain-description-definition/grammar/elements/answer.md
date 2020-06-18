# Answer
## Definition
```xml
<answer speaker="speaker" predicate="predicate_name" polarity="polarity">
```

The grammar entry of an answer given by the system or the user.

| Attributes | Type | Description |
| --- | --- | --- |
| speaker | string |  Required. Specifies the speaker of the utterance. Available options: <ul><li>system</li><li>user</li></ul> |
| predicate | string | Optional. Specifies the name of the predicate to which the grammar entry refers. Predicate names are written using lowercase separated by underscores, e.g. 'current_temperature'. |
| polarity | string | Optional. Specifies whether an answer has positive or negative polarity. Available options: <ul><li>positive</li><li>negative</li></ul> |

## Children

- [<one-of\>](/dialog-domain-description-definition/grammar/children/one-of)
    - [<item\>](/dialog-domain-description-definition/grammar/children/item)
        - [<slot\>](/dialog-domain-description-definition/grammar/children/slot)

## Behaviour

The <answer\> element in the grammar defines the way in which the system and users can give answers to questions. The attribute `polarity` specifies whether the answer is positive or negative, the attribute `predicate` indicates which predicate in the ontology the grammar entry is for, and the attribute `speaker` specifies the speaker of the answer.

An answer entry in the grammar should cover the different ways in which the system and users can answer questions, such as different expressions and word choices. These options are given using the [<one-of\>](/dialog-domain-description-definition/grammar/children/one-of) tag, where each alternative expression is an [<item\>](/dialog-domain-description-definition/grammar/children/item), which in turn can contain [<slot\>](/dialog-domain-description-definition/grammar/children/slot) tags.

System answers can make use of the attribute `polarity` in situations where a question could have different answers depending on whether the answer is positive or negative. An example of this is the possible answers to the question "Are there rooms available?" from a user wanting to book a hotel room.

### `polarity` attribute choices:

#### Positive

Indicates that an answer about a particular predicate is of positive polarity, e.g. if the user asks whether they are qualified for membership and the answer is "Yes, you have 50 points and are qualified for membership". If there is a positive polarity answer for a predicate, there is typically a negative polarity answer present in the grammar as well.

#### Negative

Indicates that an answer about a particular predicate is of negative polarity, e.g. if the user asks whether they are qualified for membership and the answer is "No, you need 20 points to be qualified for membership".

### `speaker` attribute choices:

#### User
Indicates that the <answer\> element contains possible answers that the user can give the system in response to a system question prompted by a [<findout\>](path/to/domain/findout) in [domain.xml](/domain).

#### System
Indicates that the <answer\> element contains phrases used by the system to give an answer about the `predicate` specified. It is prompted by a [<invoke_service_query\>](path/to/domain/findout) in [domain.xml](/domain).

## Examples

#### User
This user <answer\> entry contains the ways in which a user can answer certain questions in a travel booking DDD, specifically how many passengers of a certain type to add, and the destination city that the user wants to travel to.

```xml
<answer speaker="user">
  <one-of>
    <item><slot predicate="passenger_quantity_to_add" type="individual"/> <slot sort="passenger_type"/></item>
    <item>to <slot predicate="dest_city"/></item>
  </one-of>
</answer>
```

#### System

This system <answer\> entry contains the phrase the system would use to answer a question from the user about the next membership level and its requirements.

```xml
<answer predicate="next_membership_level" speaker="system">you need <slot predicate="next_membership_points" type="individual"/> points to reach <slot predicate="next_membership_level" type="individual"/> level</answer>
```

The following <answer\> entries show an example of a positive and a negative polarity answer from the system to a user question concerning the availability of rooms for booking in a hotel.
```xml
<answer polarity="positive" predicate="rooms_available" speaker="system">There are rooms available</answer>

<answer polarity="negative" predicate="rooms_available" speaker="system">Unfortunately, there are no rooms available to book at this time</answer>
```
