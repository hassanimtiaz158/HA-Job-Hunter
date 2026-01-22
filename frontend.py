import streamlit as st
import requests
import pdfplumber
import docx

st.set_page_config(
    page_title="HA-JOBHunter",
    layout="centered"
)

st.title("HA-JOBHunter")
st.write("Job Hunting Using HA Agent with Resume Matching 🔎")

BACKEND_URL = "http://127.0.0.1:8000/match"

uploaded_files = st.file_uploader(
    "Upload Resume(s)",
    accept_multiple_files=True,
    type=["pdf", "txt", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    height=200,
    max_chars=50000
)


def extract_text(file):
    """Extract text from PDF / TXT / DOCX"""
    if file.type == "application/pdf":
        text = ""
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + " "
        return text.strip()

    elif file.type == "text/plain":
        return file.read().decode("utf-8", errors="ignore").strip()

    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        return " ".join(p.text for p in doc.paragraphs).strip()

    return ""


if st.button("Analyze 🔍"):

    if not uploaded_files:
        st.warning("Please upload at least one resume.")
        st.stop()

    if not job_description.strip():
        st.warning("Please paste a job description.")
        st.stop()

    with st.spinner("Analyzing resumes..."):
        for file in uploaded_files:

            resume_text = extract_text(file)

            if not resume_text:
                st.error(f"Could not read {file.name}")
                continue

            try:
                response = requests.post(
                    BACKEND_URL,
                    json={
                        "resume_text": resume_text,
                        "job_description": job_description
                    },
                    timeout=60
                )
                response.raise_for_status()  # Raise error for non-200 responses
            except requests.exceptions.RequestException as e:
                st.error(f"Backend error ❌: {e}")
                continue

            st.divider()
            st.subheader(file.name)

            data = response.json()
            match_result = data.get("result", {})

            # ---- Score ----
            st.metric(
                label="Match Score",
                value=f"{match_result.get('match_score', 0)} %"
            )

            # ---- Skills Columns ----
            col1, col2, col3 = st.columns(3)

            with col1:
                st.write("✅ **Matched Skills**")
                st.write(match_result.get("matched_skills", []) or "None")

            with col2:
                st.write("❌ **Missing Skills**")
                st.write(match_result.get("missing_skills", []) or "None")

            with col3:
                st.write("➕ **Your Extra Skills**")
                st.write(match_result.get("your_additional_skills", []) or "None")

            # ---- Optional Explanation ----
            explanation = match_result.get("explanation", "")
            if explanation:
                st.write("**Explanation (Short):**")
                st.write(explanation[:300] + "..." if len(explanation) > 300 else explanation)
