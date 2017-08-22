import logging
import os

from pylons import config,request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes.lib.imageprocessing import ImageProcessing
from pyfisheyes.lib.helpers import md5_for_file, unchroot_path, remove_empty_dirs

from pyfisheyes.model.utils import EventHandle as _eh
from pyfisheyes import model
from webhelpers import paginate
import pyfisheyes.lib.helpers as h


log = logging.getLogger(__name__)
class AlertController(BaseController):

    def index(self):
        c.pagename = "alter"
        # Return a rendered template
        #return render('/events.mako')
        # or, return a string        
        return "404"
    
    def list(self):
        c.pagename = "alert"
        c.heading = "Alert::List"
        c.qw = ""
        if "qw" in request.params:
            qw = request.params['qw']
        else:
            qw = ""
        c.qw = qw       
        al = model.Alarminfo
        if qw:
            af = model.meta.Session.query(al).filter(al.t_name.like('%'+qw+'%')).order_by(al.logtime.desc()).order_by(al.r_weight.desc())
        else:
            af = model.meta.Session.query(al).order_by(al.logtime.desc()).order_by(al.r_weight.desc())
        c.rows = paginate.Page(
            af,
            qw=qw,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        return render("/derived/alert/list.html")
    
    def view(self,id):
        pass