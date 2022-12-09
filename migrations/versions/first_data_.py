"""empty message

Revision ID: first_data
Revises: 7c28dd75aea0
Create Date: 2022-11-30 14:39:59.963580

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime

from src.models import Worker, Category, Job, JobWorker


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = '7c28dd75aea0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    bind = op.get_bind()
    session = orm.Session(bind=bind)

    ivanov = Worker(snp='Иванов Иван Иванович', num_passport=160504, birth= "28 февраля 1990 года", telephone="+79005555700")
    petrov = Worker(snp='Петров Петр Петрович', num_passport=112032, birth= "24 июня 1980 года", telephone="+79123456798")
    semenov = Worker(snp='Семенов Семен Семенович', num_passport=123456, birth= "3 сентября 1975 года", telephone="+79123456797")
    andreev = Worker(snp='Андреев Андрей Андреевич', num_passport=234567, birth= "1 мая 1999 года", telephone="+79123456796")

    session.add_all([ivanov, petrov, semenov, andreev])
    session.flush()

    firstcategory = Category(name='Первая категория', work_on_hour=500)
    secondcategory = Category(name='Вторая категория', work_on_hour=1000)
    thirdcategory = Category(name='Третья категория', work_on_hour=1500)

    session.add_all([firstcategory, secondcategory, thirdcategory])
    session.commit()

    audit1 = Job(enterprise='Три толстяка', finish_date= datetime(2022, 4, 13), work_hours=5)
    audit2 = Job(enterprise='Лимпопо', finish_date= datetime(2022, 4, 14), work_hours=3)
    audit3 = Job(enterprise='Моя прелесть', finish_date= datetime(2022, 4, 15), work_hours=4)
    audit4 = Job(enterprise='Сова', finish_date= datetime(2022, 5, 16), work_hours=6)
    audit5 = Job(enterprise='ЕмСам', finish_date= datetime(2022, 5, 17), work_hours=7)
    audit6 = Job(enterprise='Скороед', finish_date= datetime(2022, 5, 18), work_hours=4)
    audit7 = Job(enterprise='У Иваныча', finish_date= datetime(2022, 5, 17), work_hours=2)
    audit8 = Job(enterprise='Федор Самохвалов', finish_date= datetime(2022, 5, 18), work_hours=8)

    session.add_all([audit1, audit2, audit3, audit4, audit5, audit6, audit7, audit8])
    session.commit()

    jobworker1 = JobWorker(job_id=1, worker_id=1)
    jobworker2 = JobWorker(job_id=2, worker_id=2)
    jobworker3 = JobWorker(job_id=3, worker_id=3)
    jobworker4 = JobWorker(job_id=4, worker_id=4)
    jobworker5 = JobWorker(job_id=5, worker_id=1)
    jobworker6 = JobWorker(job_id=6, worker_id=3)
    jobworker7 = JobWorker(job_id=7, worker_id=4)
    jobworker8 = JobWorker(job_id=8, worker_id=2)

    session.add_all([jobworker1, jobworker2, jobworker3, jobworker4, jobworker5, jobworker6, jobworker7, jobworker8])
    session.commit()


def downgrade() -> None:
    pass
