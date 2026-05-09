# CrewAI

A role-based multi-agent framework. Define agents as job roles, assign tasks, coordinate as a crew.

> Mental model: **a team of specialists with defined responsibilities.**

## How it works

You define agents by role and assign tasks:
```python
researcher = Agent(role="Researcher", goal="Find relevant patents", tools=[search_tool])
analyst    = Agent(role="Analyst",    goal="Identify prior art conflicts")
writer     = Agent(role="Writer",     goal="Produce a summary report")

crew = Crew(agents=[researcher, analyst, writer], tasks=[...], process=Process.sequential)
crew.kickoff()
```

CrewAI coordinates handoffs between agents, manages context passing, and handles task dependencies.

## Coordination modes

- **Sequential** — researcher → analyst → writer (default, like an assembly line)
- **Hierarchical** — a manager agent delegates to specialists and synthesizes results
- **Parallel** — multiple agents work simultaneously on independent tasks

## Sweet spot

Tasks that map naturally to human team structure:
- Patent research: search → analyze → report
- Competitive intelligence: gather → compare → summarize
- Content production: research → draft → edit → review

## Weakness

Abstraction feels forced when the problem doesn't decompose into human job titles. If your "agents" are really just pipeline steps, a DAG or LangGraph is cleaner. CrewAI shines when role specialization and inter-agent collaboration are genuinely meaningful.

## vs LangGraph

| | CrewAI | LangGraph |
|---|---|---|
| Structure | Role-based agents | Explicit graph (nodes + edges) |
| Coordination | Crew manager / sequential | You define the graph |
| Best for | Team-shaped workflows | Process-shaped workflows |
| Auditability | Medium | High (every state transition visible) |
| Cycles | Limited | Core feature |

## Related
- [[agentic-frameworks-comparison]] — side-by-side overview
- [[langgraph]] — when you need explicit graph control vs role abstraction
- [[openai-agents-sdk]] — when neither graph nor roles fit (fully emergent)
- [[llm-vs-code-driven]] — deciding how much control to give the LLM
