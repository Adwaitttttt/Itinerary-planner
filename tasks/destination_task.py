from crewai import Task

def destination_task(agent, location):
    return Task(
        description=f"List the best tourist attractions and experiences in {location}",
        expected_output="A list of must-see destinations",
        agent=agent
    )
