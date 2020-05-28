# Tutorial

This tutorial covers the steps needed to design a basic dialog domain description (DDD).

## Step 1. Create the boilerplate

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

## Step 2. Interaction test

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


## Step 3. Ontology

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
Generating models for DDD 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
[eng] Generating grammar.

Missing grammar entry: How do speakers talk about the action 'call'? Possible contents of the <action> element:

  <verb-phrase>
  <noun-phrase>
  <one-of>
[eng] Finished generating grammar.
Finished generating models for DDD 'basic_action'.
Training models for DDD 'basic_action'.
[eng] Asserting that language grammar is lower case...Done.
[eng] Compiling generated grammar.
[eng] Finished compiling generated grammar.
[eng] No ASR specified, will not build language model.
[eng] Copying ASR language modules from '/private/tmp/ddd_root/basic_action/grammar/build/eng' to ddd directory...Done.
[eng] Not using word list correction, will not generate word list.
```

Apparently, ontology entries require their corresponding grammar entries.

## Step 4. Grammar

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

## Step 5. Plan

A plan is a description of the steps required by the system in order to fulfill a goal. For example, in order to make a phone call, the system first needs to find out who to call. (Typically, a goal is something that is expressed by the user in dialog, but it can also be activated by an event.)

Although plans are sequences of instructions, designing a dialog plan is different from writing a software program, since plans are interpreted much less strictly than a typical programming language. Instead, it is more appropriate to see plans as [behavioural scripts](https://en.wikipedia.org/wiki/Behavioral_script): simplified descriptions that guide the system in executing a commonly performed routine. The "brain" - in TDM's case the dialog move engine - uses the plan as a stereotypical or ideal scenario, rather than as literal instructions to be executed blindly. For example, if the system, in following a plan for making phone calls, asks the user who to call, and the user follows up by asking about the weather, TDM doesn't see this as an exception or failure of the phone-calling plan; instead, it activates a weather plan (if it has one), and is open for resuming the phone-calling activity at a later point.

Seeing plans as behavioural scripts rather than programs can be helpful in the design process. As a dialog developer, you are not supposed to try to imagine all the possible paths that a conversation can take, and to write rules or logic for all those paths. Instead, general dialog capabilities such as asking control questions in the case of uncertainty or switching between topics are provided by the dialog engine (the "brain").   

Zooming in to the specific details, let's first check the boilerplate, in `basic_action/domain.xml`.

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
      <invoke_service_action name="Call" postconfirm="true"/>
    </plan>
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
Generating models for DDD 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
[eng] Generating grammar.

Missing grammar entry: How does the system ask about 'selected_contact'?

Example:

  <question speaker="system" predicate="selected_contact" type="wh_question">
    <utterance>what is selected contact</utterance>
  </question>


[eng] Finished generating grammar.
Finished generating models for DDD 'basic_action'.
Training models for DDD 'basic_action'.
[eng] Asserting that language grammar is lower case...Done.
[eng] Compiling generated grammar.
[eng] Finished compiling generated grammar.
[eng] No ASR specified, will not build language model.
[eng] Copying ASR language modules from '/private/tmp/ddd_root/basic_action/grammar/build/eng' to ddd directory...Done.
[eng] Not using word list correction, will not generate word list.
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

## Step 6. Service interface

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

As can be seen, the system doesn't understand John. We need to add an entity recognizer to our service interface. It needs to recognize entities of our `contact` sort. Our boilerplate service interface is basically empty, in `basic_action/service_interface.xml`, so let's just add it.

```xml
<?xml version="1.0" encoding="utf-8"?>
<service_interface>
    <entity_recognizer name="BasicActionRecognizer">
        <target>
            <http endpoint="http://127.0.0.1:10102/contact_recognizer"/>
        </target>
    </entity_recognizer>
</service_interface>
```

Here, we use an HTTP target with an end-point that runs an HTTP service. An HTTP service can be hosted anywhere where TDM can reach it. In this tutorial, we assume that the service is hosted locally, i.e. on the same machine as TDM (127.0.0.1), but this is not required. Generally, the developer can choose any web development framework as long as it is within the constraints of the [HTTP service API protocol](APIs/http_service).

The entity recognizer is responsible for finding all dynamic entities in utterances. Its accuracy affects the behaviour of the dialogue system. Since the search is conducted during runtime, particular care should be taken to ensure that the method is accurate, robust and has sufficient performance. See the [API documentation](APIs/http_service/#entity-recognizer-requests) for details about request and response formats for entity recognizers.

In this case, we are providing you with a ready-to-use [HTTP service](http_service_example.py), which includes an entity recognizer. It uses [Flask web framework](http://flask.pocoo.org/docs/1.0/) and [jinja2](http://jinja.pocoo.org/docs/2.10/) templates in plain python.

As the service is hosted locally in this case, we recommend to save it in the DDD folder `basic_action`. Then, **spawn** it with Flask:

```bash
export FLASK_APP=basic_action/http_service_example.py
flask run --port=10102
```

And then, build and test.

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
            <http endpoint="http://127.0.0.1:10102/call"/>
        </target>
    </action>
    <entity_recognizer name="BasicActionRecognizer">
        <target>
            <http endpoint="http://127.0.0.1:10102/contact_recognizer"/>
        </target>
    </entity_recognizer>
</service_interface>
```

To implement the 'call' action, see the [API documentation](APIs/http_service/#action-requests) for details about request and response formats for actions. However, you can also find and use the 'call' action that has been already implemented in the example HTTP service.

Build again.

```bash
tdm build
```

```diff
Generating models for DDD 'basic_action'.
[eng] Cleaning build directory 'build/eng'...Done.
[eng] Generating grammar.

Missing grammar entry: How does the system report that the service action 'Call' ended? Example:

  <report action="Call" status="ended">
    <utterance>performed Call</utterance>
  </report>


[eng] Finished generating grammar.
Finished generating models for DDD 'basic_action'.
Training models for DDD 'basic_action'.
[eng] Asserting that language grammar is lower case...Done.
[eng] Compiling generated grammar.
[eng] Finished compiling generated grammar.
[eng] No ASR specified, will not build language model.
[eng] Copying ASR language modules from '/private/tmp/ddd_root/basic_action/grammar/build/eng' to ddd directory...Done.
[eng] Not using word list correction, will not generate word list.
```

As can be seen, we need to add a grammar entry for the service action `Call`. This is required because we said so in the plan. Remember `postconfirm="true"` in the `invoke_service_action` entry of the plan?

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

## Step 7. One-shot utterances

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

## Step 8. Adding a language

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

Check our HTTP service to see that name of the contacts are already there translated in French (and even Dutch):

```python
CONTACTS_FRENCH = {
    "Jean": JOHN,
    u"Élise": LISA,
    "Marie": MARY,
    u"André": ANDY,
}

CONTACTS_DUTCH = {
    "Jan": JOHN,
    "Lisa": LISA,
    "Maria": MARY,
    "Andreas": ANDY,
}
```

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

## Step 9. How to continue

This tutorial has illustrated how to implement the [basic action example](examples#basic-action). The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/basic_action).

In order to continue, go to the [examples](examples) section to find an example similar to your desired functionality. Steal the best ideas from there, adjusting them for yor domain. Remember to work test driven, adding a test first, then making it work.
