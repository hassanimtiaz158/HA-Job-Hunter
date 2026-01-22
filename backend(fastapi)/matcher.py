import re
from sentence_transformers import SentenceTransformer, util


SKILL_DB = [
    "python", "java", "c", "c++", "c#", "go", "rust", "swift",
    "kotlin", "javascript", "typescript", "php", "ruby",
    "html", "css", "bootstrap", "tailwind css",
    "react", "next.js", "vue", "angular",
    "fastapi", "django", "flask", "spring boot",
    "node.js", "express.js",
    "sql", "mysql", "postgresql", "mongodb", "redis",
    "machine learning", "deep learning",
    "tensorflow", "pytorch", "scikit-learn",
    "nlp", "langchain", "langgraph",
    "docker", "kubernetes", "aws", "azure", "gcp",
    "git", "github", "streamlit", "postman"
]


def clean_text(text: str) -> str:
    text = text.lower().replace("\n", " ")
    text = " ".join(text.split())
    return re.sub(r"[^a-z0-9\s\+\#\.\-]", "", text)


def extract_skills(text: str) -> list:
    return [
        skill for skill in SKILL_DB
        if re.search(r"\b" + re.escape(skill) + r"\b", text)
    ]



_model = None

def get_model():
    global _model
    if _model is None:
        print("🔹 Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
    return _model



def match_score(resume_text: str, job_description: str) -> dict:
    model = get_model()   

    resume_clean = clean_text(resume_text)
    jobd_clean = clean_text(job_description)

    resume_embedding = model.encode(resume_clean, convert_to_tensor=True)
    jobd_embedding = model.encode(jobd_clean, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jobd_embedding).item()

    resume_skills = set(extract_skills(resume_clean))
    jobd_skills = set(extract_skills(jobd_clean))

    return {
        "match_score": round(similarity * 100, 2),
        "matched_skills": sorted(resume_skills & jobd_skills),
        "missing_skills": sorted(jobd_skills - resume_skills),
        "your_additional_skills": sorted(resume_skills - jobd_skills)
    }
