---
name: technical-writer
description: Technical documentation and writing skill. Use for creating READMEs, API documentation, tutorials, runbooks, changelogs, and any technical prose. Follows progressive disclosure with templates for common document types.
---

# 📝 Writer Skill

> Activated when the user needs technical documentation, explanations, READMEs, tutorials, or any form of technical writing.

## Activation Triggers

- "Write docs for...", "Document this...", "Create a README"
- "Explain how...", "Write a tutorial for..."
- "Create a runbook", "Write a changelog", "Draft an ADR"
- Any request where the primary deliverable is written documentation

## Methodology

### 1. Identify the Documentation Type

Determine what kind of document is needed:

| Type | Purpose | Audience | Structure |
|------|---------|----------|-----------|
| **README** | Project overview, quickstart | New users, evaluators | Overview → Install → Usage → API |
| **API docs** | Endpoint/function reference | Developers integrating | Endpoint → Params → Response → Example |
| **Tutorial** | Teach a skill step-by-step | Learners | Setup → Steps → Verify → Next steps |
| **How-to guide** | Solve a specific problem | Practitioners | Problem → Prerequisites → Steps → Verify |
| **Explanation** | Deepen understanding of a concept | Curious developers | Context → Core idea → Implications |
| **Runbook** | Respond to operational incidents | On-call engineers | Symptoms → Diagnosis → Resolution → Escalation |
| **ADR** | Record architecture decisions | Future team members | Context → Decision → Consequences |
| **Changelog** | Communicate changes | Users, team | Version → Date → Added/Changed/Fixed/Removed |

### 2. Identify the Audience

Before writing, establish:

- **Who** will read this? (Beginner? Senior engineer? Non-technical stakeholder?)
- **What do they already know?** (Don't explain prerequisites they have; don't assume knowledge they lack)
- **What do they want to accomplish?** (Task-oriented writing is always more useful)
- **When will they read this?** (During setup? During an incident? While evaluating?)

### 3. Write with Structure

Follow these structural principles:

#### Inverted Pyramid
Put the most important information first. If someone reads only the first paragraph, they should get the essential message.

#### Progressive Disclosure
Layer detail from general to specific:
1. **One-liner**: What is this?
2. **Paragraph**: Why does it exist and who is it for?
3. **Section**: How to get started
4. **Deep dive**: Full API reference, advanced configuration

#### Scannable Formatting
- Use **headers** to create hierarchy
- Use **bullet lists** for items without order
- Use **numbered lists** for sequential steps
- Use **tables** for structured comparisons
- Use **code blocks** for anything the reader will type or see in a terminal
- Use **bold** for key terms on first use
- Use **callouts** for warnings and important notes

## Writing Principles

### Clarity Over Cleverness
- Use simple, direct language
- Prefer short sentences (under 25 words)
- One idea per paragraph
- Avoid jargon unless writing for experts — and define it on first use

### Show, Don't Just Tell
Every concept should have a **concrete example**:

```markdown
❌ "The function accepts a configuration object."

✅ "Pass a configuration object to customize behavior:

```javascript
const config = {
  timeout: 5000,
  retries: 3,
  verbose: true
};
initialize(config);
```"
```

### Be Precise
- Use exact names: "Click the **Save** button" not "Click the button"
- Use exact values: "Timeout defaults to 30 seconds" not "Timeout has a default value"
- Use exact paths: "`src/config/database.ts`" not "the config file"

### Be Honest
- If something is complex, say so — don't pretend it's simple
- If there are limitations, document them upfront
- If a step might fail, explain what to do

## Templates

### README Template

```markdown
# Project Name

One-line description of what this project does.

## Features

- Feature 1: brief description
- Feature 2: brief description
- Feature 3: brief description

## Quick Start

### Prerequisites

- Requirement 1 (version X+)
- Requirement 2

### Installation

\```bash
npm install project-name
\```

### Usage

\```javascript
import { main } from 'project-name';

const result = main({ option: 'value' });
console.log(result);
\```

## API Reference

### `functionName(params)`

Description of what the function does.

**Parameters:**

| Name | Type | Required | Default | Description |
|------|------|----------|---------|-------------|
| `param1` | `string` | Yes | — | What this parameter controls |
| `param2` | `number` | No | `10` | What this parameter controls |

**Returns:** `ReturnType` — description

**Example:**

\```javascript
const result = functionName('value', 42);
\```

## Configuration

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `OPTION_A` | `string` | `"default"` | What this controls |

## Contributing

Brief contribution guidelines or link to CONTRIBUTING.md.

## License

MIT — see [LICENSE](./LICENSE)
```

### API Endpoint Documentation Template

```markdown
## `POST /api/v1/resource`

Description of what this endpoint does.

### Authentication

Requires Bearer token in Authorization header.

### Request

**Headers:**
| Header | Value | Required |
|--------|-------|----------|
| `Authorization` | `Bearer <token>` | Yes |
| `Content-Type` | `application/json` | Yes |

**Body:**
\```json
{
  "field1": "string (required) — description",
  "field2": 42,
  "field3": {
    "nested": "value"
  }
}
\```

### Response

**`201 Created`**
\```json
{
  "id": "abc-123",
  "field1": "value",
  "createdAt": "2024-01-15T10:30:00Z"
}
\```

**`400 Bad Request`**
\```json
{
  "error": "VALIDATION_ERROR",
  "message": "field1 is required",
  "details": [...]
}
\```

**`401 Unauthorized`**
\```json
{
  "error": "UNAUTHORIZED",
  "message": "Invalid or expired token"
}
\```
```

### Runbook Template

```markdown
# Runbook: [Incident Type]

## Symptoms
- What the operator will observe
- Alerts that fire
- User reports

## Severity
- **P1**: Total outage — follow immediately
- **P2**: Degraded — follow within 1 hour

## Diagnosis

### Step 1: Check [Component]
\```bash
command to check status
\```
Expected output: [description]

### Step 2: Check [Component]
\```bash
another command
\```

## Resolution

### Quick Mitigation
Steps to restore service immediately (may not fix root cause).

### Root Cause Fix
Steps to fully resolve the underlying issue.

## Escalation
- **Team**: [Team name] — [Slack channel / pager]
- **On-call**: [Rotation link]

## Post-Incident
- [ ] Write post-mortem
- [ ] Create follow-up tickets
- [ ] Update monitoring/alerts
```

## Quality Checklist

Before finalizing any documentation, verify:

- [ ] **Accurate**: Is everything technically correct?
- [ ] **Complete**: Can someone follow this without outside help?
- [ ] **Current**: Does this reflect the actual state of the code/system?
- [ ] **Examples**: Does every concept have a concrete example?
- [ ] **Tested**: Have you mentally walked through the steps?
- [ ] **Scannable**: Can someone find what they need in 10 seconds?
- [ ] **Audience-appropriate**: Is the tone and depth right for the reader?
