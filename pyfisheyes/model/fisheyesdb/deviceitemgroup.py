"""devicebase model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, String, VARCHAR

from pyfisheyes.model.meta import Base

class DeviceItemGroup(Base):
    __tablename__ = "device_item_group"
    
    id = Column(Integer(11), primary_key=True)
    nice_name = Column(String(50))
    location_name = Column(String(50))
    title1 = Column(String(50))
    title2 = Column(String(50))
    title3 = Column(String(50))
    short_scale = Column(Integer(11))
    chart_id = Column(Integer(11))

    def __init__(self):
        self.id = 0
        self.nice_name = ""
        self.location_name = ""
        self.title1 = ""
        self.title2 = ""
        self.title3 = ""
        self.short_scale = 0
        self.chart_id = 0
