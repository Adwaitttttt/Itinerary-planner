from flask import Flask, render_template, request, jsonify
from crew import create_crew
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_itinerary', methods=['POST'])
def generate_itinerary():
    try:
        data = request.get_json()
        location = data.get('location', 'Goa')
        days = int(data.get('days', 5))
        
        # Create and run the crew
        travel_crew = create_crew(location, days)
        result = travel_crew.kickoff()
        
        # Convert CrewOutput to string
        itinerary_text = str(result)
        
        return jsonify({
            'success': True,
            'itinerary': itinerary_text
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Create templates directory if it doesn't exist
    os.makedirs('templates', exist_ok=True)
    app.run(debug=True, port = 5000) 