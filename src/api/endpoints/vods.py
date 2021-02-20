from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from src import models, crud, schemas
from src.api.endpoints import get_db

router = APIRouter()


@router.post("/", response_model=schemas.Vod)
def create_vod(actor_id: int, vod: schemas.VodCreate, db: Session = Depends(get_db)):
    db_vod = crud.get_vod_by_title(db, title=vod.title)
    if db_vod:
        raise HTTPException(status_code=400, detail="Title already exist")
    return crud.create_vod(db=db, vod=vod, actor_id=actor_id)


@router.get("/", response_model=List[schemas.Vod])
def read_vods(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vods = crud.get_vods(db, skip=skip, limit=limit)
    # print(vods)
    return vods





