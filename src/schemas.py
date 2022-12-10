from pydantic import BaseModel
from datetime import date

class JobBase(BaseModel):
    
    enterprise: str
    finish_date: date
    work_hours: int


class JobCreate(JobBase):

    pass


class Job(JobBase):

    id: int

    class Config:

        orm_mode = True

class JobWorkerBase(BaseModel):
    
    pass


class JobWorkerCreate(JobWorkerBase):

    pass


class JobWorker(JobWorkerBase):

    id: int
    job_id: int
    worker_id: int

    class Config:
        orm_mode = True



class CategoryBase(BaseModel):

    name: str
    work_on_hour: int


class CategoryCreate(CategoryBase):

    pass


class Category(CategoryBase):

    id: int

    class Config:
        orm_mode = True

class WorkerBase(BaseModel):

    snp: str
    num_passport: int 
    birth: str
    telephone: str
    

class WorkerCreate(WorkerBase):

    pass


class Worker(WorkerBase):
    
    id: int
    category_id: int
    worker_job: list[JobWorker] = []

    class Config:

        orm_mode = True