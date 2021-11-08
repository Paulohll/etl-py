import pytest
import lib.models as models
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from lib.db import connect_args
from lib.models import Student
from datetime import datetime


@pytest.fixture(scope="session")
def connection():
    engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)
    return engine.connect()


@pytest.fixture(scope="session")
def engine():
    engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)
    return engine


def seed_database(engine):

    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = Session()
    students = [
        {
            "source_student_id": '123abc34',
            "name": "Paulo",
            "surname": "Horna",
            "country": "Peru",
            "update_date": datetime.now(),
            "created_date": datetime.now(),
        },
    ]

    for student in students:
        db_student = Student(**student)
        session.add(db_student)
    session.commit()


@pytest.fixture(scope="session")
def setup_database(engine):
    models.Base.metadata.bind = engine
    models.Base.metadata.create_all()
    seed_database(engine)
    yield
    # models.Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    transaction = connection.begin()
    yield scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    transaction.commit()


def test_connection(setup_database, db_session):
    pass


# def test_exits_table():
#     assert utils.validate_table('warehouse_students') == True

# def test_insert_students(setup_database):
#     pass
