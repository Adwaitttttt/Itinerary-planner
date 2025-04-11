# Itinerary Planner

A sophisticated AI-powered travel itinerary planner built using CrewAI. This application helps users create detailed travel plans by coordinating multiple specialized AI agents to handle different aspects of trip planning.

## Features

- **Destination Recommendations**: Get personalized destination suggestions based on your preferences
- **Hotel Suggestions**: Find suitable accommodations for your stay
- **Restaurant Recommendations**: Discover local dining options
- **Weather Information**: Get weather forecasts for your travel dates
- **Detailed Itinerary**: Receive a comprehensive day-by-day travel plan

## Project Structure

```
itenery-planner/
├── agents/
│   ├── destination_recommender.py
│   ├── hotel_suggester.py
│   ├── restaurant_finder.py
│   ├── weather_reporter.py
│   └── itinerary_builder.py
├── tasks/
│   ├── destination_task.py
│   ├── hotel_task.py
│   ├── restaurant_task.py
│   ├── weather_task.py
│   └── itinerary_task.py
├── main.py
├── crew.py
└── requirements.txt
```

## Prerequisites

- Python 3.8 or higher
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd itenery-planner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

Run the application using:
```bash
python main.py
```

The application will prompt you for:
- Destination location
- Number of days for your trip

## Components

### Agents
- **Destination Recommender**: Suggests travel destinations
- **Hotel Suggester**: Finds suitable accommodations
- **Restaurant Finder**: Recommends dining options
- **Weather Reporter**: Provides weather forecasts
- **Itinerary Builder**: Creates the final travel plan

### Tasks
Each agent has a corresponding task that defines its specific responsibilities and objectives.

## Dependencies

- crewai: Framework for creating AI agents
- crewai_tools: Additional tools for CrewAI
- load_dotenv: Environment variable management
- openai: OpenAI API integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.