from typing import List, Union
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None
    scopes: List[str] = []