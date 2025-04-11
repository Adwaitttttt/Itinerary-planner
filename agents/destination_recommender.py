from crewai import Agent
from dotenv import load_dotenv

load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"]="gpt-4o-mini"

destination_agent = Agent(
    role='Destination Expert',
    goal='Suggest tourist attractions and must-visit places',
    backstory='You are an experienced travel guide and expert in crafting trip destinations.',
    allow_delegation=False,
    verbose=True
)
