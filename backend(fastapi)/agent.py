import os
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from matcher import match_score

# 🔐 SET YOUR GROQ API KEY
os.environ["GROQ_API_KEY"] = "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"

# -------- Initialize GROQ LLM --------
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0
)

# -------- Prompt --------
prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template="""
You are an AI job assistant.

Resume:
{resume}

Job Description:
{job}

First, analyze skill match.
Then give:
1. Match score
2. Missing skills
3. Suggestions to improve resume
"""
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

# -------- Main function used by FastAPI --------
def run_agent(resume_text: str, job_description: str):
    rule_based = match_score(resume_text, job_description)

    llm_response = llm_chain.run({
        "resume": resume_text,
        "job": job_description
    })

    return {
        "rule_based_result": rule_based,
        "llm_analysis": llm_response
    }
