import motor.motor_asyncio
from bson import ObjectId
from decouple import config

from app.server.database.database_helper import user_helper, shorten_helper

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


async def add_shorten(shorten_data: dict, user_collect_id: str = None) -> dict:
    shorten_data['user_collect_id'] = user_collect_id
    shorten = await shorten_collection.insert_one(shorten_data)
    new_shorten = await shorten_collection.find_one({"_id": shorten.inserted_id})
    return shorten_helper(new_shorten)        


