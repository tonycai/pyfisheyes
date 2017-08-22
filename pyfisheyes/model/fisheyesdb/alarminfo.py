"""pyf_alarminfo model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, Time, DateTime

from pyfisheyes.model.meta import Base


class Alarminfo(Base):
    __tablename__ = "pyf_alarminfo"
    
    
    id = Column(Integer, primary_key=True) #0
    t_name = Column(String(100))           #1
    tid = Column(Integer)                  #2
    datei = Column(Date)                   #3
    t_status = Column(String(250))         #4
    r_weight = Column(Integer)             #5
    r_mode = Column(String(20))            #6
    start_time = Column(Time)              #7
    end_time = Column(Time)                #8
    t_threshold = Column(Integer)          #9
    a_level = Column(String(50))           #10
    logtime = Column(DateTime)             #11
    
    def __init__(self, arr):
        
        t_name1 = arr[1]
        if not isinstance(arr[1], unicode):
            t_name1 = unicode(arr[1], 'utf-8')
        
        t_status1 = arr[4]
        if not isinstance(arr[4], unicode):
            t_status1 = unicode(arr[4], 'utf-8')
        
        r_mode1 = arr[6]
        if not isinstance(arr[6], unicode):
            r_mode1 = unicode(arr[6], 'utf-8')
               
        a_level1 = arr[10]   
        if not isinstance(arr[10], unicode):
            a_level1 = unicode(arr[10], 'utf-8')    
            
        #self.id = arr[0]
        self.t_name = t_name1
        self.tid = arr[2]
        self.datei = arr[3]
        self.t_status = t_status1
        self.r_weight = arr[5]
        self.r_mode = r_mode1
        self.start_time = arr[7]
        self.end_time = arr[8]
        self.t_threshold = arr[9]
        self.a_level = a_level1
        self.logtime = arr[11]

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.t_name)
    
    def t_name_urlencode(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.urlencode( self.t_name.encode('utf-8'))
    