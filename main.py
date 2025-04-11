from crew import create_crew

if __name__ == "__main__":
    location = "Goa"
    days = 5
    travel_crew = create_crew(location, days)
    result = travel_crew.kickoff()
    print("\n\n🧳 Final Itinerary:\n")
    print(result)
