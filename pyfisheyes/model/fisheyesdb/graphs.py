"""Graph model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date
from pyfisheyes.model.meta import Base

class Graphs(Base):
    __tablename__ = "graphs"
   

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    mediadata = Column(String(200))

    def __init__(self, datei='', m=''):
        self.datei = datei
        self.mediadata = m

    def __repr__(self):
        return "<Graphs('%s')" % self.datei
    
    def tostring(self):
        return "Graphs('%s','%s','%s','%s')" % (self.id,self.template_id,self.datei,self.mediadata)
    
    def tostringlist(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.tostringlist(self.mediadata,True)
    
    def exporttoexcel(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.exporttoexcel(self.mediadata)