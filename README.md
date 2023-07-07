# Anime API

This is the backend API for the animeguess project. The URL for the api is at: `https://api.animeguesser.moe`.

The API utilizes an AWS serverless architecture:

![API Architecture](api-arch.png)

## Routes
The current available routes are as followed:

### /time
This route will be a `GET` which will allow the client user to recieve the days since our first day (2023/07/01) and
the amount of time until the next day.

On success, it will return a HTTP 200 with a JSON containing:
```
{"currentDay": 6, "timeUntil": "5:07:45.864285"}
```

### /search
This route will be a `POST` with the search query. It will require the `Content-Type` header to specifically be `application/json`.

On success, it will return a HTTP 200 with a JSON list of anime titles. Ex:

```
{"titles":["919","\"Bungaku Shoujo\" Movie","3-Nen D-Gumi Glass no Kamen","3 Choume no Tama: Onegai! Momo-chan wo Sagashite!!","#1"]}
```