import motor.motor_asyncio
from decouple import config

from app.server.database.database_helper import user_helper, shorten_helper
from app.server.core.utils import *

MONGO_DETAILS = config('MONGO_DETAILS')

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.shorten

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
    shorten_data['input_desired_keyword'] = check_input_desired_keyword(shorten_data['input_desired_keyword'])               

    shorten = await shorten_collection.insert_one(shorten_data)
    new_shorten = await shorten_collection.find_one({"_id": shorten.inserted_id})
    return shorten_helper(new_shorten)        


