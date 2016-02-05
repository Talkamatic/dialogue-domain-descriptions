# Step 1. Create the boilerplate

First we need to create the DDD boilerplate.

```bash
mkdir ddd_root; cd ddd_root 
tdm_create_app.py BasicAction basic_action
```

Before your DDD can be used, it needs to be built.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
```

To make sure your DDD and all dependencies are working as intended, let's run interaction tests.

```bash
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```bash
Ran 1 test in 0.386s

OK
```

The test reports OK. We're ready to start adding dialogue to our DDD. 

# Step 2. Interaction test

Since we're working test driven, let's add an interaction test first.

Interaction tests verifiy the dialogue, providing user utterances and specifying the expected system responses.

Modify `basic_action/test/interaction_tests_eng.txt`, add a test for the new dialogue that we want to support. In this case, we want to make a call to John.

```diff
--- call first-name
S> What would you like to do?
U> call john
S> Calling John.
```

Let's build and run the tests again to verify that they fail.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

TDM will complain that it does not understand instead of placing the call to John.

```diff
call first-name:
basic_action/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ I heard you say call john. I don't understand. So, What would you like to do?
```

This happens because there's no notion of calling, and no notion of people, in the DDD.


# Step 3. Ontology

The ontology declares what users can do and talk about, much like header files. In order to call someone we need to add the notion of calling, and the notion of people, to the ontology.

Our boilerplate ontology is basically empty, in `basic_action/ontology.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="BasicActionOntology">
</ontology>
```

We extend it with an action to make calls, a contact `sort` and a predicate `selected_contact` so that we can select an individual of our contact sort. A dynamic sort means its individuals are decided during run time, through the service interface.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="BasicActionOntology">
  <action name="call"/>
  <sort name="contact" dynamic="true"/>
  <predicate name="selected_contact" sort="contact"/>
</ontology>
```

Let's build and run the tests again to see if we missed something.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
```

We receive a warning when generating the grammar.

```diff
Building GF 3.3 for application 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
[eng] Generating GF 3.3 grammar.
Missing grammar entry: How do speakers talk about the action call? Specify the utterance:

  <action name="call">call</action>

Alternatively, you can specify several possible utterances in a list:

  <action name="call">
    <one-of>
      <item>call one way</item>
      <item>call another way</item>
      <item>call <slot predicate="city" type="individual"/></item></one-of>
  </action>
[eng] Asserting that included grammars are lower case...Done.
[eng] Finished generating GF 3.3 grammar.
[eng] Building GF 3.3 grammar.
[eng] Finished building GF 3.3 grammar.
[eng] Converting GF 3.3 grammar to python format...Done.
[eng] Text-only, skipped building ASR language model.
[eng] Copying build results from 'build/eng' to application directory...Done.
Finished building GF 3.3 for application 'basic_action'.
```

Apparently, ontology entries require their corresponding grammar entries.

But the build still seems to have succeeded. What happens if we run the tests?

```bash
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

No difference, apparently.

```diff
call first-name:
basic_action/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ I heard you say call john. I don't understand. So, What would you like to do?
```

How about that grammar entry?


# Step 4. Grammar

The grammar defines what our users and system can say. Our previous build attempt told us to add an entry for the `call` action. Let's look at the boilerplate, in `basic_action/grammar/grammar_eng.xml`.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="top">main menu</action>
  <action name="up">go back</action>
</grammar>
```

It contains entries for the default actions `top` and `up`. For now, let's extend it with the `call` action.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="top">main menu</action>
  <action name="up">go back</action>
  <action name="call">call</action>
</grammar>
```

Let's build and test.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```diff
call first-name:
basic_action/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ The function is not implemented.
```

TDM replies! It means we did something right but apparently we need to implement the functionality as well. We need to add a plan to our domain


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

We get the top goal for free. Remember its grammar entry `main menu`. This is the only goal on TDM's agenda at startup. It will make TDM ask us which goal we want to achieve. Remember the corresponding default interaction test.

```diff
--- main menu
S> What would you like to do?
```

Anyway, let's add a new goal and plan, corresponding to our `call` action and `selected_contact` predicate. Extend the domain.

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
      <dev_perform action="Call" device="BasicActionDevice" postconfirm="true"/>
    </plan>
    <postcond><device_activity_terminated action="Call"/></postcond>
  </goal>
</domain>
```

Build.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
```

```diff
Building GF 3.3 for application 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
[eng] Generating GF 3.3 grammar.
Missing grammar entry: How does the system ask about selected_contact?

Example:

  <question speaker="system" predicate="selected_contact" type="wh_question">what is selected contact</question>


