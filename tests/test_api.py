from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.main import app, get_db
from src.models import Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Тестовая БД

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

Base.metadata.drop_all(bind=engine)  # Удалем таблицы из БД
Base.metadata.create_all(bind=engine)  # Создаем таблицы в БД


def override_get_db():
    """
    Данная функция при тестах будет подменять функцию get_db() в main.py.
    Таким образом приложение будет подключаться к тестовой базе данных.
    """
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db  # Делаем подмену

client = TestClient(app)  # создаем тестовый клиент к нашему приложению


def test_create_job():
    """
    Тест на создание новой работы.
    """
    response = client.post(
        "/jobs/",
        json={"enterprise": "Один Барсук", "finish_date": "2022-10-19", "work_hours": "10"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["enterprise"] == "Один Барсук"



def test_create_exist_job():
    """
    Проверка случая, когда мы пытаемся добавить существующую работу
    в БД, т.е. когда данная работа уже присутствует в БД.
    """
    response = client.post(
        "/jobs/",
        json={"enterprise": "Один Барсук", "finish_date": "2022-10-19", "work_hours": "10"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Такая работа уже существует"


def test_get_job():
    """
    Тест на получение списка работ из БД
    """
    response = client.get("/jobs/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["enterprise"] == "Один Барсук"


def test_get_job_by_id():
    """
    Тест на получение работы из БД по его id
    """
    response = client.get("/jobs/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["enterprise"] == "Один Барсук"


def test_job_not_found():
    """
    Проверка случая, если пользователь с таким id отсутствует в БД
    """
    response = client.get("/jobs/15")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такой работы нет"

#---------------------------------------------------------------------------

def test_create_category():

    response = client.post(
        "/categories/",
        json={"name": "Половинная категория", "work_on_hour": "525"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Половинная категория"


def test_create_exist_category():

    response = client.post(
        "/categories/",
        json={"name": "Половинная категория", "work_on_hour": "525"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Такая категория уже существует"


def test_get_category():

    response = client.get("/categories/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["name"] == "Половинная категория"


def test_get_category_by_id():

    response = client.get("/categories/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["name"] == "Половинная категория"


def test_category_not_found():

    response = client.get("/categories/4")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такой категории нет"

#-----------------------------------------------------

def test_create_worker():
    
    response = client.post(
        "/workers/",
        json={
            "snp": "dsadas", 
            "num_passport": "123777", 
            "birth": "2132", 
            "telephone": "3213", 
            "category_id": "1"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["snp"] == "dsadas"


def test_create_exist_worker():

    response = client.post(
        "/workers/",
        json={
            "snp": "dsadas", 
            "num_passport": "123777", 
            "birth": "2132", 
            "telephone": "3213", 
            "category_id": "1"}
    )
    assert response.status_code == 400, response.text
    data = response.json()
    assert data["detail"] == "Такой уже рабочий есть"


def test_get_worker():

    response = client.get("/workers/")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data[0]["snp"] == "dsadas"


def test_get_worker_by_id():

    response = client.get("/workers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["snp"] == "dsadas"


def test_workers_not_found():

    response = client.get("/workers/5")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого работника нет"

#---------------------------------------------------------------

def test_create_jobworker():
    
    response = client.post(
        "/jobworkers/1/2/",
        json={
            "worker_id": "1", 
            "job_id": "2"}
    )
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["worker_id"] == 1

def test_get_jobworker_id():
    
    response = client.get("/jobworkers/1")
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["worker_id"] == 1

def test_jobworkers_not_found():
    
    response = client.get("/jobworkers/5")
    assert response.status_code == 404, response.text
    data = response.json()
    assert data["detail"] == "Такого нет"