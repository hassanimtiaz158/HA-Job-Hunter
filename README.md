# HA-Job-Hunter
An AI-powered job hunting agent that autonomously analyzes job descriptions, matches resumes, generates customized cover letters, and controls application decisions using LangGraph workflows, LangChain orchestration, and LangSmith monitoring, powered by open-source LLMs via Ollama.


##  Architecture View

| Layer | Component | Description |
|------|----------|-------------|
| 1 | Frontend (Streamlit) | User interface for uploading resumes, job descriptions, and viewing results |
| 2 | FastAPI Backend | Handles API requests, orchestration, and communication between components |
| 3 | LangGraph | Manages agent decision flow and autonomous application logic |
| 4 | LangChain | Executes chains, tools, and prompt orchestration |
| 5 | LLM (LLaMA 3 via Ollama) | Performs reasoning, text generation, and semantic understanding |
| 6 | Vector DB (FAISS / Chroma) | Stores embeddings for resume and job description similarity search |
| 7 | LangSmith | Provides monitoring, tracing, and observability of agent workflows |

