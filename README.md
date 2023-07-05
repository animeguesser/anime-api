# Anime API

This is the backend API for the animeguess project using FastAPI in Python

## Running
To run the API, first install the required packages:
```
pip install -r requirements.txt
```

Now you can run using `uvicorn`:
```
uvicorn app.main:app --host 0.0.0.0 --reload
```

## Routes
The current available routes are as followed:

### /ping
This is a simple health check route for a HTTP `GET`.

On success, it will return a HTTP 200 with JSON containing:
```
{"Ping":"Pong"}
```

### /time
This route will be a `GET` which will allow the client user to recieve the days since our first day (2023/07/01) and
the amount of time until the next day.

On success, it will return a HTTP 200 with a JSON containing:
```
{"days_since":4,"time_until":65782.799797}
```