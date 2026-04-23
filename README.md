# Lansweeper PO Skills

Claude AI skills system for the Product Owner workflow at Lansweeper — part of the **Way of Working 2026** initiative.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                 ORCHESTRATION                    │
│               orchestrator-po                    │
├────────────────────┬────────────────────────────┤
│      RESEARCH      │        EXECUTION           │
│  jira-researcher   │  jira-ticket-creator       │
│  confluence-res.   │  sprint-planner            │
│  slack-researcher  │  stakeholder-communicator  │
│  figma-researcher  │                            │
├────────────────────┴────────────────────────────┤
│                   OUTPUT                         │
│       test-plan-creator · technical-writer       │
└─────────────────────────────────────────────────┘
```

## Quick Install

Download the latest bundle from [Releases](../../releases) and install individual `.skill` files in Claude, or clone the repo for direct access.

### Option A — Install individual skills

1. Go to [Releases](../../releases) and download the `.skill` files you need
2. Install each one in Claude's skill manager

### Option B — Clone the repo

```bash
git clone git@github.com:AdrianAmZa/lansweeper-po-skills.git
```

Then point Claude to the `skills/` directory.

## Skills Reference

| Layer | Skill | Description |
|-------|-------|-------------|
| Orchestration | `orchestrator-po` | Meta-skill that routes to the right PO skill based on the request |
| Research | `jira-researcher` | Search and extract from Jira with progressive retrieval |
| Research | `confluence-researcher` | Navigate Confluence pages, spaces, and hierarchies |
| Research | `slack-researcher` | Search Slack channels, threads, and messages |
| Research | `figma-researcher` | Extract design context from Figma files via MCP |
| Execution | `jira-ticket-creator` | Create structured Jira issues (Outcome/Milestone/Epic/Story/Task/Bug/Vulnerability) with full templates |
| Execution | `sprint-planner` | Sprint planning, capacity, velocity, and backlog grooming |
| Execution | `stakeholder-communicator` | Status reports, release notes, executive summaries |
| Output | `test-plan-creator` | Structured Jira Test Plans with the Lansweeper template |
| Output | `technical-writer` | READMEs, API docs, runbooks, changelogs |
| Utility | `chat-export` | Export conversations for portability |

## Key Concepts

- **Karpathy self-evaluation loop**: generate → evaluate → refine (max 2 passes)
- **Progressive layered retrieval**: metadata → SKILL.md → bundled resources
- **MCP integrations**: Atlassian, Slack, Figma
- **Templates**: FAC/TAC tables, DoR/DoD, BLUF, AI_CONTEXT delimiters

## Building a New Release

```bash
python bundle_skills.py ./skills --version <version>
```

This generates:
- `dist/individual/` — one `.skill` file per skill
- `dist/lansweeper-po-skills-v<version>.zip` — full bundle
- `dist/manifest.json` — machine-readable index

Then create the GitHub release:

```bash
gh release create v<version> \
  dist/lansweeper-po-skills-v<version>.zip \
  dist/individual/*.skill \
  --title "v<version> — PO Skills Bundle" \
  --notes-file dist/RELEASE_NOTES.md
```

## Contributing

1. Edit skills in `skills/<skill-name>/SKILL.md`
2. Test with Claude
3. Run `python bundle_skills.py ./skills --version <next>`
4. Open a PR

## License

Internal use — Lansweeper Product team.
