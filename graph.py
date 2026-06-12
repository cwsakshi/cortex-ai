from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from tavily import TavilyClient

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY")
)

# Step 1 — Define State

class State(TypedDict):
    question: str
    answer: str
    is_research: bool
    search_results: str
    sub_questions: list 


def classifier_node(state: State) -> State:
    question = state["question"]
    prompt = f"""You are a strict classifier. Answer ONLY with yes or no, nothing else.
    Is this a question that requires research, analysis, or factual investigation?
    Simple personal questions like 'what should I eat' or 'what to wear' are NOT research questions.
    Question: {question}
    Answer (yes or no only):"""
    response = llm.invoke(prompt)
    answer = response.content.strip().lower()
    print(f"LLM said: {answer}")
    return {"is_research": "yes" in answer}

def planner_node(state: State) -> State:
    question = state["question"]

    prompt = f"""You are a research planner. Break the following question into 3-4 focused sub-questions that together will help answer the main question comprehensively.
    
    Main question: {question} 

    Return ONLY a numbered list of sub-questions, nothing else. Example format:
    1. Sub-question one
    2. Sub-question two
    3. Sub-question three"""

    response = llm.invoke(prompt)

    #parse the numbered list into a python list 
    lines = response.content.strip().split("\n")
    sub_questions = [line.split(". ", 1)[1] for line in lines if line.strip() and line[0].isdigit()]
    
    print(f"Sub-questions: {sub_questions}")
    return {"sub_questions": sub_questions}

def search_node(state: State) -> State:
    sub_questions = state['sub_questions']

    all_results =""
    for question in sub_questions:
        results = tavily.search(question)
        all_results += f"Search results for: {question}\n"
        for r in results["results"][:2]:   # only first 2 results
            all_results += r["title"] + "\n"
            all_results+= r["content"][:500] + "\n\n"     # only first 500 chars

    return {"search_results": all_results} 

def reject_node(state: State) -> State:
    return{"answer": "Sorry, this doesn't seem like a research question."}

def route_question(state: State)-> State:
    if state["is_research"]:
        return "answer"
    else:
        return "reject"
    
# Step 2 — Define Node

def answer_node(state: State) -> State:
    question = state["question"]
    search_results = state["search_results"]
    
    prompt = f"""You are a research assistant. Based on the search results below, 
answer the following question in a structured way.

Question: {question}

Search Results:
{search_results}

Provide a comprehensive answer based on the search results."""
    
    response = llm.invoke(prompt)
    return {"answer": response.content}

# Step 3 — Build the Graph
graph = StateGraph(State)

graph.add_node("classifier", classifier_node)
graph.add_node("planner", planner_node)
graph.add_node("search", search_node)
graph.add_node("answer", answer_node)
graph.add_node("reject", reject_node)

graph.set_entry_point("classifier")

graph.add_conditional_edges("classifier", route_question, {
    "answer": "planner",
    "reject": "reject"
})

graph.add_edge("planner", "search")
graph.add_edge("search", "answer")
graph.add_edge("answer", END)
graph.add_edge("reject", END)

app = graph.compile()

# Step 4 — Run the Graph
result = app.invoke({"question": "What is the impact of AI on healthcare?"})
print(result["answer"])