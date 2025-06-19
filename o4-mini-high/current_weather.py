from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel, Field
import httpx

app = FastAPI()

class MeasurementParams(BaseModel):
    latitude: float = Field(..., description="Latitude in decimal degrees")
    longitude: float = Field(..., description="Longitude in decimal degrees")
    start_date: str = Field(..., regex=r"^\d{4}-\d{2}-\d{2}$", description="Start date in YYYY-MM-DD format")
    end_date: str = Field(..., regex=r"^\d{4}-\d{2}-\d{2}$", description="End date in YYYY-MM-DD format")
    hourly: str = Field("temperature_2m", description="Hourly parameter to fetch, e.g., temperature_2m, relativehumidity_2m")

@app.get("/measurements")
async def get_measurements(
    latitude: float = Query(..., description="Latitude in decimal degrees"),
    longitude: float = Query(..., description="Longitude in decimal degrees"),
    start_date: str = Query(..., regex=r"^\d{4}-\d{2}-\d{2}$", description="Start date in YYYY-MM-DD"),
    end_date: str = Query(..., regex=r"^\d{4}-\d{2}-\d{2}$", description="End date in YYYY-MM-DD"),
    hourly: str = Query("temperature_2m", description="Hourly variable to retrieve")
):
    """
    Fetch atmospheric measurements from Open-Meteo API based on provided parameters.

    - **latitude**: decimal degrees.
    - **longitude**: decimal degrees.
    - **start_date**, **end_date**: date range in YYYY-MM-DD.
    - **hourly**: variable to fetch (e.g., temperature_2m).

    Returns the JSON response from Open-Meteo or an error if the request fails.
    """
    base_url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": hourly,
        "timezone": "UTC"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(base_url, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code,
                                detail=f"Open-Meteo API error: {exc.response.text}")
        except httpx.RequestError as exc:
            raise HTTPException(status_code=502, detail=f"Network error: {exc}")

    return response.json()

# To run: uvicorn main:app --reload
