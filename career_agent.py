from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

class CareerState(TypedDict):
    current_skills: str
    dream_role: str
    timeline: str
    search_results: str
    skill_gaps: str
    roadmap: str

def search_node(state: CareerState) -> CareerState:
    dream_role = state["dream_role"]

    queries = [
        f"What skills are requierd for {dream_role} in 2026",
        f"{dream_role} job requirements and responsibilities",
        f"How to become {dream_role} roadmap"
    ]

    all_results = ""
    for query in queries:
        results = tavily.search(query)
        all_results += f"Search results for: {query}\n"
        for r in results["results"][:2]:   # only first 2 results
            all_results += r["title"] + "\n"
            all_results+= r["content"][:500] + "\n\n"     # only first 500 chars

    return {"search_results": all_results}

def gap_analyzer_node(state: CareerState) -> CareerState:
    current_skills = state["current_skills"]
    dream_role = state["dream_role"]
    search_results = state["search_results"]
 
    prompt = f"""You are a career advisor. Based on the job market research below, analyze the skill gap.

User's current skills: {current_skills}
Dream role: {dream_role}

Job market research:
{search_results}

Provide a structured analysis with:
1. Skills the user ALREADY HAS that are relevant ✅
2. Skills the user is MISSING that are critical ❌
3. Skills that would be GOOD TO HAVE but not critical ⚠️

Be specific and concise."""

    try:
        response = llm.invoke(prompt)
        return {"skill_gaps": response.content}
    except Exception as e:
        print(f"LLM call failed: {e}")
        return {"skill_gaps": "Sorry, something went wrong analyzing your skill gap. Please try again."}


def roadmap_node(state: CareerState) -> CareerState:
    current_skills = state["current_skills"]
    dream_role = state["dream_role"]
    timeline = state["timeline"]
    skill_gaps = state["skill_gaps"]

    prompt = f"""You are a career coach. Create a personalized week-by-week learning roadmap.

User's current skills: {current_skills}
Dream role: {dream_role}
Timeline: {timeline}
Skill gaps identified: {skill_gaps}

Create a structured roadmap with:
1. Week by week plan based on the timeline
2. For each week: what to learn and FREE resources (YouTube, GitHub, documentation)
3. One mini project to build each week to practice
4. Final goal: what they should be able to do by the end

Be specific, actionable, and only suggest completely free resources."""

    try:
        response = llm.invoke(prompt)
        return {"roadmap": response.content}
    except Exception as e:
        print(f"LLM call failed: {e}")
        return {"roadmap": "Sorry, something went wrong building your roadmap. Please try again."}
    
#build the graph 
graph = StateGraph(CareerState)

graph.add_node("search", search_node)
graph.add_node("gap_analyzer", gap_analyzer_node)
graph.add_node("roadmap", roadmap_node)

graph.set_entry_point("search")
graph.add_edge("search", "gap_analyzer")
graph.add_edge("gap_analyzer", "roadmap")
graph.add_edge("roadmap", END)

career_app = graph.compile()

def interview_prep(company: str, role: str) -> str:
    queries =[
        f"{company} {role} interview question 2026",
        f"{company} {role} interview process and rounds",
        f"How to crack {company} {role} interview tips"
    ]

    all_results = ""
    for query in queries:
        results = tavily.search(query)
        for r in results["results"][:2]:   # only first 2 results
            all_results += r["title"] + "\n"
            all_results+= r["content"][:400] + "\n\n"     # only first 400 chars

            prompt = f"""You are an interview coach. Based on the research below, help a candidate prepare for {role} at {company}.

Research:
{all_results}

Provide:
1. 🎯 What {company} tests in {role} interviews
2. 📝 Top 5 likely interview questions
3. 📚 What to study in the next 7 days
4. 💡 Key tips specific to {company}

Be specific and actionable."""
    
    response = llm.invoke(prompt)
    return {"interview_prep": response.content}

def resume_analyzer(resume_text: str, dream_role: str) -> dict:
    queries = [
        f"{dream_role} resume requirements and key skills 2026",
        f"What recuriters look for in {dream_role} resumes",
    ]

    all_results = ""
    for query in queries:
        try:
            results = tavily.search(query)
            for r in results["results"][:2]:
                all_results += r["title"] + "\n"
                all_results += r["content"][:400] + "\n\n"
        except Exception as e:
            print(f"Tavily search failed for query '{query}': {e}")
            continue

    if not all_results:
        return {"resume_analysis": "Sorry, we couldn't research this role right now. Please try again in a moment."}
    
    prompt = f"""You are an expert resume reviewer. Analyze this resume against the requirements for {dream_role}.

Resume:
{resume_text}

Job Market Research:
{all_results}

Provide:
1. ✅ Strengths — what's already strong in this resume
2. ❌ Missing — critical skills/keywords missing for {dream_role}
3. 📝 Specific suggestions — exact changes to make
4. 🎯 ATS Score estimate — out of 10, how well this resume would pass automated screening

Be specific and actionable."""

    try:
        response = llm.invoke(prompt)
        return {"resume_analysis": response.content}
    except Exception as e:
        print(f"LLM call failed: {e}")
        return {"resume_analysis": "Sorry, something went wrong analyzing your resume. Please try again."}


if __name__ == "__main__":
    result = career_app.invoke({
        "current_skills": "Python, Pandas, SQL, LangChain, LangGraph, Streamlit, basic ML",
        "dream_role": "AI/ML Engineer at a startup",
        "timeline": "4 weeks",
        "search_results": "",
        "skill_gaps": "",
        "roadmap": ""
    })
    
    print("=== SKILL GAP ANALYSIS ===")
    print(result["skill_gaps"])
    print("\n=== YOUR ROADMAP ===")
    print(result["roadmap"])