from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Vod(Base):
    __tablename__ = "vods"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True)
    actor = Column(String)
