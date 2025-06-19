````markdown
# Open-Meteo Flask API

A simple Flask API endpoint that fetches atmospheric measurements from the [Open-Meteo](https://open-meteo.com/) service.

## Overview

This API allows you to retrieve current and hourly weather data (temperature, precipitation, wind speed, etc.) for a specified latitude and longitude by proxying requests to the Open-Meteo API.

## Features

- Fetch current weather data
- Fetch hourly data for temperature, precipitation, and wind speed
- Automatic timezone adjustment based on location

## Requirements

- Python 3.7+
- Flask
- Requests

## Installation

1. Clone or download this repository (or save `app.py`).

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
````

3. Install dependencies:

   ```bash
   pip install flask requests
   ```

## Running the API

Run the Flask application with:

```bash
python app.py
```

By default, it will start on `http://127.0.0.1:5000`.

## Usage

Send a GET request to the `/weather` endpoint with `latitude` and `longitude` query parameters.

Example:

```bash
curl "http://127.0.0.1:5000/weather?latitude=52.52&longitude=13.41"
```

### Query Parameters

| Parameter | Description                         | Required |
| --------- | ----------------------------------- | -------- |
| latitude  | Latitude of the location (decimal)  | Yes      |
| longitude | Longitude of the location (decimal) | Yes      |

### Sample Response

```json
{
  "latitude": 52.52,
  "longitude": 13.41,
  "generationtime_ms": 0.2799034118652344,
  "utc_offset_seconds": 7200,
  "timezone": "Europe/Berlin",
  "timezone_abbreviation": "CEST",
  "elevation": 38.0,
  "current_weather": {
    "temperature": 15.3,
    "windspeed": 11.2,
    "winddirection": 210,
    "weathercode": 3,
    "time": "2025-06-19T16:00"
  },
  "hourly": {
    "time": [...],
    "temperature_2m": [...],
    "precipitation": [...],
    "windspeed_10m": [...]
  }
}
```

## Error Handling

* If either `latitude` or `longitude` is missing, the API returns HTTP 400 with an error message.
* If the Open-Meteo API request fails, the API returns HTTP 500 with error details.

## License

This project is provided as-is for educational purposes.

---

Feel free to customize or extend this API to suit your needs!

```
```
