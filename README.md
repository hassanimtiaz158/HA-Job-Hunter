# HA-Job-Hunter
An AI-powered job hunting agent that autonomously analyzes job descriptions, matches resumes, generates customized cover letters, and controls application decisions using LangGraph workflows, LangChain orchestration, and LangSmith monitoring, powered by open-source LLMs via Ollama.


# Architecture View
Frontend (Streamlit)
        ↓
FastAPI Backend
        ↓
LangGraph (Decision Flow)
        ↓
LangChain (Chains + Tools)
        ↓
LLM (LLaMA 3 via Ollama)
        ↓
Vector DB (FAISS / Chroma)
        ↓
LangSmith (Monitoring)

