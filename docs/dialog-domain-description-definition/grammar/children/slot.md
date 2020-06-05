# Slot
## Definition
```xml
<slot predicate="predicate_name">
```

The grammar entry of the verb phrase (VP) child of the <item\> element.

| Attributes | Type | Description |
| --- | --- | --- |
| predicate | string | Required. Specifies the name of the predicate from which the slot is filled. Predicate names are written using lowercase separated by underscores, e.g. 'current_temperature'. |

## Parents

- [<answer\>](/tdm_documentation/grammar/elements/answer)
- [<report\>](/tdm_documentation/grammar/elements/report)
- [<validity\>](/tdm_documentation/grammar/elements/validity)
<!--(Can it also be a part of a <question> or an <action> without <item> being between them? If not, should we maybe add these as parents with <item> under them otherwise, for clarity?-->
- [<item\>](/tdm_documentation/grammar/children/item)

## Behaviour

The <slot\> element in the grammar occurs inside its various parent tags and serves as a slot for data from the given predicate, which the system gets from the predicate's <question\> <!--(Can the slot be filled in other ways?)-->. Parent elements can contain multiple <slot\> elements if necessary. The <slot\> attribute `predicate` indicates which predicate that the slot gets its data from. 

## Examples

### <slot\> inside <item\> tags:

```xml
<action name="browse_restaurants">
   <one-of>
      ...
      <item>i want to browse <slot sort="type_food"/> restaurants</item>
      <item>browse <slot sort="type_food"/></item>
      <item>i would like to eat <slot sort="type_food"/></item>
      <item>i want <slot sort="type_food"/></item>
      <item>i want to eat <slot sort="type_food"/></item>
      ...
   </one-of>
</action>
```

### Multiple <slot\> tags inside an <answer\> tag:

```xml
<answer predicate="next_membership_level" speaker="system">you need <slot predicate="next_membership_points" type="individual"/> points to reach <slot predicate="next_membership_level" type="individual"/> level</answer>
```

### <slot\> inside a <report\> tag:

```xml
<report action="AddToBasketDairy" status="ended">Ok. We will add <slot predicate="selected_dairy"/> to the order.</report>
```

### <slot\> inside a <validity\> tag:

```xml
<validity name="CityValidity">invalid parameters <slot predicate="dest_city" type="individual"/></validity>
```
