# Parameters
## Definition
```xml
<parameters question_type="type" predicate="p">
```

The element defines parameters to a particular question.


Attribute | Type | Description |
--- | --- | --- |
verbalize | boolean | Optional. Describes whether a question should be verbalized or not by the system.|
incremental | boolean | Optional. If set to true, the question is subject to "incremental search", i.e. that the answer to the question is specified step-by-step by the user |
graphical_type | string | Optional. For historical reasons, the graphical type of a question must be set to "list" for incremental search to work.
allow\_goal\_accommodation | boolean | Optional.|
max\_spoken\_alts | integer | Optional. The maximum number of possible answers the the question that are read out to the user. Used in connection with incremental search. |
max\_reported\_hit\_count | integer | Optional. The maximum number of hits that are reported to the user. Used in connection with incremental search. |
source | string | Optional. One of the values "domain" or "service" is expected. Used in connection with incremental search. |

## Parents
- [<domain\>](/dialog-domain-description-definition/domain/elements/domain)

## Children
- [<ask_feature\>](/dialog-domain-description-definition/domain/children/ask_feature)


## Behaviour


## Examples
### A parameter set designed to do incremental search for a person.

The question that is supposed to get an answer from a findout is the WH-question over the predicate "person". The parameter source is set to service, which means that a http service query will be used to find possible answers to the question. Incremental search is activated. The maximum number of hits that will be reported to the user is 10.

```xml
  <parameters question_type="wh_question" predicate="person" graphical_type="list"
              source="service" incremental="true" max_reported_hit_count="10">
    <ask_feature predicate="person_name"/>
    <ask_feature predicate="person_city" kpq="true"/>
    <ask_feature predicate="person_area"/>
  </parameters>
```
