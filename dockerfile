# Use Python 3.12 slim base image
FROM python:3.12.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies and rest of the application
COPY requirements.txt .
COPY agents/ ./agents/
COPY tasks/ ./tasks/
COPY templates/ ./templates/
COPY crew.py .
COPY itinerary_planner.py .
COPY .env .

#Install the python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask   
ENV FLASK_APP=itinerary_planner.py
ENV FLASK_ENV=production
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
