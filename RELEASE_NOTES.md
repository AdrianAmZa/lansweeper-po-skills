## 🚀 v1.1.0 — Outcome & Milestone Templates

Extends the `jira-ticket-creator` skill with two new issue type templates covering the strategic layers of the ACME hierarchy.

### What's New

**`jira-ticket-creator` — Outcome template**
- Pure product narrative — no technical language, no task lists
- Structure: Overview → Strategic Context → Milestones in Scope → Success Criteria → Dependencies & Risks → AI Analysis Notes
- No Metadata, no Out of Scope by design — lives at the vision level

**`jira-ticket-creator` — Milestone template**
- Product checkpoint grouping Epics under a shared goal
- Structure: Overview → Strategic Context → Epics in Scope → Success Criteria → Out of Scope → Dependencies & Risks → AI Analysis Notes → Metadata
- Excludes Feature Flags, UX, QA, Pendo, and Story Points

### Full hierarchy now supported

```
Outcome → Milestone → Epic → Story → Task → Bug → Vulnerability
```

### How to Install

**Full bundle**: Download `lansweeper-po-skills-v1.1.0.zip` and extract.

**Individual skills**: Download specific `.skill` files and install in Claude.

**Update only `jira-ticket-creator`**: Download `jira-ticket-creator.skill` and replace your existing installation.

---

## 🚀 v1.0.0 — PO Skills Bundle (WoW 2026)

First official release of the Lansweeper Product Owner skills system for Claude.

### Included Skills (11)

**Orchestration**
- `orchestrator-po` — Routes requests to the right PO skill

**Research**
- `jira-researcher` — Progressive retrieval from Jira
- `confluence-researcher` — Navigate Confluence hierarchies
- `slack-researcher` — Search Slack channels and threads
- `figma-researcher` — Extract design context via Figma MCP

**Execution**
- `jira-ticket-creator` — Structured issue creation with full templates
- `sprint-planner` — Sprint planning, velocity, and backlog grooming
- `stakeholder-communicator` — Status reports and executive summaries

**Output**
- `test-plan-creator` — Jira Test Plans with Lansweeper template
- `technical-writer` — Technical documentation and READMEs

**Utility**
- `chat-export` — Export conversations for portability

### How to Install

**Full bundle**: Download `lansweeper-po-skills-v1.0.0.zip` and extract.

**Individual skills**: Download specific `.skill` files and install in Claude.

### Key Features
- Karpathy self-evaluation loop (generate → evaluate → refine)
- Progressive layered retrieval
- MCP integrations (Atlassian, Slack, Figma)
- Structured templates with FAC/TAC, DoR/DoD, BLUF
