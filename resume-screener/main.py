from crewai import Crew
from tasks import resume_screening_task
from pdf_utils import extract_text_from_pdf

crew = Crew(
    agents=[resume_screening_task.agent],
    tasks=[resume_screening_task]
)

# 👇 Give your PDF path here
resume_pdf_path = "resume.pdf"

# Extract text from PDF
resume_text = extract_text_from_pdf(resume_pdf_path)

# Job Description (keep as text for now)
job_description = """
Looking for a Python developer with Django, REST APIs,
Docker, and AWS experience. Minimum 3 years experience required.
"""

if not resume_text:
    print("❌ Could not extract text from PDF")
else:
    result = crew.kickoff(inputs={
        "resume": resume_text,
        "job_description": job_description
    })

    print("\nFinal Result:\n", result)