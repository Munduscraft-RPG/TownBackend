from sqlalchemy import Column, String, Integer
from app.database import Base


class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    quantity = Column(Integer)
