from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():

    db = SessionLocal() # pragma: no cover
    try:# pragma: no cover
        yield db# pragma: no cover
    finally:# pragma: no cover
        db.close()# pragma: no cover

@app.get("/workers/", response_model=list[schemas.Worker])
def get_workers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    workers = crud.get_workers(db, skip=skip, limit=limit)
    return workers

@app.get("/workers/{worker_id}", response_model=schemas.Worker)
def read_worker_by_id(worker_id: int, db: Session = Depends(get_db)):

    db_worker = crud.get_worker_by_id(db, worker_id=worker_id)
    if db_worker is None:
        raise HTTPException(status_code=404, detail="Такого работника нет")
    return db_worker

@app.post("/workers/{worker_id}/jobs/", response_model=schemas.Job)
def create_for_worker_job(worker_id: int, job: schemas.JobCreate, db: Session = Depends(get_db)):
    
    return crud.create_for_worker_job(db=db, job=job, worker_id=worker_id)

@app.post("/workers/", response_model=schemas.Worker)
def create_worker(worker: schemas.WorkerCreate, db: Session = Depends(get_db)):

    db_worker = crud.get_worker_by_name(db, worker_name=worker.snp)
    if db_worker:
        raise HTTPException(status_code=400, detail="Такой уже рабочий есть")
    return crud.create_worker(db=db, worker=worker)


@app.get("/jobs/{job_id}", response_model=schemas.Job)
def get_job_by_id(job_id: int, db: Session = Depends(get_db)):

    db_job = crud.get_job_by_id(db, job_id=job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Такой работы нет")
    return db_job

@app.get("/jobs/", response_model=list[schemas.Job])
def get_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    jobs = crud.get_jobs(db, skip=skip, limit=limit)
    return jobs



@app.post("/categories/", response_model=schemas.Category)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):

    return crud.create_category(db=db, category=category)

@app.get("/categories/", response_model=list[schemas.Category])
def get_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories


@app.get("/categories/{category_id}", response_model=schemas.Category)
def get_category_by_id(category_id: int, db: Session = Depends(get_db)):

    db_category = crud.get_category_by_id(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Такой категории нет")
    return db_category