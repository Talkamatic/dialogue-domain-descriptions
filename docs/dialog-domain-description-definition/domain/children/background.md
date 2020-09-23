# Background
## Definition
```xml
<background predicate="p"/>
```

Defining that a predicate should be used as background when asking or answering a question.

Attribute | Type | Description |
--- | --- | --- |
Predicate| String | The predicate over which the proposition used as background is defined.|

## Parents
- [<parameters\>](/dialog-domain-description-definition/domain/elements/parameters)

## Children
None

## Behaviour
The background parameters are passed to generation, so that it can be given as background to asking or answering a question.

NB! The order in which the background elements are defined decides the order of the background in the generated utterance. In other words it overrides the predicates in the slot definitions in the grammar.

## Examples
### Background elements for unit and ingredient

Background defined in order to be able to answer the question about quantity and ingredient in the following way: "You need 500 grams of flour".

```xml
  <parameters predicate="ingredient_quantity">
    <background predicate="unit"/>
    <background predicate="selected_ingredient"/>
  </parameters>
```
