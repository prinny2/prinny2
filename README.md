## Vinícius Paes da Serra Freire

**Desenvolvedor Full-Stack** — Next.js · Python · Google Cloud
Belém, PA · disponível para remoto

Construo sistemas de ponta a ponta: do pipeline de dados ao checkout com pagamento real.
Meus projetos não param no deploy — dois deles processam dados de produção e cobram clientes.

---

### Projetos

**[lead-intelligence](https://github.com/prinny2/lead-intelligence)** · Python · `público`
Biblioteca de qualificação de leads com decisão comercial explícita — `accept` / `review` / `reject` —
e lista de motivos rastreáveis para auditoria. Núcleo genérico, sem LLM e sem dependência de API externa:
clone e rode em 30 segundos. 22 arquivos de teste cobrindo validação, scoring, qualificação e o fluxo
ponta a ponta.

**ResonAnza** · Python, FastAPI, React · `privado`
Plataforma de inteligência geoespacial que reinterpreta **31.244 poços públicos da ANP** — dados
perfurados pela indústria do petróleo — para mapear potencial geotérmico e osmótico na transição
energética brasileira. Pipeline com extração por OCR, correção de Horner sobre Bottom Hole Temperature,
calibração automática por bacia e ranqueamento para ciclo ORC. **155 testes** em CI. Deploy em Cloud Run.

**[LeadBellus](https://github.com/prinny2/leadvitta-app)** · Next.js 15, TypeScript, Stripe · `público` · [leadbellus.com.br](https://www.leadbellus.com.br)
Micro-SaaS em produção para clínicas de estética: transforma a mensagem da cliente no WhatsApp em
3 respostas prontas no tom da clínica, com guardrails de compliance, follow-up e condução até o
agendamento. Clerk + Firebase (ponte de sessão), Firestore, **Stripe LIVE** com webhook e paywall por
uso, WhatsApp via Z-API com auto-resposta, cadeia de fallback OpenAI → Anthropic → Gemini.
**398 testes** (Vitest), deploy na Vercel.

> Repositórios privados: código disponível sob solicitação em processo seletivo.

---

### Stack

| | |
|---|---|
| **Front-end** | Next.js, React, TypeScript, TailwindCSS |
| **Back-end** | Python, FastAPI, Node.js, APIs REST |
| **Dados** | PostgreSQL, Supabase, Firebase/Firestore, pandas, NumPy, SciPy |
| **Cloud** | Google Cloud (Cloud Run, Vertex AI, Gemini), Vercel, Docker |
| **Pagamentos** | Stripe — checkout, assinaturas, webhooks |
| **Qualidade** | pytest, GitHub Actions, Git |

---

### Formação

Três anos de Engenharia de Produção na UEPA — ciclo completo de cálculo, álgebra linear, estatística e
física. É a base que uso no tratamento de dados científicos da ResonAnza, não uma linha solta no currículo.

---

**Contato:** vpaes.freire02@gmail.com
