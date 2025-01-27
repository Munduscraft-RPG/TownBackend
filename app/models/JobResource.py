from sqlalchemy import Column, Integer, ForeignKey, PrimaryKeyConstraint
from app.database import Base


class JobResource(Base):
    __tablename__ = "jobs_resources"
    job_id = Column(Integer, ForeignKey("jobs.id"))
    resource_id = Column(Integer, ForeignKey("resources.id"))
    quantity = Column(Integer)
    __table_args__ = (
        PrimaryKeyConstraint("job_id", "resource_id"),
    )
