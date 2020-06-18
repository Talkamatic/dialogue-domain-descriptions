# Item
## Definition
```xml
<item>
```

The grammar entry of items. Each item contains a separate phrase that can be used by the system or the user to speak about the parent element.

## Parents

- [<one-of\>](/dialog-domain-description-definition/grammar/children/one-of)

## Children

- [<slot\>](/dialog-domain-description-definition/grammar/children/slot)
- [<vp\>](/dialog-domain-description-definition/grammar/children/vp)
    - [<infinitive\>](/dialog-domain-description-definition/grammar/children/vp)
    - [<imperative\>](/dialog-domain-description-definition/grammar/children/vp)
    - [<ing-form\>](/dialog-domain-description-definition/grammar/children/vp)
    - [<object\>](/dialog-domain-description-definition/grammar/children/vp)

## Behaviour

In the grammar, <item\> is the child of the <one-of\> tag. It has no attributes and can contain [<slot\>](/dialog-domain-description-definition/grammar/children/slot) tags.

Each <item\> tag contains one phrase that can be used by the system or user to speak about the parent element that it belongs to. This parent element could be an [<action\>](/dialog-domain-description-definition/grammar/elements/action), a [<question\>](/dialog-domain-description-definition/grammar/elements/question), an [<answer\>](/dialog-domain-description-definition/grammar/elements/answer), a [<report\>](/dialog-domain-description-definition/grammar/elements/report), or an [<individual\>](/dialog-domain-description-definition/grammar/elements/individual).

<item\> tags can also contain a [<vp\>](/dialog-domain-description-definition/grammar/children/vp) tag, which specifies the verb of an expression in different grammatical moods and inflected forms for use in Grammatical Framework to generate grammatical forms. See [<vp\>](/dialog-domain-description-definition/grammar/children/vp) for further information.

## Examples

### Action example with three types of <item\> tags: basic, with <slot\>, and with <vp\>.

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
