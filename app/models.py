from sqlalchemy import Column, Integer, String
from database import Base


class NPC(Base):
    __tablename__ = "npcs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    surname = Column(String, unique=True, nullable=False)
    birth_day = Column(Integer, unique=True, nullable=False)

