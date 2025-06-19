# Atmospheric Measurements Proxy API

This repository contains a **FastAPI** micro‑service that exposes a single endpoint, `/atmospheric`, which proxies the [Open‑Meteo Forecast API](https://api.open-meteo.com). It lets your front‑end or other internal services fetch atmospheric measurements (temperature, pressure, humidity, etc.) without dealing with CORS, rate limits, or external network rules.

---

## Prerequisites

| Requirement           | Notes                                                               |
| --------------------- | ------------------------------------------------------------------- |
| **Python ≥ 3.9**      | Any recent CPython distribution works (CPython 3.9, 3.10, 3.11...). |
| **pip / venv**        | Recommended to isolate dependencies.                                |
| **(Optional) Docker** | A lightweight container recipe is provided below.                   |

---

## Installation

1. **Clone the repository** (or copy the two files `main.py` and `README.md` into a directory):

   ```bash
   git clone https://github.com/your‑org/atmospheric‑proxy.git
   cd atmospheric‑proxy
   ```

2. **Create and activate a virtual environment** *(optional but recommended)*:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install runtime dependencies**:

   ```bash
   python -m pip install --upgrade pip
   pip install fastapi uvicorn httpx
   ```

   > **Tip 🛈** Add `pip install "uvicorn[standard]"` for production‑grade extras like `uvloop` and `httptools`.

---

## Running the API

### Development mode (live reload)

```bash
uvicorn main:app --reload
```

* The server starts on **[http://127.0.0.1:8000](http://127.0.0.1:8000)** by default.
* Interactive Swagger UI: **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**
* ReDoc documentation: **[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)**

### Production mode

```bash
uvicorn main:app --host 0.0.0.0 --port 8080 --workers 4
```

### Query example

```bash
curl "http://127.0.0.1:8000/atmospheric?latitude=45.5&longitude=-73.6&hourly=temperature_2m,pressure_msl"
```

Response (truncated):

```json
{
  "latitude": 45.5,
  "longitude": -73.6,
  "generationtime_ms": 0.32,
  "hourly": {
    "time": ["2025-06-19T00:00", "2025-06-19T01:00", ...],
    "temperature_2m": [22.1, 21.6, ...],
    "pressure_msl": [1014.2, 1014.1, ...]
  }
}
```

---

## Environment variables (optional)

| Variable             | Default | Description                          |
| -------------------- | ------- | ------------------------------------ |
| `OPEN_METEO_TIMEOUT` | `10`    | Upstream request timeout in seconds. |

*(When defined, this variable overrides the hard‑coded 10 s timeout in `main.py`.)*

---

## Docker (optional)

Build and run a minimal container (Python 3.12‑slim):

```bash
docker build -t atmospheric-proxy .
docker run -p 8000:8000 atmospheric-proxy
```

Dockerfile example:

```Dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY main.py .
RUN pip install --no-cache-dir fastapi uvicorn httpx
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## License

[MIT](LICENSE)

---

## Acknowledgements

* [Open‑Meteo](https://open-meteo.com) – free weather API
* [FastAPI](https://fastapi.tiangolo.com/) – modern, fast (high‑performance) web framework
