from datetime import datetime, timezone
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator
from app.server.core.utils import _get_milliseconds, get_day_key, get_domain_random


class ShortenModel(BaseModel):
    long_url: str = Field(...)
    domain_name: Optional[str] = None
    input_desired_keyword: Optional[str] = None
    time_limit: Optional[int] = None
    click_limit: Optional[int] = None
    got_rougue: Optional[int] = None
    not_child: Optional[int] = None
    not_work: Optional[int] = None
    contains_politics: Optional[int] = None
    contains_promotions: Optional[int] = None
    contains_violence: Optional[int] = None
    created_at: Optional[datetime] = datetime.now(timezone.utc)

    class Config:
        schema_extra = {
            'example': {                
                'long_url': 'https//www.youtube.com',
                'domain_name': 'reddit.fyi',
                'input_desired_keyword': 'poperver',
                'time_limit': None,
                'click_limit': None,
                'got_rougue':  None,
                'not_child': None,
                'not_work': None,
                'contains_politics': None,
                'contains_promotions': None,
                'contains_violence': None           
            }
        }

    @validator("long_url")
    def validate_long_url(cls, value: str) -> str: 
        if cls is None:
            raise HTTPException(status_code=400, detail={"status_code":400, "error_message":"Bad Request"})    
        if value[0:8] != 'https://':
            raise HTTPException(status_code=405, detail={"status_code":405, "error_message":"Long url must start with https://"})                    
        return value 

    @validator("domain_name")
    def validate_domain_name(value: str) -> str:
        if value is None or value == '':
            value = get_domain_random()                
        return value 

    @validator("input_desired_keyword")
    def validate_input_desired_keyword(value: str) -> str:
        if value is None or value == '':
            day_key = get_day_key(datetime.now().timetuple().tm_yday)
            millis = _get_milliseconds()
            value =  "".join(sorted(millis + day_key))                
        return value 

    @validator("time_limit")
    def validate_time_limit(value: int) -> str:
        if value is None or value == '':
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":"time_limit only accepts seconds as input"})
        from datetime import datetime, timedelta
        x = datetime.now() + timedelta(seconds=value)            
        return x.strftime('%Y-%m-%d %H:%M %p')

    @validator("click_limit")
    def validate_click_limit(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":"Invalid click_limit format"})
        if value not in range(1, 1000000):
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":"click limit accpets values between 1 Aand 1000000"})   
        return value 

    @validator("got_rougue")
    def validate_got_rougue(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":" Invalid got_rougue format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value                  
       
    @validator("not_child")
    def validate_not_child(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":"Invalid not_child format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value  

    @validator("not_work")
    def validate_not_work(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":"Invalid not_work format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value  

    @validator("contains_politics")
    def validate_contains_politics(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":" Invalid contains_politics format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value   

    @validator("contains_promotions")
    def validate_contains_promotions(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":" Invalid contains_promotions format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value   

    @validator("contains_violence")
    def validate_contains_violence(value: int) -> int:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail={"staus_code":405, "error_message":"Invalid contains_violence format"})
        if value != 1:
            raise HTTPException(status_code=405, detail={"staus_code":405, "error_message":" Link classification accepts 1 or null as input"})   
        return value



def ResponseModel(data):
    return  {
                'status_code':200,
                'error_message':None,
                'customer_id': data['customer_id'],
                'request_id': data['id'],
                'created_at': data['created_at'],
                'long_url': data['long_url'],
                'short_url': data['short_url'] if 'short_url' in data else None ,
                'domain_name': data['domain_name'] if 'domain_name' in  data else None,
                'input_desired_keyword': data['input_desired_keyword'] if 'input_desired_keyword' in data else None ,
                'time_limit': data['time_limit'] if 'time_limit' in data else None ,
                'click_limit': data['click_limit'] if 'click_limit' in data else None ,
                'not_child': data['not_child'] if 'not_child' in data else None ,
                'not_work': data['not_work'] if 'not_work' in data else None ,
                'contains_politics': data['contains_politics'] if 'contains_politics' in data else None,
                'contains_promotions': data['contains_promotions'] if 'contains_promotions' in data else None,
                'contains_violence': data['contains_violence'] if 'contains_violence' in data else None,
                'go_rougue': data['go_rougue'] if 'go_rougue' in data else None
                }


def ErrorResponseModel(error, code, message):
    return {
        'error': error,
        'code': code,
        'message': message
    }