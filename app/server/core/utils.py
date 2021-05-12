import os
import time
import json
import random
from decouple import config
from functools import lru_cache
from fastapi import HTTPException
from datetime import datetime

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
KEY_PATH = config('KEY_PATH')
DOMAIN_LIST =['io.deals','amzn.how','ytube.page','twttr.site','insta.blue','dev.care','ios.page','etsy.one','reddit.fyi','claim.run','howdy.biz','yelp.pw','pinterest.blue','wlmart.in','wiki.army','lnkd.dev','unrobinhood.com','moneylion.co.in','chime.expert','ebay.party','url.gifts','url.cafe','url.toys']

def get_domain_random():
    random_index = random.randint(0,len(DOMAIN_LIST)-1)
    return DOMAIN_LIST[random_index]


@lru_cache
def _get_keys():
    data_file = os.path.join(BASE_DIR, KEY_PATH)
    with open(data_file, "r") as keys:
        return json.load(keys)


def get_day_key(day_of_year: int) -> str:
    keys = _get_keys()
    return keys[day_of_year - 1]    


def check_domain_name(domaine = None, user_obj: dict = None):
    if domaine:
        if domaine in DOMAIN_LIST:
            return domaine
        if 'custom_domains' in user_obj and domaine not in user_obj['custom_domains']:            
            raise HTTPException(status_code=400, detail="Domain name not found in system")       
    else:
        return get_domain_random()
    

def check_input_desired_keyword(inpt_dsrd_kword=None):
    if inpt_dsrd_kword:
        return inpt_dsrd_kword
    else:    
        day_key = get_day_key(datetime.now().timetuple().tm_yday)
        millis = _get_milliseconds()
        return "".join(sorted(millis + day_key))    


def _get_milliseconds() -> str:
    millis = int(round(time.time() * 1000))
    str_millis = str(millis)
    str_millis = str_millis[-6:]
    str_millis = hex(int(str_millis))
    return str_millis[2:]        