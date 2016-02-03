# dialogue-domain-descriptions
Learn how to voice-enable your applications by looking at these simple dialogue domain description (DDD) examples.

### incremental_search
Is your user asking for something? Make sure your application replies with just the perfect amount of questions to find one and only one match.

    U> Call John
    S> What's his last name?
    U> Johnson
    S> Calling John Johnson at 0702446698.

Incremental search utilizes predicate features, which are declared in the ontology of the DDD. When a service is queried for individuals of the predicate, the features need to match. By asking the user to specify more features, the search can be narrowed down to finally match a single individual.
