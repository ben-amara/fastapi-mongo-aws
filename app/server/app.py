from fastapi import FastAPI
from .routes.api import router as ShortenRouter

app = FastAPI()

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this api fast app (AWS-MONGO)."}


app.include_router(ShortenRouter, tags=["Shorten"], prefix="/shorten")
