# LLM-Driven vs Code-Driven Control

The most important design decision in any agentic system.

> **Python drives discovery (guaranteed coverage), LLM handles judgment (ambiguous interpretation).**

## The one decision rule

> **Can you write the transition condition as code?**
> - **Yes** → traditional state machine or DAG. Faster, deterministic, no LLM cost.
> - **No, requires reading complex information** → [[langgraph]] (known states) or [[openai-agents-sdk]] (unknown states).

## Why this matters for security tools

LLM-driven discovery risks **silent false negatives**:
- LLM can skip steps without telling you
- LLM can hallucinate results ("port 22 is closed" when it wasn't checked)
- LLM can stop early when it feels it has enough
- None of these failures are visible unless you audit every call

Python cannot do any of these. `for host in hosts: scan(host)` always scans every host.

**Correct split for deterministic, auditable security tools:**
- Python drives the flow: enumerate → scan → parse → store
- LLM handles judgment: "is this finding significant?", "what should I try next?", "is this evidence sufficient to escalate?"

## The spectrum

```
← More deterministic                          More emergent →

Python pipeline → Traditional SM → LangGraph → CrewAI → OpenAI Agents SDK
(DAG/Airflow)     (code transitions) (LLM at   (role-   (LLM plans
                                      edges)    based)    everything)
```

Sliding right = more LLM control, more flexibility, less predictability, higher cost.

## When to move right on the spectrum

Move toward LLM control when:
1. Transition conditions **cannot be expressed as code** — they require language understanding
2. The **workflow path is unknown upfront** — it depends on what you discover
3. **Coverage guarantees are not required** — missing a step is acceptable

Stay left when:
1. You can write `if/else` for every transition
2. Missing a step would be a bug (security scan, compliance check)
3. Auditability is required — every decision must be explainable

## Examples

| Condition | Python? | LLM? |
|---|---|---|
| `if alert.severity > 8` | Yes | No |
| "Is this log suspicious enough to escalate?" | No | Yes |
| `for host in subnet: scan(host)` | Yes | No |
| "Has sufficient reconnaissance been done?" | No | Yes |
| `if response.status_code == 200` | Yes | No |
| "Does this contract clause represent unusual risk?" | No | Yes |

## Related
- [[langgraph]] — LLM at transition points, you define the graph
- [[openai-agents-sdk]] — LLM plans and drives everything
- [[graph-dag-state-machine]] — conceptual foundations
- [[agentic-frameworks-comparison]] — framework overview
