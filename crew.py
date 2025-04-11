from crewai import Crew
from agents.destination_recommender import destination_agent
from agents.hotel_suggester import hotel_agent
from agents.restaurant_finder import restaurant_agent
from agents.weather_reporter import weather_agent
from agents.itinerary_builder import itinerary_agent

from tasks.destination_task import destination_task
from tasks.hotel_task import hotel_task
from tasks.restaurant_task import restaurant_task
from tasks.weather_task import weather_task
from tasks.itinerary_task import itinerary_task

def create_crew(location, days):
    crew = Crew(
        agents=[
            destination_agent,
            hotel_agent,
            restaurant_agent,
            weather_agent,
            itinerary_agent
        ],
        tasks=[
            destination_task(destination_agent, location),
            hotel_task(hotel_agent, location),
            restaurant_task(restaurant_agent, location),
            weather_task(weather_agent, location),
            itinerary_task(itinerary_agent, days)
        ],
        verbose=True
    )
    return crew
