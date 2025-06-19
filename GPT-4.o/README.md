# Weather API

This is a simple FastAPI application that provides an HTTP endpoint to fetch current atmospheric measurements (temperature, humidity, and surface pressure) using the [Open-Meteo API](https://open-meteo.com/).

## Features

* Fetch current weather data for any location on Earth
* Returns temperature, relative humidity, and surface pressure
* Based on real-time data from Open-Meteo

## Requirements

* Python 3.8+

## Installation

1. **Clone the repository or download the script:**

```bash
mkdir weather-api
cd weather-api
touch weather_api.py  # or place the script here
```

2. **Create and activate a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install fastapi uvicorn httpx
```

## Running the API

Start the FastAPI server with Uvicorn:

```bash
uvicorn weather_api:app --reload
```

This will start the server at:

```
http://127.0.0.1:8000
```

## Example Request

You can access the `/weather` endpoint by providing latitude and longitude:

```
GET /weather?latitude=45.5&longitude=-73.6
```

Or open it in a browser:

```
http://127.0.0.1:8000/weather?latitude=45.5&longitude=-73.6
```

### Sample Response

```json
{
  "latitude": 45.5,
  "longitude": -73.6,
  "current_weather": {
    "temperature_2m": 23.1,
    "relative_humidity_2m": 61,
    "surface_pressure": 1013.2
  }
}
```

## Interactive Docs

FastAPI automatically provides interactive API documentation:

* Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## License

This project is open-source and free to use.
