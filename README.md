# 🧠 Cortex AI — Multi-Agent Career Intelligence System

> Built to solve a real problem: *"I don't know what skills I need, what gaps I have, or where to start."*

## 🚀 Live Demo
👉 [Try Cortex AI here](https://cortex-ai-eykbu9tsrjn33djzgdwkz4.streamlit.app/)

---

## What it does

Cortex AI is a **multi-agent LLM system** with 4 specialized modes — each powered by a different agent pipeline built with LangGraph.

### 🎯 Career Intelligence
Tell Cortex your current skills, dream role, and timeline. It will:
- Search the job market in real time via Tavily
- Identify your exact skill gaps vs. role requirements
- Generate a personalized week-by-week learning roadmap with free resources
- Download your roadmap and skill gap analysis as a text file

### 🎤 Interview Prep
Tell Cortex the company and role you're interviewing for. It will:
- Research real interview processes and what the company actually tests
- Generate the top 5 most likely interview questions
- Build a 7-day targeted study plan
- Give company-specific tips

### 📄 Resume Analyzer
Paste your resume and your dream role. It will:
- Compare your resume against real job market requirements
- Identify missing keywords and critical skill gaps
- Give specific, actionable suggestions
- Estimate your ATS score out of 10

### 🔍 Research Assistant
Ask any research question. It will:
- Classify intent and break it into focused sub-questions
- Search the web in parallel for each sub-question
- Synthesize a structured, source-grounded research report
- Deliver results in under 60 seconds

---

## 🏗️ Architecture

```
User Input
    ↓
[Classifier Node] — intent routing
    ↓
[Planner Node] — query decomposition
    ↓
[Search Node] — parallel Tavily web search
    ↓
[Gap Analyzer Node] — skill gap analysis
    ↓
[Roadmap Generator Node] — week-by-week plan
    ↓
Structured Report (rendered in Streamlit)
```

All agents are connected via **conditional edges and shared state** in LangGraph — adding new agents doesn't break the existing pipeline.

---

## 🛠️ Tech Stack — Fully Free

| Tool | Purpose |
|---|---|
| LangGraph | Multi-agent orchestration via stateful graph |
| LangChain | LLM chains, prompt templates |
| Groq + LLaMA 3.3 70B | Fast LLM inference (free tier) |
| Tavily API | Real-time web search for agents |
| ChromaDB | Vector storage for embeddings |
| HuggingFace | Sentence transformer embeddings |
| Streamlit Cloud | UI + deployment (free tier) |

---

## ⚙️ Engineering Highlights

- **Error handling throughout** — every Tavily search and LLM call is wrapped in try/except with graceful fallback messages, so the system never crashes on API failures
- **Scalable architecture** — new agents can be added as LangGraph nodes without touching existing pipeline
- **Fully free stack** — no paid APIs required, runs entirely on free tiers
- **Live deployment** — generates a full structured report in under 60 seconds

---

## 🏃 Run Locally

```bash
git clone https://github.com/cwsakshi/cortex-ai
cd cortex-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your API keys to `.env`:
```
GROQ_API_KEY=your_key
TAVILY_API_KEY=your_key
```

Run:
```bash
streamlit run app.py
```

---

## 👤 Built by

**Sakshi Singh** — B.Tech Textile Engineering | AI/ML Minor | VJTI Mumbai 2027

CEO, E-Cell VJTI | Data & Automation Intern, D'Decor Home Fabrics

[LinkedIn](https://linkedin.com/in/sakshi-singh) | [GitHub](https://github.com/cwsakshi)

