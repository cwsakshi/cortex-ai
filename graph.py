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

def search_node(state: State) -> State:
    question = state["question"]
    results = tavily.search(question)

    content =""
    for r in results["results"]:
        content += r["title"] + "\n"
        content += r["content"] + "\n\n"   

    return {"search_results": content} 

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
graph.add_node("search", search_node)
graph.add_node("answer", answer_node)
graph.add_node("reject", reject_node)

graph.set_entry_point("classifier")

graph.add_conditional_edges("classifier", route_question, {
    "answer": "search",
    "reject": "reject"
})

graph.add_edge("search", "answer")
graph.add_edge("answer", END)
graph.add_edge("reject", END)

app = graph.compile()

# Step 4 — Run the Graph
result = app.invoke({"question": "What is the impact of AI on healthcare?"})
print(result["answer"])