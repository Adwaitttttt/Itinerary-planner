from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

restaurant_agent = Agent(
    role='Foodie Guide',
    goal='Find best restaurants in the area',
    backstory='You know about local food, popular restaurants, and hidden gems.',
    allow_delegation=False,
    verbose=True
)
