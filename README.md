# AI-Powered Travel Itinerary Planner

A sophisticated AI-powered travel itinerary planner built using CrewAI and Flask. This application helps users create detailed travel plans by coordinating multiple specialized AI agents to handle different aspects of trip planning.

## 🌟 Features

- **Destination Recommendations**: Get personalized destination suggestions based on your preferences
- **Hotel Suggestions**: Find suitable accommodations for your stay
- **Restaurant Recommendations**: Discover local dining options
- **Weather Information**: Get weather forecasts for your travel dates
- **Detailed Itinerary**: Receive a comprehensive day-by-day travel plan
- **Web Interface**: User-friendly web interface for easy interaction
- **Docker Support**: Easy deployment using Docker containers

## 🏗️ Project Structure

```
itinerary-planner/
├── agents/                      # AI Agents for different planning aspects
│   ├── destination_recommender.py    # Agent for suggesting travel destinations
│   ├── hotel_suggester.py           # Agent for finding accommodations
│   ├── restaurant_finder.py         # Agent for recommending restaurants
│   ├── weather_reporter.py          # Agent for weather information
│   └── itinerary_builder.py         # Agent for creating final itinerary
├── tasks/                        # Tasks assigned to each agent
│   ├── destination_task.py          # Task for destination recommendations
│   ├── hotel_task.py               # Task for hotel suggestions
│   ├── restaurant_task.py          # Task for restaurant recommendations
│   ├── weather_task.py             # Task for weather information
│   └── itinerary_task.py           # Task for itinerary creation
├── templates/                    # Web interface templates
│   └── index.html                # Main web interface
├── crew.py                      # Crew creation and management
├── itinerary_planner.py         # Flask application entry point
├── requirements.txt             # Project dependencies
├── dockerfile                   # Docker configuration
└── README.md                    # Project documentation
```

## 📋 Prerequisites

- Python 3.12 or higher
- OpenAI API key
- pip (Python package installer)
- Docker (optional, for containerized deployment)

## 🚀 Installation

### Option 1: Local Installation

1. Clone the repository:
```bash
git clone <repository-url>
```

2. Change to the project directory:
```bash
cd Itinerary-Planner
```

3. Create and activate a virtual environment:
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

### Option 2: Docker Installation

1. Build the Docker image:
```bash
docker build -t itinerary-planner .
```

2. Run the container:
```bash
docker run -p 5000:5000 -e OPENAI_API_KEY=your_api_key_here itinerary-planner
```

## 💻 Usage

### Running the Application

1. Make sure your virtual environment is activated and you have set up your `.env` file.

2. Start the Flask application:
```bash
python itinerary_planner.py
```

3. Access the web interface at `http://localhost:5000`

### Web Interface

The web interface provides a user-friendly way to:
- Enter your desired destination
- Specify the number of days for your trip
- Generate a comprehensive travel plan
- View detailed itinerary with all recommendations

## 🔧 Components

### Agents

1. **Destination Recommender**
   - Role: Expert travel guide
   - Goal: Suggest tourist attractions and must-visit places
   - Capabilities: Knowledge of popular destinations, local attractions, and cultural experiences

2. **Hotel Suggester**
   - Role: Accommodation specialist
   - Goal: Find suitable hotels based on budget and location
   - Capabilities: Access to hotel databases and user reviews

3. **Restaurant Finder**
   - Role: Food and dining expert
   - Goal: Recommend local restaurants and food spots
   - Capabilities: Knowledge of local cuisine and popular dining options

4. **Weather Reporter**
   - Role: Weather analyst
   - Goal: Provide current weather and forecast information
   - Capabilities: Access to weather APIs and real-time updates

5. **Itinerary Builder**
   - Role: Travel planner
   - Goal: Create optimized travel plans
   - Capabilities: Combines all information into a cohesive itinerary

### Tasks

Each agent performs specific tasks:
1. **Destination Task**: Lists tourist attractions and experiences
2. **Hotel Task**: Finds hotels with good ratings and moderate pricing
3. **Restaurant Task**: Lists best local food spots and restaurants
4. **Weather Task**: Provides current weather and forecast
5. **Itinerary Task**: Compiles all information into a detailed travel plan

## 📦 Dependencies

- **crewai**: Framework for creating AI agents
- **crewai_tools**: Additional tools for CrewAI
- **load_dotenv**: Environment variable management
- **openai**: OpenAI API integration
- **flask**: Web framework for the user interface

## 🔄 How It Works

1. **User Input**: User provides destination and trip duration through the web interface
2. **Agent Coordination**: The system creates a crew of specialized AI agents
3. **Task Execution**: Each agent performs its specific task:
   - Destination agent suggests places to visit
   - Hotel agent finds accommodations
   - Restaurant agent recommends dining options
   - Weather agent provides forecast
4. **Itinerary Creation**: The itinerary builder combines all information
5. **Result Presentation**: The final itinerary is displayed to the user

## 🐳 Docker Deployment

The application can be easily deployed using Docker:

1. Build the image:
```bash
docker build -t itinerary-planner .
```

2. Run the container:
```bash
docker run -p 5000:5000 -e OPENAI_API_KEY=your_api_key_here itinerary-planner
```

3. Access the application at `http://localhost:5000`

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💬 Support

For support, please:
- Open an issue in the GitHub repository
- Contact the maintainers
- Check the documentation for common issues

## 🙏 Acknowledgments

- CrewAI for providing the framework
- OpenAI for the language models
- All contributors who have helped improve this project