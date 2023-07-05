from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import tools
from .routers import time

app = FastAPI()

# Middleware CORS
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Public routes
app.include_router(tools.router)
app.include_router(time.router)