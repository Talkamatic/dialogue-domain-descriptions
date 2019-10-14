Below are examples for you to imitate. Find one that matches your desired functionality and start stealing ideas.

Remember to work test driven, adding one test at a time, then making it work, according to the [tutorial](tutorial).


# Basic action

This example is featured in the [tutorial](tutorial).

Let your user do an action, using an `entity recognizer` for its `findout`. In this case, call a contact where the contact name is the recognized entity.

    U> Call John
    S> Calling John.

This is an example of the basic [action](/#actions), [answer](/#answers) and [feedback](/#feedback) concepts in TDM. It shows what is needed in order to perform an `action` that you implement yourself in the python `service interface`. In addition, it uses an `entity recognizer` to recognize contacts during run time.

The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/basic_action).


# Basic query

Let your user ask a question. While similar to the [basic action](examples/#basic-action) example, a query lets the system speak an answer to a question rather than performing an action. In this case, it answers what phone number a contact has.

    U> What is John's number?
    S> John's number is 0701234567.

This is an example of the basic [query](/#queries) and [answer](/#answers) concepts in TDM. It shows what is needed in order to ask a `query` that is answered by the system. You implement the answer logic yourself in the python `service interface`.

The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/basic_query).


# Parameter validation

Should some actions or questions be unavailable, disallowed or prohibited for your user? Parameter validation makes it easy to decide at run-time. This example is based on the [basic action example](examples/#basic-action), disallowing phone calls to contacts with no phone number.

    U> Call Andy
    S> Andy has no phone number.

When a service is queried for parameters to actions and queries, the parameter is validated against all matching validators. If invalid, a specific grammar entry is used to provide system feedback and the answer is neglected.

The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/parameter_validation).


# Incremental search

Is your user looking for a single item in a set of many? Make sure your application asks just the perfect amount of questions to find one and only one match. In this case, contacts to call are searched with first and last names.

    U> Call John
    S> What's his last name?
    U> Johnson
    S> Calling John Johnson at 0702446698.

Incremental search utilizes predicate features, which are declared in the ontology of the DDD. When a service is queried for individuals of the predicate, the features need to match. By asking the user to specify more features, the search can be narrowed down to finally match a single individual.

The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/incremental_search).


# Android

Is your Android device placing the calls for your users? Forward your actions to the Android frontend and do the job there.

    U> Call John
    S> Calling John.

This example combines the examples of action, query, parameter validation and entity recognition into one DDD and forwards the 'Call' action to the frontend. It can be used together with the [android-example](https://github.com/Talkamatic/android-example), an Android app to showcase how your frontend hears, speaks and thinks.

The source code is available on [Github](https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master/android).
