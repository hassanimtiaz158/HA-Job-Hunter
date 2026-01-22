from groq import Groq
import os

client = Groq(api_key=os.getenv("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"))

def explain_match(result: dict) -> str:
    prompt = f"""
You are an AI career assistant.

Match Score: {result['match_score']}%
Matched Skills: {result['matched_skills']}
Missing Skills: {result['missing_skills']}
Additional Skills: {result['your_additional_skills']}

Explain the result clearly and give improvement advice.
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
