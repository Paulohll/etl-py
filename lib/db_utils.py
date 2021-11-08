import pandas as pd
import pytest
import lib.models as models
from sqlalchemy import create_engine, inspect, text, exc
from sqlalchemy.sql.expression import table
from lib.models import Student
from lib.db import connect_args
from faker import Faker


def insert_df_into_db(df, table_name, columns_list):
    """Inserts a dataframe given into a default database. We need to provide
    the columns in the dataframe in the same order we want to insert them in the database.
    :param df: The dataframe we want to insert
    :param table_name: The table of the database we want to insert the data in
    :param columns_list: The columns of the table in the database we want to
    insert the data in
    :return: The total number of rows inserted
    """
    #establish engine connection
    engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)

    # prepare columns and values
    column = ",".join(columns_list)
    values = ",:".join(columns_list)

    try:
        if not validate_table(table_name):
            raise Exception("The table does not exist")

        with engine.connect() as conn:
            rowcount = 0
            data = df.to_dict('records')

            stm = text("""INSERT INTO """+table_name+""" ("""+column +
                       """,update_date,created_date) VALUES(:"""+values+""",current_timestamp,current_timestamp)""")

            for line in data:
                r = conn.execute(stm, **line)
                rowcount = r.rowcount + 1

    except exc.SQLAlchemyError as e:
        raise(e)
    else:
        return rowcount


def get_df_from_query(query, table_name_cols):
    ##User faker to generate random data
    faker = Faker()
    return pd.DataFrame({'student_id': [faker.bothify(text='????????????'),faker.bothify(text='????????????')], 'name':
                         [faker.first_name(), faker.first_name()], 'surname': [faker.last_name(), faker.last_name()], 'country':
                         [faker.country(), faker.country()]})


def read_dw_sql(query):
    """Return warehouse data
    :param query  The sql query 
    :return result query on warehouse """
    engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)
    df=pd.read_sql(query, engine.connect())
    return df


def validate_table(table_name):
    """validate if the table exists
    :return false or true"""

    # establish engine connection
    engine = create_engine('postgresql+psycopg2://', connect_args=connect_args)

    # validate
    insp = inspect(engine)
    ret = insp.dialect.has_table(engine.connect(), table_name)

    return ret


