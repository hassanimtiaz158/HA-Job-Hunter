from langchain.tools import tool
from matcher import match_score

@tool
def match_score_tool(resume_text: str, job_description: str) -> str:
    result = match_score(resume_text, job_description)
    summary = (
        f"Match Score: {result['match_score']}%\n"
        f"Matched Skills: {', '.join(result['matched_skills'])}\n"
        f"Missing Skills: {', '.join(result['missing_skills'])}\n"
        f"Your Additional Skills: {', '.join(result['your_additional_skills'])}"
    )
    return summary
