# -*- coding: utf-8 -*-
import logging
import time,datetime
from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from webhelpers import paginate
from pyfisheyes import model

log = logging.getLogger(__name__)

class ListController(BaseController):

    def index(self):
        return ""
    
    def day(self):
        c.pagename = "day"
        categories = model.meta.Session.query(model.Categories).filter_by(graphtype="day").order_by('typeid')
        c.rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        return render("/derived/list/list.html")
    
    def hour(self):
        c.pagename = "hour"
        categories = model.meta.Session.query(model.Categories).filter_by(graphtype="hour").order_by('typeid')
        c.rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        return render("/derived/list/list.html")
    
    def host(self):
        c.pagename = "host"
        categories = model.meta.Session.query(model.Categories).filter_by(graphtype="host").order_by('typeid')
        c.rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        return render("/derived/list/list.html")
    
    def realtime(self):
        c.pagename = "realtime"
        t = model.Categories
        m = model.meta.Session.query(t).filter_by(graphtype="realtime")
        c.view_mode="fullscreen"
        c.r_typecode = {u'稳定':'10000', u'功能':'20000', u'速度':'30000'}
        if 'fullscreen' in request.params :
            page_rows = 1000
            template_name = "/derived/list/realtime.html"
        elif 'report' in request.params :
            page_rows = 1000
            template_name = "/derived/list/report.html"
            c.refresh = True 
            c.view_mode = "report" 
        elif 'viewmdays' in request.params :
            page_rows = 1
            template_name = "/derived/list/report_7days.html"
            c.refresh = True 
            c.view_mode = "viewmdays"
        elif 'montoring' in request.params :
            page_rows = 1000
            template_name = "/derived/list/realtime.html"
            c.refresh = True 
            c.view_mode = "montoring"
            if 'disrf' in request.cookies:
                c.disrf = request.cookies['disrf']
            else:
                c.disrf = 'false'
        else:
            page_rows = 20
            template_name = "/derived/list/list.html"
            
        sw = ""
        filter = ""
        t1 = 0
        t2 = ""
        filter_list = []
        if 's' in request.params :
            sw = request.params.get('s', '')
            m = m.filter(t.typename.like('%'+sw+'%'))
        if 'odate' in request.params :
            odate = request.params.get('odate', '')
            adate = datetime.datetime.strptime(odate,'%Y-%m-%d')
        else :
            adate = datetime.datetime.today()
            odate = adate.strftime('%Y-%m-%d')
        if 'typeid' in request.params :
            t1 = request.params.get('typeid', '')
        if 'typename' in request.params :
            t2 = request.params.get('typename', '')
        if 'filter' in request.params :
            filter = request.params.get('filter', '')
            filter_list = str(filter).split(',')
            m = m.filter(~t.typecode.in_(filter_list))
        c.filter_list = filter_list
       
        categories = m.order_by(t.alertlevel.desc()).order_by(t.r_weight.desc()).order_by(t.rankcode.asc())
        c.count = categories.count()
        c.sw = sw
        c.odate = odate
        c.imgpath = config["app_conf"]["img_path"]
        c.t1 = t1
        c.t2 = t2
        x = 0
        dys = 0
        if 'dys' in request.params:
            dys = int(request.params["dys"])
        else:
            dys = 7
        ldate = [adate]*dys
        rdate = [str(adate)[0:10]]*dys
        while 0 <= x < dys:
            if x == dys-1:
                ldate[x] = ldate[x-1] - datetime.timedelta(days=1)
                rdate[x] = ldate[x].strftime('%Y-%m-%d')
            else:
                ldate[x+1] = ldate[x] - datetime.timedelta(days=1)
                rdate[x+1] = ldate[x+1].strftime('%Y-%m-%d')
            x+=1
        c.rdate = rdate
        c.rows = categories
        c.rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            items_per_page = page_rows,
        )
        import random
        c.rnd = random.randint(1,1000000)
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()
        c.currentdatetime = gh.getCurrentDateTime("%H:%M:%S")
        return render(template_name)
