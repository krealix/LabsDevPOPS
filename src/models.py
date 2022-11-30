from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id=al{self.id})>"

class Worker(BaseModel):
    __tablename__ = "workers"

    snp = Column(String)
    num_passport = Column(Integer, unique=True)
    birth = Column(String)
    telephone = Column(String)

    jobs = relationship("Job", back_populates="worker_job")

class Category(BaseModel):
    __tablename__ = "categories"

    name = Column(String)
    work_on_hour = Column(Integer)

class Job(BaseModel):
    __tablename__ = "jobs"

    enterprise = Column(String)
    finish_date = Column(DateTime)
    work_hours = Column(Integer)
    worker_id = Column(Integer, ForeignKey("workers.id"))

    worker_job = relationship("Worker", back_populates="jobs")