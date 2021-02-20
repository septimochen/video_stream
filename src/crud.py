from sqlalchemy.orm import Session

from . import models, schemas


def get_actor(db: Session, actor_id: int):
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()

def get_actor_by_name(db: Session, name: str):
    return db.query(models.Actor).filter(models.Actor.name == name).first()

def get_actors(db: Session, skip: int =0, limit:int =100):
    return db.query(models.Actor).offset(skip).limit(limit).all()


def create_actor(db:Session, actor: schemas.ActorCreate):
    db_actor = models.Actor(name=actor.name, avatar=actor.avatar)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def get_vod(db: Session, vod_id: int):
    return db.query(models.Vod).filter(models.Vod.id == vod_id).first()


def get_vods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vod).offset(skip).limit(limit).all()


def get_vod_by_title(db: Session, title: str):
    return db.query(models.Vod).filter(models.Vod.title == title).first()


def create_vod(db: Session, vod: schemas.VodCreate, actor_id: int):
    db_vod = models.Vod(**vod.dict(), actor_id=actor_id)
    db.add(db_vod)
    db.commit()
    db.refresh(db_vod)
    return db_vod