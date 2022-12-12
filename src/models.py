from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):  # pragma: no cover
        return f"<{type(self).__name__}(id=al{self.id})>"

class Worker(BaseModel):
    __tablename__ = "workers"

    snp = Column(String)
    num_passport = Column(Integer, unique=True)
    birth = Column(String)
    telephone = Column(String)

    category_id = Column(Integer, ForeignKey('categories.id'))
    worker_job = relationship("JobWorker", backref="worker")


class Category(BaseModel):
    __tablename__ = "categories"

    name = Column(String)
    work_on_hour = Column(Integer)

    category_worker = relationship("Worker")

class Job(BaseModel):
    __tablename__ = "jobs"

    enterprise = Column(String)
    finish_date = Column(DateTime)
    work_hours = Column(Integer)

    job_worker = relationship("JobWorker", backref="job")

class JobWorker(BaseModel):
    __tablename__ = "jobworkers"

    job_id = Column(Integer, ForeignKey("jobs.id"))
    worker_id = Column(Integer, ForeignKey("workers.id"))