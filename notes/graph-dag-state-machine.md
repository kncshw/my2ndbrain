# Graph, DAG, and State Machine

Foundational concepts behind all workflow and agent orchestration systems.

## Hierarchy

```
All Graphs
├── Cyclic Directed Graphs
│   ├── State Machines (code-driven transitions)
│   └── LangGraph (LLM-driven transitions)  → [[langgraph]]
└── DAGs (Directed Acyclic Graphs)
    ├── Used as pipeline orchestrators (Airflow, Prefect)
    └── Pure dependency graphs (Makefile, git history)
```

DAG and state machine are **siblings** under the graph family — not parent and child. A DAG *can* be used as a state machine (Airflow does this), but it is not inherently one.

## Graph

A mathematical structure of **nodes** connected by **edges**.

- Edges can be directed (one-way) or undirected (two-way)
- No restrictions on cycles or structure
- Most general concept — everything below is a specialization

```
A → B → C
↑       │
└───────┘   (cycle allowed)
```

## DAG (Directed Acyclic Graph)

A directed graph with **no cycles** — every node executes at most once.

- Guarantees a topological ordering (A always before B)
- Models **dependencies and ordering**, not behavior over time
- What it is NOT: a state machine — DAG adds no concept of "active state" or event-triggered transitions

```
A → B → D
↓       ↑
C ──────┘   (no cycles, strict ordering)
```

**Real-world use:** Airflow, Prefect, Makefile, git commit history, ML training pipelines.

## State Machine

A graph where **nodes = states** and **edges = transitions** triggered by events or conditions.

- Only one node is active at a time
- Adds **behavioral semantics** — models how a system behaves over time
- Can be cyclic (loop back) or acyclic

```
[idle] --event--> [processing] --done--> [complete]
                      │
                   --error--> [failed]
```

**Real-world use:** traffic lights, order workflows, network protocol handling, alert triage pipelines.

## Comparison

| | Graph | DAG | State Machine |
|---|---|---|---|
| Cycles allowed | Yes | No | Optional |
| Direction | Optional | Always | Always |
| Active node concept | No | No | Yes (one at a time) |
| Transition triggers | None | None | Events / conditions |
| Models | Relationships | Dependencies | System behavior over time |

## Related
- [[langgraph]] — cyclic directed graph with LLM-driven state machine semantics
- [[llm-vs-code-driven]] — when to use LLM vs code for transition logic
- [[agentic-frameworks-comparison]] — framework overview
