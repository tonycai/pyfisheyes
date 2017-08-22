"""realtime model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, DateTime

from pyfisheyes.model.meta import Base


class Realtime(Base):
    __tablename__ = "realtime"
    
    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    datei = Column(Date)
    houri = Column(Integer)
    minutei = Column(Integer)
    valuei = Column(Integer)
    logtime = Column(DateTime)
    
    def __init__(self, id=0, tid=0, datei='0000-00-00', houri=0, minutei=0, valuei=0):
        
        if not isinstance(id, unicode):
            id = unicode(id, 'utf-8')
        if not isinstance(tid, unicode):
            tid = unicode(tid, 'utf-8')
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')
        if not isinstance(houri, unicode):
            houri = unicode(houri, 'utf-8')
        if not isinstance(minutei, unicode):
            minutei = unicode(minutei, 'utf-8')
        if not isinstance(valuei, unicode):
            valuei = unicode(valuei, 'utf-8')
        if not isinstance(logtime, unicode):
            logtime = unicode(logtime, 'utf-8')
            
        self.id = id
        self.tid = tid
        self.datei = datei
        self.houri = houri
        self.minutei = minutei
        self.valuei = valuei
        self.logtime = logtime

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    def getLogstuff(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.getLogstuff(self.tid, self.datei, self.logtime)
    
    def time(self):
        time = ""
        logtime = str(self.logtime).split(' ')
        time = logtime[1]
        return time
    
    def exporttoexcel(self):        
        return u"\t %s \t %s \t %s" % (self.datei, str(self.logtime)[11:16], self.valuei)
    
    def formatValue(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.numformat(self.valuei)
