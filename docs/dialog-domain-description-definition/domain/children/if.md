# If Then Else
## Definition
```xml
<if>
    <condition>
        <proposition .../>
    </condition>
    <then>
        ...
    </then>
    <else>
    ...
    </else>
</if>
```

An if then else element for branching plans. The `if` element can be used recursively. Both the `then` and `else` elements are optional (but to be meaningful at least one is needed).

## Parents
- [<plan\>](/dialog-domain-description-definition/domain/children/plan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)

## Children
- [<condition\>](/dialog-domain-description-definition/domain/children/if)
    - [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<then\>](/dialog-domain-description-definition/domain/children/is_shared_fact)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
    - [<assume\_system\_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get_done)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
    - [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)
- [<else\>](/dialog-domain-description-definition/domain/children/proposition)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
    - [<assume\_system/_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get_done)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
    - [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)

## Behaviour


## Examples
### If/Then element for assuming the answer "200 g" if the selected ingredient is water

```xml
<if>
  <condition>
    <proposition predicate="selected_ingredient" value="water_ingredient"/>
  </condition>
  <then>
    <assume_system_belief>
      <proposition predicate="quantity" value="200 g"/>
    </assume_system_belief>
  </then>
</if>
```

### If/Then/Else element for jumping to another goal depending on a proposition

```xml
<if>
  <condition>
    <proposition predicate="sourdough_status" value="existing"/>
  </condition>
  <then>
    <jumpto action="freshen_up_sourdough"/>
  </then>
  <else>
    <jumpto action="start_sourdough"/>
  </else>
</if>
```
