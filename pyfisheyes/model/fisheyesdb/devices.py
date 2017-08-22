"""devices model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, Date,Text, DateTime, String, VARCHAR, UnicodeText

from pyfisheyes.model.meta import Base

class Devices(Base):
    __tablename__ = "devices"
    
    id = Column(Integer, primary_key=True)
    dname = Column(String(200))
    ditem = Column(String(200))
    dsn = Column(String(20))
    max_value = Column(Integer(11))
    rank = Column(Integer(11))
    
    def __init__(self):
        self.id = 0
        self.dname = ''
        self.ditem = ''
        self.dsn = '' 
        self.max_value = 0
        self.rank = 0
class V_Devices(Base):
    __tablename__ = "v_devices"
    
    id = Column(Integer, primary_key=True)
    dname = Column(String(200))
    ditem = Column(String(200))
    
    def __init__(self):
        self.id = 0
        self.dname = ''
        self.ditem = ''