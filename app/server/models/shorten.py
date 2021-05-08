from datetime import datetime, timezone
from typing import Optional
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


class ShortenModel(BaseModel):
    long_url: str = Field(...)
    domain_name: Optional[str] = None
    input_desired_keyword: Optional[str] = None
    time_limit: Optional[str] = None
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
    def validate_long_url(value: int) -> str:
        if value[0:8] == 'https://':
            raise HTTPException(status_code=400, detail="long_url must contain 'https://'")  
        return value 


    @validator("click_limit")
    def validate_click_limit(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid click_limit format")
        if value not in range(1, 1000000):
            raise HTTPException(status_code=405, detail="click_limit should beetwen 1 - 1 000 000")   
        return value 

    @validator("got_rougue")
    def validate_got_rougue(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid got_rougue format")
        if value != 1:
            raise HTTPException(status_code=405, detail="got_rougue should beetwen equal to 1")   
        return value                  
       
    @validator("not_child")
    def validate_not_child(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid not_child format")
        if value != 1:
            raise HTTPException(status_code=405, detail="not_child should beetwen equal to 1")   
        return value  

    @validator("not_work")
    def validate_not_work(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid not_work format")
        if value != 1:
            raise HTTPException(status_code=405, detail="not_work should beetwen equal to 1")   
        return value  

    @validator("contains_politics")
    def validate_contains_politics(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid contains_politics format")
        if value != 1:
            raise HTTPException(status_code=405, detail="contains_politics should beetwen equal to 1")   
        return value   

    @validator("contains_promotions")
    def validate_contains_promotions(value: int) -> str:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid contains_promotions format")
        if value != 1:
            raise HTTPException(status_code=405, detail="contains_promotions should beetwen equal to 1")   
        return value   

    @validator("contains_violence")
    def validate_contains_violence(value: int) -> int:
        if not isinstance(value, int):
            raise HTTPException(status_code=400, detail="Invalid contains_violence format")
        if value != 1:
            raise HTTPException(status_code=405, detail="contains_violence should beetwen equal to 1")   
        return value



def ResponseModel(data):
    return  {
                'status_code':200,
                'error_message':None,
                'user_collect_id': data['user_collect_id'],
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