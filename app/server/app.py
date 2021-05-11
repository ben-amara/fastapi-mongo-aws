from fastapi import FastAPI
from .routes.api import router as ShortenRouter

app = FastAPI()

app.include_router(ShortenRouter, tags=["Shorten"], prefix="")
