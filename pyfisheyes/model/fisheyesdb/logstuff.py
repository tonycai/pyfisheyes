"""realtime model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime

from pyfisheyes.model.meta import Base


class Logstuff(Base):
    __tablename__ = "logstuff"
    
    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    datei = Column(Date)
    stuff = Column(Text)
    logtime = Column(DateTime)
    
    def __init__(self, id=0, tid=0, datei='0000-00-00', houri=0, minutei=0, valuei=0):
        
        if not isinstance(id, unicode):
            id = unicode(id, 'utf-8')
        if not isinstance(tid, unicode):
            tid = unicode(tid, 'utf-8') 
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')       
        if not isinstance(stuff, unicode):
            stuff = unicode(stuff, 'utf-8')        
        if not isinstance(logtime, unicode):
            logtime = unicode(logtime, 'utf-8')
        
        self.id = id
        self.tid = tid
        self.datei = datei       
        self.stuff = stuff
        self.logtime = logtime

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    

