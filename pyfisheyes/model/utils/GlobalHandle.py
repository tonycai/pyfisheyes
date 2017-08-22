# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
import datetime
import calendar
from urllib import quote
import pyfisheyes.lib.helpers as h

log = logging.getLogger(__name__)

class GlobalHandle():
    
    def __init__(self, request=None):
        self.r = request
        self.username = ""
        self.uid = 0
            
    def getUID(self):        
        if self.r.environ.get('REMOTE_USER'):
            self.username = self.r.environ.get('REMOTE_USER')
        else:
            return 0
        e = model.meta.Session.query(model.Users).filter_by(username=self.username).first()
        if e:
            self.uid = e.uid
        return self.uid
    
    def getUserName(self, uid=0):
        e = model.meta.Session.query(model.Users).filter_by(uid=uid).first()
        if e:
            self.username = e.username
        return self.username
    
    def getUserRealIP(self):
        return self.r.environ.get("X_FORWARDED_FOR", self.r.environ["REMOTE_ADDR"])
    
    def getCurrentDateTime(self, ft="%Y-%m-%d %H:%M:%S"):
        now = datetime.datetime.now()
        return now.strftime(ft)
    
    def urlencode(self, s):       
       return quote(s)
   
    def numformat(self, v):
        import re
        pattern = re.compile(r'(?<=\d)(?=(\d\d\d)+(?!\d))')
        return pattern.sub(',', str(v))
    
    def dayname(self, date):
        log.debug("date:" + date)
        d = date.split('-')
        try:
            day_name = calendar.day_name[calendar.weekday(int(d[0]), int(d[1]), int(d[2]))]
        except:
            day_name = "None"        
        return day_name[0:3]
    
    def tostringlist(self, md, sup=False):        
        from pyfisheyes.model.utils import EventHandle as _eh        
        eh = _eh.EventHandle()
        
        
        opts = md.split(',')
        for x, item in enumerate(opts):
            if x == 0:
                if sup:
                    num = eh.isExistEvent(opts[0])
                    more = ""
                    if num > 0:
                        more = " [<a href='/events/list/" + opts[x] + "'>...</a>] "
                    opts[x] = h.literal(opts[x] + " [<a href='/events/new/" + opts[x] + "'>+</a>] " + more + self.dayname(opts[x]) + "")
                else:
                    opts[x] = opts[x]
            else:
                opts[x] = self.numformat(item)
        return opts
    
    def exporttoexcel(self, md):
        formatstr = ""
        opts = md.split(',')
        for x, item in enumerate(opts):
            formatstr += "\t" + item
        return formatstr
    
    def getLogstuff(self, tid, datei, logtime):
        logstuff_id = 0
        html_content = ""     
        data = model.meta.Session.query(model.Logstuff).filter_by(tid=tid).filter_by(datei=datei).filter_by(logtime=logtime)
        for i,d in enumerate(data):
            logstuff_id = d.id
        
        if logstuff_id > 0:
            html_content = h.literal(" <a href='/logstuffshow/index/" + str(logstuff_id) + "' title='详细' target='_blank'>...</a> ")
        
        
        return html_content
