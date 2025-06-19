"""
app.py - Simple Flask API to fetch atmospheric measurements from Open-Meteo

This API provides current and hourly weather data for a given latitude and longitude
by querying the open-meteo.com public API.

Usage:
    Start the Flask app and make a GET request to /weather endpoint with
    'latitude' and 'longitude' query parameters.

Example:
    GET /weather?latitude=52.52&longitude=13.41

Dependencies:
    - Flask
    - requests
"""

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/weather', methods=['GET'])
def get_weather():
    """
    Endpoint to fetch atmospheric measurements from Open-Meteo API.

    Query Parameters:
        latitude (str): Latitude of the location (required)
        longitude (str): Longitude of the location (required)

    Returns:
        JSON response with weather data or error message.
    """
    # Retrieve latitude and longitude from query parameters
    lat = request.args.get('latitude')
    lon = request.args.get('longitude')

    # Validate required parameters
    if not lat or not lon:
        return jsonify({"error": "Please provide latitude and longitude query parameters."}), 400

    # Open-Meteo API endpoint
    url = 'https://api.open-meteo.com/v1/forecast'

    # Parameters for the Open-Meteo API request
    params = {
        'latitude': lat,
        'longitude': lon,
        'current_weather': True,                    # Include current weather data
        'hourly': 'temperature_2m,precipitation,windspeed_10m',  # Requested hourly data parameters
        'timezone': 'auto'                          # Automatically adjust timezone based on location
    }

    try:
        # Make a GET request to the Open-Meteo API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse JSON data from response
        data = response.json()

        # Return the weather data as JSON response
        return jsonify(data)

    except requests.RequestException as e:
        # Handle request exceptions and return error response
        return jsonify({
            "error": "Failed to fetch data from Open-Meteo API",
            "details": str(e)
        }), 500

if __name__ == '__main__':
    # Run the Flask app in debug mode (only for development)
    app.run(debug=True)
