from typing import List, Optional

from pydantic import BaseModel
from sqlalchemy import orm

class ActorBase(BaseModel):
    name: str
    avatar: str

class ActorCreate(ActorBase):
    pass

class Actor(ActorBase):
    id: int
    # vods: List[Vod] = []

    class Config:
        orm_mode = True
class VodBase(BaseModel):
    title: str
    thumbnail: str
    length: str

class VodCreate(VodBase):
    pass

class Vod(VodBase):
    id: int
    actor: Actor

    class Config:
        orm_mode = True




