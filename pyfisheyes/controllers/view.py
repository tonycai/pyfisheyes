# -*- coding: utf-8 -*-
import logging
import os
import Cookie
from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh
import pyfisheyes.lib.helpers as h
from datetime import datetime, timedelta, date

log = logging.getLogger(__name__)

class ViewController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/view.mako')
        # or, return a string
        return 'Hello World'
    
    def data(self, id, page=1, date2="", date=""):        
        #assert id and isinstance(id, basestring)
        #assert page and isinstance(page, basestring)
        #assert date and isinstance(date, basestring)
        #assert date2 and isinstance(date2, basestring)    
        if 'd2' in request.params:
            date2 = request.params['d2']
        if 'pweekday' in request.params:
            c.pweekday = "1"
        else:
            c.pweekday = '0'
        if 'ck' in request.params:
            c.ck = "1"
        else:
            c.ck = "0"
        if id and isinstance(id, basestring):
            pass
        else:
            id = 0
        if page and isinstance(page, basestring):
            pass
        else:
            page = 1
        
        if date and isinstance(date, basestring):
            pass
        else:
            date = ""
        
        if date2 and isinstance(date2, basestring):
            pass
        else:
            date2 = ""
        if 'd' in request.params :
            date2 = request.params['d']
        vh = _vh.ViewHandle()
        
        t = vh.__getConfig__(id)
        if not t:
            abort(404)
            
        date = vh.__getDate__(date, int(t.labels))
        if t.graphtype == "realtime":            
            date2 = vh.__getDate__(date2, 0)            
        else:
            date2 = vh.__getDate__(date2)
        #if request.cookies.has_key('set_default_day') and 'd2' not in request.params:
        if 'set_default_day' in request.cookies and 'd2' not in request.params:
            date2 = request.cookies['set_default_day']
        
        sw = ""
        if 's' in request.params :
            sw = request.params['s']
        
        c.sw = sw
        c.t = t
        c.list_alarm_threshold = eval(t.alarm_threshold)
        c.date = date
        c.date2 = date2
        c.imgpath = config["app_conf"]["img_path"]
        c.opt = "0"
        c.topic = t.typename
        c.template_id = t.typeid
        c.items = str(t.items).split(',')
        c.pagesize = t.labels
        c.yesterday = vh.__getDate__("")
        #if request.cookies.has_key('set_default_day'):
        if 'set_default_day' in request.cookies:
            c.set_default_day = "checked='checked'"
        else:
            c.set_default_day = ""
        if t.graphtype in ['day', 'realtime']:
            orderby = 0
        else:
            orderby = 1
        rows = vh.getRowsData(t.graphtype, t.typeid, date, date2, orderby)
        if rows == None:
            abort(404)
        
        c.pre_topic = vh.__getTopic__(id, "pre", t.graphtype)
        c.next_topic = vh.__getTopic__(id, "next", t.graphtype)
        
        c.pagename = t.graphtype
        c.datasupport = t.datasupport
        c.accessed = t.accessed
        c.from_date = date
        c.to_date = date2
        if t.graphtype == "realtime":
            c.sumvalue = vh.sumValue(rows)
        
        c.rows = paginate.Page(
            rows,
            partial='partial',
            page=page,
            date=date,
            date2=date2,
            items_per_page=30)
        events = vh.getEvents(t.typeid, date2)
        log.info('+++++++++++++++++++++++++++++++++++===')
        log.info(events)
        log.info('+++++++++++++++++++++++++++++++++++===')
        if events:
            
            c.events = events
        
        if 'partial' in request.params:                
            return render('/derived/view/onlydata.html')
        else:
            return render('/derived/view/view.html')
            #return c.events
    def graph(self, id, opt="0", date="", date2="1970-01-01", big=False):       
        assert id and isinstance(id, basestring)
        assert opt and isinstance(opt, basestring)
        assert date and isinstance(date, basestring)
        assert date2 and isinstance(date2, basestring)
        ys = request.params.get('ys','')
        today = datetime.now().strftime('%Y-%m-%d')
        
        vh = _vh.ViewHandle()
        
        t = vh.__getConfig__(id, 0)
        if not t:
            abort(404)
        
        
        if opt == "":
            opt = "0"
        
        date = vh.__getDate__(date, int(t.labels))      
        if big==False:  
            date2 = vh.__getDate__(date2)
        names = t.items.split(',')
        titles = t.titles.split(',')          
        
        if t.graphtype == "realtime":
            hidden = False
            if 'pweekday' in request.params :
                hidden = True
            if big==False:  
                gp = self.rtgrap_big(t, vh, "660x250", titles, date2, hidden, ys)
            else:
                #fsize = date2
                gp = self.rtgrap_big(t, vh, "7126x350", titles, date, hidden, ys)
        else:
            if t.graphtype == "day":
                rows = vh.getRowsData(t.graphtype, t.typeid, date, date2, 1)
            else:
                rows = vh.getRowsData(t.graphtype, t.typeid, date, date2, 0)
            
            if t.graphtype == "hour":
                date3 = vh.__getDateSub__(date2, 7)      
                rows2 = vh.getRowsData(t.graphtype, t.typeid, date, date3)
            else:
                date3 = ""
                rows2 = None
            
            if rows == None:
                abort(404)
            
            gp = vh.getGraphData(t.graphtype,
                                    rows,
                                    rows2,
                                    names,
                                    titles,
                                    opt,
                                    date,
                                    date2,
                                    date3)
        #if big==False:  
        response.headers['Content-type'] = 'image/png'
        
        if date2 == today or date == today:
            exp = timedelta(seconds=300)
            now = datetime.utcnow()
            response.headers['Cache-Control'] = 'max-age=300'
            response.headers['Expires'] = (now + exp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        elif datetime.strptime(date2,'%Y-%m-%d').date() < datetime.strptime(today,'%Y-%m-%d').date() or datetime.strptime(date2,'%Y-%m-%d').date() < datetime.strptime(today,'%Y-%m-%d').date():
            exp = timedelta(seconds=315360000)
            now = datetime.utcnow()
            response.headers['Cache-Control'] = 'max-age=315360000'
            response.headers['Expires'] = (now + exp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        else:
            exp = timedelta(seconds=0)
            now = datetime.utcnow()
            response.headers['Cache-Control'] = 'max-age=0'
            response.headers['Expires'] = (now + exp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        return gp
    
    def graph2(self, id, opt, date, fsize):       
        assert id and isinstance(id, basestring)
        assert opt and isinstance(opt, basestring)
        assert date and isinstance(date, basestring)
        assert fsize and isinstance(fsize, basestring)
        #/view/graph2/100/1/2011-04-16/660x250/1.png
        #/view/graph2/100/1/2011-04-16/7126x250/2.png
        gp = self.graph(id, opt, date, "1979-10-10", True)
        #response.headers['Content-type'] = 'image/png'
        #return "%s , %s, %s, %s" % (id, opt, date, fsize)
        return gp
    
    def realtimegraph(self, id):
        assert id and isinstance(id, basestring)
        vh = _vh.ViewHandle()
        
        t = vh.__getConfig__(id, 0)
        if not t:
            abort(404)       
        
        gp = self.rtgrap(t, vh)
        
        exp = timedelta(seconds=60)
        now = datetime.utcnow()
        response.headers['Cache-Control'] = 'max-age=60'
        response.headers['Expires'] = (now + exp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        response.headers['Content-type'] = 'image/png'
        return gp

    def rtgrap(self, t , vh, min=4, titles=None):
        vip = []
        if 'vip_justin' in request.params:
            min = 18
            vip.append (600)
        gp = None
        line1_color = 0x000080   
        timerange1 = vh.getTimeRange(min, 0)
        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
        
        
        if t.u_baseface and t.baseface:
            
            td = vh.__getDate__("", 0).split("-")
            bf = str(t.baseface).split("-")
            days = (date(int(td[0]), int(td[1]), int(td[2])) - date(int(bf[0]), int(bf[1]), int(bf[2]))).days 
            timerange2 = vh.getTimeRange(min, days)
            line2_color = 0x80ff9966L
        else:
            timerange2 = vh.getTimeRange(min, 7)
            line2_color = 0x999999
        rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)
        
        lables1 = vh.makeLabels(timerange1)
        lables2 = vh.makeLabels(timerange2)
        
        #vh.update_alert_level(rows1, t)
        allt = vh.exec_alarm_threshold(rows1, rows2, t)
        #log.info("ratio:" + str(allt[1]) + "; typeid:" + str(t.typeid))
        #self.critical_color = 0xff0000
        #self.warning_color = 0xff9900
        if int(allt[0]) == 1:
            line1_color = 0xff9900
        
        if int(allt[0]) == 2:
            line1_color = 0xff0000
            
        e_tup = (rows1, rows2, lables1, lables2, line1_color, line2_color ,vip)
        gp = vh.getRealtimeGraphData(e_tup, 'small')
        return gp
    
    def rtgrap_big(self, t , vh, fsize, titles, date1, hd, ys=''):
        
        gp = None
        if date1 == vh.__getDate__("", 0):
            c_day = True
        else:
            c_day = False
        timerange1 = vh.getSharpDayMinute(date1)
        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
        line1_color = 0x000080
        line2_color = 0x999999
        if t.u_baseface and t.baseface and c_day:
            timerange2 = vh.getSharpDayMinute(str(t.baseface))            
        else:
            timerange2 = vh.getSharpDayMinute(date1, 7)          
            
        if t.r_mode in ['c', 'd']:
            if t.u_baseface and t.baseface and c_day:
                line2_color = 0x80ff9966L
            else:
                line2_color = 0x809999ffL
        else:
            if t.u_baseface and t.baseface and c_day:
                line2_color = 0x80ff9966L
        
        lables2 = vh.makeLabels(timerange2)
        if hd:            
            rows2 = []            
        else:            
            rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)
        
        lables1 = vh.makeLabels(timerange1)
        
        date2 = date1.replace("-", "/")
        titles.append(" From " + date2 + " 00:00:00 To " + date2 + " 23:59:59")   
        list_alarm_threshold = eval(t.alarm_threshold)
        helth_range = int(list_alarm_threshold[5])
        fs = fsize.split('x')
        f_width = int(fs[0])
        f_height = int(fs[1])
        e_tup = (rows1, rows2, lables1, lables2, titles, t.critical, t.warning, False, line1_color, line2_color, t.r_mode, helth_range, f_width, f_height)
        
        gp = vh.getRealtimeGraphData(e_tup, "big",ys)
        return gp
          
    @h.auth.authorize(h.auth.is_valid_user)
    def exporttoexcel(self, id, page=1, date="", date2=""):
        assert id and isinstance(id, basestring)
        vh = _vh.ViewHandle()  
        t = vh.__getConfig__(id)
        if not t:
            abort(404)
        #/view/exporttoexcel/65/1/2011-03-11/2011-03-11    
        date = vh.__getDate__(date, int(t.labels))
        
        date2 = vh.__getDate__(date2)
        
        if t.graphtype == "realtime":
            c.columns = "N \t datei \t minute \t value" 
        else: 
            c.columns = "N"         
            items = str(t.items).split(',')
            for x, item in enumerate(items):
                c.columns += "\t" + item
        
        c.pagename = t.graphtype
        c.template_id = t.typeid
        c.typename = t.typename
        
        rows = vh.getRowsData(t.graphtype, t.typeid, date, date2)
        
        if rows == None:
            abort(404)
        
        c.rows = rows
        
        return render('/derived/view/exporttoexcel.html')
    
    def webapi(self, id):        
        assert id and isinstance(id, basestring)
        vh = _vh.ViewHandle()
        t = vh.__getConfig__(id)        
        if not t:
            abort(404)
            
        c.template_id = t.typeid
        c.typename = t.typename
        c.items = t.items.split(",")                                                                            
        c.pagename = t.graphtype     
        
        return render('/derived/view/webapi.html')
    
    def webapipost(self, id):        
        assert id and isinstance(id, basestring)
        vh = _vh.ViewHandle()
        t = vh.__getConfig__(id)        
        if not t:
            abort(404)
        from pyfisheyes.model.utils import WebAPI as _w
        WebAPI = _w.WebAPI(t, request)
                                                                                 
        if t.graphtype == "day":
            if WebAPI.SaveDataForGraphsDay():
                return WebAPI.message
        elif t.graphtype == "hour":            
            if WebAPI.SaveDataForGraphsHour():
                return WebAPI.message
        elif t.graphtype == "host":
            if WebAPI.SaveDataForGraphsHost():
                return WebAPI.message
        elif t.graphtype == "realtime":
            if WebAPI.SaveDataForGraphsRealtime():
                return WebAPI.message
        else:            
            log.debug("post error")
            
        #redirect('/view/data/' + id)    
        return "success"

