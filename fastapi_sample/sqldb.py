from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



url = "mysql://root:0074@localhost:3306/mydb"
engine=create_engine(url)

SessonLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db=SessonLocal()
    try:
        yield db
    finally:
      db.close()