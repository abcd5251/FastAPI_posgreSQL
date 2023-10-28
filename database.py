from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

conn = psycopg2.connect(database="test_database", user="allen_test", 
                        password="123456", host="localhost", 
                        port="3000")
cursor = conn.cursor()
cursor.execute("CREATE DATABASE test_database")
conn.commit()
cursor.close()

URL_DATABASE = "postgresql://allen_test:123456@localhost:3000/test_database"

engine = create_engine(URL_DATABASE)

SessionLocal =sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
