# Dialog Formalism

The Dialog Formalism is a formal language for expressing semantics and domain knowledge within the framework of issue-based dialog management (Larsson, 2002)[^Larsson, 2002] based on the information state approach (Larsson, Traum, 2000)[^Larsson, Traum, 2000], (Traum, Larsson, 2003)[^Traum, Larsson, 2003], which is the foundation of TDM.

[^Larsson, 2002]:
    Larsson, S. (2002). Issue-based dialogue management. Department of Linguistics, University of Gothenburg.
[^Larsson, Traum, 2000]:
    Larsson, S., & Traum, D. R. (2000). Information state and dialogue management in the TRINDI dialogue move engine toolkit. Natural language engineering, 6(3-4), 323-340.
[^Traum, Larsson, 2003]:
    Traum, D. R., & Larsson, S. (2003). The information state approach to dialogue management. In Current and new directions in discourse and dialogue (pp. 325-353). Springer, Dordrecht.

For readers familiar with logic, the Dialog Formalism is closely related to first-order predicate logic.

Some of the constructs of the Dialog Formalism are described below, with corresponding example expressions.

## Semantics

The Dialog Formalism covers semantics, constructs that occur in language, regardless of the actual language.

### Predicates
Predicates are used to formalise the meanings of nouns, verbs and adjectives.

They typically correspond to slots in form-based (slot-filling) dialog management.

Example: `selected_contact`

### Individuals
Individuals can be arguments of predicates, which corresponds to being values of slots in form-based dialog management. It also aligns with the term "entity" used in many other contexts.

In TDM, `yes` and `no` are modelled as individuals, even if they are not individuals in the concrete sense, but this allows them to be used in answers.

Examples:

- `contact_john`, which would correspond to `John` in natural language.
- `yes`
- `no`

### Propositions
A proposition expresses something that can be true or false, can be believed to be true, or can be taken as a fact. Propositions have a [predicate](#predicates), a polarity (positive or negative), an arity (nullary or unary) and optionally an argument (an [individual](#individuals), typically).

Negative polarity is expressed using the negation operator `~` as prefix.

#### Nullary proposition

A nullary proposition has no argument.

Examples:

- `need_visa` expresses that a visa is needed.
- `~need_visa` expresses that a visa is _not_ needed.

#### <a name="unary-propositions"></a>Unary propositions

A unary proposition takes an individual as an argument.

Examples:

- `selected_contact(contact_john)` expresses that the selected contact is John.
- `~selected_contact(contact_john)` expresses that the selected contact is _not_ John.

#### <a name="goal-propositions"></a>Goal propositions

A goal proposition expresses that a particular [goal](#goals) should be targeted. It has the form `goal(G)` where G is a [goal](#goals).

Examples:

`goal(perform(call))` expresses that the goal of performing `call` should be targeted.
`goal(resolve(?X.phone_number(X)))` expresses that the goal of resolving `?X.phone_number(X)` should be targeted.

### Actions
An action is something that can be performed.

Example: `call`

### Questions
A question is something that can be asked, answered and resolved. Its expression begins with the question operator `?`.

#### <a name="yn-questions"></a>Yes-no questions

A yes-no question is a question that can be answered with a yes or no.

Examples:

- `?need_visa` expresses a question regarding whether a visa is needed.
- `?selected_contact(contact_john)` expresses a question regarding whether the selected contact is John.

#### <a name="wh-questions"></a>WH questions

A WH question is a question about what, when, where etc. It is expressed as a lambda abstraction.

Example: `?X.selected_contact(X)` expresses a question about which contact to select.

#### <a name="alt-questions"></a>Alternative questions

An alternative question is a question containing multiple alternative answers expressed as a set of propositions.

Example: `?set([number_to_call(home), number_to_call(mobile)])` expresses a question about whether to call the home or mobile number.

#### <a name="knowledge-precondition-questions">Knowledge precondition questions

A knowledge precondition question is a question about whether the the answer to a question is known.

Example: `?know_answer(?X.contact_to_call_first_name(X))` expresses a question about whether the first name of the contact to call is known.

### Moves
(Dialog) moves reflect the meaning and function of something that is communicated in a dialog. Utterances spoken by the user or system correspond to sequences of moves. TDM supports many different kinds of dialog moves, the most common of which are described below.

#### <a name="ask-moves"></a>Ask moves

An ask move represents the act of asking a question. It has the form `ask(Q)` where `Q` is a [question](#questions).

Example: `ask(?X.selected_contact(X))`

#### <a name="request-moves"></a>Request moves

A request move represents the act of requesting an action that needs to be performed. It has the form `request(A)` where `A` is an [action](#actions).

Example: `request(call)`

#### <a name="answer-moves"></a>Answer moves

An answer move represents the act of answering a question. It has the form `answer(A)` where `A` can be a [proposition](#propositions) (in a so called propositional answer) or an [individual](#individuals) (in a so called sortal answer). The individual of a sortal answer combines with a question to form a proposition; for example, the question `?x.selected_name(x)` combined with the individual `contact_john` forms the proposition `selected_name(contact_john)`.

Examples:

- `answer(contact_john)`
- `answer(selected_contact(contact_john))`
- `answer(yes)`
- `answer(no)`


## Domain knowledge

In addition to semantics, the Dialog Formalism also covers domain knowledge such as goals and (the contents of) plans.

### Goals
A goal expresses an [action](#actions) to perform or a [question](#questions) to resolve, as elaborated below.

#### Perform goals

A perform goal has the form `perform(A)` where A is an [action](#actions).

Example: `perform(call)` expresses the goal of performing the action `call`.

#### Resolve goals

A resolve goal has the form `resolve(Q)` where Q is a [question](#questions).

Example: `resolve(?X.phone_number(X))` expresses the goal of resolving the question `?X.phone_number(X)`.

### Plan items
For every goal, there is a corresponding plan for how the goal can be fulfilled. Plans are however not fully expressed in the dialog formalism, but instead covered by the [XML domain format of dialog domain descriptions](for-dialog-designers/tutorial.md#step-5-plan). Individual plan items, the pieces that the plan consists of and each an instruction to TDM, can be expressed though. This section describes some of the most common items.

#### Findout

A `findout` item expresses an instruction to find the answer to a question, e.g. by asking the user or asking a service.

Example: `findout(?X.selected_contact(X))`

#### Bind

The `bind(Q)` construction, where `Q is a question, lets the system understand answers to a question `Q that it does not ask explicitly. This makes it possible to take optional and unrequested parameters that the user provides into consideration. 

For example, if `bind(?x.price-class(x))` is in a plan in a travel agency domain, the system will understand something like "I would like to travel business class", but it will not ask e.g. "What price class did you have in mind?".


#### Invoke service action

An `invoke_service_action` expresses an action to be performed by a service.

Example: `invoke_service_action(Call, {preconfirm=interrogative, postconfirm=True, downdate_plan=False})`

#### Invoke service query

An `invoke_service_query` expresses an instruction to find the answer to a question by asking a service.

Example: `invoke_service_query(?X.phone_number(X))`
