"""
main.py
--------

FastAPI micro‑service exposing an **/atmospheric** endpoint that proxies the
**Open‑Meteo** Forecast API (https://api.open-meteo.com). It lets internal
clients retrieve atmospheric measurements (temperature, pressure, humidity,
etc.) without worrying about CORS, API evolutions, or outbound‑traffic rules.

Quick start
===========

1. **Install dependencies**

   ```bash
   python -m pip install --upgrade fastapi uvicorn httpx
   ```

2. **Run the application**

   ```bash
   uvicorn main:app --reload
   ```

3. **Query example**

   ```text
   http://127.0.0.1:8000/atmospheric
       ?latitude=45.5
       &longitude=-73.6
       &hourly=temperature_2m,pressure_msl
   ```

Notes
-----
* All query parameters map 1‑to‑1 to Open‑Meteo's own API.
* Requests are performed asynchronously with a 10 s upstream timeout.
* Upstream failures are surfaced as **502 Bad Gateway**.
"""

from __future__ import annotations

from typing import List, Optional

import httpx
from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Atmospheric Measurements API", version="0.2.0")

OPEN_METEO_BASE_URL = "https://api.open-meteo.com/v1/forecast"


@app.get(
    "/atmospheric",
    response_class=JSONResponse,
    tags=["Atmospheric Data"],
    summary="Atmospheric measurements proxy",
    description="Retrieve temperature, pressure, humidity and other hourly "
    "variables from the Open‑Meteo Forecast API.",
)
async def get_atmospheric(
    latitude: float = Query(
        ..., ge=-90, le=90, description="Latitude in decimal degrees (−90 … 90)"
    ),
    longitude: float = Query(
        ..., ge=-180, le=180, description="Longitude in decimal degrees (−180 … 180)"
    ),
    hourly: Optional[List[str]] = Query(
        None,
        description=(
            "Comma‑separated list of hourly variables supported by Open‑Meteo, "
            "e.g. temperature_2m, relativehumidity_2m, pressure_msl"
        ),
    ),
    start_date: Optional[str] = Query(
        None,
        regex=r"^\d{4}-\d{2}-\d{2}$",
        description="First calendar date to include (YYYY‑MM‑DD)",
    ),
    end_date: Optional[str] = Query(
        None,
        regex=r"^\d{4}-\d{2}-\d{2}$",
        description="Last calendar date to include (YYYY‑MM‑DD)",
    ),
):
    """Proxy the Open‑Meteo Forecast API and return its JSON payload.

    Parameters
    ----------
    latitude : float
        Latitude in decimal degrees (−90 … 90).
    longitude : float
        Longitude in decimal degrees (−180 … 180).
    hourly : list[str] | None
        One or more hourly variables such as ``temperature_2m`` or
        ``pressure_msl`` (see Open‑Meteo docs). If omitted, Open‑Meteo’s
        defaults are returned.
    start_date, end_date : str | None
        ISO‑8601 date strings in *YYYY‑MM‑DD* format delimiting the forecast
        range.

    Returns
    -------
    fastapi.responses.JSONResponse
        The raw JSON returned by Open‑Meteo.

    Raises
    ------
    fastapi.HTTPException
        *502 Bad Gateway* when Open‑Meteo fails or times out.
    """

    params: dict[str, str | float] = {
        "latitude": latitude,
        "longitude": longitude,
    }

    if hourly:
        params["hourly"] = ",".join(hourly)
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date

    async with httpx.AsyncClient(timeout=10) as client:
        try:
            response = await client.get(OPEN_METEO_BASE_URL, params=params)
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Upstream Open‑Meteo returned {exc.response.status_code}",
            ) from exc
        except httpx.RequestError as exc:
            raise HTTPException(status_code=502, detail=str(exc)) from exc

    return JSONResponse(response.json())
