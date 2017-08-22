import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CookieController(BaseController):

    def _index(self):
        # Return a rendered template
        #return render('/cookie.mako')
        # or, return a string
        return 'Hello World'

    def index(self):
        name = 'NULL'
        if 'name' in request.cookies:
            name = request.cookies['name']
        return 'cookie name=%s' % name

    def setcookie(self):
        response.set_cookie("name", "tony")
        #response.set_cookie(self, key, value='', max_age=None, path='/', domain=None, secure=None,
        #         httponly=False, version=None, comment=None, expires=None, overwrite=False)
        return "write cookie ok"
