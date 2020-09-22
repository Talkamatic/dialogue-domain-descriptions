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
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
    - [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get_done)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
    - [<assume\_system\_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
- [<else\>](/dialog-domain-description-definition/domain/children/proposition)
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
    - [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get_done)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
    - [<assume\_system/_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)

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
