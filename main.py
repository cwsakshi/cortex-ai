from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    api_key=api_key
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI research assistant."),
    ("human", "Explain {topic} in simple terms in 3 lines.")
])

chain = prompt | llm

response = chain.invoke({"topic": "quantum computing"})

print(response.content)