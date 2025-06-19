# Atmospheric Measurements API Endpoint

This API endpoint provides atmospheric measurements such as temperature, wind speed, wind direction, and weather code using the Open-Meteo API.

## Requirements

* Python 3.x
* Flask
* Requests

## Installation

1. **Clone the repository**

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Set up the virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install flask requests
```

## Running the Application

Execute the Flask application using:

```bash
python <filename>.py
```

The API will start running on `http://0.0.0.0:5000`.

## Usage

To retrieve atmospheric data, make a GET request to:

```
GET http://localhost:5000/atmospheric?latitude=45.50&longitude=-73.57
```

Replace `latitude` and `longitude` with desired values.

## Example Response

```json
{
  "temperature": 22.3,
  "windspeed": 5.6,
  "winddirection": 180,
  "weathercode": 1
}
```

## Error Handling

If there's an issue retrieving data from Open-Meteo, you'll get an error response:

```json
{
  "error": "Failed to retrieve data from Open-Meteo"
}
```
