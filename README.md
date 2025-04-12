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
itinerary-planner/
├── agents/
│   ├── destination_recommender.py    # Agent for suggesting travel destinations
│   ├── hotel_suggester.py           # Agent for finding accommodations
│   ├── restaurant_finder.py         # Agent for recommending restaurants
│   ├── weather_reporter.py          # Agent for weather information
│   └── itinerary_builder.py         # Agent for creating final itinerary
├── tasks/
│   ├── destination_task.py          # Task for destination recommendations
│   ├── hotel_task.py               # Task for hotel suggestions
│   ├── restaurant_task.py          # Task for restaurant recommendations
│   ├── weather_task.py             # Task for weather information
│   └── itinerary_task.py           # Task for itinerary creation
├── app.py                          # Main application entry point
├── crew.py                         # Crew creation and management
├── main.ipynb                      # Jupyter notebook for interactive development and testing
├── requirements.txt                # Project dependencies
└── README.md                       # Project documentation
```

## Prerequisites

- Python 3.11 or higher
- OpenAI API key
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Change to the project directory:
```bash
cd Itinerary-Planner
```

3. Create and activate a virtual environment (recommended):
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/MacOS
python -m venv venv
source venv/bin/activate
```

4. Install the required dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Running the Application

1. Make sure your virtual environment is activated and you have set up your `.env` file.

2. You can run the application in two ways:

   a. Using the Python script:
   ```bash
   python app.py
   ```

   b. Using the Jupyter Notebook:
   ```bash
   jupyter notebook
   ```
   Then open `main.ipynb` for an interactive development experience.

3. The application will use the default location (Goa) and duration (5 days). To modify these:
   - In `app.py`:
   ```python
   location = "Your Destination"  # Change this to your desired location
   days = 7  # Change this to your desired number of days
   ```
   - In `main.ipynb`, you can modify these parameters in the notebook cells

### Interactive Development with Jupyter Notebook

The `main.ipynb` file provides an interactive environment for:
- Testing individual agents and tasks
- Visualizing the workflow
- Experimenting with different parameters
- Debugging and development
- Step-by-step execution of the itinerary planning process

## Components

### Agents

- **Destination Recommender**: Suggests travel destinations and must-visit places
- **Hotel Suggester**: Finds suitable accommodations based on budget and location
- **Restaurant Finder**: Recommends local dining options and hidden gems
- **Weather Reporter**: Provides current weather and forecast information
- **Itinerary Builder**: Creates the final comprehensive travel plan

### Tasks

Each agent has a corresponding task that defines its specific responsibilities:
- Destination Task: Lists tourist attractions and experiences
- Hotel Task: Finds hotels with good ratings and moderate pricing
- Restaurant Task: Lists best local food spots and restaurants
- Weather Task: Provides current weather and forecast
- Itinerary Task: Compiles all information into a detailed travel plan

## Dependencies

- crewai: Framework for creating AI agents
- crewai_tools: Additional tools for CrewAI
- load_dotenv: Environment variable management
- openai: OpenAI API integration
- ipykernel: Jupyter kernel for Python

## How It Works

1. The application creates a crew of specialized AI agents
2. Each agent is assigned a specific task related to travel planning
3. Agents work together to gather and process information
4. The final itinerary is compiled and presented to the user

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. When contributing:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please open an issue in the GitHub repository or contact the maintainers.

## Acknowledgments

- CrewAI for providing the framework
- OpenAI for the language models
- All contributors who have helped improve this project