<span style="font-size: 2em">**VP**</span>
## Definition
```xml
<vp>
```

The grammar entry of the verb phrase (VP) child of the <item\> element.

| Attributes | Type | Description |
| --- | --- | --- |
| N/A | N/A | N/A |

## Parents

- [<item\>](/tdm_documentation/grammar/children/item)

## Children

- [<infinitive\>](/tdm_documentation/grammar/children/vp)
- [<imperative\>](/tdm_documentation/grammar/children/vp)
- [<ing-form\>](/tdm_documentation/grammar/children/vp)
- [<object\>](/tdm_documentation/grammar/children/vp)

## Behaviour

The <vp\> element in the grammar defines the way in which the system <!--(Is it also for the user?)--> can speak about a given <item\>. It defines a basic utterance for the <item\>'s parent element in three grammatical forms: infinitive, imperative, and ing-form <!--(gerund)--> to be used by the NLG <!--(Is it also for the user?)--> in generating expressions, such as for grounding.

<span style="font-size: 1.2em">**Children**</span>

**`<infinitive\>`**

Contains the infinitive form of the verb used in the <vp\>, e.g. "make" from the sentence "make a reservation".

**`<imperative\>`**

Contains the imperative form of the verb used in the <vp\>, e.g. "make" from the sentence "make a reservation".

**`<ing-form\>`**

Contains the ing-form (gerund) <!--(Could this also be a continuous form, or only gerund?)--> form of the verb used in the <vp\>, e.g. "making" from the sentence "making a reservation".

**`<object\>`**

Contains the object of the sentence in the <vp\>, e.g. "a reservation" from the sentence "make/making a reservation".

## Examples

```xml
<action name="make_reservation">
   <one-of>
     <item>
        <vp>
            <infinitive>make</infinitive>
            <imperative>make</imperative>
            <ing-form>making</ing-form>
            <object>a reservation</object>
        </vp>
     </item>
     <item>...</item>
   </one-of>
</action>
```