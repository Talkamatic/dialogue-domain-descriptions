This document describes API version 1.0 for HTTP services. It needs to be implemented by services invoked by TDM over HTTP. Services are used by DDDs to invoke actions, invoke queries, recognize entities, and to validate parameters.

TDM invokes service methods with an HTTP request to the endpoint specified in `service_interface.xml`, using the POST method and a JSON body. It expects the status code to be 200 OK. (For other status codes, TDM reports an error to the user.)

The request body always contains a version number, specifying the version of the service integration format. The service can use the version in the request to validate that the service implementation is compatible with the request. The service also returns a version number in the response body, corresponding to the version of this API used when implementing the service. If the service returns a version number that is not compatible with the request, TDM reports an error to the user.

Responses from services adhere to the [JSend specification](https://github.com/omniti-labs/jsend). See [response format](#response-format) for a general description.

The exact format of the request and the response depends on the service method and is described below.

# Action requests
**Request**

Below is an example of a request body for an action called `SetTemperature`, invoked when the user has requested to set the temperature to 23 degrees:

```json
{
  "version": "1.0",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "action",
    "name": "SetTemperature",
    "parameters": {
      "degrees": {
        "sort": "integer",
        "value": 23,
        "grammar_entry": "23"
      }
    }
  },
  "context": {
    "active_ddd": "MyDDD",
    "facts": {
      "degrees": {
        "sort": "integer",
        "value": 23,
        "grammar_entry": "23"
      }
    },
    "language": "eng",
    "invocation_id": "2222-ijkl-3333-mnop"
  }
}
```

Format for `request`: see [Request object](#request-object).

Format for `session`: see [Session object](#session-object).

Format for `context`: see [Context object](#context-object).

**Response**

Actions invoked over HTTP can either succeed or fail with an expected reason. Below is the expected response body for the request above, when successful:

```json
{
  "status": "success",
  "data": {
    "version": "1.0"
  }
}
```

Format for `status` and `data`: see [Response format](#response-format).

But say that someone tries to set the temperature of a refrigerator to 23 degrees, which is more than it can handle. If there's a failure reason `temperature_too_high` declared in `service_interface.xml`, the service can fail expectedly with:

```json
{
  "status": "fail",
  "data": {
    "version": "1.0",
    "reason": "temperature_too_high"
  }
}
```

Format for `status` and `data`: see [Response format](#response-format).

The `data` object additionally contains these action specific members:

- `reason` matching the failure that occurred. It needs to match one of the failure reasons declared for this action in `service_interface.xml`.

# Query requests
Queries are invoked by TDM to retrieve information from a service, e.g. in order to be able to respond to a question from a user, or to fetch alternatives for alternative questions.

**Request**

Below is an example of a request body for a query called `current_temperature` with the parameter `location`, invoked when the user has asked for the temperature in London:

```json
{
  "version": "1.0",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "query",
    "name": "current_temperature",
    "parameters": {
      "location": {
        "sort": "city",
        "value": "city_012345",
        "grammar_entry": "London"
      }
    },
    "min_results": 1,
    "max_results": 1
  },
  "context": {
    "active_ddd": "MyDDD",
    "facts": {
      "location": {
        "sort": "city",
        "value": "city_012345",
        "grammar_entry": "London"
      }
    },
    "language": "eng",
    "invocation_id": "2222-ijkl-3333-mnop"
  }
}
```

Format for `request`: see [Request object](#request-object).

The `request` object additionally contains these query specific members:

- `min_results` specifies the minimum number of results that the service should return as a non-negative integer. If the service returns fewer results than specified by `min_results`, TDM reports an error to the user.
- `max_results` specifies the maximum number of results that the service should return. `max_results` is either a positive integer, or `null` meaning that there is no upper bound. If the service returns more results than specified by `max_results`, TDM reports an error to the user.

Format for `session`: see [Session object](#session-object).

Format for `context`: see [Context object](#context-object).

**Response**

Below is an example of a response body for the request above, when the current temperature in London is 17 degrees:

```json
{
  "status": "success",
  "data": {
    "version": "1.0",
    "result": [
      {
        "value": 17,
        "confidence": 1.0,
        "grammar_entry": null
      }
    ]
  }
}
```

General format for responses: see [Response format](#response-format).

`data` additionally contains these members specific to queries:

- `result`: contains a list result items. Each result item is an object with the following members:
    - `value` can be either a number, string or `null`, depending on the query's predicate. For predicates of sort `integer` or `real`, a number is expected. For predicates of sort `datetime`, an ISO 8601 string is expected. For predicates of a custom sort, a string is expected, corresponding to the name of the individual. For dynamic sorts, the value `null` is supported, in which case a grammar entry is required.
    - `confidence` should normally be set to 1.0. However, when the information is uncertain - e.g. when making a prediction from a user model - `confidence` can be set to a value from 0.0 to 1.0.
    - `grammar_entry` can be set to specify a natural-language represention of the result. This is required for dynamic sorts, when `value` is `null`.

## Additional query example: Multiple results
Below is an example of a request and response for a query called `selected_contact` which is used to determine whether a single contact can be identified based on a first and last name. In the example, only the first name is known, and the service returns two matching contacts.

Request:

```json
{
  "version": "1.0",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "query",
    "name": "selected_contact",
    "parameters": {
      "selected_first_name": {
        "sort": "first_name",
        "value": "fist_name_john",
        "grammar_entry": "John"
      },
      "selected_last_name": null
    },
    "min_results": 0,
    "max_results": null
  },
  "context": {
    "active_ddd": "MyDDD",
    "facts": {
      "selected_first_name": {
        "sort": "first_name",
        "value": "fist_name_john",
        "grammar_entry": "John"
      }
    },
    "language": "eng",
    "invocation_id": "2222-ijkl-3333-mnop"
  }
}
```

Response:

```json
{
  "status": "success",
  "data": {
    "version": "1.0",
    "result": [
      {
        "value": "contact_john_johnson",
        "confidence": 1.0,
        "grammar_entry": "John Johnson"
      },
      {
        "value": "contact_john_thompson",
        "confidence": 1.0,
        "grammar_entry": "John Thompson"
      }
    ]
  }
}
```

Also note that for this request example, the service may return an empty list of results if no matching contacts were found for the given parameters.

# Entity recognizer requests
Entity recognizers are invoked by TDM to identify entities in user utterances.

**Request**

Below is an example of a request body for an entity recognition invocation when the user has said "what is the temperature in London":

```json
{
  "version": "1.0",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "entity_recognizer",
    "name": "LocationRecognizer",
    "utterance": "what is the temperature in London"
  },
  "context": {
    "active_ddd": "MyDDD",
    "facts": {},
    "language": "eng",
    "invocation_id": "2222-ijkl-3333-mnop"
  }
}
```

Format for `request`: see [Request object](#request-object).

The `request` object additionally contains these members specific to entity recognizers:

- `utterance` is the user utterance that should be searched for entities. It's a string.

Format for `session`: see [Session object](#session-object).

Format for `context`: see [Context object](#context-object).

**Response**

Below is an example of a response body for the request above:

```json
{
  "status": "success",
  "data": {
    "version": "1.0",
    "result": [
      {
        "grammar_entry": "London",
        "sort": "city",
        "value": "city_012345"
      }
    ]
  }
}
```

General format for responses: see [Response format](#response-format).

`data` additionally contains these members specific to entity recognizers:

- `result`: contains a list of zero or more result items. Each result item is an object with the following members:
    - `grammar_entry`: Natural-language representation of the recognized entity.
    - `sort`: The entity's sort, corresponding to the sort's name in `ontology.xml`.
    - `value`: ID or semantic representation of the entity if known, otherwise `null`. For static (non-dynamic) sorts, the `value` is mandatory and should correspond to the semantic name of an individual.

# Validator requests
Validators are invoked by TDM to determine if information provided by the user is valid. If not, relevant feedback is given to the user.

**Request**

Below is an example of a request body for a validator called `RouteValidator` with the parameters `departure` and `destination`:

```json
{
  "version": "1.0",
  "session": {
    "session_id": "0000-abcd-1111-efgh"
  },
  "request": {
    "type": "validator",
    "name": "RouteValidator",
    "parameters": {
      "departure": {
        "sort": "city",
        "value": "city_012345",
        "grammar_entry": "London"
      },
      "destination": {
        "sort": "city",
        "value": "city_099998",
        "grammar_entry": "Chippinghirst"
      }
    }
  },
  "context": {
    "active_ddd": "MyDDD",
    "facts": {
      "departure": {
        "sort": "city",
        "value": "city_012345",
        "grammar_entry": "London"
      },
      "destination": {
        "sort": "city",
        "value": "city_099998",
        "grammar_entry": "Chippinghirst"
      }
    },
    "language": "eng",
    "invocation_id": "2222-ijkl-3333-mnop"
  }
}
```

Format for `request`: see [Request object](#request-object).

Format for `session`: see [Session object](#session-object).

Format for `context`: see [Context object](#context-object).

**Response**

Below is an example of a response body for the request above:

```json
{
  "status": "success",
  "data": {
    "version": "1.0",
    "is_valid": false
  }
}
```

General format for responses: see [Response format](#response-format).

`data` additionally contains these validator specific members:

- `is_valid`: can be either `true` or `false`, specifying whether the combination of parameters is valid or not.

# Request object
In general, the `request` object contains the following members. It may also contain additional method specific members.

- `type` is the method type, e.g. `action` or `query`. All methods that can be declared in `service_interface.xml` are supported. See examples for each of them above.
- `name` is the method name, as specified in `service_interface.xml`.
- `parameters` contains values for all parameters that are specified for the method in `service_interface.xml`. If a parameter is unknown, its value is `null`. Otherwise it's an object containing:
    - `sort`: ID of the predicate's sort as defined in the ontology.
    - `value`: ID of the value. For the sorts `integer` and `real`, the ID is a number. For other sorts, e.g. `string`, `datetime` and custom sorts, the ID is a string.
    - `grammar_entry`: Natural-language representation of the value.

Example:
```json
{
  "request": {
    "type": "validator",
    "name": "contact_validator",
    "parameters": {
      "selected_first_name": {
        "sort": "first_name",
        "value": "fist_name_john",
        "grammar_entry": "John"
      },
      "selected_last_name": null
    }
  }
}
```

# Session object
The `session` object contains the following members:

- `session_id`: String representing the current TDM session.

# Context object
The `context` object contains the following members:

- `active_ddd`: The name of the currently active DDD.
- `facts`: Information gathered during the conversation (see [Facts object](#facts-object)).
- `language`: ID of the current language.
- `invocation_id`: A unique identifer for the invocation from TDM. This ID can be logged for analytics and issue reporting.

## Facts object
The `facts` object contains a map of key-value pairs for information gathered during the conversation, e.g. from the user. The map may be empty.

The key is a string matching a predicate as defined in the ontology. The value is an object with the following members:

- `sort`: ID of the predicate's sort as defined in the ontology.
- `value`: ID of the value. For the sorts `integer` and `real`, the ID is a number. For other sorts, e.g. `string`, `datetime` and custom sorts, the ID is a string.
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

# Response format
All service responses adhere to the [JSend specification](https://github.com/omniti-labs/jsend).

In general, responses can have one of three appearances, corresponding to the status of the invocation: `success`, `fail` and `error`. See the examples below.

Success:
```json
{
  "status": "success",
  "data": {
    "version": "1.0"
  }
}
```

Successful method invocations need to set their `status` to `success`.

The `data` object contains mostly method specific members. All methods need however include:

- `version`: the version of the API used to process the request and format the response. If the version is not compatible with the request, TDM reports an error to the user.

Fail:
```json
{
  "status": "fail",
  "data": {
    "version": "1.0"
  }
}
```

Failures cannot be used with queries, entity recognizers or validators, but is supported by [actions](#action-requests). If a `fail` status is not supported or is reported unexpectedly, it is treated as an `error`. `error` is however preferred over `fail` since a helpful message can be provided. TDM will report the error to the user, but will not mention any details.

To report a failure, the `status` need to be set to `fail`.

The `data` object contains mostly method specific members. All methods need however include:

- `version`: the version of the API used to process the request and format the response.

Error:
```json
{
  "status": "error",
  "message": "Could not communicate with the database.",
  "code": 135,
  "data": {
    "version": "1.0"
  }
}
```

When a service encounters an error, i.e. an exception, the `status` need to be set to `error`. TDM will report the error to the user, but will not mention any details.

`message` should be a human-readable message, explaining what went wrong. It will be logged but is not exposed to end-users.

`code` (optional) is a numeric code identifying the error, if applicable.

The `data` needs to contain:

- `version`: the version of the API used to process the request and format the response.
