"""
weather_api.py

This module implements a FastAPI application with an endpoint that retrieves atmospheric
measurements from the Open-Meteo API. It allows clients to specify geographic coordinates
(latitude and longitude) and returns current temperature, relative humidity, and surface pressure.

Dependencies:
- FastAPI
- httpx
- uvicorn

Run the server:
    uvicorn weather_api:app --reload

Example request:
    GET /weather?latitude=45.5&longitude=-73.6
"""

from fastapi import FastAPI, Query, HTTPException
import httpx

app = FastAPI()

@app.get("/weather")
async def get_weather(
    latitude: float = Query(..., ge=-90.0, le=90.0, description="Latitude of the location (-90 to 90)"),
    longitude: float = Query(..., ge=-180.0, le=180.0, description="Longitude of the location (-180 to 180)")
):
    """
    Retrieve current atmospheric measurements for a specified location.

    Parameters:
    - latitude (float): Latitude of the target location.
    - longitude (float): Longitude of the target location.

    Returns:
    - JSON object containing latitude, longitude, and current weather measurements including:
        - temperature_2m: Temperature at 2 meters above ground (°C)
        - relative_humidity_2m: Relative humidity at 2 meters above ground (%)
        - surface_pressure: Surface pressure (hPa)

    Raises:
    - HTTPException: If the Open-Meteo API returns an error or the request fails.
    """
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude={lat}&longitude={lon}"
        "&current=temperature_2m,relative_humidity_2m,surface_pressure"
    ).format(lat=latitude, lon=longitude)

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            return {
                "latitude": data.get("latitude"),
                "longitude": data.get("longitude"),
                "current_weather": data.get("current")
            }
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail="Error from Open-Meteo API")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
