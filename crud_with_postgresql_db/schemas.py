from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    name: str
    actor: Optional[str]
    class Config:
        orm_mode = True