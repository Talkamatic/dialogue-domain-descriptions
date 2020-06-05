# Pipeline API

This document describes API version 3.3 for HTTP frontends, enabling frontends to integrate with TDM over HTTP. It covers e.g. how input from the user and output from TDM are communicated between TDM and the client.

## Important concepts

This section describes some concepts that are important to understand and comply with when integrating TDM in a dialog system.

### Requests and responses

TDM serves an HTTP server and responds to requests done by the client. The client is the consumer of the API outlined in this document.

The client invokes TDM with an HTTP request to the interaction endpoint, e.g. `http://localhost:9090/interact`, using the POST method and a JSON body. The client should expect the status code to be 200 OK. For other status codes, the client should report an error to the user.

The request body always contains a version number, specifying the version of the HTTP API format.

The exact format of the request and the response depends on the type of request as described in the separate sections below.

### Turn taking

Turn taking is a vital part of dialog between humans, read for instance [the Wikipedia article](https://en.wikipedia.org/wiki/Turn-taking). Since TDM is based on research on human-human dialog, turn taking is a central concept here too.

The TDM client is responsible for managing turn-taking on behalf of the machine, because it's the component that is closest to the human, in the human-machine dialog that TDM enables. Since the machine is intended to assist the human, the human decides the pace, the turn taking, of the conversation. In spoken dialog, turn taking happens in close collaboration with the spoken output of the system, which means that the system's turn management needs to happen as close to this component, the text-to-speech component (TTS), as possible.

TDM enables intuitive turn taking by instructing its client how to deal with the user input that it's range of sensors can pick up. The instructions are straightforward and revolve around passivity. If the user is passive, for instance doesn't know what to say, for a given amount of time, the client sends TDM a [passivity request](#passivity-requests), which lets the system take the next turn instead of the user.

The user should be considered passive when not doing anything related to the dialog. If the user however takes some action (although not completing its turn just yet), for instance by typing (if it's a text interface) or talking (if it's a spoken interface), the user should be considered active and the passivity request should not be sent to TDM. Instead the user should be allowed to complete its turn, resulting in an input request.

TDM instructs its client about how much time of passivity that should pass before sending the passivity request in the `output.expected_passivity` field of the [response](#response-format).

For instance, if TDM responds with:

```json
{
  "output": {
    ...
    "expected_passivity": 1.0
  },
  ...
}
```

then the client should send a [passivity request](#passivity-requests) when the user has been passive for 1 second. The 1 second should start counting when the system utterance has reached the user, which in a spoken interface means when the TTS finished speaking TDM's utterance.

Note that sometimes TDM does not have anything to say when the user becomes passive (`"expected_passivity": null`), and sometimes it just needs to progress the conversation immediately after saying something (`"expected_passivity": 0.0`).

Read the details about how to interpret the `expected_passivity` value in the [response format section](#response-format).

### Errors

When an error occurs in TDM during a request, for instance due to incomplete turn management, the [response](#response-format) contains the `"error"` field. It's important to note that this could mean that the session stops. If it has stopped, further requests on the same session will report errors that the provided session ID is unknown.

## Start session requests
When a new session should be started, the client issues a `start_session` request. The response contains initial output from TDM and a session ID that can be used in subsequent requests. For more details, see [the response format](#response-format).

If a session ID is provided together with the `start_session` request, an error is given. The integrity of the session is however maintained.

### Request

Example:

```json
{
  "version": "3.3",
  "session": {},
  "request": {
    "start_session": {}
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object).

The `start_session` object may contain the following optional members:

- `ddd_set`: A string specifying a DDD set for the session. If omitted, a default DDD set configured by the backend is used.

The `start_session` request may be issued on its own, so that the system will start the conversation; or combined with `natural_language_input`, `semantic_input` and `event` requests to start the conversation from there.

Example when combined with `natural_language_input`:

```json
{
  "version": "3.3",
  "request": {
    "start_session": {},
    "natural_language_input": {...}
  }
}
```

### Response

See [response format](#response-format).

## Natural language input requests
When the client detects natural language input from the user, it issues a request and receives output from TDM. The request can contain either hypotheses with the `speech` modality, or a single utterance with the `text` modality.

### Request

Speech input example:

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "natural_language_input": {
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
  }
}
```

Text input example:

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "natural_language_input": {
      "modality": "text",
      "utterance": "I'm searching for flights from London to Paris tomorrow"
    }
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object)

See the [natural language input object](shared_objects.md#natural-language-input-object) for more details.

The `natural_language_input` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:
```json
{
  "version": "3.3",
  "request": {
    "start_session": {},
    "natural_language_input": {...}
  }
}
```

### Response

See [response format](#response-format).

## Semantic input requests
When the client has user input on a semantic format, as a user move, it should issue the `semantic_input` request.

Semantic in this case means that the user input does not need to be interpreted; the user move is already known. This is useful when an external natural language understanding (NLU) component has already interpreted the input; when the user presses a button in a GUI; or for instance when the user makes a gesture which is interpreted as a user move.

### Request

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "semantic_input": {
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
          "natural_language_form": "John",
          "ddd": "phone"
        }
      ]
    }
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object).

- `interpretations`: A list of [interpretation objects](#interpretation-object). TDM will use confidence scores and the context of the current state of the session to decide which interpretation to act upon.
- `entities`: (optional) A list of [entity objects](#entity-object). TDM can use these entities in interpretations and for natural language generation.

See the [semantic input object](shared_objects.md#semantic-input-object) for more details.


The `semantic_input` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:

```json
{
  "version": "3.3",
  "request": {
    "start_session": {},
    "semantic_input": {...}
  }
}
```

### Response

See [response format](#response-format).

## Passivity requests
When the client detects user passivity, it issues a request and receives output from TDM.

### Request

Example:

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "passivity": {}
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object).

The `passivity` request may not be combined with other requests in the same call.

### Response

See [response format](#response-format).

## Event requests
When the client detects that an event pertaining to a relevant DDD has occurred, it should issue an event notification request, and receives output from TDM.

### Request

Example:

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "event": {
      "name": "IncomingCall",
      "status": "started",
      "parameters": {
        "caller": "contact_12345"
      }
    }
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object).

The `event` object contains the following members:

- `name`: A string corresponding to the name of the event, specified as an action in the service interface.
- `status`: Either `started` or `ended`.
- `parameters`: A map of key-value pairs pertaining to the event, corresponding to the parameters specified for the action in the service interface. The key is a string matching the parameter's predicate, and the value is a string containing the ID of the value (e.g. a number or a string depending on the sort).

The `event` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:

```json
{
  "version": "3.3",
  "request": {
    "start_session": {},
    "event": {...}
  }
}
```

### Response

See [response format](#response-format).

## Response format
The response format differs when the request was successful compared to when it encountered an error.

### Successful request

The TDM response from a successful request typically contains an output utterance and other relevant information. Example:

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "output": {
    "moves": ["ask(?X.selected_contact(X))"],
    "utterance": "Who do you want to call?",
    "expected_passivity": 5.0,
    "actions": []
  },
  "nlu_result": {
    "selected_utterance": "call John",
    "confidence": 0.88
  },
  "context": {
    "active_ddd": "my_ddd",
    "facts": {},
    "language": "eng",
    "goal": "perform(call)",
    "plan": ["findout(?X.selected_contact(X))"],
    "facts_being_grounded": {},
    "selected_hypothesis": {
      "utterance": "call John",
      "confidence": 0.88
    },
    "selected_interpretation": [{
      "ddd": "send_to_frontend",
      "understanding_confidence": "0.749",
      "perception_confidence": "0.88",
      "semantic_expression": "request(call)"
    }],
    "expected_input": {
      "alternatives": [
        {"semantic_expression": "answer(contact_john)"},
        {"semantic_expression": "answer(contact_lisa)"}
      ]
    }
  }
}
```

The `session` object is always provided and contains the same data that was provided in the request. Unlike requests however, it always contains:

- `session_id`: The ID of the current session.

The `output` object is provided unless an error has occurred and has the following members:

- `moves`: The moves made by the system this turn. This is a list of [move expressions in the dialog formalism](../formalism.md#moves), where the moves should be uttered in the listed order. Moves here are similar to the `semantic_expression` field of [move objects](#move-object).
- `utterance`: A string representing the output utterance from the system and should be realized by the client (e.g. by speaking it or displaying it as text).
- `expected_passivity`: If not null, the value is a number corresponding to the number of seconds of user passivity after which the client is expected to make a [passivity request](#passivity-requests). If the value is 0.0, the passivity notification request should be issued immediately after having realized the system output.
- `actions`: A list of [action invocation objects](#action-invocation-object), which needs to be invoked by the client. TDM assumes that the actions will succeed and reports them accordingly.

The `nlu_result` object is provided for [natural language input requests](#natural-language-input-requests), unless an error has occurred. It has the following members:

- `selected_utterance`: The utterance selected as the best candidate among the list of hypotheses.
- `confidence`: A number representing the joint confidence of the input and the NLU processing.

The `context` object is provided unless an error has occurred and contains the following members:

- `active_ddd`: The name of the currently active DDD.
- `facts`: Information gathered during the conversation (see [facts object](#facts-object)).
- `language`: ID of the current language.
- `goal`: Currently active goal, expressed as a [goal in the dialog formalism](../formalism.md#goals).
- `plan`: Remaining items on the current plan, represented by a list of [plan items in the dialog formalism](../formalism.md#plan-items).
- `facts_being_grounded`: Information that the system is currently grounding with the user, represented as a list of [facts objects](#facts-object).
- `selected_hypothesis`: The natural language hypothesis that the system decided to act on. If the system turn was requested with a [natural language input request](#natural-language-input-requests), this corresponds to one of the [hypothesis objects](shared_objects.md#hypothesis-object) that were part of it. This field is `null` if a hypothesis could not be determined.
- `selected_interpretation`: The semantic interpretation that the system decided to act on. If the system turn was requested with a [semantic input request](#semantic-input-requests), this corresponds to one of the [interpretation objects](shared_objects.md#interpretation-object) that were part of it. This field is `null` if an interpretation could not be determined.
- `expected_input`: An [expected input object](#expected-input-object), containing alternatives that TDM considers expected by the user the next turn. This field is `null` if TDM does not expect input, or if it doesn't know what input to expect.

A `warnings` field is provided if warnings have been issued, as a list of strings, one string per warning. This can for instance happen when TDM is updated to a new version of this frontend API and the previous version is deprecated. In such cases, update your request formats to comply with the warning and avoid potential future errors:

### <a name="error-response"></a>Request that encountered an error

The TDM response when an error was encountered in the request contains an error description.

```json
{
  "version": "3.3",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "error": {
    "description": "An exception was encountered when processing the request"
  }
}
```

An `error` object is provided if an error has occurred. In such cases, an error should be reported to the user by the client, and the session should not be resumed with further requests. The `error` field has the following members:

- `description`: A human readable technical description of the error.

## Session object

A session object can contain frontend-specific session data. The data is forwarded as is to all service calls on the [HTTP API for services](service_api.md#session-object). That way, the data can be used in service calls directly; or influence the dialog, for instance by being retrieved through service queries.
Note that session data is not automatically stored or attached to the session within TDM. It is returned in the [response](#response-format) and can be injected in future requests. If specific data should be available to all service calls on a session, the data needs to be injected in every request on that session, or the DDD needs to retrieve it into the dialog state, for instance by a service query.
For all requests except [start session](pipeline_api.md#start-session-requests), a `session_id` is required and used to identify to which session the request is being made.
For start session requests however, the `session_id` is disallowed and instead generated by TDM. It should be retrieved from the [response](#response-format).

Example for start session request:

```json
{
  "session": {
    "my_frontend": {
      "user_id": "123-abc-456-def",
      "position": {
        "latitude": "57.699188",
        "longitude": "11.948313"
      }
    }
  }
}
```

Example otherwise:

```json
{
  "session": {
    "session_id": "0000-abcd-1111-efgh",
    "my_frontend": {
      "user_id": "123-abc-456-def",
      "position": {
        "latitude": "57.699188",
        "longitude": "11.948313"
      }
    }
  }
}
```

## Output object

The `output` object contains the following members:

- `moves`: The moves made by the system this turn. This is a list of [move expressions in the dialog formalism](../formalism.md#moves). Moves here are similar to the `semantic_expression` field of [move objects](#move-object).
- `utterance`: A string representing the output utterance from the system and should be realized by the client (e.g. by speaking it or displaying it as text).
- `expected_passivity`: If not null, the value is a number corresponding to the number of seconds of user passivity after which the client is expected to make a [passivity request](#passivity-requests). If the value is 0.0, the passivity notification request should be issued immediately after having realized the system output.
- `actions`: A list of [action invocation objects](action-invocation-object), which needs to be invoked by the client. TDM assumes that the actions will succeed and reports them accordingly.

## NLU results object

The `nlu_result` object contains the following members:

- `selected_utterance`: The utterance selected as the best candidate amoung the list of natural language input hypotheses.
- `confidence`: A number representing the joint confidence of the input and the NLU processing.

## Context object

The `context` object contains the following members:

- `active_ddd`: The name of the currently active DDD.
- `facts`: Information gathered during the conversation (see [facts object](facts-object)).
- `language`: ID of the current language.
- `goal`: Currently active goal, expressed as a [goal proposition in the dialog formalism](../formalism.md#goal-propositions).
- `plan`: Remaining items on the current plan, represented by a list of [plan items in the dialog formalism](../formalism.md#plan-items).
- `facts_being_grounded`: Information that the system is currently grounding with the user, represented as a list of [facts objects](facts-object).
- `selected_hypothesis`: The natural language hypothesis that the system decided to act on. If the system turn was requested with a [natural language input request](#natural-language-input-requests), this corresponds to one of the [hypothesis objects](shared_objects.md#hypothesis-object) that were part of it. This field is `null` if a hypothesis could not be determined.
- `selected_interpretation`: The semantic interpretation that the system decided to act on. If the system turn was requested with a [semantic input request](#semantic-input-requests), this corresponds to one of the [interpretation objects](shared_objects.md#interpretation-object) that were part of it. This field is `null` if an interpretation could not be determined.
- `expected_input`: An [expected input object](expected-input-object), containing alternatives that TDM considers expected by the user the next turn. This field is `null` if TDM does not expect input, or if it doesn't know what input to expect.

## Action invocation object

An action invocation object contains information about an action to be invoked by the client. The object has the following members:

- `name` is a string corresponding to the action's name in `service_interface.xml`.
- `parameters` contains values for all parameters that are specified for the method in `service_interface.xml`. If a parameter is unknown, its value is `null`. Otherwise it's an object containing:
    - `sort`: ID of the predicate's sort as defined in the ontology.
    - `value`: ID of the value. For the sorts `integer` and `real`, the ID is a number. For other sorts, e.g. `string`, `datetime` and custom sorts, the ID is a string.
    - `grammar_entry`: Natural-language representation of the value.

Example:

```json
{
  "name": "call",
  "parameters": {
    "selected_contact": {
      "sort": "contact",
      "value": "contact_john",
      "grammar_entry": "John"
    }
  }
}
```

## Facts object

The `facts` field contains a map of key-value pairs for information gathered during the conversation, e.g. from the user. The map may be empty.

The key is a string matching a predicate as defined in the ontology. The value is an object with the following members:

- `sort`: ID of the predicate's sort as defined in the ontology.
- `value`: ID of the value (e.g. a number or a string depending on the sort). For predicates of sort `datetime`, the ID is an ISO 8601 string.
- `grammar_entry`: Natural-language representation of the value.

Example:

```json
{
  "facts": {
    "departure": {
      "sort": "city",
      "value": "city_012345",
      "grammar_entry": "London"
    },
    "destination": {
      "sort": "city",
      "value": "city_012346",
      "grammar_entry": "Newcastle"
    }
  }
}
```

## Expected input object
The expected input object contains alternatives that TDM considers expected by the user the next turn. They can for instance be used to add quick-answer buttons to a GUI or chat client.

The object has the following members:

- `alternatives`: A list of [alternative objects](#alternative-object).

If TDM asks a [yes-no question](../formalism.md#yn-questions), it expects the yes or no [answer](../formalism.md#answer-moves):

```json
{
  "alternatives": [
    {"semantic_expression": "answer(yes)"},
    {"semantic_expression": "answer(no)"}
  ]
}
```

If TDM asks an [alternative question](../formalism.md#alt-questions) or a [wh-question](../formalism.md#wh-questions) where the alternatives are known, the expected input object either contains [answer moves](../formalism.md#answer-moves) with [unary propositions](../formalism.md#unary-propositions):

```json
{
  "alternatives": [
    {"semantic_expression": "answer(selected_contact(contact_john))"},
    {"semantic_expression": "answer(selected_contact(contact_lisa))"}
  ]
}
```

... or [request](../formalism.md#request-moves) and [ask moves](../formalism.md#ask-moves):

```json
{
  "alternatives": [
    {"semantic_expression": "request(call)"},
    {"semantic_expression": "ask(?X.phone_number(X))"}
  ]
}
```

## Alternative object
An alternative object contains information about the moves that the user is expected to take the next turn. It contains the following members:

- `semantic_expression`: A semantic expression of the expected move, expressed in the [dialog formalism](../formalism.md#moves).
