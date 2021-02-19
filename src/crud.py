from sqlalchemy.orm import Session

from . import models, schemas


def get_vod(db: Session, vod_id: int):
    return db.query(models.Vod).filter(models.Vod.id == vod_id).first()


def get_vods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Vod).offset(skip).limit(limit).all()


def get_vod_by_title(db: Session, title: str):
    return db.query(models.Vod).filter(models.Vod.title == title).first()


def create_vod(db: Session, vod: schemas.VodCreate):
    db_vod = models.Vod(**vod.dict())
    db.add(db_vod)
    db.commit()
    db.refresh(db_vod)
    return db_vod