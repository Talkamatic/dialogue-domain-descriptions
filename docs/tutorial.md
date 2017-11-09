# Step 1. Create the boilerplate

First we need to create the DDD boilerplate.

```bash
mkdir ddd_root; cd ddd_root 
tdm create-ddd basic_action
```

Before your DDD can be used, it needs to be built.

```bash
tdm build
```

To make sure your DDD and all dependencies are working as intended, let's run interaction tests.

```bash
tdm test eng
```

```bash
Ran 1 test in 0.386s

OK
```

The test reports OK. We're ready to start adding dialogue to our DDD. 

# Step 2. Interaction test

Since we're working test driven, let's add an interaction test first.

Interaction tests verifiy the dialogue, providing user utterances and specifying the expected system responses.

Modify `basic_action/test/interaction_tests_eng.txt`, add a test for the new dialogue that we want to support. We proceed one step at a time, starting with a very simple dialogue.

```diff
--- call
S> What would you like to do?
U> call
S> Who do you want to call?
```

Let's run the tests again to verify that they fail. (We don't need to rebuild after only modifying tests.)

```bash
tdm test eng
```

TDM will complain that it does not understand instead the user.

```diff
On line 7 of basic_action/test/interaction_tests_eng.txt,
expected:
  S> Who do you want to call?

but got:
  S> I heard you say call. I don't understand. So, What would you like to do?
```

This happens because there's no notion of calling in the DDD.


# Step 3. Ontology

The ontology declares what users can do and talk about, much like header files. In order to call someone we need to add the notion of calling, and the notion of people, to the ontology.

Our boilerplate ontology is basically empty, in `basic_action/ontology.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="BasicActionOntology">
</ontology>
```

We extend it with an action to make calls:

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="BasicActionOntology">
  <action name="call"/>
</ontology>
```

Let's build and run the tests again to see if we missed something.

```bash
tdm build
```

We now receive a warning.

```diff
Building generated grammar for DDD 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
Not using RASA NLU, will not clean RASA build directories.
[eng] Generating grammar.

Missing grammar entry: How do speakers talk about the action 'call'? Possible contents of the <action> element:

  <verb-phrase>
  <noun-phrase>
  <one-of>
[eng] Asserting that language grammar is lower case...Done.
[eng] Finished generating grammar.
[eng] Building generated grammar.
[eng] Finished building generated grammar.
[eng] Not using RASA NLU, will not generate and build RASA models.
[eng] Not using word list correction, will not generate word list.
[eng] No ASR specified, will not build language model.
Finished building generated grammar for DDD 'basic_action'.
```

Apparently, ontology entries require their corresponding grammar entries.

# Step 4. Grammar

The grammar defines what our users and system can say. Our previous build attempt told us to add an entry for the `call` action. Let's extend `basic_action/grammar/grammar_eng.xml` with the `call` action.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="call">
    <verb-phrase>
      <verb ref="call"/>
    </verb-phrase>
  </action>

  <lexicon>
    <verb id="call">
      <infinitive>call</infinitive>
    </verb>
  </lexicon>
</grammar>
```

This grammar definition describes that the action `call` can be referenced with a verb phrase containing the verb `call`. It also contains a lexicon describing the grammar of `call` in English. We only need to specifiy the infinitive form for the verb; the other forms, such as imperative, are derived automatically.

Let's build and test.

```bash
tdm build
tdm test eng
```

```diff
On line 7 of basic_action/test/interaction_tests_eng.txt,
expected:
  S> Who do you want to call?

but got:
  S> The function is not implemented.
```

TDM replies! It means we did something right but apparently we need to implement the functionality as well. We need to add a plan for calling.

# Step 5. Plan

Plans group together what our users can talk about. The plan is executed in order to reach a goal, for example to perform an action. When talking about something in the plan, TDM infers which goal is being implied and puts it at the top of the agenda.

Let's check the boilerplate, in `basic_action/domain.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<domain name="BasicActionDomain" is_super_domain="true">
  <goal type="perform" action="top">
    <plan>
      <forget_all/>
      <findout type="goal"/>
    </plan>
  </goal>
