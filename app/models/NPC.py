from sqlalchemy import Column, Integer, String
from app.database import Base


class NPC(Base):
    __tablename__ = "npcs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    day_of_birth = Column(String)
