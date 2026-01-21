import re
from sentence_transformers import SentenceTransformer, util

# ---------------- Skill Database ----------------
SKILL_DB = [
    # Programming
    "python", "java", "c", "c++", "c#", "go", "rust", "swift",
    "kotlin", "javascript", "typescript", "php", "ruby",

    # Web
    "html", "css", "bootstrap", "tailwind css",
    "react", "next.js", "vue", "angular",

    # Backend
    "fastapi", "django", "flask", "spring boot",
    "node.js", "express.js",

    # Databases
    "sql", "mysql", "postgresql", "mongodb", "redis",

    # AI / ML
    "machine learning", "deep learning",
    "tensorflow", "pytorch", "scikit-learn",
    "nlp", "langchain", "langgraph",

    # DevOps / Cloud
    "docker", "kubernetes", "aws", "azure", "gcp",

    # Tools
    "git", "github", "streamlit", "postman"
]

# ---------------- Text Cleaning ----------------
def clean_text(text: str) -> str:
    text = text.lower().replace("\n", " ")
    text = " ".join(text.split())
    text = re.sub(r"[^a-z0-9\s\+\#\.\-]", "", text)
    return text


# ---------------- Skill Extraction ----------------
def extract_skills(text: str) -> list:
    skills = []
    for skill in SKILL_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, text):
            skills.append(skill)
    return skills



# ---------------- Embedding Model ----------------
model = SentenceTransformer("all-MiniLM-L6-v2")


# ---------------- Resume Matching ----------------
def match_score(resume_text: str, job_desc: str) -> dict:
    resume_clean = clean_text(resume_text)
    jobd_clean = clean_text(job_desc)

    resume_embedding = model.encode(resume_clean, convert_to_tensor=True)
    jobd_embedding = model.encode(jobd_clean, convert_to_tensor=True)

    similarity = util.cos_sim(resume_embedding, jobd_embedding).item()

    resume_skills = set(extract_skills(resume_clean))
    jobd_skills = set(extract_skills(jobd_clean))

    return {
        "match_score": round(similarity * 100, 2),
        "matched_skills": sorted(resume_skills & jobd_skills),
        "missing_skills": sorted(jobd_skills - resume_skills)
    }


# ---------------- Local Test ----------------
#if __name__ == "__main__":
#    resume = "I am a Python developer. I use Git and Docker."
#    jd = "Need Python developer with AWS and Docker"
#    print(match_score(resume, jd))
