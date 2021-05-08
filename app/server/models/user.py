from typing import Optional

from pydantic import BaseModel, Field


class UserModel(BaseModel):
    customer_id: str = Field(...)
    api_key: str = Field(...)
    secret: str = Field(...)
