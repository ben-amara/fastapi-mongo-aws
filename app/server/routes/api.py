from fastapi import APIRouter, Body, Request, Depends, Header
from fastapi.encoders import jsonable_encoder
from app.server.auth.check_token import _get_authorization_token
from app.server.database.database import *
from app.server.models.user import *
from app.server.models.shorten import *

router = APIRouter()


@router.post("/", response_description="Student data added into the database")
async def create_shorten(request: Request, shorten: ShortenModel = Body(...), user_collect_id: dict = Depends(_get_authorization_token)):    
    shorten = jsonable_encoder(shorten)    
    new_shorten = await add_shorten(shorten, user_collect_id)
    return ResponseModel(new_shorten)
    

