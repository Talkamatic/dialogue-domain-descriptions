# Action
## Definition
```xml
<action name="action_name">
```

The grammar entry of an action. Defines how the system and the user can speak about and request actions.

Attribute | Type | Description |
--- | --- | --- |
name | string | Required. Should match the name of the corresponding action in ontology. The action names in <action> elements are written using lowercase separated by underscores, e.g. 'set_temperature'. |

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
The <action\> element in the grammar defines the way in which the system and users can speak about a given action. The attribute `name` indicates which action in the ontology the grammar entry is for.

An action entry in the grammar should cover the different ways a user could speak about the action, such as different expressions and word choices. These options are given using the [<one-of\>](/dialog-domain-description-definition/grammar/children/one-of) tag, where each alternative expression is an [<item\>](/dialog-domain-description-definition/grammar/children/item). [<item\>](/dialog-domain-description-definition/grammar/children/item) tags can contain [<vp\>](/dialog-domain-description-definition/grammar/children/vp) or [<slot\>](/dialog-domain-description-definition/grammar/children/slot) tags.

## Examples
### Action entry for setting an alarm with three different expressions:

```xml
<action name="set_alarm">
  <one-of>
    <item>set the alarm</item>
    <item>set alarm</item>
    <item>alarm</item>
  </one-of>
</action>
```
### Action entry containing expression with <slot\> tag:

```xml
<action name="set_alarm">
  <one-of>
    <item>set the alarm</item>
    <item>set alarm</item>
    <item>set the alarm to <slot predicate="time_to_set" type="individual"/></item>
  </one-of>
</action>
```
### Action entry containing expression with <vp\> tag:

```xml
<action name="set_alarm">
  <one-of>
    <item>
      <vp>
        <infinitive>set</infinitive>
        <imperative>set</imperative>
        <ing-form>setting</ing-form>
        <object>the alarm</object>
      </vp>
    </item>
    <item>set alarm</item>
    <item>set the alarm to <slot predicate="time_to_set" type="individual"/></item>
  </one-of>
</action>
```
