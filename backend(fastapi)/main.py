from fastapi import FastAPI
from pydantic import BaseModel
from matcher import match_score

app = FastAPI(title="HA-JobHunter Backend")

# -------- Request Schema --------
class MatchRequest(BaseModel):
    resume_text: str
    job_description: str

# -------- Match Endpoint --------
@app.post("/match")
def match(request: MatchRequest):
    # Call matcher function
    result = match_score(request.resume_text, request.job_description)

    # Return only concise match info
    return {"result": result}

# -------- Root Endpoint --------
@app.get("/")
def root():
    return {"message": "HA-JobHunter Backend is running"}
