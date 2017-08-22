#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model import multiline as _m

log = logging.getLogger(__name__)

class ApperrorlogController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/apperrorlog.mako')
        # or, return a string
        return 'Hello World'

    def data(self):        
        c.topic = "AppErrorLog"
        try :
            page_set = int(request.params['page'])
        except:
            page_set = 1 
        c.rows = paginate.Page(
        model.meta.Session.query(model.Apperrorlog),
        page = page_set,
        items_per_page = 10)
        
        return render('/displaydata.mako')

    def graph(self):
        response.headers['Content-type'] = 'image/png'

        names = ['datei','error']
        titles = ['生产环境中的错误日志','errors per day','Jun 12, 2010']

        rows = model.meta.Session.query(model.Apperrorlog).all()

        return _m.Multiline(rows,names,titles).display()