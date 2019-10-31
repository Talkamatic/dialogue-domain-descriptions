This document describes API version 3.1 for HTTP frontends, enabling frontends to integrate with TDM over HTTP. It covers e.g. how input from the user and output from TDM are communicated between TDM and the client.

The client invokes TDM with an HTTP request to the interaction endpoint, e.g. `http://localhost:9090/interact`, using the POST method and a JSON body. The client should expect the status code to be 200 OK. For other status codes, the client should report an error to the user.

The request body always contains a version number, specifying the version of the HTTP API format.

The exact format of the request and the response depends on the type of request as described below.

# Start session requests
When a new session should be started, the client issues a `start_session` request. The response contains initial output from TDM and a session ID that can be used in subsequent requests. For more details, see [the response format](#response-format).

If a session ID is provided together with the `start_session` request, an error is given. The integrity of the session is however maintained.

**Request**

Example:

```json
{
  "version": "3.1",
  "session": {},
  "request": {
    "start_session": {}
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object)

The `start_session` object may contain the following optional members:

- `ddd_set`: A string specifying a DDD set for the session. If omitted, a default DDD set configured by the backend is used.

The `start_session` request may be issued on its own, so that the system will start the conversation; or combined with `natural_language_input`, `semantic_input` and `event` requests to start the conversation from there.

Example when combined with `natural_language_input`:

```json
{
  "version": "3.1",
  "request": {
    "start_session": {},
    "natural_language_input": {...}
  }
}
```

**Response**

See [response format](#response-format).

# Natural language input requests
When the client detects natural language input from the user, it issues a request and receives output from TDM. The request can contain either hypotheses with the `speech` modality, or a single utterance with the `text` modality.

**Request**

Speech input example:

```json
{
  "version": "3.1",
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
  "version": "3.1",
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

The `natural_language_input` object contains the following members:

- `modality`: Should be either `speech` or `text` depending on how the input was detected.
- `hypotheses`: A list of [hypothesis objects](#hypothesis-object) which should be provided if `modality` is `speech`; otherwize the field should be omitted.
- `utterance`: A string containing the utterance if `modality` is `text`; otherwize the field should be omitted.

The `natural_language_input` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:
```json
{
  "version": "3.1",
  "request": {
    "start_session": {},
    "natural_language_input": {...}
  }
}
```

**Response**

See [response format](#response-format).

# Semantic input requests
When the client has user input on a semantic format, as a user move, it should issue the `semantic_input` request.

Semantic in this case means that the user input does not need to be interpreted; the user move is already known. This is useful when an external natural language understanding (NLU) component has already interpreted the input; when the user presses a button in a GUI; or for instance when the user makes a gesture which is interpreted as a user move.

The semantic format is different for each of the supported user moves. See [the move object section](#move-object) for examples.

**Request**

```json
{
  "version": "3.1",
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
      ]
    }
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object)

The `semantic_input` object contains the following members:

- `interpretations`: A list of [interpretation objects](#interpretation-object). TDM will use confidence scores and the context of the current state of the session to decide which interpretation to act upon.

The `semantic_input` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:

```json
{
  "version": "3.1",
  "request": {
    "start_session": {},
    "semantic_input": {...}
  }
}
```

**Response**

See [response format](#response-format).

# Passivity requests
When the client detects user passivity, it issues a request and receives output from TDM.

**Request**

Example:

```json
{
  "version": "3.1",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "passivity": {}
  }
}
```

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object)

The `passivity` request may not be combined with other requests in the same call.

**Response**

See [response format](#response-format).

# Event requests
When the client detects that an event pertaining to a relevant DDD has occurred, it should issue an event notification request, and receives output from TDM.

**Request**

Example:

```json
{
  "version": "3.1",
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

The `session` object can contain frontend-specific session data to be used in dialog or by services. For more details, see [the session object](#session-object)

The `event` object contains the following members:

- `name`: A string corresponding to the name of the event, specified as an action in the service interface.
- `status`: Either `started` or `ended`.
- `parameters`: A map of key-value pairs pertaining to the event, corresponding to the parameters specified for the action in the service interface. The key is a string matching the parameter's predicate, and the value is a string containing the ID of the value (e.g. a number or a string depending on the sort).

The `event` request may be combined with the `start_session` request when a session does not yet exist, but may not be combined with other requests.

Example:

```json
{
  "version": "3.1",
  "request": {
    "start_session": {},
    "event": {...}
  }
}
```

**Response**

See [response format](#response-format).

# Session object
A session object can contain frontend-specific session data. The data is forwarded as is to all service calls on the [HTTP API for services](http_service.md#session-object). That way, the data can be used in service calls directly; or influence the dialog, for instance by being retrieved through service queries.

Note that session data is not automatically stored or attached to the session within TDM. It is returned in the [response](#response-format) and can be injected in future requests. If specific data should be available to all service calls on a session, the data needs to be injected in every request on that session, or the DDD needs to retrieve it into the dialog state, for instance by a service query.

For all requests except [start session](#start-session-requests), a `session_id` is required and used to identify to which session the request is being made.

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

# Hypothesis object
A hypothesis object contains information about what the user is believed to have uttered, consisting of the following members:

- `utterance`: A string containing the utterance.
- `confidence`: A number from 0.0 to 1.0 representing the confidence of the hypothesis.

# Interpretation object
An interpretation translates an utterance into one or several semantic moves. An interpretation object contains:

- `utterance`: (optional) A string containing the utterance.
- `modality`: The modality that the user used to provide the original input. One of `speech`, `text`, `haptic`, `other`.
- `moves`: A list of [move objects](#move-object).

# Move object
A move object contains information about how a user move was interpreted. Its members are:

- `ddd`: (optional) A string containing the DDD name. For DDD independent moves (e.g. `answer(yes)` and `request(up)`), this field may be omitted; in which case the currently active DDD will be used to parse the semantic expression.
- `perception_confidence`: A float between `0.0` and `1.0`, representing the confidence that a spoken utterance actually matches the textual utterance, for instance when a speech-to-text (STT) component turned it into text. If no perception component was used, the confidence should be set to `1.0`.
- `understanding_confidence`: A float between `0.0` and `1.0`, representing the confidence that the textual utterance actually represents this move, for instance when an NLU component interprets the textual utterance. If no understanding component was used, for instance if the user pressed a button, the confidence should be set to `1.0`.
- `semantic_expression`: A semantic expression, representing the move itself. Supported moves are `request`, `ask` and `answer`. See examples below for details.

**Example of a `request` move:**

A `request` move has just one parameter: An action. In this case the `call` action, which must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "request(call)",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.5234
}
```

**Example of builtin `request` move:**

The builtin and DDD independent actions `top` and `up` can be requested without including the DDD name:

```json
{
  "semantic_expression": "request(top)",
  "perception_confidence": 0.56,
  "understanding_confidence": 0.65305
}
```

**Example of an `ask` move:**

An `ask` move is a more complex parameter than the `request`. For those who know Prolog this might look familiar. `?X.phone_number(X)` means that we're asking for an unknown phone number individual. In this case, the `phone_number` predicate must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "ask(?X.phone_number(X))",
  "perception_confidence": 0.31,
  "understanding_confidence": 0.10126
}
```

**Example of a sortal `answer` move:**

A sortal `answer` move has an individual as its parameter. In this case, the individual `contact_john`, must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "answer(contact_john)",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.98532
}
```

**Example of a propositional `answer` move:**

A propositional `answer` move has a proposition as its parameter, consisting of a predicate and an individual. In this case, the predicate `selected_contact`, and the individual `contact_john`, must be defined in the ontology of the `phone` DDD.

```json
{
  "ddd": "phone",
  "semantic_expression": "answer(selected_contact(contact_john))",
  "perception_confidence": 0.65,
  "understanding_confidence": 0.71347
}
```

**Example of builtin sortal `answer` move:**

The builtin and DDD independent answers `yes` and `no` can be used without including the DDD name:

```json
{
  "semantic_expression": "answer(yes)",
  "perception_confidence": 0.834,
  "understanding_confidence": 0.71359
}
```

# Response format
The response format differs when the request was successful compared to when it encountered an error.

**Successful request**

The TDM response from a successful request typically contains an output utterance and other relevant information. Example:

```json
{
  "version": "3.1",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "output": {
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
    "language": "eng"
  }
}
```

The `session` object is always provided and contains the same data that was provided in the request. Unlike requests however, it always contains:

- `session_id`: The ID of the current session.

The `output` object is provided unless an error has occurred and has the following members:

- `utterance`: A string representing the output utterance from the system and should be realized by the client (e.g. by speaking it or displaying it as text).
- `expected_passivity`: If not null, the value is a number corresponding to the number of seconds of user passivity after which the client is expected to make a [passivity request](#passivity-requests). If the value is 0.0, the passivity notification request should be issued immediately after having realized the system output.
- `actions`: A list of [action invocation objects](#action-invocation-object), which needs to be invoked by the client. TDM assumes that the actions will succeed and reports them accordingly.

The `nlu_result` object is provided for [natural language input requests](#natural-language-input-requests), unless an error has occurred. It has the following members:

- `selected_utterance`: The utterance selected as the best candidate amoung the list of hypotheses.
- `confidence`: A number representing the joint confidence of the input and the NLU processing.

The `context` object is provided unless an error has occurred and contains the following members:

- `active_ddd`: The name of the currently active DDD.
- `facts`: Information gathered during the conversation (see [facts object](#facts-object)).
- `language`: ID of the current language.

A `warnings` field is provided if warnings have been issued, as a list of strings, one string per warning. This can for instance happen when TDM is updated to a new version of this frontend API and the previous version is deprecated. In such cases, update your request formats to comply with the warning and avoid potential future errors:

**Request that encountered an error**

The TDM response when an error was encountered in the request contains an error description.

```json
{
  "version": "3.1",
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

# Action invocation object
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

# Facts object
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
