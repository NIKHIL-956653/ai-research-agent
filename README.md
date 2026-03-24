# 🤖 AI Research Agent

An intelligent AI agent that searches the internet 
and answers your questions in real time!

## 🚀 Tech Stack
- 🐍 Python
- 🦜 LangChain + LangGraph
- 🔍 Tavily Search API
- 🤖 OpenRouter (Free LLMs!)
- 🖥️ Streamlit UI
- 🐳 Docker

## ⚙️ Setup

### 1. Clone the repository
git clone https://github.com/NIKHIL-956653/ai-research-agent.git
cd ai-research-agent

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate

### 3. Install dependencies
pip install -r requirements.txt

### 4. Create .env file
cp .env.example .env
Add your API keys in .env:
OPENROUTER_API_KEY=your_key
TAVILY_API_KEY=your_key

### 5. Run locally
streamlit run streamlit_app.py

### 6. Run with Docker
docker build -t ai-research-agent .
docker run -p 8501:8501 --env-file .env ai-research-agent

### 7. Open browser
http://localhost:8501

## 🔑 Get Free API Keys
- OpenRouter: https://openrouter.ai (Free!)
- Tavily: https://app.tavily.com (Free!)

## 🧠 How it works
1. You ask any question
2. Agent thinks and plans
3. Tavily searches internet
4. LLM generates smart answer
5. Shows in Streamlit UI!

## 🆚 RAG vs Agent
RAG = Searches your documents only
Agent = Searches internet + thinks dynamically!

## 🎓 Built by Nikhil Chandra
