# 🚀 HA-Job-Hunter

**HA-Job-Hunter** is an AI-powered job-hunting assistant designed to intelligently analyze job descriptions, match resumes, and provide structured insights to help candidates improve their chances of selection.  
The system leverages **modern AI orchestration frameworks** such as **LangGraph**, **LangChain**, and **LangSmith**, combined with semantic similarity techniques and LLM-based reasoning.

---

## ✨ Key Features

- 📄 **Multi-Resume Upload** (PDF, DOCX, TXT)
- 🧠 **Semantic Resume ↔ Job Matching** using embeddings
- 📊 **Match Score Calculation**
- ✅ **Skill Extraction**
  - Matched skills  
  - Missing skills  
  - Additional skills
- 🔗 **LangGraph-based Agent Workflow**
- 🧩 **LLM-powered Explanation (optional)**
- 🖥️ **Clean Streamlit Frontend**
- ⚡ **FastAPI Backend**
- 📈 **Extensible for LangSmith Monitoring**

---

## 🧠 System Architecture Overview

| Layer | Component | Description |
|------|----------|-------------|
| 1️⃣ | Frontend (Streamlit) | User interface for uploading resumes, job descriptions, and viewing results |
| 2️⃣ | FastAPI Backend | Handles API requests and orchestrates the matching workflow |
| 3️⃣ | LangGraph | Controls agent flow and structured decision-making |
| 4️⃣ | LangChain | Tool and prompt orchestration |
| 5️⃣ | LLM (Grok / Open-Source) | Generates explanations and reasoning |
| 6️⃣ | Embeddings (Sentence Transformers) | Computes semantic similarity between resumes and jobs |
| 7️⃣ | LangSmith (Optional) | Monitoring, tracing, and observability |

---

## 🖥️ Frontend Implementation (Streamlit)

The frontend of **HA-Job-Hunter** is built using **Streamlit** and provides a simple, interactive interface for users to submit resumes and job descriptions for analysis.

---

### 📄 1. Resume Upload Section

- Supports **multiple resume uploads**
- Accepted formats:
  - 📄 PDF  
  - 📝 DOCX  
  - 📃 TXT  
- Automatically extracts text content from uploaded resumes

---

### 📝 2. Job Description Input Section

- Dedicated **text area** for pasting full job descriptions
- Supports long job postings and detailed requirements
- Serves as the reference document for resume matching

---

### ▶️ 3. Analyze Action Button

- Triggers the complete backend workflow:
  - Text preprocessing
  - Skill extraction
  - Embedding generation
  - Similarity computation
  - LangGraph agent execution
- Ensures user-controlled execution

---

### ⚡ User Experience Highlights

- Minimal and intuitive UI
- Clear workflow:
  **Upload Resumes → Paste Job Description → Analyze**
- Real-time feedback during processing

---

### ✅ Purpose of the Frontend

The frontend acts as a bridge between the user and the AI-powered backend, ensuring that all inputs are collected cleanly and displayed in an understandable, structured format.

---

## ⚙️ Backend Workflow

1. Resume and job description are received via FastAPI
2. Text is cleaned and normalized
3. Skills are extracted using keyword matching
4. Semantic similarity is computed using embeddings
5. Match score is calculated
6. LangGraph coordinates:
   - Matching logic
   - Optional explanation generation
7. Structured JSON response is sent to frontend

---

## 🔗 LangGraph Integration

LangGraph is used to:
- Define **explicit agent steps**
- Control execution order
- Enable future extensions like:
  - Auto-apply logic
  - Resume improvement suggestions
  - Job ranking pipelines

---

## 🧪 Example Output

- **Match Score:** `72.45%`
- **Matched Skills:** Python, FastAPI, SQL
- **Missing Skills:** Docker, Kubernetes
- **Additional Skills:** LangChain, Machine Learning

Displayed in **column-based format** for clarity.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** FastAPI
- **Agent Framework:** LangGraph
- **Orchestration:** LangChain
- **LLM:** Grok / Open-Source LLMs
- **Embeddings:** Sentence-Transformers
- **Monitoring:** LangSmith (optional)

---

## 🚧 Future Enhancements

- Resume improvement suggestions
- Job ranking & recommendations
- Automated cover-letter generation
- Application tracking dashboard
- Recruiter-side matching tools

---

## 👨‍💻 Author

**Hasan Ali**  
AI & Backend Developer  
Focused on Agentic AI, NLP, and Applied Machine Learning

---

## 📜 License

This project is for **educational and research purposes**.  
Feel free to extend and customize.

---

⭐ *If you find this project useful, consider starring the repository!*
