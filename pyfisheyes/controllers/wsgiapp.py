import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class WsgiappController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/wsgiapp.mako')
        # or, return a string
        return 'Hello World'
