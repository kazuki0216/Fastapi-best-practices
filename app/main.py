from fastapi import FastAPI
from .routers import cafe_menu, weathers

app = FastAPI()

app.include_router(weathers.router, prefix="/api")
app.include_router(cafe_menu.router, prefix="/api")
