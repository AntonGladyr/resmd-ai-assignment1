# current_weather.py
# FastAPI endpoint for retrieving atmospheric measurements (temperature, humidity, pressure)
# from the Open-Meteo API for a given latitude and longitude.
# Uses asynchronous HTTP requests for efficient concurrent handling.

from fastapi import FastAPI, Query
import httpx

app = FastAPI()

@app.get("/atmospheric-measurements")
async def get_atmospheric_measurements(
    latitude: float = Query(..., description="Latitude of the location"),
    longitude: float = Query(..., description="Longitude of the location")
):
    """
    Retrieve atmospheric measurements (temperature, humidity, pressure) for a given location.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        dict: JSON response containing hourly temperature, relative humidity, and pressure data
              from the Open-Meteo API for the specified coordinates.
    """
    # Construct the Open-Meteo API URL with the provided latitude and longitude
    url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={latitude}&longitude={longitude}"
        "&hourly=temperature_2m,relative_humidity_2m,pressure_msl"
    )
    # Create an asynchronous HTTP client session
    async with httpx.AsyncClient() as client:
        # Send a GET request to the Open-Meteo API
        response = await client.get(url)
        # Raise an exception if the request was unsuccessful
        response.raise_for_status()
        # Parse the JSON response body
        data = response.json()
    # Return the parsed data to the client
    return data