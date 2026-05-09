# OpenAI Agents SDK

No predefined states or graph — the LLM decides what to do next, which tools to call, and when to stop. Fully emergent at runtime.

> Mental model: **LLM draws the map AND drives the car.**

## How it works

You give the agent tools and a goal. It figures out the path:
```python
agent = Agent(
    name="security-researcher",
    instructions="You are a penetration testing assistant...",
    tools=[nmap_scan, search_cve, check_exploit_db]
)
result = Runner.run_sync(agent, "Assess the attack surface of 192.168.1.0/24")
```

The agent decides: call nmap → interpret results → search CVEs for found services → synthesize findings. You didn't define that sequence — it emerged.

## Key capabilities

- **Multi-agent handoffs** — one agent hands off to a specialist mid-task
- **Structured output** — enforce output schema via Pydantic models
- **Sessions & memory** — maintain context across turns
- **Human-in-the-loop** — pause and request approval before sensitive actions
- **Tracing** — full observability of tool calls and decisions
- **Guardrails** — input/output validation, safety checks

## Sweet spot

Use when:
- The next step **genuinely depends on what you discover** — can't be planned upfront
- Workflow paths are **unknown or highly variable**
- You need **open-ended exploration** (research, investigation, debugging)

Examples: coding assistants, open-ended research, customer support with backend access, security reconnaissance.

## Weakness

- **Harder to audit** — emergent paths are less predictable than explicit graphs
- **Silent false negatives** — LLM may skip steps, stop early, or hallucinate results
- **Non-deterministic** — same input may produce different paths
- **Cost** — more LLM calls than a structured pipeline

For security tools requiring **guaranteed coverage**, Python drives the flow — LLM only handles judgment. See [[llm-vs-code-driven]].

## vs LangGraph

| | OpenAI Agents SDK | LangGraph |
|---|---|---|
| States defined upfront | No — emergent | Yes — explicit graph |
| Who plans the path | LLM | You |
| Auditability | Lower | Higher |
| Flexibility | Maximum | Constrained to your graph |
| Best for | Unknown paths | Known states, some LLM judgment |

## Related
- [[langgraph]] — when you need an explicit graph with LLM at decision points
- [[llm-vs-code-driven]] — the fundamental tradeoff
- [[agentic-frameworks-comparison]] — side-by-side overview
