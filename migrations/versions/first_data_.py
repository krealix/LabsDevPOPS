"""empty message

Revision ID: first_data
Revises: cdd860b81a11
Create Date: 2022-11-30 14:39:59.963580

"""
from alembic import op
from sqlalchemy import orm
from datetime import datetime

from src.models import Worker, Category, Job


# revision identifiers, used by Alembic.
revision = 'first_data'
down_revision = 'cdd860b81a11'
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

    audit1 = Job(enterprise='Три толстяка', finish_date= datetime(2022, 4, 13), work_hours=5, worker_id=ivanov.id)
    audit2 = Job(enterprise='Лимпопо', finish_date= datetime(2022, 4, 14), work_hours=3, worker_id=petrov.id)
    audit3 = Job(enterprise='Моя прелесть', finish_date= datetime(2022, 4, 15), work_hours=4, worker_id=semenov.id)
    audit4 = Job(enterprise='Сова', finish_date= datetime(2022, 5, 16), work_hours=6, worker_id=andreev.id)
    audit5 = Job(enterprise='ЕмСам', finish_date= datetime(2022, 5, 17), work_hours=7, worker_id=ivanov.id)
    audit6 = Job(enterprise='Скороед', finish_date= datetime(2022, 5, 18), work_hours=4, worker_id=semenov.id)
    audit7 = Job(enterprise='У Иваныча', finish_date= datetime(2022, 5, 17), work_hours=2, worker_id=andreev.id)
    audit8 = Job(enterprise='Федор Самохвалов', finish_date= datetime(2022, 5, 18), work_hours=8, worker_id=petrov.id)

    session.add_all([audit1, audit2, audit3, audit4, audit5, audit6, audit7, audit8])
    session.commit()


def downgrade() -> None:
    pass
