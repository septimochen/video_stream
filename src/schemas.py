from typing import List, Optional

from pydantic import BaseModel


class VodBase(BaseModel):
    title: str
    actor: str

class VodCreate(VodBase):
    pass

class Vod(VodBase):
    id: int

    class Config:
        orm_mode = True

