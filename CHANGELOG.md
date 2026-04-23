# Changelog

All notable changes to the Lansweeper PO Skills system are documented here.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
Versioning follows [Semantic Versioning](https://semver.org/).

---

## [1.1.0] — 2026-04-23

### Added

#### `jira-ticket-creator` — Outcome template (new)

New template for the **Outcome** issue type — the highest level in the ACME hierarchy, sitting above Milestones. Designed to be purely strategic and narrative: no technical language, no task lists, readable by anyone in the company.

**Structure:**
1. Outcome Overview
2. Strategic Context
3. Milestones in Scope
4. Success Criteria
5. Dependencies & Risks
6. AI Analysis Notes

**Deliberately excluded:** Metadata, Out of Scope, Feature Flags, UX, QA, Pendo Tracking, Story Points.

**Karpathy Loop criteria added:**
- Overview must be free of technical jargon
- Success Criteria must be business-level results, not delivery milestones
- Each Milestone in scope must visibly contribute to the Outcome goal
- AI Analysis Notes must include at least 1 open question for leadership

---

#### `jira-ticket-creator` — Milestone template (new)

New template for the **Milestone** issue type — product checkpoints that group Epics under a shared objective. Less technical than an Epic, more executable than an Outcome.

**Structure:**
1. Milestone Overview
2. Strategic Context
3. Epics in Scope
4. Success Criteria
5. Out of Scope
6. Dependencies & Risks
7. AI Analysis Notes
8. Metadata *(administrative reference, placed last)*

**Deliberately excluded:** Feature Flags, UX/Design, QA Strategy, Pendo Tracking, Story Points.

**Karpathy Loop criteria added:**
- Overview must read as product narrative, no technical jargon
- Success Criteria must be observable outcomes, not "Epic X is done"
- Each Epic in scope must contribute directly to the Milestone goal
- Out of Scope must have at least 1 item for stakeholder alignment
- AI Analysis Notes must include at least 1 open question for the PO

---

### Changed

#### `jira-ticket-creator`
- `description` frontmatter updated: now lists `Outcome / Milestone / Epic / Story / Task / Bug / Vulnerability`
- Step 1 issue type list updated to include Outcome and Milestone
- Template order now reflects the full ACME hierarchy: `Outcome → Milestone → Epic → Story → Task → Bug → Vulnerability`

#### `README.md`
- Skills Reference table updated: `jira-ticket-creator` now correctly lists all supported issue types

---

### First real-world application

The **Milestone template** was applied for the first time on **ACME-53461** — *Extending BI Datasets in order to unify entity model* — under Outcome ACME-51729 (*From IT reporting to business intelligence*).

---

## [1.0.0] — 2026-03-01

Initial public release of the Lansweeper PO Skills system.

**Skills included:**
- `orchestrator-po`
- `jira-researcher`
- `confluence-researcher`
- `slack-researcher`
- `figma-researcher`
- `jira-ticket-creator` (Epic / Story / Task / Bug / Vulnerability)
- `sprint-planner`
- `stakeholder-communicator`
- `test-plan-creator`
- `technical-writer`
- `chat-export`
