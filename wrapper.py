from sqlalchemy.orm import sessionmaker, Session
import pymysql
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey,Integer,Date

MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "8452691"
MYSQL_DB = "entreprise"


# SQLALCHEMY_DATABASE_URI="mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,MYSQL_PWD,MYSQL_HOST,MYSQL_PORT,MYSQL_DB)
SQLALCHEMY_DATABASE_URI='sqlite:///entreprise-sqlite.db'
engine = create_engine(SQLALCHEMY_DATABASE_URI,connect_args={'check_same_thread': False})

Session = sessionmaker(bind=engine)
session = Session()
# Base = automap_base()
Base = declarative_base()
# Base.prepare(engine, reflect=True)

class Employee(Base):
    __tablename__="employee"
    id=Column('id',Integer, primary_key=True )
    first_name=Column('first_name', String(80))
    last_name=Column('last_name', String(80))
    birthdate=Column('birthdate',Date)
# Employee = Base.classes.employee


def get_user_by_id(id):
    try:
        result = session.query(Employee).get(id)
        return result

    except Exception as e:
        print(e)
        return False

def get_all_users():
    try:
        result = session.query(Employee).filter_by()

        return result
    except Exception as e:
        print(e)
        return False