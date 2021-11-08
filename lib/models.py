from sqlalchemy import TIMESTAMP, Column, String, Integer
from sqlalchemy import create_engine, MetaData, Sequence
from sqlalchemy.ext.declarative import declarative_base
from lib.db import connect_args

engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)
meta = MetaData(engine)
Base = declarative_base(metadata=meta)

class Student(Base):
    __tablename__ = 'warehouse_students'
    id = Column(Integer, primary_key=True)
    source_student_id = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    surname = Column(String(255), nullable=False)
    country = Column(String(255), nullable=False)
    update_date = Column(TIMESTAMP, nullable=False)
    created_date = Column(TIMESTAMP, nullable=False)
