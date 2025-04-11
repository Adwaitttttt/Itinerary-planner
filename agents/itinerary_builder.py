from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

itinerary_agent = Agent(
    role='Itinerary Planner',
    goal='Create a travel plan combining all info',
    backstory='You are an expert in creating optimized and personalized itineraries.',
    allow_delegation=True,
    verbose=True
)
