For better language coverage of your DDDs, you may want to enable the machine-learning based Rasa NLU.

This guide is written for version `0.14.6` of Rasa NLU.

Before getting started, make sure to use hosted a Rasa NLU with the necessary dependencies installed. For instance, if you plan on using a Spacy pipeline, ensure that it has the appropriate language models and Spacy itself installed.

For more information, read up on the [Rasa NLU documentation](https://legacy-docs.rasa.com/docs/nlu/0.14.6/). We recommend [running it in Docker](https://legacy-docs.rasa.com/docs/nlu/0.14.6/docker/).

# Generate training data

In order to use Rasa NLU with TDM, we need to train the model. The Tala SDK can be used to generate training data for your DDD: `tala generate-rasa my-ddd eng > training_data.yml`.

# Configure the pipeline

The generated training data comes with the `spacy_sklearn` pipeline by default. At the head of the training data we find:

```yml
language: "en"

pipeline: "spacy_sklearn"

data: |
...
```

Here, the pre-configured `spacy_sklearn` pipeline will be used, but [there are others to choose from too](https://legacy-docs.rasa.com/docs/nlu/0.14.6/choosing_pipeline/).

It's also possible to configure the pipeline oneself, by listing the components explicitly. For instance, this is the `spacy_sklearn` pipeline:
```yml
pipeline:
- name: "SpacyNLP"
- name: "SpacyTokenizer"
- name: "RegexFeaturizer"
- name: "SpacyFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "SklearnIntentClassifier"
```

# Add pre-trained named entity recognizers (NERs)

Rasa NLU [supports pre-trained NERs](https://legacy-docs.rasa.com/docs/nlu/0.14.6/entities/) to be part of the pipeline, for instance the NER from [Duckling](https://legacy-docs.rasa.com/docs/nlu/0.14.6/components/#ner-duckling-http) which can be used together with TDM.

In this version of TDM, the following Duckling entities are supported:
- `number`: maps to the `integer` sort.
- `time`: maps to the `datetime` sort.

To enable it, make sure it's available to the Rasa server and add its component to an explicit pipeline:

```yml
- name: "DucklingHTTPExtractor"
  url: "http://duckling:8000"
```

Here, Duckling is available to the Rasa server at `http://duckling:8000`. The `spacy_sklearn` pipeline with the addition of Duckling then becomes:

```yml
pipeline:
- name: "SpacyNLP"
- name: "SpacyTokenizer"
- name: "RegexFeaturizer"
- name: "SpacyFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "SklearnIntentClassifier"
- name: "DucklingHTTPExtractor"
  url: "http://duckling:8000"
```

# Train the model

Once the training data and pipeline are configured, train your model according to the [Rasa NLU HTTP API](https://legacy-docs.rasa.com/docs/nlu/0.14.6/http/#post-train).

For instance with:

```bash
curl -XPOST -H 'Content-Type: application/x-yml' 'http://my-rasa-nlu.my-cloud.com:5000/train?project=my-ddd&model=my-model' --data-binary @training_data.yml
```

In this case, the URL, `project` and `model` also need to be specified in the DDD config in the next step.


# Configure the DDD

Make sure to configure Rasa NLU in the DDD config, for instance at `my_ddd/ddd.config.json`, by adding language specific `rasa_nlu` objects. For instance, for English:

```json
{
    "rasa_nlu": {
        "eng": {
            "url": "http://my-rasa-nlu.my-cloud.com:5000/parse",
            "config": {
                "project": "my-ddd",
                "model": "my-model"
            }
        }
    }
}
```

The `rasa_nlu` object contains the following fields:

- `url`: A string URL, pointing to the [`/parse` endpoint of a Rasa NLU server](https://legacy-docs.rasa.com/docs/nlu/0.14.6/http/#post-parse).
- `config`: An object sent in the JSON payload when TDM posts it to the `url`. It can contain for instance `project` and `model`, as specified by [the Rasa NLU HTTP API](https://legacy-docs.rasa.com/docs/nlu/0.14.6/http/#post-parse). TDM also adds the field `"q": "<user utterance>"`.

If Rasa NLU should not be used for a particular language, remove the language altogether:

```json
{
    "rasa_nlu": {}
}
```
