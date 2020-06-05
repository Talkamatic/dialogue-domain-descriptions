# Individual
## Definition
```xml
<individual name="individual_name">
```

The grammar entry of an individual. Defines how the system and the user can speak about individuals.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. Should match the name of the corresponding individual in ontology. The individual names in <individual> elements are written using lowercase separated by underscores, e.g. 'set_temperature'. |

## Children

- [<one-of\>](/tdm_documentation/grammar/children/one-of)
    - [<item\>](/tdm_documentation/grammar/children/item)

## Behaviour

The <individual\> element in the grammar defines the way in which the system and users can speak about a given individual. The attribute `name` indicates which individual in the ontology the grammar entry is for. Individuals are typically nouns or names of e.g. places, people, etc.

An individual entry in the grammar should contain at least one phrase which can be used to refer to the individual in question. It is also possible to specify multiple ways of referring to the same individual. Multiple options, when used, are given using the [<one-of\>](/tdm_documentation/grammar/children/one-of) tag, where each alternative expression is an [<item\>](/tdm_documentation/grammar/children/item).

## Examples

### Basic individual entry.

```xml
<individual name="london">London</individual>
```

### Individual entry with [<one-of\>](/tdm_documentation/grammar/children/one-of) and [<item\>](/tdm_documentation/grammar/children/item).

```xml
<individual name="united_kingdom">
  <one-of>
    <item>The UK</item>
    <item>United Kingdom</item>
    <item>Great Britain</item>
  </one-of>
</individual>
```
