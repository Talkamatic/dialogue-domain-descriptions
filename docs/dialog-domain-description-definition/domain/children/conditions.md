# Conditions
## Definitions
```xml
    <has_shared_value predicate="p"/>
    <has_private_value predicate="p"/>
    <has_shared_or_private_value predicate="p"/>
    <is_shared_commitment predicate="p" value="x"/>
    <is_private_belief predicate="p" value="x"/>
    <is_private_belief_or_shared_commitment predicate="p" value="x"/>
```

Conditions that evaluate to true depending on what the current beliefs of the system are.

Attribute | Type | Description |
--- | --- | --- |
predicate | string | Required. The value must me enumerated in the ontology.
predicate | string | Required for the `has_*_value` conditions. The value must me enumerated in the ontology.

## Parents
- [<downdate\_condition\>](/dialog-domain-description-definition/domain/children/downdate_condition)
- [<if\>](/dialog-domain-description-definition/domain/children/if)

## Children
- None

## Behaviour
The `has_*_value` conditions evaluate to true if there is a
proposition in either shared commitments or in private beliefs or in
any of them, depending on the actual condition.

The `is_*` conditions evaluate to true if the proposition specified in
the attributes is to be found in in either shared commitments or in
private beliefs or in any of them, depending on the actual condition.

## Examples

### `has_shared_value`:

This condition will evaluate to `true` if it is known by the user and
the system whether the flight is late or not.

```xml
<has_shared_value predicate="flight_departure"/>
```

### `has_private_value`:

This condition will evaluate to `true` if it is known by the system
but not by the user whether the flight is late or not.

```xml
<has_private_value predicate="flight_departure"/>
```

### `has_shared_or_private_value`:

This condition will evaluate to `true` if it is known, possibly only
by the system, whether the flight is late or not.

```xml
<has_shared_or_private_value predicate="flight_departure"/>
```

### `is_shared_commitment`:

This condition will evaluate to `true` if it is known by the user and
the system that the flight is late.

```xml
<is_shared_commitment predicate="flight_departure" value="late"/>
```

### `is_private_belief`:
This condition will evaluate to `true` if it is known only by the
system that the flight is late.

```xml

<is_private_belief predicate="flight_departure" value="late"/>
```

### `is_private_belief_or_shared_commitment`:

This condition will evaluate to `true` if it is known, possibly only
by the system, whether the flight is late or not.

```xml
<is_private_belief_or_shared_commitment predicate="flight_departure" value="late"/>
```
