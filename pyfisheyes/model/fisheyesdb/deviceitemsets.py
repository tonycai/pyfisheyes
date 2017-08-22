"""devicebase model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, String, VARCHAR

from pyfisheyes.model.meta import Base

class DeviceItemSets(Base):
    __tablename__ = "device_item_sets"
    
    id = Column(Integer(11), primary_key=True)
    item_key = Column(String(50))
    nice_name = Column(String(50))
    location_name = Column(String(50))
    line_color = Column(Integer(11))
    title1 = Column(String(50))
    title2 = Column(String(50))
    title3 = Column(String(50))
    short_scale = Column(Integer(11))
    chart_id = Column(Integer(11))
    adjustv = Column(Integer(11))
    group_id = Column(Integer(11))

    def __init__(self):
        self.id = 0
        self.item_key = ""
        self.nice_name = ""
        self.location_name = ""
        self.line_color = 806458586
        self.title1 = ""
        self.title2 = ""
        self.title3 = ""
        self.short_scale = 0
        self.chart_id = 0
        self.group_id = 0
        self.adjustv = 1
