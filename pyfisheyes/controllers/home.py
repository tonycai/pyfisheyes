import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from webhelpers import paginate
from pyfisheyes import model

log = logging.getLogger(__name__)

class HomeController(BaseController):
    requires_auth = False

    def index(self):
        c.pagename = "homepage"
        
        
        return render('/derived/homepage/home.html')
