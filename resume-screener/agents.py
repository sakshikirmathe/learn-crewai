import os
from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

llm = LLM(
    model="openrouter/stepfun/step-3.5-flash:free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    temperature=0.2
)

resume_screener_agent = Agent(
    role="Resume Screening Expert",
    goal="Evaluate candidate resumes against job descriptions and determine fit accurately",
    backstory=(
        "You are a highly experienced technical recruiter. "
        "You strictly follow evaluation rules and always return valid JSON output. "
        "If output is not valid JSON, the system will fail."
    ),
    llm=llm,
    verbose=True
)