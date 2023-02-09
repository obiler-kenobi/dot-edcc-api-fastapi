from typing import List, Optional

from pydantic import BaseModel, Field

class TokenPayload(BaseModel):
    scopes: List[str]

class DataModel(BaseModel):
    id: int

class CreateResponse(BaseModel):
    data: DataModel
    message: str

class ErrorModel(BaseModel):
    detail: str

class DiscordPayload(BaseModel):
    content: str