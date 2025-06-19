# Atmospheric Measurements API

A FastAPI service that fetches hourly atmospheric measurements (temperature, humidity, wind speed, etc.) from the [Open-Meteo API](https://open-meteo.com).

## Prerequisites

* **Python**: 3.8 or newer
* **Internet** connection to reach the Open-Meteo endpoints

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/atmospheric-measurements-api.git
   cd atmospheric-measurements-api
   ```

2. **Create and activate a virtual environment** (recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate       # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install --upgrade pip
   pip install fastapi httpx uvicorn
   ```

## Running the Server

Start the FastAPI application with Uvicorn:

```bash
uvicorn main:app --reload
```

* The `--reload` flag enables automatic restarts on code changes.
* By default, the server listens on `http://127.0.0.1:8000`.

To bind to a specific host or port:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8080
```

## Usage

### GET `/measurements`

Fetch hourly measurements for a given location and date range.

**Query Parameters**:

| Parameter    | Type   | Required | Description                                                                    |
| ------------ | ------ | -------- | ------------------------------------------------------------------------------ |
| `latitude`   | float  | yes      | Latitude of the location (e.g., `37.7749`)                                     |
| `longitude`  | float  | yes      | Longitude of the location (e.g., `-122.4194`)                                  |
| `start_date` | string | yes      | Start date in `YYYY-MM-DD` format (inclusive)                                  |
| `end_date`   | string | yes      | End date in `YYYY-MM-DD` format (inclusive)                                    |
| `hourly`     | string | yes      | Comma-separated list of variables (e.g., `temperature_2m,relativehumidity_2m`) |

**Example Request**:

```bash
curl "http://127.0.0.1:8000/measurements?latitude=37.7749&longitude=-122.4194&start_date=2025-06-01&end_date=2025-06-02&hourly=temperature_2m,relativehumidity_2m"
```

**Sample Response** (abridged):

```json
{
  "latitude": 37.7749,
  "longitude": -122.4194,
  "generationtime_ms": 12.3,
  "utc_offset_seconds": 0,
  "hourly": {
    "time": ["2025-06-01T00:00", "2025-06-01T01:00", …],
    "temperature_2m": [13.4, 13.1, …],
    "relativehumidity_2m": [82, 84, …]
  }
}
```

## Project Structure

```
atmospheric-measurements-api/
├── main.py            # FastAPI application
├── README.md          # This file
├── requirements.txt   # (optional) pinned dependencies
└── example.env        # Sample environment variables
```

## Development & Testing

* **Modify** `main.py` to add new endpoints or parameters.
* **Testing**: Add `pytest` tests under a `tests/` directory.
* **Linting**: Use `black`, `flake8`, or similar tools for code style.

## License

MIT © Your Name
