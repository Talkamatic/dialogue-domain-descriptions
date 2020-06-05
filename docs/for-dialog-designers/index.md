# Introduction

The task of the dialog designer is to define and design the dialog domain and the flow of the conversations in that domain, which will result in building a domain-specific dialog system.

Thanks to the principle of separation of concerns that underpins TDM, where knowledge about the domain (e.g., a phone book domain or a navigation domain) is separated from general knowledge about dialog, dialog designers can focus on defining domain-specific knowledge, such as information about concepts.

Designers can also focus on what words should be used to talk about these concepts, although specific languages are contained in grammars that are themselves separated from both domain and dialog knowledge in order to simplify expansion to even more languages.

General dialog capabilities such as:

- ensuring that users can say anything at anytime
- the handling of questions and answers
- providing feedback
- grounding
- topic switching
- incremental search

are all built into TDM and do not need to be provided by dialog designers. This makes it easier to build dialog systems since general dialog strategies need not be reinvented each time a new system is built. It allows the dialog designer to focus on domain-specific design.

## Dialog Domain Descriptions

In TDM a domain-specific application is implemented in the form of a Dialog Domain Description (DDD). A DDD is a declarative description of a particular dialog domain.

Firstly, it contains an [ontology](tutorial.md#step-3-ontology) specifying all the things ([actions](../formalism.md#actions), [predicates](../formalism.md#predicates) and [individuals](../formalism.md#individuals)) that we want to be able to talk about.

Secondly, a domain contains [dialog plans](tutorial.md#step-5-plan) representing the desired flow of the dialog.

Thirdly, a [grammar](tutorial.md#step-4-grammar) defines the words and expressions that the user and system can use in talking about the domain.

Lastly, through a [service interface](tutorial.md#step-6-service-interface) we can connect the information in the dialog to the real world and vice versa.
