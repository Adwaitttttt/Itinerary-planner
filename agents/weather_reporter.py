from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

weather_agent = Agent(
    role='Weather Analyst',
    goal='Provide current weather and forecast',
    backstory='You have access to weather APIs and give real-time updates.',
    allow_delegation=False,
    verbose=True
)
