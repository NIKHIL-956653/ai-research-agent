from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="openrouter/auto",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.3
)

search_tool = TavilySearch(max_results=3)

tools = [search_tool]

agent = create_react_agent(llm, tools)

if __name__ == "__main__":
    result = agent.invoke({
        "messages": [
            ("user", "What is LangChain?")
        ]
    })
    print(result['messages'][-1].content)