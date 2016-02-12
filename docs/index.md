A number of concepts need to be known to the developer when creating TDM Dialogue Domain Descriptions (DDDs).

We recommend new developers to start by reading [the introductory presentation](https://github.com/Talkamatic/dialogue-domain-descriptions/blob/master/tdm-ddd-development.pdf) by Alexander and studying the basic concepts below.

After that, work through [the tutorial](tutorial) for hands on practice, or skip straight to [the example DDDs](examples)


# Basic concepts

Some basic concepts in TDM are Actions, Questions, Answers and Feedback.


## Actions

An action is requested by the user and performed by the system. It may or may not require a number of answers in order to be performed. Example:

```diff
U> Call.
```

or

```diff
U> Call John.
```


## Questions

A question is asked by the user or the system, when they want a piece of information. It can be formulated as a question, or as a request. Similar to an action, it may or may not require a number of answers in order to be answered.

```diff
U> What is John's number?
```

or

```diff
U> Tell me John's number.
```


## Answers

An answer is provided by the user or the system, providing information that is relevant for a question or request. When provided by the user, it can be resolving or not. If the question is about a contact, the following would be an answer:

```diff
U> John
```


## Feedback

Feedback is given by the system to inform the user. For example that actions have been performed, that the system did not hear what the user said, etc.

```diff
S> Calling John.
```

or

```diff
S> I did not hear.
```
