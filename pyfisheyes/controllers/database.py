import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes import model

log = logging.getLogger(__name__)

class DatabaseController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/database.mako')
        # or, return a string
        #return 'Hello World'
        c.msgs = model.meta.Session.query(model.Msg).all()
        return render('/database.mako')

    def add(self):
        content = request.POST['content']
        msg = model.Msg()
        msg.content = content
        model.meta.Session.add(msg)
        model.meta.Session.commit()
        return "add %s ok..." % content
