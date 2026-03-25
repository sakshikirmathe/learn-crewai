from crewai import Crew
from tasks import resume_screening_task

crew = Crew(
    agents=[resume_screening_task.agent],
    tasks=[resume_screening_task]
)

# Example Resume
resume = """
Python developer with 2 years experience.
Worked with Django, REST APIs, MySQL.
Basic knowledge of Docker.
"""

# Example Job Description
job_description = """
Looking for a Python developer with Django, REST APIs,
Docker, and AWS experience. Minimum 3 years experience required.
"""

result = crew.kickoff(inputs={
    "resume": resume,
    "job_description": job_description
})

print("\nFinal Result:\n", result)