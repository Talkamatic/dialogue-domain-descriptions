Below are examples for you to imitate. Find one that matches your desired functionality and start stealing ideas.

Remember to work test driven, adding one test at a time, then making it work, according to the [tutorial](tutorial).

The source code of all examples is available on [GitHub][github file browser].


# Basic action

This example is featured in the [tutorial](tutorial).

Let your user do an action, using an `entity recognizer` for its `findout`. In this case, call a contact where the contact name is the recognized entity.

    U> Call John
    S> Calling John.

This is an example of the basic [request](/#request) and [action](/#actions) concepts in TDM. It shows what is needed in order to perform an `action` that you implement yourself in the python `service interface`. In addition, it uses an `entity recognizer` to recognize contacts during run time.

# Incremental search

Is your user looking for a single item in a set of many? Make sure your application asks just the perfect amount of questions to find one and only one match. In this case, contacts to call are searched with first and last names.

    U> Call John
    S> What's his last name?
    U> Johnson
    S> Calling John Johnson at 0702446698.

Incremental search utilizes predicate features, which are declared in the ontology of the DDD. When a service is queried for individuals of the predicate, the features need to match. By asking the user to specify more features, the search can be narrowed down to finally match a single individual.

[github file browser]: https://github.com/Talkamatic/dialogue-domain-descriptions/tree/master
