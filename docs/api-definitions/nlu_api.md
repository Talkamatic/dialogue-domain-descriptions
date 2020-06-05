# NLU API

This document describes the API for NLUs, enabling 3rd party NLUs to integrate with the TDM pipeline. It covers how the TDM pipeline sends requests to the NLU, and how it expects responses to come back.
The endpoint that the TDM pipeline calls to reach the NLU is configurable on the pipeline side, but it's recommended to accept requests on the root URL, e.g: `http://nlu/`.

## Request
When the TDM pipeline needs to understand what a user has said, it sends a request to the NLU. The request contains natural language input consisting of either hypotheses with the `speech` modality, or a single utterance with the `text` modality.

See the [natural language input object](pipeline_api.md#natural-language-input-object).

Example:

```json
{
  "modality": "speech",
  "hypotheses": [
    {
      "utterance": "I want chinese",
      "confidence": 0.86
    },
  ]
}
```
## Response

The NLU's output must be converted into semantic input containing `interpretations` and `entities`.

See the [semantic input object](pipeline_api.md#semantic-input-object).

Example:
```json
{
  "interpretations": [
    {
      "utterance": "I want to have chinese food",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.86,
          "understanding_confidence": 0.92215,
          "ddd": "my_restaurants",
          "semantic_expression": "request(restaurant_search)"
        },
        {
          "perception_confidence": 0.86,
          "understanding_confidence": 0.98532,
          "ddd": "my_restaurants",
          "semantic_expression": "answer(cuisine_chinese)"
        }
      ]
    },
    {
      "utterance": "I want to have chinese food",
      "modality": "speech",
      "moves": [
        {
          "perception_confidence": 0.86,
          "understanding_confidence": 0.5234,
          "ddd": "my_restaurants",
          "semantic_expression": "request(restaurant_search)"
        }
      ]
    }
  ],
  "entities": [
    {
      "name": "cuisine_chinese",
      "sort": "cuisine",
      "natural_language_form": "chinese",
      "ddd": "my_restaurants"
    }
  ]
}
```
