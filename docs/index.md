A number of concepts need to be known to the developer when creating TDM Dialogue Domain Descriptions (DDDs).

We recommend new developers to start by reading [the introductory presentation](https://github.com/Talkamatic/dialogue-domain-descriptions/blob/master/tdm-ddd-development.pdf) by Alexander and studying the basic concepts below.

After that, work through [the tutorial](tutorial) for hands on practice, or skip straight to [the example DDDs](examples)


# Basic concepts

The basic concepts in TDM are Questions, Answers, Requests, Actions
and Feedback.


## Question

A question is a request for information. It can be formulated as a
question, or as a request.

```diff
U> What is John's number?
```

or

```diff
U> Tell me John's number.
```


## Answer

An answer is something that provides information which is relevant for
a question, and that may be resolving. If the question is about a contact,
the following would answer the question:

```diff
U> John      # relevant and resolving
```

```diff
U> not Mary  # relevant but not resolving
```


## Actions

Actions are things that the system can carry out, such as calling a contact, displaying a certain kind of menu, rerouting a travel plan etc.


## Request

A request is an expression of a wish from the user for the system to
carry out some action.

```diff
U> Call.
```

or

```diff
U> Call John.
```


## Feedback

The system may give feedback to the user, indicating that actions are
started or stopped, or that the system did not hear what the user
said, etc.

```diff
S> Calling John.
```

or

```diff
S> I did not hear.
```
