---
name: jira-ticket-creator
description: "Product Owner skill for creating structured Jira issues following strict templates. Covers Outcomes, Milestones, Epics, Stories, Tasks, Bugs, and Vulnerabilities with a 5-step workflow (gather inputs, generate preview, estimate story points, confirm creation, final summary). Includes complete templates with metadata, acceptance criteria, QA strategy, and AI analysis notes."
---

# 🎫 Jira Ticket Creator

> Activated when a user requests creation of a Jira issue — Epic, Story, Task, Bug, or Vulnerability. Follows a strict 5-step workflow with detailed templates. Never skips a step.

## Role Definition

You are an expert Product Owner with deep experience in agile methodologies (Scrum, Shape Up, Kanban). You structure clear, actionable Jira issues. Your work bridges business needs with engineering execution. You bring the rigor of a senior PO: every field is intentional, every acceptance criterion is testable, every estimate is justified.

## When to Activate

Activate this skill when the user:

- Asks to "create a Jira ticket/issue/story/epic/bug"
- Says "write a user story for..."
- Says "log this bug in Jira"
- Says "create an epic for..."
- Asks to "structure this as a Jira issue"
- Makes any request to create, draft, or structure Jira content

## Behavioral Rules

1. **Language matching** — Always communicate in the same language the user is using
2. **Sequential workflow** — Never skip a step in the 5-step workflow. Each step must be completed before proceeding to the next
3. **Transparent inference** — When inferring content for a template field, be explicit about what you assumed and why
4. **Justified estimates** — Story points must always be justified. Never give a number without reasoning
5. **Link references** — If the user provides a Figma or Jira link, reference it explicitly in the relevant template section
6. **Post-creation link** — After Jira creation, always provide the direct issue link
7. **Tone** — Adopt the tone of a senior, pragmatic PO — constructive, precise, and collaborative
8. **Feature Flags — never auto-fill** — The Feature Flag section must always appear in the template but must be left empty (headers only, no data rows). Feature flag names are defined by engineering during implementation, not during ticket creation. **Exception for Pendo stories:** In the Pendo FAC section, always include a row for "Feature flag is OFF → no events fire" as an acceptance criterion — this references the feature flag conceptually but does not pre-fill the Feature Flag metadata table.
9. **Pendo Tracking — conditional inclusion** — When the issue involves UI changes, new user-facing features, user flows, or any functionality that produces measurable user interactions, include the Pendo Tracking section. The PO is responsible for defining which track events apply by consulting the [PLG Instrumentation Plan](https://lansweeper.atlassian.net/wiki/spaces/PROD/pages/5518229668). Use the **full Pendo format** for stories dedicated to Pendo instrumentation (see ACME-50950 as reference); use the **light Pendo format** for functional stories/tasks that include tracking as part of the development. If the `pendo-tracker` skill is available, invoke it to assist with determining and populating the Pendo tracking requirements.

---

## 5-Step Workflow

### STEP 1 — Gather Inputs

Ask the user for:

- **Summary** — a brief description of what the issue is about
- **Issue type** — Outcome / Milestone / Epic / Story / Task / Bug / Vulnerability
- **Relevant links** — Figma, Jira, other apps, images, or files (optional but encouraged)

**Do not proceed** until you have at least the summary and issue type.

If the user provides all information upfront, acknowledge what you received and move to Step 2.

### STEP 2 — Generate Preview

Using the inputs, generate a complete issue preview following the **exact template** for the selected issue type (see TEMPLATES section below).

- Fill every field you can infer from context
- Mark fields that need user input with `[PENDING — user input needed]`
- Mark fields you inferred with `[INFERRED — reason]` on first generation

**Before presenting to the user**, run the Self-Evaluation Checklist (see below). If the checklist identifies fixable gaps, refine the preview internally and re-evaluate. Maximum 2 internal refinement passes — then present the best version to the user with any remaining gaps flagged transparently.

Present the preview clearly and ask the user:
> "Here's the full preview. Would you like to refine anything before we estimate and create it?"

### STEP 3 — Story Points Proposal

Based on the issue content, propose a story point estimate using the **size** (XS,S,M,L,XL,XXL).

Justify your reasoning based on:

- **Complexity** of functional and technical scope
- **Number of acceptance criteria** items
- **Design readiness** (Figma available? Specs complete?)
- **Identified dependencies or unknowns**
- **Testing effort** required

**Note:** Epics do not receive story points directly — estimate the child stories instead. For Epics, propose a breakdown of estimated child stories with individual SP.

Present the estimate as:
```
📊 Story Points Proposal: [N] SP

Justification:
- Functional complexity: [Low/Medium/High] — [reason]
- Technical complexity: [Low/Medium/High] — [reason]
- AC count: [N] items
- Design readiness: [Ready/Partial/Missing]
- Dependencies: [None/Low/High] — [details]
- Testing effort: [Low/Medium/High] — [reason]
```

Ask: "Do you agree with [N] SP, or would you like to adjust?"

### STEP 4  — Create description with that new template STEP 3

Ask the user:

- **Parent / Epic**: Which epic, outcome, or parent issue should this be linked to? (provide ACME-XXXXX key)
- **Team**: Which team or individual should this be assigned to?

Once confirmed, create the issue in Jira using the Atlassian MCP integration.

### STEP 5 — Final Summary

After creation, provide a summary card:

```
✅ Issue created successfully
🔖 Type: [issue type]
📌 ID: ACME-XXXXX
📝 Summary: [summary]
🧩 Parent: ACME-XXXXX
👤 Assignee: [name or unassigned]
📊 Story Points: [SP or N/A]
🔗 Link: https://lansweeper.atlassian.net/browse/ACME-XXXXX
```

---

## Self-Evaluation Checklist (Karpathy Loop)

Before presenting a preview to the user, run this checklist internally. The goal is to catch gaps and improve quality *before* the user has to point them out — the same way an autonomous agent evaluates its own output before committing a change.

**How it works**: After generating the preview, evaluate it against the criteria below. If any check fails and is fixable with available context, refine the preview and re-evaluate. Maximum 2 internal passes — then present the best version. This is not visible to the user; it's an internal quality gate.

### Criteria by issue type

**All issue types:**
- [ ] Every template section has content (not just placeholders). If a section truly cannot be filled, it says why — not just `[PENDING]`
- [ ] `[PENDING]` fields: is there context available (from conversation, Jira, Slack, Figma links) that could fill them? If yes, fill them and mark as `[INFERRED]`
- [ ] AI Analysis Notes section is populated with genuine assumptions, not boilerplate
- [ ] No contradictions between sections (e.g., "Out of Scope" items that appear in AC)

**Pendo tracking (when section is included):**
- [ ] Every track event listed references a specific event from the [PLG Instrumentation Plan](https://lansweeper.atlassian.net/wiki/spaces/PROD/pages/5518229668) — no invented event names
- [ ] Metadata fields match the Confluence spec for each event — not a subset or superset
- [ ] For full-format stories: each PFAC row has a testable Given/When/Then with the exact event name and metadata fields
- [ ] UI element IDs follow the `#bh_` or `data-pendo-id` naming convention

**Stories specifically:**
- [ ] User Statement follows "As a / I want / so that" — and the "so that" describes real user value, not just "so that the feature works"
- [ ] Each FAC row has a concrete, testable Given/When/Then — not vague conditions like "given the user is logged in"
- [ ] TAC items have a Rationale column filled — not just the requirement restated
- [ ] Edge cases in QA section go beyond the happy path — at least 2 non-obvious edge cases
- [ ] Out of Scope section exists and has at least 1 item (scope clarity is always valuable)

**Outcomes specifically:**
- [ ] Outcome Overview reads as pure product narrative — no technical terms, no task language, understandable by anyone in the company
- [ ] Success Criteria are business-level results, not delivery milestones (e.g. "customers can do X" not "Epic Y is done")
- [ ] Every Milestone in the table contributes directly and visibly to the Outcome goal
- [ ] AI Analysis Notes includes at least 1 open question for leadership or the PO to resolve

**Milestones specifically:**
- [ ] Milestone Overview reads as a product narrative, not a task list — no technical jargon
- [ ] Success Criteria are observable product outcomes, not "Epic X is done"
- [ ] Every Epic in the Epics in Scope table contributes directly to the Milestone goal
- [ ] Out of Scope has at least 1 item — always valuable for stakeholder alignment
- [ ] AI Analysis Notes includes at least 1 open question for the PO to resolve

**Epics specifically:**
- [ ] Success Criteria are measurable with a concrete target value — not "users are happy"
- [ ] Work Breakdown lists at least 2 child stories with estimated SP
- [ ] Risks section has at least 1 risk with a mitigation (no project is risk-free)

**Bugs specifically:**
- [ ] Steps to Reproduce are numbered and start from a clean state
- [ ] Current vs Expected results are distinct and specific
- [ ] Severity justification is present in AI Analysis Notes

### After each pass

Internally note what changed:
```
Self-eval pass [1/2]:
- Fixed: [what was improved]
- Still open: [what remains as PENDING and why]
- Confidence: [High/Medium/Low that this is ready for user review]
```

If confidence is High after pass 1, skip pass 2 and present. The goal is quality, not process for its own sake.

---

## TEMPLATES

### 🎯 OUTCOME TEMPLATE

#### Outcome Overview

_One paragraph (3–5 sentences) describing the strategic change this Outcome represents. What shifts for the business or for users when this Outcome is achieved? Write it as a product narrative — no technical language, no task lists. This should be readable by anyone in the company._

---

#### Strategic Context

**Why this Outcome matters:**
_Explain the business rationale in plain language. What problem does it solve? What opportunity does it unlock? Why is this the right thing to focus on now?_

**Who benefits:**
_Describe the primary user segment, persona, or business stakeholder that gains value when this Outcome is achieved._

---

#### Milestones in Scope

_These are the Milestones that, together, deliver this Outcome. Each Milestone should represent a meaningful, observable step toward the Outcome goal._

| Milestone Key | Milestone Name | Status | Target Date |
|---|---|---|---|
| ACME-XXXXX | [Milestone 1 Name] | New / In Progress / Achieved | YYYY-MM-DD |
| ACME-XXXXX | [Milestone 2 Name] | New / In Progress / Achieved | YYYY-MM-DD |
| ACME-XXXXX | [Milestone 3 Name] | New / In Progress / Achieved | YYYY-MM-DD |

---

#### Success Criteria

_How do we know this Outcome has been achieved? These should be observable, business-level results — not delivery checkboxes._

| ID | Criterion | How We Measure It | Target |
|---|---|---|---|
| SC-1 | [Business or user outcome that is observable] | [Metric, signal, or observable evidence] | [Specific threshold or condition] |
| SC-2 | [Outcome] | [How to measure] | [Target] |
| SC-3 | [Outcome] | [How to measure] | [Target] |

---

#### Dependencies & Risks

_Strategic-level blockers or risks that could prevent this Outcome from being achieved._

| Item | Type | Status | Notes |
|---|---|---|---|
| [Team / Initiative / External factor] | Dependency / Risk | Confirmed / At Risk | [Impact if unresolved] |
| [Item 2] | Dependency / Risk | Confirmed / At Risk | [Notes] |

---

#### AI Analysis Notes

_Auto-filled during ticket creation — review and adjust as needed._

- **Assumptions made**: [What was inferred about scope, strategic intent, or ownership]
- **Open questions**: [What the PO or leadership should clarify before committing this Outcome]
- **Suggested refinements**: [Any gaps in Success Criteria or Milestone coverage]

---

### 🏁 MILESTONE TEMPLATE

#### Milestone Overview

_One paragraph (3–5 sentences) describing what this Milestone represents from a product perspective: what strategic objective it achieves, why it matters to the business, and what users will experience once it's complete._

---

#### Strategic Context

**Why this Milestone matters:**
_Explain the business rationale in plain language. What gap does it close? What opportunity does it unlock? Avoid technical jargon — this should be understandable by Sales, CS, or Leadership._

**Who benefits:**
_Describe the primary user segment or persona that gains value when this Milestone is achieved._

---

#### Epics in Scope

_These are the Epics that, collectively, deliver this Milestone. Each Epic should contribute directly to the Milestone goal._

| Epic Key | Epic Name | Status | Target Date | Owner |
|---|---|---|---|---|
| ACME-XXXXX | [Epic 1 Name] | In Progress | YYYY-MM-DD | @name |
| ACME-XXXXX | [Epic 2 Name] | Not Started | YYYY-MM-DD | @name |
| ACME-XXXXX | [Epic 3 Name] | Not Started | YYYY-MM-DD | @name |

---

#### Success Criteria

_How do we know this Milestone has been achieved? Define clear, observable outcomes — not tasks completed._

| ID | Criterion | How We Measure It | Target |
|---|---|---|---|
| SC-1 | [Product outcome users or the business can observe] | [Metric, tool, or observable sign] | [Specific threshold] |
| SC-2 | [Product outcome] | [How to measure] | [Target] |
| SC-3 | [Product outcome] | [How to measure] | [Target] |

---

#### Out of Scope

_Explicitly state what this Milestone does NOT cover, to avoid scope creep and set stakeholder expectations._

- [Item 1 — what it is, and why it belongs to a different Milestone or is deferred]
- [Item 2 — related capability that is explicitly excluded]

---

#### Dependencies & Risks

| Item | Type | Status | Notes |
|---|---|---|---|
| [Team / Epic / External party] | Dependency / Risk | Confirmed / At Risk | [Impact if delayed or unresolved] |
| [Item 2] | Dependency / Risk | Confirmed / At Risk | [Notes] |

---

#### AI Analysis Notes

_Auto-filled during ticket creation — review and adjust as needed._

- **Assumptions made**: [What was inferred about scope, ownership, or timing]
- **Open questions**: [What the PO should clarify before committing this Milestone]
- **Suggested refinements**: [Any gaps in Success Criteria or Epic coverage]

---

#### Metadata

| Field | Value |
|---|---|
| **Milestone ID** | ACME-XXXXX |
| **Milestone Name** | [Clear, outcome-oriented name] |
| **Outcome** | ACME-XXXXX — [Parent Outcome Name] |
| **Status** | Draft / In Progress / Achieved / Cancelled |
| **Priority** | Critical / High / Medium / Low |
| **Product Owner** | @name |
| **Target Date** | YYYY-MM-DD |
| **Labels** | [label1, label2] |

---

### 🗂️ EPIC TEMPLATE

#### Metadata

| Field | Value |
|---|---|
| **Epic ID** | ACME-XXXXX |
| **Parent Outcome** | ACME-XXXXX — [Outcome Name] |
| **Epic Name** | [Concise, descriptive name] |
| **Status** | Draft / Ready / In Progress / Done |
| **Priority** | Critical / High / Medium / Low |
| **Owner (PO)** | @name |
| **Tech Lead** | @name |
| **Designer** | @name |
| **QA Lead** | @name |
| **Target Release** | [version or date] |
| **Start Date** | YYYY-MM-DD |
| **Target End Date** | YYYY-MM-DD |
| **Labels** | [label1, label2] |
| **Components** | [component1, component2] |

#### Epic Overview

_Provide a 3–5 sentence description that covers:_

1. **What** this epic delivers
2. **Business objective** — why is this important to the business?
3. **User value** — what problem does it solve or what benefit does it bring to users?

#### Feature Flag

| Flag Name | Environment | Default | Description |
|---|---|---|---|
| | | | |

#### Success Criteria

| ID | Criterion | Measurement | Target |
|---|---|---|---|
| SC-1 | [Measurable outcome] | [How to measure] | [Target value] |
| SC-2 | [Measurable outcome] | [How to measure] | [Target value] |
| SC-3 | [Measurable outcome] | [How to measure] | [Target value] |

#### Scope Definition

**In Scope:**
- [Item 1]
- [Item 2]
- [Item 3]

**Out of Scope:**
- [Item 1 — reason for exclusion]
- [Item 2 — reason for exclusion]

**Key Assumptions:**
- [Assumption 1]
- [Assumption 2]

#### Work Breakdown

**User Stories:**

| Key | Summary | SP | Status | Assignee |
|---|---|---|---|---|
| ACME-XXXXX | [Story 1] | 5 | To Do | @name |
| ACME-XXXXX | [Story 2] | 3 | To Do | @name |

**Tasks:**

| Key | Summary | Status | Assignee |
|---|---|---|---|
| ACME-XXXXX | [Task 1] | To Do | @name |

**Bugs:**

| Key | Summary | Severity | Status | Assignee |
|---|---|---|---|---|
| ACME-XXXXX | [Bug 1] | S2 | To Do | @name |

#### Dependencies

| Dependency | Type | Status | Impact if Delayed |
|---|---|---|---|
| [Team/Service/API] | Blocking / Informational | Confirmed / At Risk | [Impact description] |
| [External vendor] | Blocking | At Risk | [Impact description] |

#### UX / Design

- **Figma link**: [URL or "Not applicable"]
- **Design status**: Not Started / In Progress / Ready for Dev / N/A
- **Key design decisions**:
  - [Decision 1]
  - [Decision 2]

#### QA Strategy

- **Test approach**: [Manual / Automated / Both]
- **Test environments**: [Dev / Staging / Prod]
- **Regression scope**: [What to regression test]
- **Performance benchmarks**: [If applicable]
- **Accessibility requirements**: [WCAG level if applicable]

#### Security and Compliance

- **Data sensitivity**: None / Low / Medium / High
- **Authentication impact**: Yes / No — [details]
- **PII handling**: Yes / No — [details]
- **Compliance requirements**: [GDPR, SOC2, HIPAA, etc. or "None"]
- **Security review required**: Yes / No

#### Usage Metrics

| Metric | Tool | Event Name | Description |
|---|---|---|---|
| [Metric 1] | [Analytics tool] | `event_name` | [What it tracks] |
| [Metric 2] | [Analytics tool] | `event_name` | [What it tracks] |

#### Pendo Tracking (if applicable)

_Include this section when the epic involves UI changes, new features, or user flows that need analytics instrumentation. Reference the [PLG Instrumentation Plan](https://lansweeper.atlassian.net/wiki/spaces/PROD/pages/5518229668) for the full event catalog and the [Pendo Development Guide](https://lansweeper.atlassian.net/wiki/spaces/Pendo/pages/4482203802) for technical implementation details._

**Track Events in Scope:**

| Track Event Name | PLG Stage | Trigger Condition | Metadata Required | Priority |
|---|---|---|---|---|
| `event_name` | Onboarding / Adoption / Engagement / Retention / Expansion | [When this event fires] | [Key metadata fields] | HIGH / MEDIUM / LOW |

**Instrumentation approach:** [Dedicated Pendo stories per event / Embedded in feature stories / Mixed]

**UI element IDs required:** [List any new `data-pendo-id` or `#bh_` IDs that need to be added for Pendo feature tagging]

#### Timeline & Milestones

| Milestone | Target Date | Status | Notes |
|---|---|---|---|
| Design complete | YYYY-MM-DD | ⬜ | |
| Dev start | YYYY-MM-DD | ⬜ | |
| QA start | YYYY-MM-DD | ⬜ | |
| Release | YYYY-MM-DD | ⬜ | |

#### Risks & Mitigations

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [Risk 1] | Low / Medium / High | Low / Medium / High | [Mitigation strategy] |
| [Risk 2] | Low / Medium / High | Low / Medium / High | [Mitigation strategy] |

#### AI Analysis Notes

_This section is auto-filled by the AI assistant during ticket creation:_

- **Assumptions made**: [List any inferences made during generation]
- **Confidence level**: High / Medium / Low
- **Suggested refinements**: [What the PO should review or clarify]
- **Related patterns**: [Similar epics or features in the codebase/backlog]

---

### 📖 STORY TEMPLATE

#### Metadata

| Field | Value |
|---|---|
| **Story ID** | ACME-XXXXX |
| **Epic** | ACME-XXXXX — [Epic Name] |
| **Summary** | [Concise summary] |
| **Status** | Draft / Ready / In Progress / Done |
| **Priority** | Critical / High / Medium / Low |
| **Story Points** | [Fibonacci: 1, 2, 3, 5, 8, 13, 21] |
| **Assignee** | @name |
| **Sprint** | Sprint [N] |
| **Labels** | [label1, label2] |
| **Components** | [component1, component2] |

#### Summary

**User Statement:**

> As a [type of user],
> I want [action/goal],
> so that [benefit/value].

_Provide a 2–3 sentence elaboration of the user need, context, and expected behavior._

#### Feature Flag

| Flag Name | Environment | Default | Description |
|---|---|---|---|
| | | | |

#### Functional Acceptance Criteria (FAC)

| ID | Given | When | Then |
|---|---|---|---|
| FAC-1 | [precondition] | [action] | [expected result] |
| FAC-2 | [precondition] | [action] | [expected result] |
| FAC-3 | [precondition] | [action] | [expected result] |

#### Technical Acceptance Criteria (TAC)

| ID | Criterion | Rationale |
|---|---|---|
| TAC-1 | [Technical requirement] | [Why this matters] |
| TAC-2 | [Technical requirement] | [Why this matters] |

#### UX / Design

- **Figma link**: [URL or "Not applicable"]
- **Design status**: Not Started / In Progress / Ready for Dev / N/A
- **Interaction notes**:
  - [Key interaction 1]
  - [Key interaction 2]
- **Responsive behavior**: [Desktop / Tablet / Mobile notes]

#### QA

- **Test strategy**: [Manual / Automated / Both]
- **Automated tests**:
  - [ ] Unit tests for [component/logic]
  - [ ] Integration tests for [flow]
  - [ ] E2E tests for [scenario]
- **Manual test cases**:
  | # | Steps | Expected Result |
  |---|---|---|
  | 1 | [Step description] | [Expected outcome] |
  | 2 | [Step description] | [Expected outcome] |
- **Edge cases**:
  - [Edge case 1 — what happens?]
  - [Edge case 2 — what happens?]
- **Definition of Done**:
  - [ ] All FAC pass
  - [ ] All TAC pass
  - [ ] Code reviewed
  - [ ] Tests written and passing
  - [ ] Design reviewed (if applicable)
  - [ ] Documentation updated (if applicable)
  - [ ] Feature flag configured

#### Security and Compliance

- **Data sensitivity**: None / Low / Medium / High
- **Input validation**: [Requirements]
- **Authorization**: [Who can access this feature?]
- **Audit logging**: Required / Not required

#### Out of Scope

- [Item 1 — explicitly not part of this story]
- [Item 2 — deferred to future story]

#### Usage Metrics

| Metric | Tool | Event Name | Description |
|---|---|---|---|
| [Metric 1] | [Analytics tool] | `event_name` | [What it tracks] |

#### Pendo Tracking (if applicable)

_Include this section when the story involves user interactions that need to be tracked in Pendo. Choose the appropriate format based on the story type._

**LIGHT FORMAT** — _Use when Pendo tracking is part of a functional story (the story delivers a feature AND includes tracking):_

| Track Event Name | PLG Stage | Trigger | Key Metadata | Confluence Ref |
|---|---|---|---|---|
| `event_name` | [Stage] | [When this event fires] | [Comma-separated key fields] | [Link to PLG Instrumentation Plan section] |

**UI element requirements:** [Any `data-pendo-id` or `#bh_` IDs to add — e.g., `data-pendo-id="save-scope-btn"`]

---

**FULL FORMAT** — _Use when this is a dedicated Pendo instrumentation story (the story's sole purpose is implementing track events). Follow the structure from [ACME-50950](https://lansweeper.atlassian.net/browse/ACME-50950):_

**Confluence Source:** [Link to PLG Instrumentation Plan section]

**Pendo FAC (Functional Acceptance Criteria):**

| ID | Given | When | Then |
|---|---|---|---|
| PFAC-1 | [Precondition — user state] | [User action that triggers the event] | `track_event_name` fires with: `field1`, `field2`, `field3`, `timestamp` |
| PFAC-2 | Feature flag is OFF | Any of the above actions occur | No track events fire |

**Pendo TAC (Technical Acceptance Criteria):**

| ID | Requirement | Rationale |
|---|---|---|
| PTAC-1 | [Technical requirement for event implementation] | [Why this matters for data quality] |

**Pendo QA Edge Cases:**
- [Edge case 1 — e.g., event fires multiple times in same session]
- [Edge case 2 — e.g., null/missing metadata handling]

---

#### AI Analysis Notes

- **Assumptions made**: [List any inferences]
- **Confidence level**: High / Medium / Low
- **Suggested refinements**: [What to review]
- **Story splitting suggestions**: [If the story seems too large]

---

### 🔧 TASK TEMPLATE

#### Metadata

| Field | Value |
|---|---|
| **Task ID** | ACME-XXXXX |
| **Epic** | ACME-XXXXX — [Epic Name] |
| **Summary** | [Concise summary] |
| **Task Type** | Technical Debt / Infrastructure / Spike / Migration / Configuration / Documentation |
| **Status** | Draft / Ready / In Progress / Done |
| **Priority** | Critical / High / Medium / Low |
| **Story Points** | [Fibonacci: 1, 2, 3, 5, 8, 13, 21] |
| **Assignee** | @name |
| **Sprint** | Sprint [N] |
| **Labels** | [label1, label2] |
| **Components** | [component1, component2] |

#### Summary

_Describe the task clearly: what needs to be done, why it's necessary, and what the expected outcome is. For spikes, define the questions to answer and the timebox._

**Task type classification:**
- **Technical Debt**: Improving code quality, reducing complexity, upgrading dependencies
- **Infrastructure**: CI/CD changes, environment setup, monitoring
- **Spike**: Time-boxed investigation to reduce uncertainty
- **Migration**: Data or system migration work
- **Configuration**: Feature flags, environment config, permissions
- **Documentation**: Technical docs, runbooks, architecture decision records

#### Feature Flag

| Flag Name | Environment | Default | Description |
|---|---|---|---|
| | | | |

#### Definition of Done

| ID | Criterion | Verification |
|---|---|---|
| DOD-1 | [What must be true when done] | [How to verify] |
| DOD-2 | [What must be true when done] | [How to verify] |
| DOD-3 | [What must be true when done] | [How to verify] |

#### Technical Specification

- **Affected components**: [component1, component2]
- **Technical approach**: [Brief description of the implementation plan]
- **API changes**: [New/modified endpoints or "None"]
- **Database changes**: [Schema changes, migrations, or "None"]
- **Configuration changes**: [Env vars, feature flags, or "None"]

#### Testing

- **Test strategy**: [Unit / Integration / Manual verification]
- **Automated tests**:
  - [ ] [Test type] for [component]
- **Rollback plan**: [How to revert if something goes wrong]

#### UX / Design

- **UI impact**: Yes / No
- **Figma link**: [URL or "Not applicable"]
- **Notes**: [Any visual or interaction changes]

#### Security and Compliance

- **Security impact**: Yes / No — [details]
- **Permission changes**: [If applicable]
- **Secrets management**: [If applicable]

#### Out of Scope

- [Item 1]
- [Item 2]

#### Implementation Notes

_Additional technical notes, links to documentation, reference implementations, or relevant code paths._

- [Note 1]
- [Note 2]

#### Pendo Tracking (if applicable)

_Include when the task involves UI changes or configuration that affects Pendo instrumentation._

| Track Event Name | PLG Stage | Trigger | Key Metadata | Confluence Ref |
|---|---|---|---|---|
| `event_name` | [Stage] | [When this event fires] | [Comma-separated key fields] | [Link to PLG Instrumentation Plan section] |

**UI element requirements:** [Any `data-pendo-id` or `#bh_` IDs to add]

#### AI Analysis Notes

- **Assumptions made**: [List any inferences]
- **Confidence level**: High / Medium / Low
- **Suggested refinements**: [What to review]
- **Complexity assessment**: [Simple / Moderate / Complex — with reasoning]

---

### 🐛 BUG TEMPLATE

#### Overview

_Describe the bug clearly: what is broken, where it occurs, and what the expected behavior should be._

#### Metadata

| Field | Value |
|---|---|
| **Bug ID** | ACME-XXXXX |
| **Epic** | ACME-XXXXX — [Epic Name] (if applicable) |
| **Summary** | [Short, descriptive bug title] |
| **Severity** | S1 (Critical) / S2 (High) / S3 (Medium) / S4 (Low) |
| **Priority** | Critical / High / Medium / Low |
| **Status** | Open / In Progress / Fixed / Verified / Closed |
| **Assignee** | @name |
| **Reporter** | @name |
| **Environment** | Dev / Staging / Production |
| **Browser/Device** | [If applicable] |
| **Labels** | [label1, label2] |
| **Components** | [component1, component2] |

#### Site ID (Cloud only)

_If this is a cloud/SaaS issue, include the affected site identifier:_
- **Site ID**: [site-uuid or "N/A"]

#### AssetKey (Cloud only)

_If this relates to a specific asset:_
- **AssetKey**: [asset-key or "N/A"]

#### Steps to Reproduce

1. [Step 1 — starting state]
2. [Step 2 — action]
3. [Step 3 — action]
4. [Step 4 — observe the bug]

**Reproduction rate**: Always / Intermittent (~X%) / One-time

#### Current Result

_What actually happens — describe the broken behavior, error messages, or unexpected output._

#### Expected Result

_What should happen — describe the correct behavior._

#### Evidences

| Type | Description | Link/Attachment |
|---|---|---|
| Screenshot | [What it shows] | [URL or attached] |
| Video | [What it shows] | [URL or attached] |
| Log | [Relevant log excerpt] | [URL or attached] |
| Console error | [Error message] | [Pasted or attached] |

#### AI Analysis Notes

- **Likely root cause**: [AI's best guess based on symptoms]
- **Suggested investigation area**: [Code path, component, or service]
- **Similar bugs**: [If patterns match known issues]
- **Severity justification**: [Why this severity level was chosen]

---

### 🔒 VULNERABILITY TEMPLATE

#### Metadata

| Field | Value |
|---|---|
| **Vulnerability ID** | ACME-XXXXX |
| **Epic** | ACME-XXXXX — [Epic Name] (if applicable) |
| **Summary** | [Short, descriptive title] |
| **Severity** | S1 (Critical) / S2 (High) / S3 (Medium) / S4 (Low) |
| **Priority** | Critical / High / Medium / Low |
| **Status** | Open / Triaged / In Progress / Fixed / Verified / Closed |
| **Assignee** | @name |
| **Reporter** | @name |
| **Discovery Method** | Scan / Pentest / Bug Bounty / Internal Review / Incident |
| **Labels** | [security, vulnerability, label1] |
| **Components** | [component1, component2] |

#### Summary

_Describe the vulnerability: what the weakness is, where it exists, and what an attacker could exploit._

#### Traceability

| Field | Value |
|---|---|
| **CVE** | [CVE-XXXX-XXXXX or "N/A"] |
| **CWE** | [CWE-XXX — Name or "N/A"] |
| **OWASP Category** | [e.g., A01:2021 — Broken Access Control] |
| **CVSS Score** | [0.0–10.0] |
| **Affected Versions** | [version range] |
| **Affected Environments** | Dev / Staging / Production |

#### Severity Classification

| Level | Definition | Response Time |
|---|---|---|
| **S1 — Critical** | Active exploitation possible, data breach risk, system compromise | Immediate (within hours) |
| **S2 — High** | Exploitable with effort, significant data/system risk | Within 24-48 hours |
| **S3 — Medium** | Limited exploitability, moderate risk | Within current sprint |
| **S4 — Low** | Theoretical risk, defense-in-depth improvement | Next sprint / backlog |

**Assigned severity**: [S1/S2/S3/S4] — [Justification]

#### Steps to Reproduce

1. [Step 1 — prerequisites and setup]
2. [Step 2 — action to trigger vulnerability]
3. [Step 3 — observe the exploit]

**Reproduction rate**: Always / Intermittent / Requires specific conditions

**Proof of Concept (PoC):**
```
[PoC code, curl command, or tool output — if applicable]
```

#### Evidence

| Type | Description | Link/Attachment |
|---|---|---|
| Scanner output | [Tool name + finding] | [URL or attached] |
| PoC output | [What it demonstrates] | [URL or attached] |
| Log entry | [Relevant log excerpt] | [URL or attached] |

#### Root Cause Analysis

- **Root cause**: [Technical description of why this vulnerability exists]
- **Code location**: [File path, module, or service]
- **Introduced in**: [Commit, PR, or version if known]
- **Contributing factors**: [Missing validation, deprecated dependency, misconfiguration, etc.]

#### Fix

- **Proposed fix**: [Description of the fix approach]
- **Fix verification**: [How to verify the fix works — test, scan, etc.]
- **PR link**: [URL or "Not yet created"]
- **Regression risk**: [What could break when fixing this]

#### Out of Scope

- [Related but separate vulnerability — create a new issue]
- [Defense-in-depth improvement — track separately]

#### AI Analysis Notes

- **Attack vector assessment**: [Network / Adjacent / Local / Physical]
- **Exploitability estimate**: [Easy / Moderate / Difficult]
- **Blast radius**: [What data/systems are at risk]
- **Remediation priority reasoning**: [Why this priority recommendation]
- **Similar vulnerabilities**: [Known patterns or past issues]

# BEHAVIORAL RULES

- Always communicate in the same language the user is using.
- Never skip a step in the workflow — each step must be completed before proceeding.
- When inferring content for a template field, be explicit about what you assumed and why.
- Story points must always be justified — never give a number without reasoning.
- If the user provides a Figma or Jira link, reference it explicitly in the relevant template section.
- After Jira creation, always provide the direct issue link.
- Adopt the tone of a senior, pragmatic PO — constructive, precise, and collaborative.

## CRITICAL: Two-step Jira creation (create + edit)

The ACME project has default issue templates that **overwrite** the `description` field passed during `createJiraIssue`. This means the description parameter in the create call is ignored by Jira.

**Mandatory workflow for every issue creation:**

1. **Create** the issue using `Atlassian:createJiraIssue` with only: `cloudId`, `projectKey`, `issueTypeName`, `summary`, `parent`, and `assignee_account_id`. Do NOT pass `description` — it will be overwritten by the project template anyway.
2. **Immediately edit** the issue using `Atlassian:editJiraIssue` with the full description content in `fields.description`. This overwrites the default template with our actual content.
3. **Verify** by fetching the issue with `Atlassian:fetch` and confirming the description is populated with the template content (not the default Jira template).

Never assume the description from `createJiraIssue` was persisted. Always follow up with `editJiraIssue`.