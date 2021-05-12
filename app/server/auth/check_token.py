from fastapi import Request, HTTPException, Header
from app.server.database.database import *


async def _get_authorization_token (customer_id:str  = Header(...), api_key:str  = Header(...), secret:str  = Header(...)):        
    if customer_id is None or api_key is None or secret is None:
        print("Failed here.")
        raise HTTPException(status_code=400, detail={"status_code":400, "error_message":"Bad Request"})

    if customer_id == '' or api_key == '' or secret == '':        
        raise HTTPException(status_code=401, detail={"status_code":401, "error_message":"Invalid Credentials"})  

    v = await verify_token(customer_id, api_key, secret)
    if v is None:
        raise HTTPException(status_code=401, detail={"status_code":401, "error_message":"Invalid Credentials"})
    else:
        return v

async def verify_token(customer_id:str, api_key:str, secret:str) -> bool:
    re = await retrieve_user(customer_id, api_key, secret)
    return re