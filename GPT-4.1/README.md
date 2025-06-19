# GPT-4.1 Atmospheric Measurements API

This project provides a FastAPI endpoint to retrieve atmospheric measurements (temperature, humidity, pressure) for a given latitude and longitude using the Open-Meteo API.

## Requirements
- Python 3.8+
- [httpx](https://www.python-httpx.org/)
- [fastapi](https://fastapi.tiangolo.com/)
- [uvicorn](https://www.uvicorn.org/)

## Installation
1. Clone this repository or copy the `GPT-4.1` folder to your project.
2. Install the required packages:

```bash
pip install fastapi httpx uvicorn
```

## Running the API
Navigate to the `GPT-4.1` directory and run:

```bash
uvicorn current_weather:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Usage
Send a GET request to `/atmospheric-measurements` with `latitude` and `longitude` query parameters. Example:

```
GET http://127.0.0.1:8000/atmospheric-measurements?latitude=45.0&longitude=-73.0
```

## Example Response
```
{
  "hourly": {
    "temperature_2m": [...],
    "relative_humidity_2m": [...],
    "pressure_msl": [...]
  },
  ...
}
```

## License
MIT
