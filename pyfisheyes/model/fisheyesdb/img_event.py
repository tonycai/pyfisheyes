"""realtime model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime

from pyfisheyes.model.meta import Base


class ImgEvent(Base):
    __tablename__ = "img_event"
    
    imgid = Column(Integer, primary_key=True)
    eid = Column(Integer, primary_key=True)
    e_i_date = Column(Date)
    
    
    def __init__(self, imgid="" ,eid="" , e_i_date="0000-00-00"):
        
        if not isinstance(imgid, unicode):
            imgid = unicode(imgid, 'utf-8')       
        if not isinstance(eid, unicode):
            eid = unicode(eid, 'utf-8')        
        if not isinstance(e_i_date, unicode):
            e_i_date = unicode(e_i_date, 'utf-8')
        
        self.imgid = imgid       
        self.eid = eid
        self.e_i_date = e_i_date