[eng] Asserting that included grammars are lower case...Done.
[eng] Finished generating GF 3.3 grammar.
[eng] Building GF 3.3 grammar.
[eng] Finished building GF 3.3 grammar.
[eng] Converting GF 3.3 grammar to python format...Done.
[eng] Text-only, skipped building ASR language model.
[eng] Copying build results from 'build/eng' to application directory...Done.
Finished building GF 3.3 for application 'basic_action'.
```

We got a new warning about a missing grammar entry. When referencing a predicate in a plan, we apparently need to specify its grammar entry. Since we're using a findout, the grammar entry is to define how TDM should speak the corresponding `question`. Let's extend the grammar.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="top">main menu</action>
  <action name="up">go back</action>
  <action name="call">call</action>
  <question speaker="system" predicate="selected_contact" type="wh_question">who do you want to call</question>
</grammar>
```

Build and test.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```diff
call first-name:
basic_action/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ Who do you want to call?
```

TDM replies again, great! But it didn't understand John. Actually, TDM's builtin robust parser ignored "John", finding the closest grammar match "call" instead.

We need to add an entity recognizer to our service interface. It needs to recognize entities of our `contact` sort.


# Step 6. Service interface

The service interface is written in python, in `basic_action/device.py`. This gives us freedom when implementing the entity recognizer, but it's under great responsibility. We can unexpectedly affect performance and stability if we're not careful. This entity recognizer should however be simple.

Let's check the boilerplate.

```python
class BasicActionDevice:
    pass
```

Totally empty, ok. Let's add the recognizer.

```python
from tdm.tdmlib import EntityRecognizer

class BasicActionDevice:
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": "0707192837",
    }
    class ContactRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
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

Let's also modify our grammar to allow the one-shot call.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="top">main menu</action>
  <action name="up">go back</action>
  <action name="call">
    <one-of>
      <item>call</item>
      <item>call <slot sort="contact"/></item>
    </one-of>
  </action>
  <question speaker="system" predicate="selected_contact" type="wh_question">who do you want to call</question>
</grammar>
```

Build and test.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```diff
DeviceError: unknown device action: Call
```

Great, TDM appears to understand John. It wants to execute the `call` action using our service interface, but could not find it. Let's add it.

```python
from tdm.tdmlib import EntityRecognizer, DeviceAction

class BasicActionDevice:
    CONTACT_NUMBERS = {
        "John": "0701234567",
        "Lisa": "0709876543",
        "Mary": "0706574839",
        "Andy": "0707192837",
    }
    class Call(DeviceAction):
        PARAMETERS = ["selected_contact.grammar_entry"]
        def perform(self, selected_contact):
            number = self.device.CONTACT_NUMBERS[selected_contact]
            # TODO: Implement calling
            success = True
            return success
    class ContactRecognizer(EntityRecognizer):
        def recognize_entity(self, string):
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

Since we didn't modify any XML files since the last build, we don't need to build again until testing.

```bash
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```diff
Exception: failed to generate report(DeviceResultProposition(Call, [selected_contact(_contact_1_)], True, None), application_name='basic_action')
```

It still errors, but the error is new. Now that the action is executed, TDM tries to report it to the user. This happens because we said so in the plan. Remember `postconfirm="true"` in the `dev_perform` entry of the plan?

```xml
      <dev_perform action="Call" device="BasicActionDevice" postconfirm="true"/>
```

Let's add the `report` grammar entry. We can reference the `selected_contact` predicate since its part of the `findout` entries of the plan.

```xml
<?xml version="1.0" encoding="utf-8"?>
<grammar>
  <action name="top">main menu</action>
  <action name="up">go back</action>
  <action name="call">
    <one-of>
      <item>call</item>
      <item>call <slot sort="contact"/></item>
    </one-of>
  </action>
  <question speaker="system" predicate="selected_contact" type="wh_question">who do you want to call</question>
  <report action="Call" status="ended">calling <slot predicate="selected_contact"/>.</report>
</grammar>
```

Build and test.

```bash
tdm_build.py -p basic_action_project -text-only -L eng
tdm_test_interactions.py -p basic_action_project -L eng -f basic_action/test/interaction_tests_eng.txt
```

```diff
Ran 1 test in 1.202s

OK
```

Success!


# Step 7. How to continue

This tutorial has illustrated how to implement the [basic action example](examples#basic-action).

In order to continue, go to the [examples](examples) section to find an example similar to your desired functionality. Steal the best ideas from there, adjusting them for yor domain. Remember to work test driven, adding a test first, then making it work.
