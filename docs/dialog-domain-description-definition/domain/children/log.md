# Log
## Definition
```xml
<log message="This is a log message">
```

The plan item logs a message on DEBUG level.

Attribute | Type | Description |
--- | --- | --- |
message | string | Required. The value of the message attribute is currently the only thing that is logged.|

## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)

## Children
None

## Behaviour
Using the <log/> element will log the message on debug level. The log entry will contain the following:
```json
{
    "message": "This is a log message",
    "event": "Executing <log> element in domain.xml"
}
```

## Examples
### Assume-issue entry for assuming the issue about the departure time (which is the resolve goal of another plan):

```xml
<log message="This is a log message">
```
