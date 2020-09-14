# Predicate
## Definition
```xml
<predicate name="r" sort="s"/>
```

A predicate ascribes some property to an individual. This individual is the argument of the predicate. A predicate requires its arguments to be of a specific sort. 

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. The name of the predicate. |
sort | string  | Required. The semantic sort of arguments to the predicate. |
feature_of | string | Optional. The predicate of which this predicate is a feature (if any). |


## Parents

- [<ontology\>](/dialog-domain-description-definition/ontology/ontology.md)


## Children

None.


## Behaviour

A predicate ascribes some property to an individual. This individual is the argument of the predicate. A predicate requires its arguments to be of a specific sort. 

If there is a sort `hour`, whose individuals are  integers in the range 0-23, there can be one predicate `current_hour`, and another one `alarm_hour`, of the sort `hour`. The first one is a part of the description of the current time, the sencond one i a part of the description of the current alarm time.

Predicates in TDM typically take a single argument of a specified sort (i.e. they have arity 1). Predicates that do not take an argument (arity 0), have sort `Boolean`.

Predicates can be features of other predicates. This is particularly useful for incremental search dialogue. For example, if each product belongs to a product category, one might want to search for products based on their category (among other things). To do this, the predicate for product category is defined as a feature of the predicate for products.

## Examples

### Name of person to call

```xml
<predicate name="name_to_call" sort="name">
```

### Selected product predicate, with a feature predicate for product category

```xml
<predicate name="selected_product" sort="product"/>

<predicate name="selected_category" sort="category" feature_of="selected_product"/>
```

