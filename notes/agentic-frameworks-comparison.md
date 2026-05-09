# Agentic AI Frameworks — Map of Content

#ai #agents #architecture #frameworks

## The Spectrum

```
← More deterministic                          More emergent →

Python pipeline → Traditional SM → LangGraph → CrewAI → OpenAI Agents SDK
```

**Core decision rule** → [[llm-vs-code-driven]]

## Frameworks

| Framework | Mental Model | Use When |
|---|---|---|
| Python pipeline / DAG | Fixed order, no LLM | No LLM decisions in flow |
| Traditional state machine | Code drives transitions | Transition conditions are codeable |
| [[langgraph]] | You drew the map, LLM drives | Known states, some transitions need judgment |
| [[crewai]] | Team of specialists | Workflow maps to human roles |
| [[openai-agents-sdk]] | LLM draws and drives | Next step unknown upfront |

## Concepts

- [[graph-dag-state-machine]] — foundational definitions; DAG vs state machine vs graph
- [[llm-vs-code-driven]] — the one decision rule that determines where you sit on the spectrum

## Use Case Fit

| Use Case | Best Fit |
|---|---|
| Fixed probe pipeline | Python / DAG |
| SOC alert triage (known escalation rules) | Traditional state machine |
| SOC alert triage (ambiguous evidence) | [[langgraph]] |
| Patent research / digging | [[crewai]] |
| Coding assistant | [[openai-agents-sdk]] |
| Open-ended security reconnaissance | [[openai-agents-sdk]] |
| Document processing pipeline | [[langgraph]] or DAG |

## Related Projects
- `projects/gb10` — GB10 serves the model that powers these agents → [[GB10-MOC]]
