import streamlit as st

st.set_page_config(page_title="HA-JOBHunter")
st.title("HA-JOBHunter")
st.write("Job Hunting Using HA Agent with Resume Matching 🔎")


file_upload = st.file_uploader(
    "Upload Resume(s)",
    accept_multiple_files=True,
    type=["pdf", "txt", "docx"]
)

job_description = st.text_area(
    "Paste Job Description",
    max_chars=50000
)

button=st.button("Analyze")
if button:
    st.write("Analyzing.......")


