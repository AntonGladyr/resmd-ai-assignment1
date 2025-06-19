## Atmospheric Measurements API

This project provides a simple HTTP API to fetch hourly atmospheric measurements (temperature, humidity, pressure, wind speed, etc.) from the [Open-Meteo](https://api.open-meteo.com) service.

### Features

* Fetch hourly variables by latitude and longitude
* Configurable list of atmospheric measurements
* Graceful error handling for upstream failures

---

## Prerequisites

* Python 3.8 or newer installed
* `pip` for installing Python packages

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/atmosphere-api.git
   cd atmosphere-api
   ```

2. **Create (and activate) a virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

All configuration is done via query parameters on the endpoint. No additional setup or API keys are required for the free tier of Open-Meteo.

---

## Running the Server

Start the FastAPI application using `uvicorn`:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

* `--reload` enables auto-reload on code changes
* `--host 0.0.0.0` makes the server available on your network
* `--port 8000` sets the listening port

---

## API Usage

### Endpoint

```
GET /atmosphere
```

**Query Parameters**:

| Parameter | Type   | Required | Description                                                                                                          |
| --------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------- |
| latitude  | float  | Yes      | Latitude in decimal degrees (between -90 and 90)                                                                     |
| longitude | float  | Yes      | Longitude in decimal degrees (between -180 and 180)                                                                  |
| hourly    | string | No       | Comma-separated list of hourly variables (default: `temperature_2m,relativehumidity_2m,pressure_msl,wind_speed_10m`) |
| timezone  | string | No       | Timezone for returned timestamps (default: `UTC`)                                                                    |

### Example Request

```bash
curl "http://127.0.0.1:8000/atmosphere?latitude=45.50&longitude=-73.57"
```

### Example Response

```json
{
  "latitude": 45.5,
  "longitude": -73.57,
  "generationtime_ms": 0.123,
  "utc_offset_seconds": 0,
  "timezone": "UTC",
  "hourly": {
    "time": ["2025-06-19T00:00", "2025-06-19T01:00", ...],
    "temperature_2m": [18.5, 17.9, ...],
    "relativehumidity_2m": [72, 75, ...],
    "pressure_msl": [1012.3, 1012.1, ...],
    "wind_speed_10m": [3.4, 2.8, ...]
  }
}
```

---

## Extending the API

* **Add `start_date` / `end_date` parameters** to fetch historical or forecast ranges
* **Support `daily` or `minute` variables** by adding another query parameter
* **Implement response models** with Pydantic for strict schema validation
* **Switch to `httpx` and FastAPI's `async`** support for non-blocking I/O
* **Add caching** to avoid repeated upstream calls for the same parameters

---

## License

MIT License © 2025 Your Name
