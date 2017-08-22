# -*- coding: utf-8 -*-
import logging
import json
import re

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from datetime import datetime, timedelta, date, time
from pyfisheyes.model.utils import DailyReportHandle as _drh

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)
from pyfisheyes import model

class DailyReportController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/daily_report.mako')
        # or, return a string
        return 'Hello'
    
    def lookup_system(self):
        drh = _drh.DailyReportHandle() 
        i = model.Dateitems
        today = datetime.now()
        y = today.strftime('%Y-%m-%d')
        odate = request.params.get('odate',y)
        if odate > y:
            abort(404)
        clearcache = request.params.get('clear','')
        disabledlazy = request.params.get('unlazy','')
        c.disabledlazy = disabledlazy
        adate = datetime.strptime(odate,'%Y-%m-%d')
        c.odate = odate
        c.imgpath = config["app_conf"]["img_path"]
        dateitems = model.meta.Session.query(i).filter_by(datei=adate).first()
        c.sr = ''
        if dateitems is None:
            #items = drh.createitems(odate)
            sort = '3'
            if 'sort' in request.params:
                sort = request.params.get('sort','3')
            items = drh.showsimitems(adate,sort)
            c.rows=items
            c.srows = []
            if 'sr' in request.params:
                c.sr = request.params["sr"]
                for x,t in enumerate (items):
                    if re.match('.*'+request.params['sr']+'.*',t.typename,re.IGNORECASE ):
                        c.srows.append(t)
            c.simp = 1             
        elif clearcache:
            items = drh.createitems(odate)
            items = drh.updateitems(adate)
        else:
            items = json.loads(dateitems.stuff)
            c.items = items
            c.sitems = []
            if 'sr' in request.params:
                c.sr = request.params["sr"]
                for x,t in enumerate (items):
                    if re.match('.*'+request.params['sr']+'.*',t[1],re.IGNORECASE):
                        c.sitems.append(t)
            c.simp = 0
            #return dateitems.stuff
            #return render("/derived/list/daily_report.html")
        return render("/derived/list/daily_report.html")
