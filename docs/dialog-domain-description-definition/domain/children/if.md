# If Then Else
## Definition
```xml
<if>
    <proposition .../>
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
- [<proposition\>](/dialog-domain-description-definition/domain/children/proposition)
- [<has\_shared\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<has\_private\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<has\_shared\_or\_private\_value\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_shared\_commitment\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\>](/dialog-domain-description-definition/domain/children/conditions)
- [<is\_private\_belief\_or\_shared\_commitment\>](/dialog-domain-description-definition/domain/children/conditions)
- [<then\>/<else\>](/dialog-domain-description-definition/domain/children/if)
    - [<assume\_issue\>](/dialog-domain-description-definition/domain/children/assume\_issue)
    - [<assume\_shared\>](/dialog-domain-description-definition/domain/children/assume\_shared)
    - [<assume\_system\_belief\>](/dialog-domain-description-definition/domain/children/assume\_system\_belief)
    - [<bind\>](/dialog-domain-description-definition/domain/children/bind)
    - [<findout\>](/dialog-domain-description-definition/domain/children/findout)
    - [<forget\>](/dialog-domain-description-definition/domain/children/forget)
    - [<forget\_all\>](/dialog-domain-description-definition/domain/children/forget\_all)
    - [<get\_done\>](/dialog-domain-description-definition/domain/children/get\_done)
    - [<if\>](/dialog-domain-description-definition/domain/children/if)
    - [<inform\>](/dialog-domain-description-definition/domain/children/inform)
    - [<invoke\_service\_action\>](/dialog-domain-description-definition/domain/children/invoke\_service\_action)
    - [<invoke\_service\_query\>](/dialog-domain-description-definition/domain/children/invoke\_service\_query)
    - [<jumpto\>](/dialog-domain-description-definition/domain/children/jumpto)
    - [<log\>](/dialog-domain-description-definition/domain/children/log)
    - [<raise\>](/dialog-domain-description-definition/domain/children/raise)
    - [<signal\_action\_completion/>\>](/dialog-domain-description-definition/domain/children/signal\_action\_completion)
    - [<signal\_action\_failure/>\>](/dialog-domain-description-definition/domain/children/signal\_action\_failure)

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

### If/Then element for assuming the answer "200 g" if the selected ingredient is water (either in commitments or in beliefs)

```xml
<if>
  <proposition predicate="selected_ingredient" value="water_ingredient"/>
  <then>
    <assume_system_belief>
      <proposition predicate="quantity" value="200 g"/>
    </assume_system_belief>
  </then>
</if>
```
