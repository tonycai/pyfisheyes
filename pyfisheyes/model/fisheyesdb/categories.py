"""Categories model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, DateTime

from pyfisheyes.model.meta import Base
import re

class Categories(Base):
    __tablename__ = "categories"
   #c.categories = ['mysqlg1','apperrorlog','tmc']

    typeid = Column(Integer, primary_key=True)
    typename = Column(String(100))
    items = Column(String(100))
    titles = Column(String(200))
    classname = Column(String(100))
    labels = Column(Integer(2))
    disable = Column(Integer(1))
    orderby = Column(String(50))
    graphtype = Column(String(50))
    datasupport = Column(String(50))
    accessed =  Column(Integer)
    warning =  Column(Integer)
    critical =  Column(Integer)
    
    alertlevel =  Column(Integer)
    typecode =  Column(String(20))
    rankcode =  Column(Integer)    
    d_report = Column(Integer)
    r_alert = Column(Integer)
    r_weight = Column(Integer)
    r_mode = Column(String(10))
    r_snap = Column(DateTime)
    l_interval = Column(Integer)
    alarm_threshold = Column(String(200))
    baseface = Column(Date)
    u_baseface = Column(Integer)
    
    def __init__(self, datei='', _update=''):
        self.typeid = 0
        self.typename = ""
        self.classname = ""
        self.items = ""
        self.titles = ""
        self.labels = 0
        self.disable = 0
        self.orderby = ""
        self.graphtype = ""
        self.datasupport = ""
        self.accessed = 0
        self.warning = -1
        self.critical = -1        
        self.alertlevel = 0
        self.typecode = 0
        self.rankcode = 1000000
        self.d_report = 1
        self.r_alert = 0
        self.r_weight = 5
        self.r_mode = 'z'
        self.r_snap = '1970-01-01 00:00:00'
        self.l_interval = 300
        self.alarm_threshold = '[-1, -1, -1, -1, -1, -1, -1, -1]'
        self.baseface = '1970-01-01'
        self.u_baseface = 0
        

    def __repr__(self):
        return "<Categories('%s')" % self.typename
    
    def tostring(self):
        return "Categories('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.typeid, self.typename, self.items, self.titles, self.classname, self.labels, self.disable, self.orderby)
    
    def search_highlight(self, sw):
        import pyfisheyes.lib.helpers as h
        p = re.compile(sw,re.IGNORECASE)
        return h.literal(p.sub( '<span class="sword">'+sw+"</span>", self.typename))