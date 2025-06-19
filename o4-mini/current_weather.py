# main.py
from fastapi import FastAPI, HTTPException, Query
import requests

app = FastAPI(
    title="Atmospheric Measurements API",
    description="Fetches hourly atmospheric data from api.open-meteo.com",
    version="0.1.0",
)

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


@app.get("/atmosphere")
def get_atmospheric_measurements(
    latitude: float = Query(..., ge=-90.0, le=90.0, description="Latitude in degrees"),
    longitude: float = Query(..., ge=-180.0, le=180.0, description="Longitude in degrees"),
    hourly: str = Query(
        "temperature_2m,relativehumidity_2m,pressure_msl,wind_speed_10m",
        description="Comma-separated list of hourly variables to fetch"
    ),
):
    """
    Fetch hourly atmospheric measurements for a given location.

    - **latitude**: Latitude in decimal degrees (−90 to 90)  
    - **longitude**: Longitude in decimal degrees (−180 to 180)  
    - **hourly**: Comma-separated list of variables (e.g. temperature_2m)
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": hourly,
        "timezone": "UTC",
    }
    try:
        resp = requests.get(OPEN_METEO_URL, params=params, timeout=10)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"Upstream error: {e}")

    return resp.json()
