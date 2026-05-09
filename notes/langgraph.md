# LangGraph

A **cyclic directed graph** with state machine semantics where some edges are driven by LLM judgment instead of code conditions.

> Mental model: **you drew the map, LLM drives the car.**

## What makes it different from a traditional state machine

In a traditional state machine, all transitions are code:
```python
if alert.severity > 8 and alert.confirmed:
    transition("escalate")
```

In LangGraph, some transitions are LLM decisions:
```python
def should_escalate(state) -> str:
    response = llm.invoke("Is this evidence sufficient to escalate? " + state["evidence"])
    return "escalate" if response == "yes" else "investigate_more"
```

The graph structure (nodes, edges, possible paths) is still defined by you upfront. The LLM only decides *which edge to take* at LLM-driven nodes.

## Key capabilities

- **Cycles** — loop back if evidence is insufficient, retry with new info. This is the core differentiator vs DAGs.
- **Parallel branches** — fan out to multiple agents, collect results
- **Conditional fan-out** — branch based on intermediate findings
- **Persistence** — state is checkpointed; supports long-running workflows and human-in-the-loop
- **Streaming** — observe intermediate states as they happen

## When to use

Use LangGraph when:
- Workflow states are **known upfront** but some **transitions require language understanding**
- You need **auditable, inspectable** agent behavior (you can trace every state transition)
- The process may need to **loop** (retry, gather more evidence, refine)
- You need **human-in-the-loop** at defined checkpoints

Do NOT use when all transitions can be expressed as `if/else` — a traditional state machine is faster, cheaper, and more predictable. See [[llm-vs-code-driven]].

## When NOT to use

- If transition conditions are pure code → traditional state machine
- If you don't know the states upfront → [[openai-agents-sdk]] (fully emergent)
- If roles map cleanly to job titles → [[crewai]]

## Practical fit: security operations

LangGraph earns its place when judgment is genuinely required at transition points:
- "Is this log evidence suspicious **enough** to escalate?" — not a threshold, it's judgment
- "Has sufficient reconnaissance been done to proceed?" — not a rule, it's interpretation
- "Does this response indicate the agent is stuck?" — not a pattern match, it's reasoning

For deterministic steps (scan → parse → store), use Python — not LangGraph. See [[llm-vs-code-driven]].

## Related
- [[graph-dag-state-machine]] — conceptual foundations
- [[llm-vs-code-driven]] — the decision rule for when LangGraph earns its place
- [[openai-agents-sdk]] — the fully emergent alternative (no predefined graph)
- [[agentic-frameworks-comparison]] — side-by-side comparison
