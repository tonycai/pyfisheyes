"""Contacts model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base


class Contacts(Base):
    __tablename__ = "contacts"
   #c.categories = ['mysqlg1','apperrorlog','tmc']

    id = Column(Integer, primary_key=True)
    eid = Column(String(100))
    name = Column(String(100))
    ename = Column(String(200))
    title = Column(String(100))
    subtel = Column(Integer(2))
    mobile = Column(Integer(1))
    email = Column(String(50))
    forsearch = Column(String(50))

    def __init__(self, datei='', _update=''):
        self.id = 0
        self.eid = ""
        self.name = ""
        self.ename = ""
        self.title = ""
        self.subtel = ""
        self.mobile = ""
        self.email = ""
        self.forsearch = ""

    def __repr__(self):
        return "<Categories('%s')" % self.name
    
    