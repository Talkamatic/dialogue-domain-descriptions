# Ask Feature
## Definition
```xml
<ask_feature predicate="p" kpq="true">
```

The element that represents a question about a feature of an
individual, that should be asked when using incremental search for
finding an individual answer to a question.

Attribute | Type | Description |
--- | --- | --- |
predicate | string | Required. The predicate must be enumerated in the ontology, and be indicated as `feature-of` the predicate of the over-arching findout.|
kpq | boolean | Optional. Indicates if the question of the ask feature should be asked as a Knowledge Precondition Question|

## Parents
- [<parameters\>](/dialog-domain-description-definition/domain/children/parameters)

## Children
None.


## Behaviour

An `ask\_feature` is used in combination with incremental search. Each
`ask\_feature`represents a question that should be asked in order to
find the answer to the question that is subject to incremental search.

"KPQ" stands for Knowledge Precondition Question, and asks a question
on the form "Do you know ...", for instance "Do you know in what city
she lives?". The question can then be answered with "Yes", "No" or a
resolving answer to the embedded question ("Gothenburg", "London" etc.).

## Examples
### A Ask Feature corresponding to the question "In what city does the person live?"

```xml
<ask_feature predicate="person_city"/>
```

### A KPQ Ask Feature corresponding to the question "Do you know in what city the person lives?"

```xml
<ask_feature predicate="person_city" kpq="true"/>
```