</domain>
```

We get the top goal for free. This is the only goal on TDM's agenda at startup. It will make TDM ask us which goal we want to achieve. Remember the corresponding default interaction test.

```diff
--- main menu
S> What would you like to do?
```

Anyway, let's add a new goal and plan, corresponding to our `call` action. Extend the domain.

```xml
<?xml version="1.0" encoding="utf-8"?>
<domain name="BasicActionDomain" is_super_domain="true">
  <goal type="perform" action="top">
    <plan>
      <forget_all/>
      <findout type="goal"/>
    </plan>
  </goal>
  <goal type="perform" action="call">
    <plan>
      <findout type="wh_question" predicate="selected_contact"/>
      <dev_perform action="Call" postconfirm="true"/>
    </plan>
    <postcond><device_activity_terminated action="Call"/></postcond>
  </goal>
</domain>
```

In `ontology.xml`, we also need to add the `selected_contact` predicate and its sort:

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="BasicActionOntology">
  <action name="call"/>
  <sort name="contact" dynamic="true"/>
  <predicate name="selected_contact" sort="contact"/>
</ontology>
```

A dynamic sort means its individuals are decided during run time, through the service interface.

Now build the DDD.

```bash
tdm build
```

```diff
[eng] Cleaning build directory u'build/eng'...Done.
[eng] Generating GF 3.7 grammar.

Missing grammar entry: How does the system ask about 'selected_contact'?

Example:

  <question speaker="system" predicate="selected_contact" type="wh_question">
    <utterance>what is selected contact</utterance>
  </question>


[eng] Asserting that included grammars are lower case...Done.
[eng] Finished generating GF 3.7 grammar.
[eng] Building GF 3.7 grammar.
[eng] Finished building GF 3.7 grammar.
[eng] Text-only, skipped building ASR language model.
[eng] Copying build results from u'build/eng' to ddd directory...Done.
Finished building grammar with GF 3.7 for DDD 'basic_action'.
```

We got a new warning about a missing grammar entry. When referencing a predicate in a plan, we apparently need to specify its grammar entry. Since we're using a findout, the grammar entry is to define how TDM should speak the corresponding `question`. Let's extend `basic_action/grammar/grammar_eng.xml` with the following:

```xml
  <question speaker="system" predicate="selected_contact" type="wh_question">
    <utterance>who do you want to call</utterance>
  </question>
```

Build and test.

```bash
tdm build
tdm test eng
```

```diff
Ran 2 tests in 0.363s

OK
```

Everything works as expected.

# Step 6. Service interface

In the next step, we want the user to be able to reply to the question about who to call. We thus extend `basic_action/test/interaction_tests_eng.txt` accordingly:

```diff
--- call
S> What would you like to do?
U> call
S> Who do you want to call?
U> John
S> Calling John.
```

Test:

```bash
tdm test eng
```

```diff
On line 9 of basic_action/test/interaction_tests_eng.txt,
expected:
  S> Calling John.

but got:
  S> I heard you say John. I don't understand. So, Who do you want to call?
```

As can be seen, the system doesn't understand John. We need to add an entity recognizer to our service interface. It needs to recognize entities of our `contact` sort.

Check the boilerplate service interface in `basic_action/service_interface.xml`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<service_interface>
    <entity_recognizer name="BasicActionRecognizer">
        <target>
            <device_module device="BasicActionDevice"/>
        </target>
    </entity_recognizer>
</service_interface>
```

It already contains an entity recognizer that we can use directly. It's defined in `basic_action/device.py`, in plain python. This gives us freedom when implementing the entity recognizer, but it's under great responsibility. We can unexpectedly affect performance and stability if we're not careful. This entity recognizer should however be simple.

Let's check the boilerplate.

```python
from tdm.lib.device import DddDevice, EntityRecognizer


class BasicActionDevice(DddDevice):
    class BasicActionRecognizer(EntityRecognizer):
        """Entity recognizer for BasicAction"""

        def recognize(self, utterance, language):
            """Recognize entities in a user utterance, given the specified language.

            This method is responsible for finding all dynamic entities in the utterance. Its accuracy affects the
            behaviour of the dialogue system.

            Since the search is conducted during runtime, particular care should be taken to ensure that the method is
            accurate, robust and has sufficient performance.

            Args:
                utterance (str): The utterance to be searched. For example 'call John'.
                language  (str): The language code of the utterance according to the ISO 639-2/B standard.
                                 Exceptions are Swedish ('sv' instead of 'swe') and Italian ('it' instead of 'ita').

            Returns:
                list of dicts: Given the example utterance "call John", the following entity could be returned
                [
                    {
                        "sort": "contact",       # The sort must be declared in the ontology.
                        "grammar_entry": "John", # The grammar entry as it occurred in 'utterance'.
                        "name": "contact_john",  # [optional] Should be a globally unique identifier. Must never be
                                                 # found as is in a user utterance. Use for example the form Sort_ID
                                                 # (e.g. contact_john).
                    },
                ]
            """
            return []
