## Vinícius Freire

Full-stack engineer, mostly Python and TypeScript. Belém, Brazil (UTC-3).
Open to founding or early engineering roles, remote, as a contractor.

[Portfolio](https://prinny2.github.io) · [LinkedIn](https://www.linkedin.com/in/viniciuspaesfreire/) · [Resume (PDF)](https://prinny2.github.io/vinicius-freire-resume.pdf) · vpaes.freire02@gmail.com

In 2026 I built and ran three products on my own, from the data pipeline to billing and deploy.

---

### Projects

**ResonAnza** · Python, FastAPI, SQLAlchemy, Postgres, SwiftUI, React · [resonanza.com.br](https://resonanza.com.br) · code private; architecture and a tested Horner module in [resonanza-architecture](https://github.com/prinny2/resonanza-architecture)
A map of Brazil's sedimentary basins with two layers, subsurface heat and fresh groundwater, built from the same public wells: **31,000+ petroleum wells** from the oil regulator (ANP) and **~80,000 water wells** from the national groundwater registry (SIAGAS). Claude reads scanned well reports, dedicated parsers read AGP files and LAS/DLIS well logs, and every number is labeled measured or modeled and keeps its source. A Gaussian-process model maps the probability of fresh water with a bias per data source, and a blind test scores it against lab samples (Brier), leaving out any fold with no lab reference. It runs unattended on a Mac: five launchd services download the national log archive (in parallel with a Colab worker), OCR the reports, rerun the blind tests and rebuild the map every 30 minutes, with crash-safe state and health checks. Native SwiftUI app with a 3D satellite map, a phone dashboard, and a local LLM (Ollama) that answers from the project's knowledge file. FastAPI, Typer CLI, Postgres on Cloud Run, PDF/GeoJSON/KML exports. **637 pytest tests** with ruff in CI. Two fronts: **Intelligence** (water-risk mapping and aquifer monitoring from measured public data, open to pilots) and **Deep** (reading water at depth from oil-well logs: research in validation, not offered as a product). Study stage, no paying customers.

**[LeadBellus](https://github.com/prinny2/leadvitta-app)** · Next.js 16, React 19, TypeScript, Firestore, Stripe · [leadbellus.com.br](https://www.leadbellus.com.br)
WhatsApp sales replies for aesthetic clinics, written by AI. LLM fallback chain across OpenAI, Claude and Gemini with timeouts and retries, then compliance checks on every reply (no guaranteed results, diagnoses, or prices and policies the model made up). Stripe subscriptions in live mode with idempotent webhooks, WhatsApp through Meta's Cloud API and Z-API. Runs in Docker behind Caddy, deployed by GitHub Actions on every push to main. **400+ Vitest tests** with every network call mocked. Live, pre-revenue.

**[lead-intelligence](https://github.com/prinny2/lead-intelligence)** · Python, FastAPI · open source
Lead qualification for solar installers: a rules engine that returns `accept`, `review` or `reject` with a list of reasons you can audit, plus a FastAPI layer with LLM scoring (Gemini, then Claude). The core has no external dependencies: clone and run in under a minute.

> ResonAnza's product code is private; the [architecture repo](https://github.com/prinny2/resonanza-architecture) explains how it works, and I can walk through the code in an interview.

---

### Stack

| | |
|---|---|
| Languages | Python, TypeScript, JavaScript, SQL |
| Backend | FastAPI, SQLAlchemy, Typer, Node.js |
| Frontend | React, Next.js, Tailwind, SwiftUI |
| Data | PostgreSQL, SQLite, Firestore, pandas, NumPy |
| AI | OpenAI, Anthropic and Gemini APIs, Ollama; Claude Code and Codex daily |
| Cloud and ops | AWS (EC2, Lightsail), Google Cloud Run, Firebase, Docker Compose, Caddy, GitHub Actions |
| Testing | pytest, Vitest, ruff |

---

### Em português

Desenvolvedor full-stack em Belém (PA), Python e TypeScript. Em 2026 construí sozinho a ResonAnza (mapa de calor e água doce nas bacias sedimentares, a partir de 31 mil poços da ANP e 80 mil do SIAGAS, que roda sozinho num Mac), o LeadBellus (SaaS no ar com Stripe, ainda sem receita) e o lead-intelligence (open source). Disponível para vagas remotas, PJ.
