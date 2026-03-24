---
name: chat-export
description: Export the current chat conversation as a structured, portable document so it can be reloaded in a new Claude account or session. Use this skill whenever someone wants to save, export, archive, or transfer a conversation — including phrases like "exporteer deze chat", "sla dit gesprek op", "ik wil dit meenemen naar een nieuwe account", "backup maken van onze chat", "export conversation", "save this chat", "I want to continue this elsewhere", or any mention of switching accounts while preserving chat history. Always trigger when the user mentions account migration, losing chat history, or wanting to continue a conversation in a new context.
---

# Chat Export Skill

Help the user export the current conversation as a structured, portable document that can be reloaded in a new Claude session to fully restore context.

## Your Goal

Produce a **self-contained export file** (Markdown) that captures:
1. All relevant knowledge, decisions, and context from this conversation
2. A ready-to-use **resume prompt** the user can paste into a new Claude session to instantly restore context

---

## Step 1: Analyze the Conversation

Before generating anything, mentally scan the full conversation for:

- **Key topics** discussed (projects, tools, systems, decisions)
- **Established facts** about the user (role, company, preferences, constraints)
- **Decisions made** (choices, conclusions, agreed approaches)
- **Ongoing work** (tasks in progress, next steps, open questions)
- **Important context** (domain knowledge, terminology, configurations, constraints)
- **Code, configs, or structured outputs** that were produced
- **User preferences** (communication style, language, output format preferences)

---

## Step 2: Generate the Export

Create a Markdown file with the following structure:

```markdown
# Chat Export — [Short Topic Title]
**Exported:** [current date]
**Original context:** [1-sentence summary of what this conversation was about]

---

## 🧠 Context & Background

[Paragraph(s) summarizing who the user is, their role/company if known, and the broader context of this conversation. Write in third person so Claude can absorb it as background knowledge.]

---

## 📋 Topics Covered

[Bullet list of main topics discussed, each with a 1–2 line summary]

---

## ✅ Decisions & Conclusions

[List of key decisions made, conclusions reached, or approaches agreed upon. Be specific. Include reasoning where relevant.]

---

## 🔄 Work in Progress

[Any ongoing tasks, open questions, or next steps that were identified but not yet completed]

---

## 💾 Key Outputs

[Any important artifacts from this conversation: code snippets, configs, templates, structured data, analysis results. Include the actual content, not just a reference to it.]

---

## 🗝️ Important Context & Constraints

[Domain-specific knowledge, constraints, naming conventions, tool configurations, or other context that Claude needs to work effectively on follow-up tasks]

---

## ▶️ Resume Prompt

> Paste this prompt at the start of a new Claude conversation to restore full context:

---

[AUTO-GENERATED RESUME PROMPT — see instructions below]

---
```

---

## Step 3: Write the Resume Prompt

The resume prompt is the most critical part. It must be **self-contained** — a single block of text the user pastes into a fresh Claude session that immediately gives Claude full context to continue working.

**Resume prompt structure:**
```
You are picking up a working session with [name/role if known]. Here is the full context:

**Background:** [who they are, company, role, relevant personal context]

**What we were working on:** [clear summary of the main task(s)]

**Key decisions already made:** [bullet list]

**Current status / next steps:** [where things stand]

**Important constraints or preferences:** [any rules, preferences, tool limitations, language preferences, etc.]

**Relevant outputs already produced:** [include inline if short; reference by name if long]

Please acknowledge this context and ask how you can help continue.
```

The resume prompt should be **complete enough that a new Claude instance could immediately be useful** without the user having to re-explain anything.

---

## Behavior Rules

- **Be thorough, not brief.** The export is a backup — err on the side of including more rather than less.
- **Write for a fresh Claude.** Assume zero prior knowledge. Every section should make sense in isolation.
- **Preserve nuance.** If the user corrected Claude during the conversation, note the correction in the relevant section.
- **Include actual content.** Don't just say "a config was discussed" — include the actual config.
- **Language:** Match the language of the conversation (Dutch or English). The resume prompt should be in English for maximum compatibility.
- **Filename:** Use the format `chat-export_[topic-slug]_[YYYY-MM-DD].md`

---

## Step 4: Deliver

1. Save the export as a `.md` file in the outputs directory
2. Present the file to the user
3. Briefly explain:
   - What's in the file
   - How to use the resume prompt in a new session
   - That they can also share the full export file as an attachment in the new session for maximum context

**After delivering:** Offer to refine any section if something important is missing.
