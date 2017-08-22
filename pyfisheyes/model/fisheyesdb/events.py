"""Events model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text,DateTime

from pyfisheyes.model.meta import Base
import pyfisheyes.lib.helpers as h
import textile


class Events(Base):
    __tablename__ = "events"
   

    id = Column(Integer, primary_key=True)
    evtitle = Column(String(200))
    evdate = Column(DateTime)
    dt2 = Column(DateTime)
    dt3 = Column(DateTime)
    dt4 = Column(DateTime)
    evtags = Column(String(100))
    evtype = Column(String(20))
    evstatus = Column(String(20))
    evcause = Column(String(100))
    evminutes = Column(Integer)
    evlosspv = Column(Integer)
    evdomain = Column(String(50))
    evreporter = Column(Integer)
    evcreatedate = Column(DateTime)
    evreporterip = Column(String(20))
    evlastedit = Column(DateTime)
    evlasteditor = Column(Integer)
    evlasteditip = Column(String(20))
    evcontent = Column(Text)
    tid = Column(Integer)
    creator = Column(String(20))
    

    def __init__(self):
        self.id = 0
        self.evtitle = ""
        self.evdate = "0000-00-00 00:00:00"
        self.evtags = ""
        self.evtype = ""
        self.evstatus = ""
        self.evcause = ""
        self.evminutes = 0
        self.evlosspv = 0
        self.evdomain = ""
        self.evreporter = 0
        self.evcreatedate = "0000-00-00 00:00:00"
        self.evlastedit = "0000-00-00 00:00:00"
        self.dt2="0000-00-00 00:00:00"
        self.dt3="0000-00-00 00:00:00"
        self.dt4="0000-00-00 00:00:00"
        self.evlasteditor = 0
        self.evcontent = ""
        self.evreporterip = ""
        self.evlasteditip = ""
        self.tid = 0
        self.creator = ''

    def __repr__(self):
        return "<Events('%s')" % self.evtitle
    
    def getEvContent(self):
        try:
            content = h.literal(textile.textile(self.evcontent))
        except:
            content = ""
        return content