from sqlalchemy import Column, Integer, String, Boolean, DateTime,ForeignKey
from sqldb import Base,engine


class usertable(Base):
    __tablename__="usermaster"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=100))
    password = Column(String(length=100))
    
class todotable(Base):
    __tablename__="Todo_table"
    id = Column(Integer, primary_key=True, index=True)
    Name = Column(String(length=100))
    Todo_Title= Column(String(length=100))
    Todo_Description= Column(String(length=200))

