"""devicebase model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, Unicode, Date,Text, DateTime, String, VARCHAR, UnicodeText

from pyfisheyes.model.meta import Base

class DeviceBase(Base):
    __tablename__ = "device_base"
    
    id = Column(Integer(11), primary_key=True)
    hostname = Column(String(100))
    domain = Column(Integer(11))
    hardware = Column(String(100))
    cpuinfo = Column(String(100))
    cpucore = Column(Integer(11))
    memsize = Column(Integer(11))
    diskspace = Column(Integer(11))
    netcard = Column(Integer(11))
    inetaddr = Column(String(255))
    serial_no = Column(String(100))
    purchased = Column(String(100))
    os_info = Column(String(100))
    customer = Column(String(255))
    in_service = Column(Integer(11))
    notes = Column(UnicodeText())
    kernel_info = Column(String(100))
    building = Column(Integer(11))
    hidden = Column(Integer(11))
    roles = Column(Integer(11))
    for_search = Column(String(100))
    source_ip = Column(String(50))
    rack_pos = Column(String(50))
    ship_date = Column(Date)
    def __init__(self):
        self.id = 0
        self.hostname = ''
        self.domain = 0
        self.hardware = ''
        self.cpuinfo = ''
        self.cpucore = 0
        self.memsize = 0
        self.diskspace = 0
        self.netcard = 0
        self.inetaddr = ''
        self.serial_no = ''
        self.purchased = ''
        self.os_info = ''
        self.customer = ''
        self.in_service = 0
        self.notes = ''
        self.building = 0
        self.hidden = 0
        self.roles = 0
        self.for_search = ''
