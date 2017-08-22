"""chartstyle model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base
class ChartStyle(Base):
    __tablename__ = "chart_style2"
    item = Column(String(20), primary_key=True)
    permin = Column(String(20))
    style = Column(String(20))
    layer = Column(Integer(11))
    layercolor = Column(Integer(11))
    
    def __init__(self):
        self.item = ''
        self.permin = 'bit per min'
        self.style = 0
        self.layer = 1 
        self.layercolor = 0x3056B830