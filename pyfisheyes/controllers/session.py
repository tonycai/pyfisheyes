import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SessionController(BaseController):

    def _index(self):
        # Return a rendered template
        #return render('/session.mako')
        # or, return a string
        return 'Hello World'

    def index(self):
        name = session.get('name', 'NULL')
        return 'session name=%s' % name

    def setsession(self):
        session['name'] = 'tony'
        session.save()
        return "save session ok"
