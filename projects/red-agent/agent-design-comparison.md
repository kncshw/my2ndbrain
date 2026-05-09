# Agent Design: oh-soc-agent vs bis-red-agent

> Design philosophy behind [[red-agent-MOC]] and [[SOC-agent-MOC]]. The overarching principle is captured in [[llm-vs-code-driven]].

*A conversation-driven analysis. Questions are the user's own — preserved because they show the reasoning process.*

---

## LLM Steps

**Q: How many LLM steps does bis-red-agent do?**

Two fixed steps per probed port:

| Step | When | Purpose |
|------|------|---------|
| 1. `identify` | always | app name, version, has_auth, auth_type, confidence |
| 2. `escalate` | skipped if has_auth=True + no SSL-VPN markers | escalation decision + note |

Max: 2 calls per port. Min: 1.

**Q: How many LLM steps does oh-soc-agent do?**

Iterative tool-calling loop, per alert:

| Turn | What happens |
|------|-------------|
| 1 | LLM reads alert, decides which tools to call |
| 2–7 | LLM gets tool results, decides next action |
| 8 | Final response or max_turns hit |

Max: 8 calls per alert. Min: 1. Average in practice: 3–5.

Both use **Gemma4-26B** on vLLM.

---

## Tool Calling

**Q: So for bis-red-agent, it is only reasoning tasks for LLM, no tool call yet?**

Correct. Gemma4 in bis-red-agent does pure reasoning only — it reads pre-fetched content and returns structured JSON. No tool calls at all.

All actual work (curl, gobuster, openssl, hydra) is done by Python calling the Kali sandbox directly. The LLM never touches a tool — it gets results handed to it as text.

```
Python → Kali sandbox → raw output
Python → formats output → LLM prompt
LLM    → JSON response (identify / escalate)
Python → acts on JSON
```

**Q: How does oh-soc-agent force LLM to do tool calls?**

It doesn't force — the LLM decides voluntarily via the Anthropic tool use API. The engine passes tool definitions as JSON schema in every request. When the model wants a tool it returns a `tool_use` content block instead of text. The engine detects this and executes the tool, appending results as a user message. Loop continues until no more tool calls.

**Q: So I can ask bis-red-agent to use tools as well?**

Yes. The `LLMClient` already supports tools — `tools=[]` is currently passed empty. The Kali sandbox has everything (nmap, gobuster, hydra, curl, openssl). Adding tool schemas and a loop would work technically. But there is a tradeoff (see below).

---

## The Core Design Insight

**Q: What we did in bis-red-agent is to make Discovery into Reasoning with prepared data?**

Exactly. That's the core design principle:

```
Discovery (Python)          Reasoning (Gemma4)
──────────────────          ──────────────────
curl root page         →    "what app is this?"
curl fingerprint paths →    "does it have auth?"
gobuster               →    "should we escalate?"
openssl cert           →
hydra creds check      →
```

Python does all the exploration — it knows exactly what to fetch, in what order, with what flags. Gemma4 gets a clean, complete dossier and just interprets it.

This is also why temperature=0 works well here — the LLM's job is deterministic classification, not creative exploration.

---

## Why Not Let Gemma4 Drive Discovery?

**Q: Then why is Gemma4 doing well with oh-soc-agent?**

The key difference is the search space:

**oh-soc-agent discovery:**
- Data is already structured (FortiSOAR alert fields, FAZ log fields)
- Finite, labeled fields: `src_ip`, `severity`, `event_type`, `count`
- The LLM reads what's there — no choices about what to look for
- "Discovery" = reading a report someone already wrote

**bis-red-agent discovery (if LLM-driven):**
- Data is unstructured (raw HTTP responses)
- Infinite search space: which paths? which headers? which response patterns?
- The LLM has to decide what NOT to look at — missing `SVPNCOOKIE` is a silent failure
- "Discovery" = investigating an unknown system with no map

| | oh-soc-agent | bis-red-agent |
|---|---|---|
| Task | Read a patient's chart and diagnose | Examine an unknown patient with no records |
| Data | Structured, pre-labeled | Raw, unstructured |
| Miss penalty | Low — fields are explicit | High — silent false negative |
| LLM role | Interpreter | Explorer + Interpreter |

FortiSOAR logs are curated signals — a human (or scanner) already decided these fields matter. A web server is a blank wall — you have to know to look for `SVPNCOOKIE`, check `/remote/login` body, run gobuster with the right wordlist. That's why Python does discovery for bis-red-agent.

**Q: But Gemma4 in oh-soc-agent also needs to do discovery — it fetches a time-window of logs and analyzes then makes a decision whether to escalate. Why is it easier than exploring a website?**

Same answer as above but from a different angle: FortiSOAR gives the LLM a structured incident report. The "discovery" is just a query against a database with known schema. A website is an unknown system — the LLM would have to decide which URLs to probe, which headers to inspect, which response patterns mean "authenticated." Those are judgment calls with silent failure modes.

---

## RAG as a Path Forward

**Q: If I have a RAG for those applications' signatures and common features, would it become easier for Gemma4 to do discovery for bis-red-agent?**

Yes, significantly. RAG would turn open-ended exploration into structured lookup:

**Without RAG (current):**
- Gemma4 relies on training knowledge about what each app looks like
- May hallucinate or miss app-specific signals
- Python compensates by hardcoding `SVPNCOOKIE`, `_FINGERPRINT_PATHS`, etc.

**With RAG:**
```
Gemma4: "I see port 9537 with metrics"
RAG:    → retrieve CRI-O signature doc
        → "CRI-O metrics on 9537: look for container_runtime_crio_ prefix"
Gemma4: confirmed → CRI-O, high confidence
```

Two problems remain even with RAG:

1. **Tool selection is still open-ended** — RAG tells Gemma4 what signatures to look for, but Python is better at guaranteeing systematic coverage (always run gobuster, always check these 15 paths).

2. **RAG quality determines accuracy** — if the signature doc is incomplete, you get the same silent failures.

**The pragmatic hybrid:**
- Keep Python for systematic discovery (guaranteed coverage)
- Add RAG to improve LLM reasoning accuracy (better identification)
- Gemma4 still does reasoning, not exploration

RAG makes the reasoning step smarter, not the discovery step unnecessary.

---

## Summary

| Dimension | oh-soc-agent | bis-red-agent |
|-----------|-------------|---------------|
| LLM role | Explorer + Interpreter | Interpreter only |
| Tool calls | Yes — LLM driven | No — Python driven |
| LLM calls per task | 1–8 (iterative) | 1–2 (fixed pipeline) |
| Data at LLM time | Fetched on demand | Pre-fetched by Python |
| Predictability | Lower | Higher |
| Coverage guarantee | LLM judgment | Python enforced |
| Miss failure mode | Recoverable (retry tool) | Silent (wrong answer) |
| Model | Gemma4-26B | Gemma4-26B |
| Temperature | 0.2 | 0.0 |
| Design principle | LLM drives the process | Python drives, LLM synthesizes |

The overarching principle: **use LLM for reasoning, use code for discovery. Put non-determinism where it's cheap (structured retrieval) and eliminate it where it's expensive (security assessment accuracy).**
