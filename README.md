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

## 🖥️ Frontend Implementation (Streamlit)

The frontend of **HA-JOBHunter** is built using **Streamlit** and provides a simple, interactive interface for users to submit resumes and job descriptions for analysis.

---

### 📄 1. Resume Upload Section
- Added a **file upload section** that allows users to upload **multiple resumes** at once
- Supported common resume formats:
  - PDF
  - DOCX
  - TXT
- This section serves as the primary input for candidate data

---

### 📝 2. Job Description Input Section
- Added a **text area** where users can paste a complete job description
- Allows long-form input suitable for detailed job requirements
- This input is used as the reference point for resume matching

---

### ▶️ 3. Analyze Action Button
- Added an **Analyze** button to initiate the processing workflow
- Acts as a trigger for:
  - Resume analysis
  - Text cleaning
  - Embedding generation
  - Similarity matching
- Provides clear user control over when analysis starts

---

### ⚡ User Experience Highlights
- Clean and minimal interface
- Logical input flow (Resumes → Job Description → Analyze)
- Clear feedback when the analysis process begins

---

### ✅ Purpose of the Frontend
The frontend acts as a bridge between the user and the AI-powered backend, ensuring that all required inputs are collected in a structured and user-friendly way before processing begins.

---

---
