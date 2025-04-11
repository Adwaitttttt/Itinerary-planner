from crewai import Task

def weather_task(agent, location):
    return Task(
        description=f"Provide current weather in {location} and forecast",
        expected_output="Weather info in human-readable format",
        agent=agent
    )
