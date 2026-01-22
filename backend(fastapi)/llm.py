from groq import Groq
import os

client = Groq(
    api_key=os.getenv("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")
)

def explain_match(match_result: dict) -> str:
    prompt = f"""
You are an AI career assistant.

Given this resume–job match result, explain it clearly in simple human language.

Match Score: {match_result['match_score']}%

Matched Skills: {', '.join(match_result['matched_skills'])}
Missing Skills: {', '.join(match_result['missing_skills'])}
Additional Skills: {', '.join(match_result['your_additional_skills'])}

Give:
1. A short summary
2. Why the score is this
3. How the candidate can improve
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # ✅ FIXED MODEL
        messages=[
            {"role": "system", "content": "You are a helpful job matching assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.4,
        max_tokens=300
    )

    return response.choices[0].message.content
