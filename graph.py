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

# Step 2 — Define Node
def answer_node(state: State) -> State:
    question = state["question"]
    response = llm.invoke(question)
    return {"answer": response.content}

# Step 3 — Build the Graph
graph = StateGraph(State)
graph.add_node("answer", answer_node)
graph.set_entry_point("answer")
graph.add_edge("answer", END)
app = graph.compile()

# Step 4 — Run the Graph
result = app.invoke({"question": "What is artificial intelligence?"})
print(result["answer"])