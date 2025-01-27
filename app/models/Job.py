from sqlalchemy import Column, String, Integer
from app.database import Base


class Job(Base):
    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
