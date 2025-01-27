from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class NPC(Base):
    __tablename__ = "npcs"
    id = Column(Integer, primary_key=True, index=True)
    given_name = Column(String)
    surname = Column(String)
    day_of_birth = Column(Integer)
    job_id = Column(Integer, ForeignKey('jobs.id'))
