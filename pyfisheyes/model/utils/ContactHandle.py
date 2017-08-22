# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh

log = logging.getLogger(__name__)

class ContactHandle():
    
    def __init__(self, request):
        self.r = request
        
        
    def createContact(self):
        p = model.Contacts()
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)        
        return qw
    
    def saveContact(self,id):
        p = model.meta.Session.query(model.Contacts).filter_by(id=id).first()       
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)
        return qw
    
            
    