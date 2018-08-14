This document describes how to integrate a frontend with TDM over HTTP, covering e.g. how input from the user and output from TDM are communicated between TDM and the client.

The client invokes TDM with an HTTP request to the interaction endpoint, e.g. `http://localhost:9090/interact`, using the POST method and a JSON body. The client should expect the status code to be 200 OK. For other status codes, the client should report an error to the user.

The request body always contains a version number, specifying the version of the HTTP API format.

The exact format of the request and the response depends on the type of request as described below.

# Start session requests
When a new session should be started, the client issues a request, and receives the initial output from TDM.

**Request**

Example:

```json
{
  "version": 1.0,
  "request": {
    "type": "start_session"
  }
}
```

The `request` object may also contain the following optional fields:

- `ddd_set`: A string specifying a DDD set for the session. If omitted, a default DDD set configured by the backend is used.

The body may also contain an `input` object (see [Input requests](#input-requests)), containing the input from the user that triggered the request to start a new session. If omitted, TDM lets the system begin the conversation.

**Response**

See [response format](#response-format).

# Input requests
When the client detects input from the user, it issues a request and receives output from TDM.

**Request**

Speech input example:

```json
{
  "version": 1.0,
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "input"
  },
  "input": {
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
```

Text input example:

```json
{
  "version": 1.0,
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "input"
  },
  "input": {
    "modality": "text",
    "utterance": "I'm searching for flights from London to Paris tomorrow"
  }
}
```

The `input` object contains the following fields:

- `modality`: Should be either `speech` or `text` depending on how the input was detected.
- `hypotheses`: A list of [hypothesis objects](#hypothesis-object) which should be provided if `modality` is `speech`; otherwize the field should be omitted.
- `utterance`: A string containing the utterance if `modality` is `text`; otherwize the field should be omitted.

**Response**

See [response format](#response-format).

# Passivity requests
When the client detects user passivity, it issues a request and receives output from TDM.

**Request**

Example:

```json
{
  "version": 1.0,
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "passivity"
  }
}
```

**Response**

See [response format](#response-format).

# Event requests
When the client detects that an event pertaining to a relevant DDD has occurred, it should issue an event notification request, and receives output from TDM.

**Request**

Example:

```json
{
  "version": 1.0,
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "event"
  },
  "event": {
    "name": "IncomingCall",
    "status": "started"
    "parameters": {
      "caller": "contact_12345"
    }
  }
}
```

The `event` object contains the following fields:

 - `name`: A string corresponding to the name of the event, specified as an action in the service interface.
 - `status`: Either `started` or `ended`.
 - `parameters`: A map of key-value pairs pertaining to the event, corresponding to the parameters specified for the action in the service interface. The key is a string matching the parameter's predicate, and the value is a string containing the ID of the value (e.g. a number or a string depending on the sort).

**Response**

See [response format](#response-format).

# Hypothesis object

A hypothesis object contains information about what the user is believed to have uttered, consisting of the following fields:

- `utterance`: A string containing the utterance.
- `confidence`: A number from 0.0 to 1.0 representing the confidence of the hypothesis.

# Response format
The response from TDM typically contains an output utterance and other relevant information. Example:

```json
{
  "version": 1.0,
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

The `output` object is provided unless an error has occurred and has the following members:

- `utterance`: A string representing the output utterance from the system and should be realized by the client (e.g. by speaking it or displaying it as text).
- `expected_passivity`: If not null, the value is a number corresponding to the number of seconds of user passivity after which the client is expected to make a [passivity notification request](#passivity-notification). If the value is 0.0, the passivity notification request should be issued immediately after having realized the system output.
- `actions`: A list of [action invocation objects](#action-invocation-objects), representing action to be invoked by the client. TDM assumes that actions will succeed and reports them accordingly.

The `nlu_result` object is provided for [input requests](#input-requests) unless an error has occurred and contains the following fields:

- `selected_utterance`: The utterance selected as the best candidate amoung the list of hypotheses.
- `confidence`: A number representing the joint confidence of the input and the NLU processing.

The `context` object is provided unless an error has occurred and contains the following members:

 - `active_ddd`: The name of the currently active DDD.
 - `facts`: Information gathered during the conversation (see [facts object](#facts-object)).
 - `language`: ID of the current language.

An `error` field is provided if an error has occurred. In such cases, an error should be reported to the user by the client, and the session should not be resumed with further requests. The `error` field has the following members:

 - `description`: A human readable technical description of the error.

# Action invocation object
An action invocation object contains information about an action to be invoked by the client. The object has the following members:

 - `name` is a string corresponding to the action's name in `service_interface.xml`.
 - `parameters` contains values for all parameters that are specified for the method in `service_interface.xml`. If a parameter is unknown, its value is `null`. Otherwise it's an object containing:
     - `sort`: ID of the predicate's sort as defined in the ontology.
     - `value`: ID of the value. For the sorts `integer` and `real`, the ID is a number. For other sorts, e.g. `string`, `datetime` and custom sorts, the ID is a string.
     - `grammar_entry`: Natural-language representation of the value.

# Facts object
The `facts` field contains a map of key-value pairs for information gathered during the conversation, e.g. from the user. The map may be empty.

The key is a string matching a predicate as defined in the ontology. The value is an object with the following members:

 - `sort`: ID of the predicate's sort as defined in the ontology.
 - `value`: ID of the value (e.g. a number or a string depending on the sort). For predicates of sort `datetime`, the ID is an ISO 8601 string.
 - `grammar_entry`: Natural-language representation of the value.

Example:
```json
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
```
