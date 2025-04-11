from crewai import Task

def restaurant_task(agent, location):
    return Task(
        description=f"List the best local food spots and restaurants in {location}",
        expected_output="Top restaurants and food options with reviews",
        agent=agent
    )
