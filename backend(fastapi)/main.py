from fastapi import FastAPI
from pydantic import BaseModel
from matcher import match_score

app=FastAPI(title="HA-JobHunter Backend",
            description="Resume/Job Description Matcher API",
            version="1.0.0"
)

class matchrequest(BaseModel):
    resume_text:str
    job_description:str

@app.post("/match")
def match(data:matchrequest):
    result=match_score(
    resume_text=data.resume_text,
    job_description=data.job_description
    )
    return result