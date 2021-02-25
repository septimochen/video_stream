from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session
from src import models, crud, schemas
from src.api.endpoints import get_db


router = APIRouter()


@router.post("/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    db_actor = crud.get_actor_by_name(db, name=actor.name)
    if db_actor:
        raise HTTPException(status_code=400, detail="Actor already exist")
    return crud.create_actor(db=db, actor=actor)


@router.get("/{actor_id}", response_model=schemas.Actor)
def read_actors(actor_id: int, db: Session = Depends(get_db)):
    db_actor = crud.get_actor(db, actor_id=actor_id)
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor


@router.get("/", response_model=List[schemas.Actor])
def read_actors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actors = crud.get_actors(db, skip=skip, limit=limit)
    return actors