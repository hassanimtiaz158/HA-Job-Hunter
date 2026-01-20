import streamlit as st
import re
import pdfplumber
import docx
from sentence_transformers import SentenceTransformer, util
import pandas as pd

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="HA-JOBHunter")
st.title("HA-JOBHunter")
st.write("Job Hunting Using HA Agent with Resume Matching 🔎")

# ---------------- FILE INPUTS ----------------
file_upload = st.file_uploader(
    "Upload Resume(s)",
    accept_multiple_files=True,
    type=["pdf", "txt", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    max_chars=50000
)

# ---------------- UTILITY FUNCTIONS ----------------
def clean_text(text):
    text = text.lower()
    text = text.replace("\n", " ")
    text = " ".join(text.split())
    text = re.sub(r"[^a-z0-9\s@+.-]", "", text)
    return text

def extract_pdf_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    return text

def extract_docx_text(file):
    doc = docx.Document(file)
    return " ".join(p.text for p in doc.paragraphs)

def chunk_text(text, chunk_size=300):
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

def extract_skills(text):
    skill_pattern = r"\b(python|fastapi|docker|sql|langchain|aws|git|ml|ai)\b"
    return set(re.findall(skill_pattern, text))

# ---------------- MODEL ----------------
@st.cache_resource
def load_model():
    return SentenceTransformer(
        "all-MiniLM-L6-v2",
        cache_folder="./models"
    )
model = load_model()


# ---------------- ANALYZE ----------------
if st.button("Analyze"):
    if not file_upload:
        st.warning("Please upload at least one resume.")
    elif not job_description.strip():
        st.warning("Please paste a job description.")
    else:
        st.info("Analyzing resumes...")

        jd_clean = clean_text(job_description)
        jd_emb = model.encode(jd_clean, convert_to_tensor=True)
        jd_skills = extract_skills(jd_clean)

        results = []

        for resume in file_upload:
            if resume.type == "application/pdf":
                raw_text = extract_pdf_text(resume)
            elif resume.type == "text/plain":
                raw_text = resume.read().decode("utf-8", errors="ignore")
            elif resume.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                raw_text = extract_docx_text(resume)
            else:
                continue

            cleaned = clean_text(raw_text)
            chunks = chunk_text(cleaned)

            similarities = []
            for chunk in chunks:
                emb = model.encode(chunk, convert_to_tensor=True)
                sim = util.cos_sim(emb, jd_emb).item()
                similarities.append(sim)

            semantic_score = max(similarities)
            resume_skills = extract_skills(cleaned)

            matched = jd_skills.intersection(resume_skills)
            missing = jd_skills.difference(resume_skills)

            skill_score = len(matched) / len(jd_skills) if jd_skills else 0

            final_score = (0.6 * semantic_score) + (0.4 * skill_score)

            results.append({
                "Resume": resume.name,
                "Match Score (%)": round(final_score * 100, 2),
                "Matched Skills": ", ".join(matched) if matched else "None",
                "Missing Skills": ", ".join(missing) if missing else "None"
            })

        df = pd.DataFrame(results).sort_values("Match Score (%)", ascending=False)
        st.success("Analysis Complete")
        st.dataframe(df.reset_index(drop=True))
