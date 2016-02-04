# Step 1. Create the boilerplate

First we need to create the DDD boilerplate.

```bash
mkdir ddd_root; cd ddd_root 
tdm_create_app.py ExampleDdd example_ddd
```

Before your DDD can be used, it needs to be built.

```bash
tdm_build.py -p example_ddd_project -text-only -L eng
```

To make sure your DDD and all dependencies are working as intended, let's run interaction tests.

```bash
tdm_test_interactions.py -p example_ddd_project -L eng -f example_ddd/test/interaction_tests_eng.txt
```


# Step 2. Add interaction tests

If the tests report OK, we're ready to start adding dialogue to our DDD. Since we're working test driven, let's add an interaction test first.

Interaction tests the dialogue, providing a user utterance, specifying the expected system response.

Modify `example_ddd/test/interaction_tests_eng.txt`, add a test for the new dialogue that we want to support. Let's say that we want to enable phone calls to people. For instance, to John.

```diff
--- call first-name
S> What would you like to do?
U> call john
S> Calling John.
```

Let's build and run the tests again to verify that they fail.

```bash
tdm_build.py -p example_ddd_project -text-only -L eng
tdm_test_interactions.py -p example_ddd_project -L eng -f example_ddd/test/interaction_tests_eng.txt
```

TDM will complain that it does not understand instead of placing the call to John.

```diff
call first-name:
example_ddd/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ I heard you say call john. I don't understand. So, What would you like to do?
```

This happens because there's no notion of calling, and no notion of people, in the DDD.


# Step 3. Add ontology

The ontology declares what users can do and talk about, much like header files. In order to call someone we need to add the notion of calling, and the notion of people, to the ontology.

Our boilerplate ontology is basically empty.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="ExampleDddOntology">
</ontology>
```

We extend it with an action to make calls, a contact sort and a predicate selected_contact so that we can select an individual of our contact sort. A dynamic sort means its individuals are decided during run time, through the service interface.

```xml
<?xml version="1.0" encoding="utf-8"?>
<ontology name="ExampleDddOntology">
  <action name="call"/>
  <sort name="contact" dynamic="true"/>
  <predicate name="selected_contact" sort="contact"/>
</ontology>
```

Let's build and run the tests again to see if we missed something.

```bash
tdm_build.py -p example_ddd_project -text-only -L eng
```

We receive a warning when generating the grammar.

```diff
Building GF 3.3 for application 'example_ddd'.
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
Finished building GF 3.3 for application 'example_ddd'.
```

Apparently, ontology entries require corresponding grammar entries.

But the build still seems to have succeeded. What happens if we run the tests?

```bash
tdm_test_interactions.py -p example_ddd_project -L eng -f example_ddd/test/interaction_tests_eng.txt
```

No difference, apparently.

```diff
call first-name:
example_ddd/test/interaction_tests_eng.txt at line 7: system output
Expected:
- Calling John.
Got:
+ I heard you say call john. I don't understand. So, What would you like to do?
```

How about that grammar entry?


# Step 4. Add grammar
# Step 5. Add plans
# Step 6. Add service interface
# Step 7. How to continue

This tutorial has illustrated the first step towards the [incremental_search](examples#incremental_search) example.

In order to continue, go to the [examples](examples) section to find an example similar to your desired functionality. Steal the best ideas from there, adjusting them for yor domain. Remember to work test driven, adding a test first, then making it work.
