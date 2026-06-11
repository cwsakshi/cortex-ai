from tavily import TavilyClient 
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

results = client.search("What are the latest AI trends in 2025?")

for r in results["results"]:
    print(r["title"])
    print(r["content"])
    print("----")

    