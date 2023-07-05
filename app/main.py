from fastapi import FastAPI

from .routers import tools
from .routers import current_time

app = FastAPI()

app.include_router(tools.router)
app.include_router(current_time.router)