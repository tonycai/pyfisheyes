# -*- coding: utf-8 -*-
import logging

from pylons import config,request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from pyfisheyes import model
from webhelpers import paginate
import pyfisheyes.lib.helpers as h
from pyfisheyes.model.utils import ContactHandle as _ch
from turbomail import Message


log = logging.getLogger(__name__)

class ContactsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/contacts.mako')
        # or, return a string
        return 'Hello World'
    
    def list(self):
        c.pagename = "contacts"
        c.heading = "Contacts::List"
        c.qw = ""        
        log.info(config['app_conf']['my_contacts'])
        my_contacts = config['app_conf']['my_contacts']
        if len(my_contacts)>2:
            c.my_contacts = my_contacts.split(',')
        else:
            c.my_contacts = []
            
        if "qw" in request.params:
            qw = request.params['qw']
        else:
            qw = "nothing"
        c.qw = qw
        
        con = model.Contacts
        contacts = model.meta.Session.query(model.Contacts).filter(con.forsearch.like('%'+qw+'%')).order_by(con.id.asc())

        c.contacts = paginate.Page(
            contacts,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        
        return render('/derived/contacts/list.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def edit(self,id):
        assert id and isinstance(id, basestring)     
        c.pagename = "contacts"
        c.heading = "Contacts::Edit"
        c.act = 'edit'
        c.contact_id = id
        c.contact = model.meta.Session.query(model.Contacts).filter_by(id=id).first()
        return render('/derived/contacts/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def editsubmit(self,id):
        assert id and isinstance(id, basestring)
        ch = _ch.ContactHandle(request)
        qw = ""
        qw = ch.saveContact(id)
        redirect('/contacts/list/1?qw='+qw)      
        return ''
    
    @h.auth.authorize(h.auth.is_valid_user)
    def new(self):        
        c.pagename = "contacts"
        c.heading = "Contacts::New"
        c.contact = model.Contacts()     
        return render('/derived/contacts/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def newsubmit(self):
        ch = _ch.ContactHandle(request)
        qw = ch.createContact()
        redirect('/contacts/list/1?qw='+qw)     
        return ''
