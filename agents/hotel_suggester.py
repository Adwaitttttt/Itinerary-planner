from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

hotel_agent = Agent(
    role='Hotel Suggester',
    goal='Recommend best hotel options based on budget and location',
    backstory='You have access to hotel databases and user reviews to suggest ideal accommodations.',
    allow_delegation=False,
    verbose=True
)
