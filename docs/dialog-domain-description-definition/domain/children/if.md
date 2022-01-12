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
- [<postplan\>](/dialog-domain-description-definition/domain/children/postplan)
- [<then\>](/dialog-domain-description-definition/domain/children/if)
- [<else\>](/dialog-domain-description-definition/domain/children/if)


## Children
- [<condition\>](/dialog-domain-description-definition/domain/children/if)
    - [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<has\_shared\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<has\_private\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<has\_shared\_or\_private\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_shared\_commitment\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\_or\_shared\_commitment\>](/dialog-domain-description-definition/domain/children/conditions)
- [<then\>/<else\>](/dialog-domain-description-definition/domain/children/if)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume_shared)
    - [<assume\_system\_belief\>](/dialog-domain-description-definition/domain/children/assume_system_belief)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget_all\>](/dialog-domain-description-definition/domain/children/forget_all)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get_done)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<inform\>](/dialog-domain-description-definition/domain/children/inform)
    - [<invoke_service_action\>](/dialog-domain-description-definition/domain/children/invoke_service_action)
    - [<invoke_service_query\>](/dialog-domain-description-definition/domain/children/invoke_service_query)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)
    - [<signal_action_completion/>\>](/dialog-domain-description-definition/domain/children/signal_action_completion)
    - [<signal_action_failure/>\>](/dialog-domain-description-definition/domain/children/signal_action_failure)

## Behaviour


## Examples
### If/Then/Else element for jumping to another goal if there is a proposition in commitments with a certain predicate

```xml
<if>
  <has_shared_value predicate="sourdough_status"/>
  <then>
    <jumpto action="freshen_up_sourdough"/>
  </then>
  <else>
    <jumpto action="start_sourdough"/>
  </else>
</if>
```

### If/Then element for assuming the answer "200 g" if the selected ingredient is water

```xml
<if>
  <is_shared_commitment predicate="selected_ingredient" value="water_ingredient"/>
  <then>
    <assume_system_belief>
      <proposition predicate="quantity" value="200 g"/>
    </assume_system_belief>
  </then>
</if>
```
