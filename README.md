<div align="center">
  <img src="./assets/profile-header.svg" alt="Levi Qiao — AI Systems Engineer" width="100%" />

  <p>
    <strong>AI engineer building reliable agent systems and production-grade developer tools.</strong><br />
    10 years in software engineering · Architecture · Evaluation · Reliability
  </p>

  <p>
    <a href="https://www.x-nan.com">
      <img src="https://img.shields.io/badge/Site-x--nan.com-6C63FF?style=flat-square" alt="x-nan.com" />
    </a>
    <a href="https://github.com/levi-qiao/longgraph-skill">
      <img src="https://img.shields.io/github/stars/levi-qiao/longgraph-skill?style=flat-square&logo=github&label=longgraph-skill" alt="longgraph-skill stars" />
    </a>
    <a href="https://github.com/levi-qiao/herdr-agent-quota">
      <img src="https://img.shields.io/github/stars/levi-qiao/herdr-agent-quota?style=flat-square&logo=github&label=herdr-agent-quota" alt="herdr-agent-quota stars" />
    </a>
    <a href="https://x.com/guannanjiayou">
      <img src="https://img.shields.io/badge/Follow-@guannanjiayou-111827?style=flat-square&logo=x&logoColor=white" alt="Follow @guannanjiayou on X" />
    </a>
  </p>
</div>

## What I build

I work where AI prototypes become dependable systems: agent architecture,
evaluation, orchestration, and the controls that make long-running autonomous
work inspectable and verifiable.

我做可评估、可追踪、可交付的智能体工程，重点是长任务里的 context death 和验收收敛。

## Featured

[**longgraph-skill**](https://github.com/levi-qiao/longgraph-skill) — long-horizon agent skill for Claude Code, Cursor, Codex, and Grok Build. Clean-context supervisor, multi-task ledger loop, verified gates. A markdown library (loop-graph), not a framework.

[**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) — live Claude, Codex, Grok, and Agy quota in the Herdr sidebar: 5h + weekly % remaining, reset ETAs, and time-aware quota health. Local-only; never hit a limit mid-task.

## Selected work

| Project | What it does |
| --- | --- |
| [**longgraph-skill**](https://github.com/levi-qiao/longgraph-skill) | Long-horizon agents: clean-context roles, durable state, `/loop-converge` for code-convergence. |
| [**herdr-agent-quota**](https://github.com/levi-qiao/herdr-agent-quota) | Herdr plugin: live 5h + weekly remaining for Claude / Codex / Grok / Agy, plus task context. |
| [**skillmill**](https://github.com/levi-qiao/skillmill) | Docs site, PDF, or tutorial → installable agent skill (`npx skillmill`). |
| [**session-skill**](https://github.com/levi-qiao/session-skill) | Successful agent session (chat + tool traces) → installable `SKILL.md` for Cursor / Claude Code. |
| [**agent-ding**](https://github.com/levi-qiao/agent-ding) | Notify when a coding agent finishes — modular hooks, Zellij, shell helpers. |
| [**dsh-plugin-longgraph**](https://github.com/levi-qiao/dsh-plugin-longgraph) | DeepSeek Harness plugin: longgraph / loop-graph / loop-converge authoring skills. |

## Also

| Project | What it explores |
| --- | --- |
| [**obsidian-llm-wiki**](https://github.com/levi-qiao/obsidian-llm-wiki) | Maintainable knowledge system: namespaces, layered indexes, reusable agent skills. |
| [**sherlock-claude**](https://github.com/levi-qiao/sherlock-claude) | Repo + runtime logs → focused diagnoses and fix recommendations. |
| [**skillx**](https://github.com/levi-qiao/skillx) | Write once, install anywhere — skill packager for Claude Code, Grok Build, and Cursor. |

## Current focus

- **Long-horizon agents** — survive context death, keep state durable, make “done” checkable
- **Loop converge** — bind each loop to a real acceptance gate, not empty code churn
- **Quota-aware workspaces** — live 5h + weekly remaining in the Herdr sidebar so long tasks don’t die mid-run
- **Skill tooling** — turn docs and good sessions into installable skills
- **Evaluation & reliability** — evidence-based acceptance and failure analysis

## Engineering principles

> Make the state inspectable. Make “done” verifiable. Keep the system smaller
> than the problem it solves.

<div align="center">
  <sub>Python · Rust · FastAPI · LLM agents · Evaluation · Automation · Developer tooling</sub>
</div>
