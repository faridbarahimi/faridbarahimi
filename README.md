<div align="center">

<img src="./assets/aicp-hero.svg" alt="AICP — AI Collaboration & Intelligence Platform" width="100%"/>

# Farid Barahimi

### Building the control plane for AI workers.

**AICP · AI Collaboration & Intelligence Platform**  
*Human intent → governed work → coordinated AI workers → evidence → verified outcome.*

[![AICP](https://img.shields.io/badge/AICP-AI%20Worker%20Control%20Plane-111827?style=for-the-badge)](https://github.com/faridbarahimi/AICP-Core-Platform)
[![Architecture](https://img.shields.io/badge/Architecture-Governed%20Execution-172554?style=for-the-badge)](https://github.com/faridbarahimi/AICP-Core-Platform)
[![Focus](https://img.shields.io/badge/Focus-AI%20Systems%20Engineering-0f172a?style=for-the-badge)](https://github.com/faridbarahimi)

</div>

---

## ◈ AICP — The Idea

AICP is being designed as a **work orchestration and control plane for AI workers**.

It is not simply an LLM wrapper or a prompt router.

The goal is a governed execution layer where human intent becomes durable, verifiable work across heterogeneous AI workers, models, tools, machines and external services.

<div align="center"><img src="./assets/aicp-architecture.svg" alt="AICP architecture" width="100%"/></div>
### The operating principle

> **AICP does not merely answer. It governs work.**

A worker may stop. A provider may fail. A model may become unavailable. A machine may disconnect.

The task should remain a durable object that can be inspected, resumed, rerouted, verified and — when authorized — completed.

---

## ◈ Cost-Aware Execution

<div align="center"><img src="./assets/aicp-routing.svg" alt="AICP cost-aware routing" width="100%"/></div>

AICP uses **capability-aware and cost-aware routing** rather than a single default model.

The objective is to use **sufficient capability with controlled risk and cost**.

**Routing concept:** Free / Low Cost → Specialist / KAT → Claude Code or another specialist when escalation is genuinely required.

---

## ◈ Worker Continuity

<div align="center"><img src="./assets/aicp-worker-continuity.svg" alt="AICP worker continuity" width="100%"/></div>
### A fundamental invariant

**<code>WORKER STOPPED ≠ TASK STOPPED</code>**

AICP separates task state from execution resources, artifacts and evidence.

That enables:

- resumable execution
- worker/provider replacement
- checkpoint-based continuation
- isolated task transactions
- independent verification
- controlled publication
- recovery after interruption

---

## ◈ Evidence Before Trust

<div align="center"><img src="./assets/aicp-evidence.svg" alt="AICP evidence and verification" width="100%"/></div>

AICP distinguishes:

**OBSERVED → EVIDENCE → VERIFIED → AUTHORIZED → IMPLEMENTED**

And preserves:

**ACCEPTED ≠ AUTHORIZED ≠ IMPLEMENTED**

The engineering goal is simple: important claims should be traceable to evidence, and important outcomes should be independently verifiable.
---

## ◈ Architecture Principles

| Principle | Meaning |
|---|---|
| **Human Authority** | Humans retain final authority over consequential decisions. |
| **Durable Tasks** | Work survives worker/provider interruption. |
| **Isolation** | Tasks execute within explicit boundaries and controlled workspaces. |
| **Evidence** | Important claims and outcomes have inspectable proof. |
| **Verification** | Completion is not assumed because a worker reports success. |
| **Cost Control** | Routing considers capability, risk and economic fit. |
| **Provider Agnosticism** | Workers and model providers are replaceable resources. |
| **No Partial Publication** | Incomplete or unverified work is not silently promoted. |
| **Governed Machine Access** | Machines and tools are accessed through controlled interfaces. |
| **Knowledge Continuity** | Project knowledge remains durable, queryable and provenance-aware. |

---

## ◈ Current Engineering Areas

- AI Worker Orchestration & Control Plane
- Governed Execution & Human Authorization
- Task Transactions & Isolated Worktrees
- Resilience, Recovery & Worker Continuity
- Provider Capability Discovery & Real Inference Verification
- Evidence & Execution-Outcome Records
- Context Budget & Retrieval Management
- Controlled Machine Access
- AI/Economic Fit & Automation Compliance Risk
- Knowledge Continuity & Architecture Governance
- Multi-Agent Cost Control & Escalation Routing
---

## ◈ Project Ecosystem

### AICP-Core-Platform

The engineering repository for the AICP control-plane implementation, architecture decisions, tests and governed execution infrastructure.

**→ https://github.com/faridbarahimi/AICP-Core-Platform**

### Karen

The broader human-like AI worker vision that can operate across web, desktop, ChatGPT, Claude, Gemini, Grok and other capability providers.

**AICP is the control plane. Karen is the worker-oriented experience built around it.**

---

## ◈ Engineering Loop

**Human Intent** → **Task Definition** → **Governance / Policy** → **Capability Routing** → **Isolated Execution** → **Checkpoint + Evidence** → **Independent Verification** → **Authorization** → **Publication**

---

## ◈ Build Philosophy

**Small task packets.** Break large work into bounded transactions that can be executed, tested, verified and resumed independently.

**Cheap first.** Use free or low-cost capability when it is sufficient.

**Specialist escalation.** Escalate difficult work only when required.

**No silent state changes.** Important changes remain explicit, inspectable and attributable.

**Proof over confidence.** A successful response is not the same thing as a verified outcome.

---

<div align="center">

### Building infrastructure for AI that can actually do work.

**AICP — Governed Work. Coordinated Workers. Verifiable Outcomes.**

</div>