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

## ✅ Frontend (Streamlit) – What We Have Implemented

### 🖥️ 1. User Interface (UI)
- Built an interactive **Streamlit web application**
- Added:
  - App title and description
  - Page configuration
- Designed a **simple and user-friendly job hunter interface**

---

### 📄 2. Resume Upload Handling
- Enabled **multiple resume uploads**
- Supported file formats:
  - **PDF**
  - **DOCX**
  - **TXT**
- Safely handled different file types to prevent crashes

---

### ✂️ 3. Text Extraction from Resumes
- Extracted resume text from:
  - **PDF** using `pdfplumber`
  - **DOCX** using `python-docx`
  - **TXT** using file decoding
- Combined text across:
  - Multiple pages
  - Paragraphs

---

### 🧹 4. Text Cleaning & Normalization
- Converted all text to **lowercase**
- Removed unnecessary and junk characters
- Normalized whitespace
- Prepared clean text for embedding generation

---

### 🧠 5. Open-Source Embedding Model
- Used **SentenceTransformer** (`all-MiniLM-L6-v2`)
- Cached the model to avoid repeated loading
- Generated embeddings **locally**
- No API cost or external dependency

---

### 🧩 6. Resume Chunking
- Split resumes into **smaller text chunks**
- Prevented loss of important resume sections
- Improved semantic similarity accuracy

---

### 🔍 7. Semantic Similarity Matching
- Compared resume chunks with the job description
- Used **cosine similarity**
- Selected the **best-matching chunk** for each resume

---

### 🧑‍💻 8. Skill Extraction & Matching
- Extracted skills using **regex-based logic**
- Identified:
  - ✅ Matched skills
  - ❌ Missing skills
- Improved transparency and explainability

---

### 📊 9. Combined Match Scoring Logic
- Calculated a final score using:
  - Semantic similarity score
  - Skill overlap score
- Generated a **final match percentage**

---

### 📈 10. Ranking & Displaying Results
- Ranked resumes based on match score
- Displayed results in a **clean, sortable table**
- Clearly showed:
  - Match percentage
  - Matched skills
  - Missing skills

---

### ⚡ 11. User Feedback & Validation
- Displayed warnings for missing inputs
- Showed loading and success messages
- Improved overall user experience (UX)

---
