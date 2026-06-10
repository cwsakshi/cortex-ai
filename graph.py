from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

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

def classsifier_node(state: State) -> State:
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
    response = llm.invoke(question)
    return {"answer": response.content}

# Step 3 — Build the Graph
graph = StateGraph(State)
graph.add_node("classifier",classsifier_node)
graph.add_node("answer", answer_node)
graph.add_node("reject", reject_node)

graph.set_entry_point("classifier")

graph.add_conditional_edges("classifier", route_question)

graph.add_edge("answer", END)
graph.add_edge("reject", END)

app = graph.compile()

# Step 4 — Run the Graph
result = app.invoke({"question": "What is the impact of AI on healthcare?"})
print(result["answer"])