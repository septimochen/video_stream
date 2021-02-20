from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Index

from .database import Base


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    avatar = Column(String)

    vods = relationship("Vod", back_populates="actor")


class Vod(Base):
    __tablename__ = "vods"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    actor_id = Column(Integer, ForeignKey("actors.id"))
    thumbnail = Column(String)
    length = Column(String)

    actor = relationship("Actor", back_populates="vods")
