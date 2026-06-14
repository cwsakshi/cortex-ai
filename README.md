# 🧠 Cortex AI — Multi-Agent Career Intelligence System

> Built to solve a real problem: "I don't know what skills I need, what gaps I have, or where to start."

## 🚀 Live Demo
👉 [Try Cortex AI here](https://cortex-ai-eykbu9tsrjn33djzgdwkz4.streamlit.app/)

## What it does

Cortex AI is a multi-agent AI system with two modes:

### 🎯 Career Intelligence
Tell Cortex your current skills, dream role, and timeline. It will:
- Search the job market in real time
- Identify your skill gaps
- Generate a personalized week-by-week learning roadmap with free resources

### 🔍 Research Assistant
Ask any research question. Cortex will:
- Break it into focused sub-questions
- Search the web for each one
- Synthesize a structured research report

## 🏗️ Architecture
User Input → [Classifier] → [Planner] → [Search] → [Gap Analyzer] → [Roadmap] → Report

## 🛠️ Tech Stack — Fully Free

| Tool | Purpose |
|---|---|
| LangGraph | Multi-agent orchestration |
| LangChain | LLM chains and prompts |
| Groq + LLaMA 3.3 70B | Fast LLM inference |
| Tavily API | Real-time web search |
| Streamlit Cloud | UI + deployment |

## 🏃 Run Locally

```bash
git clone https://github.com/cwsakshi/cortex-ai
cd cortex-ai
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Add your API keys to `.env`:

GROQ_API_KEY=your_key

TAVILY_API_KEY=your_key

Run:
```bash
streamlit run app.py
```

## 👤 Built by
Sakshi Singh — B.Tech AI/ML Minor, VJTI Mumbai 2027

[LinkedIn](https://linkedin.com/in/sakshi-singh-ba2185288) | 
[GitHub](https://github.com/cwsakshi)


