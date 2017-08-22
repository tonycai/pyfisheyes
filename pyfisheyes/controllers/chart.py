import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes.model.chartobj import XZoneColoring as _g


log = logging.getLogger(__name__)

class ChartController(BaseController):

    def __before__(self):
        response.headers['Content-type'] = 'image/png'


    def index(self):
        return _g.XZoneColoring().display()

   
