from crewai import Task

def itinerary_task(agent, days):
    return Task(
        description="Compile all findings into a neat and engaging {days} days itinerary",
        expected_output="Detailed travel plan day-by-day",
        agent=agent
    )