```

And add the recognizer.

```python
from tdm.lib.device import DddDevice, EntityRecognizer

class BasicActionDevice(DddDevice):
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": None,
    }
    
    class BasicActionRecognizer(EntityRecognizer):
        def recognize(self, string, unused_language):
            result = []
            words = string.lower().split()
            for contact in self.device.CONTACT_NUMBERS.keys():
                if contact.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact
                    }
                    result.append(recognized_entity)
            return result
```

Build and test.

```bash
tdm build
tdm test eng
```

```diff
UnexpectedActionException: Expected one of the known actions [] but got 'Call'
```

Great, TDM appears to understand John. It wants to execute the `Call` action using our service interface, but could not find it. Let's add it to `basic_action/service_interface.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<service_interface>
    <action name="Call">
        <parameters>
            <parameter predicate="selected_contact" format="value"/>
        </parameters>
        <failure_reasons/>
        <target>
            <device_module device="BasicActionDevice"/>
        </target>
    </action>
    <entity_recognizer name="BasicActionRecognizer">
        <target>
            <device_module device="BasicActionDevice"/>
        </target>
    </entity_recognizer>
</service_interface>
```

If we build now...

```bash
tdm build
```

```diff
tdm.ddd.device_handler.MissingDeviceMethodException: The service interface defines actions [u'Call']. Expected to find [u'Call'] as 'DeviceAction' methods in device 'BasicActionDevice', but found []
```

TDM complains that the `Call` action is not found in `basic_action/device.py`. Let's add it:  

```python
from tdm.lib.device import DddDevice, EntityRecognizer, DeviceAction

class BasicActionDevice(DddDevice):
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": None,
    }
    
    class Call(DeviceAction):
        def perform(self, selected_contact):
            number = self.device.CONTACT_NUMBERS.get(selected_contact)
            # TODO: Implement calling
            success = True
            return success
            
    class BasicActionRecognizer(EntityRecognizer):
        def recognize(self, string, unused_language):
            result = []
            words = string.lower().split()
            for contact in self.device.CONTACT_NUMBERS.keys():
                if contact.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact
                    }
                    result.append(recognized_entity)
            return result
```

Build.

```bash
tdm build
```

```diff
Building generated grammar for DDD 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
Not using RASA NLU, will not clean RASA build directories.
[eng] Generating grammar.

Missing grammar entry: How does the system report that the device action 'Call' ended? Example:

  <report action="Call" status="ended">
    <utterance>performed Call</utterance>
  </report>


[eng] Asserting that language grammar is lower case...Done.
[eng] Finished generating grammar.
[eng] Building generated grammar.
[eng] Finished building generated grammar.
[eng] Not using RASA NLU, will not generate and build RASA models.
[eng] Not using word list correction, will not generate word list.
[eng] No ASR specified, will not build language model.
Finished building generated grammar for DDD 'basic_action'.
```

As can be seen, we need to add a grammar entry for the device action `Call`. This is required because we said so in the plan. Remember `postconfirm="true"` in the `dev_perform` entry of the plan?

Let's add a `report` grammar entry in `basic_action/grammar/grammar_eng.xml`. We can reference the `selected_contact` predicate since its part of the `findout` entries of the plan.

```xml
  <report action="Call" status="ended">
    <utterance>calling <individual predicate="selected_contact"/></utterance>
  </report>
```

Build and test.

```bash
tdm build
tdm test eng
```

```diff
Ran 2 tests in 0.363s

OK
```

Success!

# Step 7. One-shot utterances

The DDD so far handles very simple dialogues where the user enters one piece of information at a time. In order to support one-shot utterances such as "call John" containing several pieces of information (in this case an action and an answer regarding who to call), we need to extend the grammar. First we add a failing interaction test in `basic_action/test/interaction_tests_eng.txt`:

```bash
--- one-shot utterance
U> call John
S> Calling John.
```

Run the tests to verify that the new one fails.

```bash
tdm test eng
```

```bash
On line 13 of basic_action/test/interaction_tests_eng.txt,
expected:
  S> Calling John.

but got:
  S> I heard you say call John. I don't understand. So, What would you like to do?
