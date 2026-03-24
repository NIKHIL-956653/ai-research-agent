import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Research Agent")
st.markdown("Ask me anything — I'll search the internet for you!")
st.divider()

@st.cache_resource
def load_agent():
    llm = ChatOpenAI(
        model="openrouter/auto",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=0.3
    )
    search_tool = TavilySearch(max_results=3)
    tools = [search_tool]
    agent = create_react_agent(llm, tools)
    return agent

with st.spinner("Loading AI Agent..."):
    agent = load_agent()

st.success("Agent Ready! Ask me anything! ✅")
st.divider()

question = st.text_input(
    "💬 Your question:",
    placeholder="e.g. What are the latest AI trends in 2025?"
)

if st.button("Search & Answer 🔍"):
    if question:
        with st.spinner("Agent is thinking and searching..."):
            result = agent.invoke({
                "messages": [("user", question)]
            })
            answer = result['messages'][-1].content
        st.markdown("### 📝 Answer:")
        st.write(answer)
    else:
        st.warning("Please type a question first!")