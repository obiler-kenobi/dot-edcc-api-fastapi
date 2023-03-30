from typing import Dict
from pydantic import BaseModel

class SampleBase(BaseModel):
    sample: Dict[str, dict | str | list]
    
class SampleCreate(SampleBase):
    pass
    
class Sample(SampleBase):
    id: int

    class Config:
        orm_mode = True