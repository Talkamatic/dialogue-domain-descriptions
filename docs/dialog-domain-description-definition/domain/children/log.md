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
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

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
### Log element for logging a string:

```xml
<log message="This is a log message">
```
