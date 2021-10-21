# Hint
## Definition
```xml
<hint>
```

Defining a hint that should be given to the user in case they answer `icm:acc*neg` to a particular question.

Attribute | Type | Description |
--- | --- | --- |
None

## Parents
- [<parameters\>](/dialog-domain-description-definition/domain/elements/parameters)

## Children
- [<inform\>](/dialog-domain-description-definition/domain/children/inform)

## Behaviour
The `hint` parameter in a parameter set is presented to the user in case they reply to a question with an `icm:acc*neg` move, before the question is asked again. If there are more than one `hint` defined, they will be given in order, and when the last hint is reached, that hint will be repeated until the user answers the question. The chldren of a hint element can be any plan item, but it is recommended that the `inform` plan item is used, as this is the only one thoroughly tested.

## Examples
### Hint elements

Hints for giving two hints to the user if they say that they don't know the ingredient quantity question.

```xml
  <parameters predicate="ingredient_quantity">
    <hint>
      <inform insist="true">
          <proposition predicate="helpful_information" value="ingredient_quantity_hint_1"/>
      </inform>
    </hint>
    <hint>
      <inform insist="true">
          <proposition predicate="helpful_information" value="ingredient_quantity_hint_2"/>
      </inform>
    </hint>
  </parameters>
```
