from fastapi import FastAPI

from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from .routes.api import router as ShortenRouter

app = FastAPI()

app.include_router(ShortenRouter, tags=["Shorten"], prefix="")


@app.exception_handler(RequestValidationError)
async def handler2(request: Request, exc: Exception):
    return JSONResponse({'detail':{
            "status_code":400,
            "error_message":"Bad Request"
            }})
