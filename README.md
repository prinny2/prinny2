## Vinícius Freire

Full-stack engineer, mostly Python and TypeScript. Belém, Brazil (UTC-3).
Open to founding or early engineering roles, remote, as a contractor.

[Portfolio](https://prinny2.github.io) · [LinkedIn](https://www.linkedin.com/in/viniciuspaesfreire/) · [Resume (PDF)](https://prinny2.github.io/vinicius-freire-resume.pdf) · vpaes.freire02@gmail.com

In 2026 I built and ran three products on my own, from the data pipeline to billing and deploy.

---

### Projects

**ResonAnza** · Python, FastAPI, SQLAlchemy, Postgres, React · [resonanza.com.br](https://resonanza.com.br) · code private, site public in [resonanza-site](https://github.com/prinny2/resonanza-site)
Energy data platform on public records from Brazil's oil regulator (ANP) for **31,244 wells**. Claude reads scanned PDF reports, dedicated parsers read AGP files and LAS well logs, and every record is checked against a schema before it is stored. Every number is labeled measured or modeled and keeps its source. FastAPI with JWT auth and rate limiting, Typer CLI, React 19 dashboard, Postgres on Cloud Run, PDF/GeoJSON/KML exports. **450+ pytest tests** with ruff and coverage in CI. Study stage.

**[LeadBellus](https://github.com/prinny2/leadvitta-app)** · Next.js 16, React 19, TypeScript, Firestore, Stripe · [leadbellus.com.br](https://www.leadbellus.com.br)
WhatsApp sales replies for aesthetic clinics, written by AI. LLM fallback chain across OpenAI, Claude and Gemini with timeouts and retries, then compliance checks on every reply (no guaranteed results, diagnoses, or prices and policies the model made up). Stripe subscriptions in live mode with idempotent webhooks, WhatsApp through Meta's Cloud API and Z-API. Runs in Docker behind Caddy, deployed by GitHub Actions on every push to main. **400+ Vitest tests** with every network call mocked. Live, pre-revenue.

**[lead-intelligence](https://github.com/prinny2/lead-intelligence)** · Python, FastAPI · open source
Lead qualification for solar installers: a rules engine that returns `accept`, `review` or `reject` with a list of reasons you can audit, plus a FastAPI layer with LLM scoring (Gemini, then Claude). The core has no external dependencies: clone and run in under a minute.

> ResonAnza's code is private; I can walk through it in an interview.

---

### Stack

| | |
|---|---|
| Languages | Python, TypeScript, JavaScript, SQL |
| Backend | FastAPI, SQLAlchemy, Typer, Node.js |
| Frontend | React, Next.js, Tailwind |
| Data | PostgreSQL, SQLite, Firestore, pandas, NumPy |
| AI | OpenAI, Anthropic and Gemini APIs, Ollama; Claude Code and Codex daily |
| Cloud and ops | AWS (EC2, Lightsail), Google Cloud Run, Firebase, Docker Compose, Caddy, GitHub Actions |
| Testing | pytest, Vitest, ruff |

---

### Em português

Desenvolvedor full-stack em Belém (PA), Python e TypeScript. Em 2026 construí sozinho a ResonAnza (dados públicos da ANP para 31.244 poços), o LeadBellus (SaaS no ar com Stripe, ainda sem receita) e o lead-intelligence (open source). Disponível para vagas remotas, PJ.
