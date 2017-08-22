# -*- coding: utf-8 -*-
import logging
import re

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from pyfisheyes import model
from pyfisheyes.model.utils import ViewHandle as _vh
log = logging.getLogger(__name__)

class LogstuffshowController(BaseController):

    def index(self, tid, datei, timei):
        assert tid and isinstance(tid, basestring)
        assert datei and isinstance(datei, basestring)
        assert timei and isinstance(timei, basestring)
        content = "No Content"
        totalN = 0
        
        vh = _vh.ViewHandle()
        t = vh.__getConfig__(tid, 0)
        if not t:
            abort(404)
        
        #typename = t.typename + " ("+datei+" "+timei+")\n\n"
        typename = datei + " " + timei[0:5] + "\n\n"
        
        t = model.Logstuff
        data = model.meta.Session.query(t).filter_by(tid=tid).filter_by(datei=datei).filter_by(logtime=datei + " " + timei)
        for i, d in enumerate(data):
            content = d.stuff
            
            
        
        response.headers['Content-type'] = 'text/plain'
        response.charset = 'utf8'
        p = re.compile('\n')
        res = p.sub('<br />', typename + content)

        return res
