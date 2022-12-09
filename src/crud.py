from sqlalchemy.orm import Session

from src import models, schemas

def create_category(db: Session, category: schemas.CategoryCreate):

    db_category = models.Category(category_name=category.name, work_on_hour=category.work_on_hour)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category



def create_worker(db: Session, worker: schemas.WorkerCreate):

    db_worker = models.Worker(snp=worker.snp, num_passport=worker.num_passport, birth=worker.birth, telephone=worker.telephone)
    db.add(db_worker)
    db.commit()
    db.refresh(db_worker)
    return db_worker


# def create_for_worker_job(db: Session, job: schemas.JobCreate, worker_id: int):
     
#     db_job = models.Job(**job.dict(), worker_id=worker_id)
#     db.add(db_job)
#     db.commit()
#     db.refresh(db_job)
#     return db_job

def create_job(db: Session, job: schemas.JobCreate):
    
    db_job = models.Job(enterprise=job.enterprise, work_hours=job.work_hours, finish_date=job.finish_date)
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job

def create_jobworker(db: Session, jobworker: schemas.JobWorker, worker_id: int, job_id: int):
 
    db_jobworker = models.JobWorker(**jobworker.dict(), worker_id=worker_id, job_id=job_id)
    db.add(db_jobworker)
    db.commit()
    db.refresh(db_jobworker)
    return db_jobworker


def get_category_by_id(db: Session, category_id: int):

    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_worker_by_id(db: Session, worker_id: int):

    return db.query(models.Worker).filter(models.Worker.id == worker_id).first() # pragma: no cover

def get_job_by_id(db: Session, job_id: int):
     
    return db.query(models.Job).filter(models.Job.id == job_id).first()


def get_jobworker_id(db: Session, jobworker_id: int):
 
    return db.query(models.JobWorker).filter(models.JobWorker.id == jobworker_id).first()



def get_category_by_name(db: Session, category_name: str):
    return db.query(models.Category).filter(models.Category.name == category_name).first()

def get_worker_by_name(db: Session, worker_name: str):
    return db.query(models.Worker).filter(models.Worker.snp == worker_name).first()

def get_job_by_enterprise(db: Session, enterprise: str):
    return db.query(models.Job).filter(models.Job.enterprise == enterprise).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Category).offset(skip).limit(limit).all()

def get_workers(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Worker).offset(skip).limit(limit).all()

def get_jobs(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.Job).offset(skip).limit(limit).all()

def get_jobworkers(db: Session, skip: int = 0, limit: int = 100):

    return db.query(models.JobWorker).offset(skip).limit(limit).all()