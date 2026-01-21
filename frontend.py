import streamlit as st
import requests
import pdfplumber
import docx

st.set_page_config(page_title="HA-JOBHunter")
st.title("HA-JOBHunter")
st.write("Job Hunting Using HA Agent with Resume Matching 🔎")

# -------- Upload Resume --------
uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    accept_multiple_files=True,
    type=["pdf", "txt", "docx"]
)

# -------- Job Description --------
job_description = st.text_area(
    "Paste Job Description",
    max_chars=50000
)

# -------- Helpers --------
def extract_text(file):
    if file.type == "application/pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                if page.extract_text():
                    text += page.extract_text() + " "
        return text

    elif file.type == "text/plain":
        return file.read().decode("utf-8", errors="ignore")

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs)

    return ""


# -------- Analyze --------
if st.button("Analyze"):
    if not uploaded_files:
        st.warning("Please upload at least one resume")
    elif not job_description.strip():
        st.warning("Please paste job description")
    else:
        st.subheader("Results")

        for file in uploaded_files:
            resume_text = extract_text(file)  # ✅ NOW DEFINED

            response = requests.post(
                "http://127.0.0.1:8000/match",
                json={
                    "resume_text": resume_text,
                    "job_description": job_description
                }
            )

            if response.status_code == 200:
                st.write(f"### {file.name}")
                st.json(response.json())
            else:
                st.error("Backend error")
