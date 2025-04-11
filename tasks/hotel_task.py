from crewai import Task

def hotel_task(agent, location):
    return Task(
        description=f"Find hotels in {location} with good ratings and moderate pricing",
        expected_output="A list of hotel suggestions with short descriptions",
        agent=agent
    )
