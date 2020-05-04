<span style="font-size: 2em">**One-of**</span>
## Definition
```xml
<item>
```

The <one-of\> grammar entry. Each <one-of\> tag contains a set of <item\> tags that can be used by the system or the user to speak about the parent element.

## Parents

- [<action\>](/tdm_documentation/grammar/elements/action)    
- [<question\>](/tdm_documentation/grammar/elements/question)

## Children

- [<item\>](/tdm_documentation/grammar/children/item)
    - [<slot\>](/tdm_documentation/grammar/children/slot)
    - [<vp\>](/tdm_documentation/grammar/children/vp)
        - [<infinitive\>](/tdm_documentation/grammar/children/vp)
        - [<imperative\>](/tdm_documentation/grammar/children/vp)
        - [<ing-form\>](/tdm_documentation/grammar/children/vp)
        - [<object\>](/tdm_documentation/grammar/children/vp)

## Behaviour

In the grammar, the <one-of\> tag is used to provide a number of ways in which the system and the user can speak about actions, questions, answers, reports, and individuals. It is the child of these aforementioned parent elements in the cases where these elements should have more than one possible phrase that can be used to speak about them. It has no attributes.

<one-of\> tags always contain [<item\>](/tdm_documentation/grammar/children/item) tags that each contain one phrase that can be used by the system or user to speak about the parent element that it belongs to. This parent element could be an action, a question, an answer, a report, or an individual.

## Examples

**Action example with three types of <item\> tags: basic, with <slot\>, and with <vp\>.**

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