```

We now add the following lines to `basic_action/grammar/grammar_eng.xml`:

```xml
  <request action="call">
    <utterance>call <individual sort="contact"/></utterance>
  </request>
```

The element `<request>` is used when defining things that the user can say to request that an action is to be performed. In contrast to `<action>`, `<request>` is user-specific and deals with whole utterances, including potential references to individuals. The element `<individual>` acts as a slot, showing that a certain place in the utterance refers to an individual.

Now build and test.

```bash
tdm build
tdm test eng
```

```bash
Ran 3 tests in 0.523s

OK
```

# Step 8. Adding a language

If you want to add support for a new language, the following steps are needed. First you need to modify the file `backend.config.json`. In the field `supported_languages`, add `"fre"` for French and/or `"dut"` for Dutch (separated by commas). Assuming we want to add support for French, the file contents are changed to

```json
{
    "supported_languages": [
        "eng",
        "fre"
    ]
}
```

Second, we need to create interaction tests for the new language. For French, we add the file `basic_action/test/interaction_tests_fre.txt` with translated contents:

```bash
--- main menu
S> Que voulez-vous faire?

--- call
S> Que voulez-vous faire?
U> appellez
S> Qui voulez-vous appeler?
U> André
S> J'appelle André.

--- one-shot utterance
U> appellez André
S> J'appelle André.
```

Make sure to save the interaction tests with UTF-8 encoding without byte-order mark (BOM) when using non-ASCII characters.

Next, we need to handle the language inside the entity recognizer. Modify the service interface at `basic_action/device.py` to handle French:

```python
# -*- coding: utf-8 -*-

from tdm.lib.device import EntityRecognizer, DeviceAction, DddDevice


class BasicActionDevice(DddDevice):
    JOHN = "contact_john"
    LISA = "contact_lisa"
    MARY = "contact_mary"
    ANDY = "contact_andy"

    PHONE_NUMBERS = {
        JOHN: "0701234567",
        LISA: "0709876543",
        MARY: "0706574839",
        ANDY: None,
    }

    CONTACTS_ENGLISH = {
        "John": JOHN,
        "Lisa": LISA,
        "Mary": MARY,
        "Andy": ANDY,
    }

    CONTACTS_FRENCH = {
        "Jean": JOHN,
        u"Élise": LISA,
        "Marie": MARY,
        u"André": ANDY,
    }

    CONTACTS = {
        "eng": CONTACTS_ENGLISH,
        "fre": CONTACTS_FRENCH,
    }

    class Call(DeviceAction):
        def perform(self, selected_contact):
            number = self.device.PHONE_NUMBERS.get(selected_contact)
            # TODO: Implement calling
            success = True
            return success

    class BasicActionRecognizer(EntityRecognizer):
        def recognize(self, string, language):
            result = []
            words = string.lower().split()
            contacts = self.device.CONTACTS[language]
            for contact_name, identifier in contacts.iteritems():
                if contact_name.lower() in words:
                    recognized_entity = {
                        "sort": "contact",
                        "grammar_entry": contact_name,
                        "name": identifier,
                    }
                    result.append(recognized_entity)
            return result
```

Make sure to save it with UTF-8 without BOM as well.

Finally, we need to create a grammar file for the new language. For French, we add the file `basic_action/grammar/grammar_fre.xml` with the following contents:

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="call">
    <verb-phrase>
      <verb ref="call"/>
    </verb-phrase>
  </action>

  <request action="call">
    <utterance>appellez <individual sort="contact"/></utterance>
  </request>

  <lexicon>
    <verb id="call">
      <infinitive>appeller</infinitive>
    </verb>
  </lexicon>

  <question speaker="system" predicate="selected_contact" type="wh_question">
    <utterance>qui voulez-vous appeler</utterance>
  </question>

  <report action="Call" status="ended">
    <utterance>j'appelle <individual predicate="selected_contact"/></utterance>
  </report>
</grammar>
```

Build and test. Note the changed language parameter for interaction testing.

```bash
tdm build
tdm test fre
```

```bash
Ran 3 tests in 0.509s

OK
```

# Step 9. How to continue

This tutorial has illustrated how to implement the [basic action example](examples#basic-action).

In order to continue, go to the [examples](examples) section to find an example similar to your desired functionality. Steal the best ideas from there, adjusting them for yor domain. Remember to work test driven, adding a test first, then making it work.
