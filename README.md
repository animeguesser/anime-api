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

### /search
This route will be a `POST` with the search query. It will require the `Content-Type` header to specifically be `application/json`.

On success, it will return a HTTP 200 with a JSON list of anime titles. Ex:

```
{"titles":["919","\"Bungaku Shoujo\" Movie","3-Nen D-Gumi Glass no Kamen","3 Choume no Tama: Onegai! Momo-chan wo Sagashite!!","#1"]}
```

#### Testing the route
To test the route, you can simply use `CURL` to send data into the API. As long as you use `query` as the key along in the request, it
will process and return the titles.

```
curl -d '{"query":"naruto"}' -H "Content-Type: application/json" -X POST http://localhost:8000/search
```

### /answer
This route will be a `POST` with the answer query. It wiull require the `Content-Type` header to specifically be `application/json`.

If the answer query matches the correct answer as defined by the day, it will return JSON with either a key of answer either being true or false.

```
{"answer":"true"}
```

#### Testing the route
To test the route, you can simple use `CURL` to send data into the API. As long as you use `answer` as the key along in the request it will process and return JSON with true or false.
```
curl -d '{"answer":"Cowboy Bebop"}' -H "Content-Type: application/json" -X POST http://localhost:8000/answer
```