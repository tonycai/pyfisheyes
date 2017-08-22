"""messages model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime

from pyfisheyes.model.meta import Base

class Messages(Base):
    __tablename__ = "messages"
    
    id = Column(Integer, primary_key=True)
    eid = Column(Integer)
    msgdate = Column(DateTime)
    msgsubject = Column(String(20))
    msgcontent = Column(String(200))
    
    def __init__(self):
        self.id = 0
        self.eid = 0
        self.msgdate = '0000-00-00 00:00:00'       
        self.msgsubject = ''
        self.msgcontent = ''