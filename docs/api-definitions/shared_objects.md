# Shared objects

This document describes the objects that occur in requests and responses across different APIs. For example, see [TDM pipeline API](pipeline_api.md).

## Natural language input object

Speech input example:

```json
 {
  "modality": "speech",
  "hypotheses": [
    {
      "utterance": "call John",
      "confidence": 0.81
    },
    {
      "utterance": "calling John",
      "confidence": 0.65
    },
    {
      "utterance": "call him John",
      "confidence": 0.31
    }
  ]
}
```

Text input example:

```json
{
  "modality": "text",
  "utterance": "I'm searching for flights from London to Paris tomorrow"
 }
```

The natural language input contains the following members:

- `modality`: Should be either `speech` or `text` depending on how the input was detected.
- `hypotheses`: A list of [hypothesis objects](#hypothesis-object) which should be provided if `modality` is `speech`; otherwize the field should be omitted.
- `utterance`: A string containing the utterance if `modality` is `text`; otherwize the field should be omitted.

## Hypothesis object

A hypothesis object contains information about what the user is believed to have uttered, consisting of the following members:

- `utterance`: A string containing the utterance.
- `confidence`: A number from 0.0 to 1.0 representing the confidence of the hypothesis.

## Semantic input object

```json
{
  "interpretations": [
    {
      "utterance": "call John",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.81,
          "understanding_confidence": 0.92215,
          "ddd": "phone",
          "semantic_expression": "request(call)"
        },
        {
          "perception_confidence": 0.81,
          "understanding_confidence": 0.98532,
          "ddd": "phone",
          "semantic_expression": "answer(contact_john)"
        }
      ]
    },
    {
      "utterance": "calling John",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.65,
          "understanding_confidence": 0.5234,
          "ddd": "phone",
          "semantic_expression": "request(call)"
        },
        {
          "perception_confidence": 0.65,
          "understanding_confidence": 0.98532,
          "ddd": "phone",
          "semantic_expression": "answer(contact_john)"
        }
      ]
    },
    {
      "utterance": "call him John",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.31,
          "understanding_confidence": 0.2216,
          "ddd": "phone",
          "semantic_expression": "request(call)"
        },
        {
          "perception_confidence": 0.31,
          "understanding_confidence": 0.98532,
          "ddd": "phone",
          "semantic_expression": "answer(contact_john)"
        }
      ]
    },
    {
      "utterance": "call him John",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.31,
          "understanding_confidence": 0.10126,
          "ddd": "phone",
          "semantic_expression": "ask(?X.phone_number(X))"
        },
        {
          "perception_confidence": 0.31,
          "understanding_confidence": 0.98532,
          "ddd": "phone",
          "semantic_expression": "answer(contact_john)"
        }
      ]
    }
  ],
  "entities": [
    {
      "name": "contact_john",
      "sort": "contact",
      "natural_language_form": "John"
    }
  ]
}
```

The semantic input contains the following members:

- `interpretations`: A list of [interpretation objects](#interpretation-object). TDM will use confidence scores and the context of the current state of the session to decide which interpretation to act upon.
- `entities`: (optional) A list of [entity objects](#entity-object). TDM can use these entities in interpretations and for natural language generation.

The semantic format is different for each of the supported user moves. See [the move object](#move-object) for examples.

## Interpretation object

An interpretation translates an utterance into one or several semantic moves. An interpretation object contains:

- `utterance`: (optional) A string containing the utterance.
- `modality`: The modality that the user used to provide the original input. One of `speech`, `text`, `haptic`, `other`.
- `moves`: A list of [move objects](#move-object).

## Entity object

These entities are needed when entities are not defined in the DDD and can then be used in interpretations and in downstream natural language generation. An entity object contains:

- `name`: A string containing the semantic name. This name can be used to reference the entity in interpretations.
- `sort`: A string with the entity sort name.
- `natural_language_form`: A string containing the natural language or surface form of the entity.
- `ddd`: A string with the name of the DDD that the entity belongs to.

## Move object

A move object contains information about how a user move was interpreted (see [moves](../formalism.md#moves)). Its members are:

- `ddd`: (optional) A string containing the DDD name. For DDD independent moves (e.g. `answer(yes)` and `request(up)`), this field may be omitted; in which case the currently active DDD will be used to parse the semantic expression.
- `perception_confidence`: A float between `0.0` and `1.0`, representing the confidence that a spoken utterance actually matches the textual utterance, for instance when a speech-to-text (STT) component turned it into text. If no perception component was used, the confidence should be set to `1.0`.
- `understanding_confidence`: A float between `0.0` and `1.0`, representing the confidence that the textual utterance actually represents this move, for instance when an NLU component interprets the textual utterance. If no understanding component was used, for instance if the user pressed a button, the confidence should be set to `1.0`.
- `semantic_expression`: A semantic expression, representing the move itself. Supported moves are `request`, `ask` and `answer`. See examples below for details.

### Example of a `request` move:

A [request](../formalism.md#request-moves) move has just one parameter: An action. In this case the `call` action, which must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "request(call)",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.5234
}
```

### Example of builtin `request` move:

The builtin and DDD independent actions `top` and `up` can be requested without including the DDD name:

```json
{
  "semantic_expression": "request(top)",
  "perception_confidence": 0.56,
  "understanding_confidence": 0.65305
}
```

### Example of `ask` moves:

An [ask](../formalism.md#ask-moves) move contains a question. Questions are expressed with a leading `?`. Question in `ask` moves always contain a predicate that must be defined in the ontology of the DDD. There are two supported types of questions in `ask` moves: wh-questions (questions about what, when, whom, which etc.) and yes-no questions (that can be answered with a yes or no).

### Example of an `ask` move containing a wh-question:

Wh-questions are represented in a lambda-like form. In the case below, the question `?X.phone_number(X)` means that we're asking what someone's phone number is.

```json
{
  "ddd": "phone",
  "semantic_expression": "ask(?X.phone_number(X))",
  "perception_confidence": 0.31,
  "understanding_confidence": 0.10126
}
```

### Example of an `ask` move containing a yes-no question:

In the case below, the question `?missed_calls` means that we're asking whether there are any missed calls (without asking e.g. when or from whom).

```json
{
  "ddd": "phone",
  "semantic_expression": "ask(?missed_calls)",
  "perception_confidence": 0.43,
  "understanding_confidence": 0.2432
}
```

### Example of a sortal `answer` move:

A sortal [answer](../formalism.md#answer-moves) move has an individual as its parameter. In this case, the individual `contact_john`, must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "answer(contact_john)",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.98532
}
```

### Example of a propositional `answer` move:

A propositional `answer` move has a proposition as its parameter, consisting of a predicate and an individual. In this case, the predicate `selected_contact`, and the individual `contact_john`, must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "answer(selected_contact(contact_john))",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.71347
}
```

### Example of builtin sortal `answer` move:

The builtin and DDD independent answers `yes` and `no` can be used without including the DDD name:

```json
{
  "semantic_expression": "answer(yes)",
  "perception_confidence": 0.834,
  "understanding_confidence": 0.71359
}
```
