"""Users model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text,DateTime
from pyfisheyes.model.meta import Base


class Users(Base):
    __tablename__ = "users"   

    uid = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    group_uid = Column(Integer)    

    def __init__(self):
        self.uid = 0
        self.username = ""
        self.password = ""
        self.group_uid = 0

    def __repr__(self):
        return "<Events('%s')" % self.username
    
    