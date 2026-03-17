# 🧠 Lansweeper PO Skills for Claude

A curated collection of Claude custom skills optimized for Product Owner workflows at Lansweeper. These skills transform Claude into an AI-powered PO assistant that integrates with Jira, Confluence, Slack, and Figma via MCP connectors.

## What Are Claude Skills?

Skills are structured instruction files (`SKILL.md`) that give Claude domain-specific expertise. When loaded into a Claude project, they teach Claude _how_ to perform specialized tasks — following your team's templates, conventions, and quality standards — instead of relying on generic AI behavior.

Think of them as "playbooks" that Claude follows automatically when it detects a relevant request.

## Skills Overview

| Skill | Category | What It Does |
|---|---|---|
| **orchestrator-po** | 🪃 Meta | Routes complex multi-step requests to the right skills. Start here for anything ambiguous. |
| **jira-ticket-creator** | ✍️ Execution | Creates Epics, Stories, Tasks, Bugs with Lansweeper templates, acceptance criteria, and QA strategy |
| **sprint-planner** | 📅 Execution | Sprint planning, capacity calculation, backlog grooming, velocity tracking |
| **stakeholder-communicator** | 📣 Execution | Sprint updates, release notes, executive summaries, escalation reports |
| **test-plan-creator** | 🧪 Execution | Structured test plans following Lansweeper QA templates |
| **technical-writer** | 📝 Execution | READMEs, API docs, runbooks, changelogs |
| **jira-researcher** | 🔍 Retrieval | Searches and navigates Jira issues, epics, sprints, comments |
| **confluence-researcher** | 📚 Retrieval | Searches Confluence spaces, pages, and comments |
| **slack-researcher** | 💬 Retrieval | Searches Slack channels, threads, and messages |
| **figma-researcher** | 🎨 Retrieval | Extracts design context, screenshots, and tokens from Figma |

### How Skills Work Together

```
User Request (complex/ambiguous)
        │
        ▼
  orchestrator-po ──── analyzes & decomposes
        │
        ├──▶ jira-researcher ──── gathers context from Jira
        ├──▶ slack-researcher ──── pulls discussion context
        ├──▶ confluence-researcher ──── finds specs/docs
        │
        ▼
  orchestrator-po ──── synthesizes context
        │
        ├──▶ jira-ticket-creator ──── creates tickets
        ├──▶ sprint-planner ──── plans the sprint
        ├──▶ stakeholder-communicator ──── writes the update
        │
        ▼
  Final deliverable(s) to user
```

---

## 🚀 Setup Guide (for your Claude account)

### Prerequisites

- A **Claude Pro**, **Team**, or **Enterprise** account (skills require Claude Projects)
- MCP connectors enabled for: **Atlassian (Jira/Confluence)**, **Slack**, **Figma** (configure in Claude Settings → Integrations)

### Step-by-Step Setup

#### 1. Clone this repo

```bash
git clone https://github.com/AdrianAmZa/lansweeper-po-skills.git
```

#### 2. Create a Claude Project

1. Go to [claude.ai](https://claude.ai)
2. Click **"Projects"** in the left sidebar
3. Click **"Create Project"**
4. Name it something like: `Lansweeper PO Assistant`

#### 3. Upload the skills

In your project, go to **Project Knowledge** and upload each `SKILL.md` file from the `skills/` folder:

```
skills/orchestrator-po/SKILL.md
skills/jira-ticket-creator/SKILL.md
skills/sprint-planner/SKILL.md
skills/stakeholder-communicator/SKILL.md
skills/test-plan-creator/SKILL.md
skills/technical-writer/SKILL.md
skills/jira-researcher/SKILL.md
skills/confluence-researcher/SKILL.md
skills/slack-researcher/SKILL.md
skills/figma-researcher/SKILL.md
```

> **Tip:** You can drag-and-drop all 10 files at once into the Project Knowledge panel.

#### 4. Enable MCP Integrations

Make sure these integrations are connected in your Claude account (Settings → Integrations):

- ✅ **Atlassian** — for Jira and Confluence access
- ✅ **Slack** — for channel/thread search
- ✅ **Figma** — for design context extraction

#### 5. (Optional) Set Project Instructions

In your project settings, you can add custom instructions. Here's a recommended starting point:

```
You are a Product Owner assistant for Lansweeper. When I give you a task:

1. If it's complex or ambiguous, use the orchestrator-po skill to plan first.
2. Always gather context from Jira/Confluence/Slack before creating tickets.
3. Follow Lansweeper templates strictly for all Jira issues.
4. Write all Jira content in English, conversational responses in my preferred language.
5. My Jira project key is ACME on the Lansweeper Atlassian instance.
```

#### 6. Start using it!

Open a new conversation inside the project and try:

- _"Check the status of epic ACME-47657 and give me a summary"_
- _"Create a story for adding SSO configuration banners to the new UI"_
- _"Prepare a sprint status update for stakeholders"_
- _"What did the team discuss in #product-analytics last week?"_

---

## 📁 Repository Structure

```
lansweeper-po-skills/
├── README.md                          # This file
├── CHANGELOG.md                       # Version history
├── skills/
│   ├── orchestrator-po/SKILL.md       # Meta-orchestrator
│   ├── jira-ticket-creator/SKILL.md   # Jira issue creation
│   ├── sprint-planner/SKILL.md        # Sprint planning
│   ├── stakeholder-communicator/SKILL.md
│   ├── test-plan-creator/SKILL.md
│   ├── technical-writer/SKILL.md
│   ├── jira-researcher/SKILL.md       # Jira search/retrieval
│   ├── confluence-researcher/SKILL.md
│   ├── slack-researcher/SKILL.md
│   └── figma-researcher/SKILL.md
```

## 🔄 Updating Skills

When skills are updated in this repo:

1. Pull the latest changes: `git pull origin main`
2. In your Claude Project, go to Project Knowledge
3. Delete the outdated `SKILL.md` file(s)
4. Re-upload the updated version(s)

> ⚠️ Claude does not auto-sync with GitHub. You must manually re-upload changed files.

## ⚠️ Important Notes

- **Skills are read-only context** — they teach Claude behavior but don't execute code themselves. All actions happen through Claude's MCP connectors (Jira API, Slack API, etc.).
- **Jira project specifics** (project key, cloud ID, account IDs) should be set in your Project Instructions, not hardcoded in skills.
- **Skills work best together** — the orchestrator routes to specialized skills, so uploading all of them gives you the full experience.
- **MCP connectors must be enabled per-user** — each team member needs their own Atlassian/Slack/Figma connections configured.

## 📋 Permissions

| User | Role | Access |
|---|---|---|
| Adrian (AdrianAmZa) | Owner / Editor | Full read/write access |
| Selene Recio | Collaborator | Read-only access |

## 📄 License

Internal use only — Lansweeper proprietary.
