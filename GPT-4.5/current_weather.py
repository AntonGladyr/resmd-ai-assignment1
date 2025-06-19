# Atmospheric Measurements API Endpoint
# This Flask application fetches atmospheric data (temperature, windspeed, winddirection, weathercode)
# from the Open-Meteo API based on provided latitude and longitude.

from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Define endpoint '/atmospheric' for fetching atmospheric data
@app.route('/atmospheric', methods=['GET'])
def fetch_atmospheric_measurements():
    # Get latitude and longitude from request parameters with default values
    latitude = request.args.get('latitude', default='45.50', type=str)
    longitude = request.args.get('longitude', default='-73.57', type=str)

    # Construct the API URL with provided coordinates
    api_url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true'

    # Make a GET request to the Open-Meteo API
    response = requests.get(api_url)

    # If the request is successful, extract and return atmospheric data
    if response.status_code == 200:
        data = response.json()
        atmospheric_data = {
            "temperature": data['current_weather']['temperature'],
            "windspeed": data['current_weather']['windspeed'],
            "winddirection": data['current_weather']['winddirection'],
            "weathercode": data['current_weather']['weathercode']
        }
        return jsonify(atmospheric_data), 200
    else:
        # Return error message if the request failed
        return jsonify({"error": "Failed to retrieve data from Open-Meteo"}), response.status_code

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
