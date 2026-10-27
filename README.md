## Vinícius Paes da Serra Freire

**Full-stack developer** — Next.js · TypeScript · Python/FastAPI · LLM integrations<br>
Belém, Brazil (UTC−3) · open to **remote full-stack / AI-integration roles** · vpaes.freire02@gmail.com

I build products end to end — LLM prompts and data pipelines through Stripe checkout and webhooks — and ship them as a solo developer.

**[LeadBellus](https://github.com/prinny2/leadvitta-app)** — AI-assisted WhatsApp sales replies for Brazilian aesthetic clinics
- Production SaaS with **live Stripe billing**: subscriptions, billing portal, idempotent webhooks, usage-based paywall
- Next.js 15 · TypeScript · Clerk → Firebase Auth · Firestore · Z-API (WhatsApp) · OpenAI → Claude → Gemini fallback · 404 Vitest tests
- Production deployment offline since Oct 2026 — `npm install && npm run dev` runs the full app in demo mode, no keys

**[lead-intelligence](https://github.com/prinny2/lead-intelligence)** — Lead qualification for Brazilian solar installers
- `accept` / `review` / `reject` decision with traceable reasons, from a dependency-free Python core
- FastAPI service: hybrid rules + LLM scoring (Gemini → Claude Haiku), Stripe subscriptions, Firestore with JSONL fallback
- 21 pytest files; the API boots with no keys → `/docs`

<sub>🇧🇷 Versão em português abaixo.</sub>

---

### 🇧🇷 Em português

**Desenvolvedor Full-Stack** — Next.js · TypeScript · Python
Belém, PA · disponível para remoto

Construo sistemas de ponta a ponta: do pipeline de dados ao checkout com pagamento real.
Meus projetos não param no deploy — o LeadBellus foi para produção com cobrança real via Stripe.

### Projetos

**[LeadBellus](https://github.com/prinny2/leadvitta-app)** · Next.js 15, TypeScript, Stripe · `público`
Micro-SaaS para clínicas de estética: transforma a mensagem da cliente no WhatsApp em
3 respostas prontas no tom da clínica, com guardrails de compliance, follow-up e condução até o
agendamento. Clerk + Firebase Auth (ponte de sessão) + Firestore, **Stripe em modo live** (checkout, portal,
webhooks idempotentes) com paywall por uso, WhatsApp via Z-API, fallback OpenAI → Anthropic → Gemini com
timeout e retry, Supabase/Postgres com migrations e RLS, GA4 client e server.
**404 testes Vitest em 36 arquivos**. Rodou na Vercel; produção offline desde out/2026 — roda localmente em modo demo, sem chaves.

**[lead-intelligence](https://github.com/prinny2/lead-intelligence)** · Python, FastAPI · `público`
Biblioteca de qualificação de leads com decisão comercial explícita — `accept` / `review` / `reject` —
e lista de motivos rastreáveis para auditoria. Núcleo genérico, sem LLM e sem dependência de API externa:
clone e rode em 30 segundos. Em cima dele, API FastAPI com scoring híbrido regras + LLM (Gemini → Claude),
Stripe e Firestore. 21 arquivos de teste cobrindo validação, scoring, qualificação e o fluxo ponta a ponta.

**ResonAnza** · Python, FastAPI, React · `privado`
Plataforma de inteligência geoespacial que reinterpreta **31.244 poços públicos da ANP** — dados
perfurados pela indústria do petróleo — para mapear potencial geotérmico e osmótico na transição
energética brasileira. Pipeline com extração por OCR, correção de Horner sobre Bottom Hole Temperature,
calibração automática por bacia e ranqueamento para ciclo ORC. **155 testes** em CI. Deploy em Cloud Run.

> Repositórios privados: código disponível sob solicitação em processo seletivo.

---

### Stack

| | |
|---|---|
| **Front-end** | Next.js, React, TypeScript, TailwindCSS |
| **Back-end** | Python, FastAPI, Node.js, APIs REST |
| **Dados** | PostgreSQL, Supabase, Firebase/Firestore, pandas, NumPy, SciPy |
| **Cloud** | Vercel, Firebase (Auth, Firestore, Admin SDK), Gemini API, Docker |
| **Pagamentos** | Stripe — checkout, assinaturas, webhooks |
| **Qualidade** | Vitest, pytest, GitHub Actions, Git |

---

### Formação

Três anos de Engenharia de Produção na UEPA — ciclo completo de cálculo, álgebra linear, estatística e
física. É a base que uso no tratamento de dados científicos da ResonAnza, não uma linha solta no currículo.

---

**Contato:** vpaes.freire02@gmail.com
