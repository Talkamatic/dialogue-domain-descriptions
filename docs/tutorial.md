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
# Step 4. Add plans
# Step 5. Add grammar
# Step 7. How to continue

This tutorial has illustrated the first step towards the `incremental_search` example. View its complete source code at [GitHub](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/incremental_search)

In order to continue, go to the [examples](examples) section to find an example similar to your desired functionality. Steal the best ideas from there, adjusting them for yor domain. Remember to work test driven, adding a test first, then making it work.
