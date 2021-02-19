from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from src import models, crud, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Vod)
def create_vod(vod: schemas.VodCreate, db: Session = Depends(get_db)):
    db_vod = crud.get_vod_by_title(db, title=vod.title)
    if db_vod:
        raise HTTPException(status_code=400, detail="Title already exist")
    return crud.create_vod(db=db, vod=vod)


@router.get("/", response_model=List[schemas.Vod])
def read_vods(skip:int = 0, limit: int = 100, db: Session = Depends(get_db)):
    vods = crud.get_vods(db, skip=skip, limit=limit)
    return vods





