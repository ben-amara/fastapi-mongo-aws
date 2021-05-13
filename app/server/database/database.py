import motor.motor_asyncio
from decouple import config
from fastapi import HTTPException
from app.server.database.database_helper import user_helper, shorten_helper
from app.server.core.utils import *

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.links

user_collection = database.get_collection('user_list')
shorten_collection = database.get_collection('short')


async def retrieve_user(customer_id: str, api_key: str, secret: str):
    user = await user_collection.find_one({"customer_id": customer_id, "api_key": api_key, "secret": secret})
    if user is not None:
        return user_helper(user)
    else:
        return None


async def add_shorten(shorten_data: dict, user_collect: str = None) -> dict:
    shorten_data['customer_id'] = user_collect['customer_id']
    shorten_data['domain_name'] = check_domain_name(shorten_data['domain_name'], user_collect)
    if 'go_rougue' in shorten_data and shorten_data['go_rougue'] == 1:
        shorten_data['short_url'] = shorten_data['domain_name'] + '/' + get_url_extension()
        shorten_data['input_desired_keyword'] =  None
    else:
        shorten_data['short_url'] = shorten_data['domain_name'] + '/' + check_input_desired_keyword(shorten_data['input_desired_keyword'])

    if 'input_desired_keyword' in shorten_data and shorten_data['input_desired_keyword']:
        re = await check_exist_keyword(shorten_data['input_desired_keyword'])
        if re:
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":" Someone has stolen the keyword"})
    shorten = await shorten_collection.insert_one(shorten_data)
    new_shorten = await shorten_collection.find_one({"_id": shorten.inserted_id})
    return shorten_helper(new_shorten)      
      



async def check_exist_keyword(input_desired_keyword: str):
    short = await shorten_collection.find_one({"input_desired_keyword": input_desired_keyword})
    if short is not None:
        return shorten_helper(short)
    else:
        return None