"""DailyReport model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime, UnicodeText

from pyfisheyes.model.meta import Base


class Dateitems(Base):
    __tablename__ = "log_report_stuff"
    
    datei = Column(Date, primary_key=True)
    stuff = Column(UnicodeText)
    create_time = Column(DateTime)
    lastupdate_time = Column(DateTime)
    
    def __init__(self, datei="00-00-00" ,stuff="" , create_time="00-00-00 00:00:00", lastupdate_time="00-00-00 00:00:00"):
        
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')       
        if not isinstance(stuff, unicode):
            stuff = unicode(stuff, 'utf-8')        
        if not isinstance(create_time, unicode):
            create_time = unicode(create_time, 'utf-8')
        if not isinstance(lastupdate_time, unicode):
            lastupdate_time = unicode(lastupdate_time, 'utf-8')
        
        self.datei = datei       
        self.stuff = stuff
        self.create_time = create_time
        self.lastupdate_time = lastupdate_time
        

    #def __repr__(self):
        #return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    

