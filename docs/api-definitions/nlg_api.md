# NLG API

This document describes version 1.0 of the API for Natural Language Generation (NLG) components, enabling 3rd party NLGs to integrate with the TDM pipeline. It covers how the TDM pipeline sends requests to the NLG, and how it expects responses to come back.

The endpoint that the TDM pipeline calls to reach the NLG is configurable on the pipeline side, but it's recommended to accept requests on the root URL, e.g: `http://nlg/`.

## Request

When the TDM pipeline needs to generate what the system is saying, it sends a request to the NLG. The request contains moves from the dialog manager.

Example:

```json
{
  "version": "1.0",
  "moves": [
    {"semantic_expression": "icm:acc*pos"},
    {"semantic_expression": "ask(?X.selected_contact(X))"}
  ]
}
```

The following members are required:

- `version`: The version that the consumer is expecting served. This is used to detect compatibility problems.
- `moves`: A list of [Move objects](shared_objects.md#nlg-move-object).

## Response

The NLG generates a natural language utterance. It can either succeed its generation, or fail if it doesn't cover the moves sent to it.

### General example

```json
{
  "status": "success",
  ...
}
```

All responses need to contain the following members:

- `status`: `success` if the NLG successfully generated an utterance, `fail` if it failed and `error` if an error happened unexpectedly.

### Success

When the NLG succeeds in generating its utterance, use the `success` response.

```json
{
  "status": "success",
  "utterance": "Who do you want to call?"
}
```

When `status` is `success`, the following members need to be present:

- `utterance`: A string with the generated utterance.

### Failure

When the NLG fails to generate an utterance, for instance because one of the moves sent to it isn't covered, use the `fail` response.

```json
{
  "status": "fail"
}
```

### Error

When an error occurs unexpectedly, use the `error` response.

```json
{
  "status": "error",
  "description": "A helpful description of the error."
}
```

When `status` is `error`, the following members need to be present:

- `message`: A string with a helpful message.
- `code` (optional): A numeric code identifying the error, if applicable.
