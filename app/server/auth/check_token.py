from fastapi import Request, HTTPException, Header
from app.server.database.database import *


async def _get_authorization_token (customer_id:str  = Header(...), api_key:str  = Header(...), secret:str  = Header(...)):        
    if customer_id is None:
        print("Failed here.")
        raise HTTPException(status_code=401, detail="The request is missing a valid customer_id")

    if api_key is None:
        print("Failed here api_key")
        raise HTTPException(status_code=401, detail="The request is missing a valid api_key")  

    if secret is None:
        print("Failed here secret")
        raise HTTPException(status_code=401, detail="The request is missing a valid secret")

    v = await verify_token(customer_id, api_key, secret)
    if v is None:
        raise HTTPException(status_code=401, detail="User credentials are not valid")
    else:
        return v

async def verify_token(customer_id:str, api_key:str, secret:str) -> bool:
    re = await retrieve_user(customer_id, api_key, secret)
    return re