"""graphs model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base


class GraphsHost(Base):
    __tablename__ = "graphshost"
    
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    host = Column(String(50))
    mediadata = Column(String(200))
    
    def __init__(self, id='', template_id='', datei='', host='', mediadata=''):
        
        if not isinstance( template_id, unicode ):
            template_id = unicode( template_id, 'utf-8' )
        if not isinstance( datei, unicode ):
            datei = unicode( datei, 'utf-8' )
        if not isinstance( host, unicode ):
            host = unicode( host, 'utf-8' )
        if not isinstance( mediadata, unicode ):
            mediadata = unicode( mediadata, 'utf-8' )
        if not isinstance( id, unicode ):
            id  = unicode( id, 'utf-8' )

        self.id = id
        self.template_id = template_id
        self.datei = datei
        self.host = host
        self.mediadata = mediadata

    def __repr__(self):
        return u"<GraphsHost('%s, %s')" % (self.id, self.datei)    

    def tostringlist(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.tostringlist(self.mediadata,False)
    
    def exporttoexcel(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.exporttoexcel(self.mediadata)