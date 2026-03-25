from crewai import Task
from agents import resume_screener_agent

resume_screening_task = Task(
    description=(
        "You are a strict JSON generator.\n"
        "You MUST return ONLY valid JSON.\n"
        "Do NOT include any text before or after JSON.\n\n"

        "Evaluate the candidate resume against the job description.\n\n"

        "Follow these steps strictly:\n"
        "1. Extract key required skills from the job description.\n"
        "2. Extract candidate skills from the resume.\n"
        "3. Compare overlap between required and candidate skills.\n"
        "4. Evaluate relevant experience.\n"
        "5. Assign a score (0–100) using:\n"
        "   - Skills match (50%)\n"
        "   - Experience relevance (30%)\n"
        "   - Education/other factors (20%)\n"
        "6. Based on score:\n"
        "   - 80+ → Strong Fit\n"
        "   - 50–79 → Moderate Fit\n"
        "   - <50 → Weak Fit\n\n"

        "Resume:\n{resume}\n\n"
        "Job Description:\n{job_description}\n\n"

        "Return ONLY this JSON format:\n"
        "{\n"
        '  "verdict": "Strong Fit | Moderate Fit | Weak Fit",\n'
        '  "score": number between 0 and 100,\n'
        '  "matched_skills": ["skill1", "skill2"],\n'
        '  "missing_skills": ["skill1", "skill2"],\n'
        '  "reason": "maximum 2 lines explanation"\n'
        "}"
    ),
    expected_output="Valid JSON only",
    agent=resume_screener_agent
)