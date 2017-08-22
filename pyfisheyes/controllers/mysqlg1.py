#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model import multiline as _m


log = logging.getLogger(__name__)

class Mysqlg1Controller(BaseController):   
    
        
    def data(self):
        try :
            page_set = int(request.params['page'])
        except:
            page_set = 1
        
        c.topic = "MySQLG1"
        #c.rows = model.meta.Session.query(model.Mysqlg1).all()
        c.rows = paginate.Page(
        model.meta.Session.query(model.Mysqlg1),
        page = page_set,
        items_per_page = 10)

        return render('/displaydata.mako')

    def graph(self):
        response.headers['Content-type'] = 'image/png'

        names = ['datei','com_update','com_insert','com_delete','com_replace']
        titles = ['数据库 - 写','queries per day','Jun 12, 2010']

        rows = model.meta.Session.query(model.Mysqlg1).all()

        return _m.Multiline(rows,names,titles).display()
