For better language coverage of your DDDs, you may want to enable the machine-learning based Rasa NLU.

# Step 1. Download the language models

Example for English:
```bash
tdm download-spacy eng
```

Note that a limited number of languages is supported, but more are added as they become validated. Refer to the `download-spacy` command for information on language availability:
```bash
tdm download-spacy -h
```

# Step 2. Enable Rasa NLU

Make sure to enable Rasa NLU in your DDD config, for instance at `my_ddd/ddd.config.json`, by setting `enable_rasa_nlu` to `true`.

# Step 3. Create a Rasa config

The first time you enable Rasa NLU for a DDD you also need to create a Rasa config:
```bash
tdm create-rasa-config
```

This creates the file `rasa_config.json` with the following contents:

```json
{
    "duckling_url": "http://localhost:10090",
    "enable_duckling": false
}
```

# Step 4. (Optional) Enable Duckling

In order to make use of Duckling entities such as datetime and integers, you also need to enable Duckling. This makes it possible for the DDD to e.g. support expressions such as "tomorrow at 10 AM" with the built-in sort `datetime`.

In the Rasa config file (`rasa.config.json`), set `enable_duckling` to `true`.

When running the DDD, ensure Duckling has been spawned, for instance with:
```bash
docker run -p 10090:8000 rasa/duckling
```

Note that the port nummber (in this case 10090) needs to correspond with the one specified in `duckling_url` in the Rasa config.
