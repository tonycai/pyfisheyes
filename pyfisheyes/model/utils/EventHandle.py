# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
log = logging.getLogger(__name__)

class EventHandle():
    
    def __init__(self, request=None):
        self.r = request        
        
    def createEvent(self):
        e = model.Events()
        e.evtitle = self.r.params['event_name']
        e.evdate = self.r.params['d1']+' '+self.r.params['h1']+':'+self.r.params['m1']
        e.dt2 = self.r.params['d2']+' '+self.r.params['h2']+':'+self.r.params['m2']
        e.dt3 = self.r.params['d3']+' '+self.r.params['h3']+':'+self.r.params['m3']
        e.dt4 = self.r.params['d4']+' '+self.r.params['h4']+':'+self.r.params['m4']
        #e.evtags = self.r.params['event_tags']
        #e.evtype = self.r.params['event_type']
        #e.evstatus = self.r.params['event_status']
        #e.evcause = self.r.params['event_cause']
        #e.evminutes = self.r.params['event_minutes']
        #e.evlosspv = self.r.params['event_losspv']
        #e.evdomain = self.r.params['event_domain']
        e.creator = self.r.params['creator']
        gh = _gh.GlobalHandle(self.r)
        #e.evreporter = gh.getUID()
        e.evcreatedate = gh.getCurrentDateTime()
       # e.evreporterip = gh.getUserRealIP()
#        e.evlastedit = gh.getCurrentDateTime()
#        e.evlasteditor = 0       
        e.evcontent = self.r.params['event_content'] 
        #model.meta.Session.add(e)
        #result = model.meta.Session.commit()
        edict = {'evtitle':e.evtitle,
                 'evdate':e.evdate,
                 'dt2':e.dt2,
                 'dt3':e.dt3,
                 'dt4':e.dt4,
                 #'evtags':e.evtags,
                 #'evtype':e.evtype,
                 #'evstatus':e.evstatus,
                # 'evcause':e.evcause,
                # 'evminutes':e.evminutes,
                 #'evlosspv':e.evlosspv,
                # 'evdomain':e.evdomain,
                 'evcontent':e.evcontent,
                 #'evreporter':e.evreporter,
                 #'evcreatedate':e.evcreatedate,
                # 'evreporterip':e.evreporterip,
                 'creator':e.creator                 
                 } 
        columns = "evtitle,evdate,dt2,dt3,dt4,evcontent,evcreatedate,creator"
        values = ":evtitle,:evdate,:dt2,:dt3,:dt4,:evcontent,:evcreatedate,:creator"
        log.info(values)
        log.info(e.evreporter)
        result = model.meta.Session.execute("insert into events("+columns+") values("+values+");"
                                            , edict, mapper=model.Events)
        return result
    def createEImg(self, eid):
        eimg = model.ImgEvent()
        eimg.eid = int(eid)
        eimg.e_i_date = self.r.params['d1']
        eimg.imgid =self.r.params['graphs']
        eimgidlist = []
        if eimg.imgid:
            eimgidlist = eimg.imgid.split(',')
        if eimgidlist:  
            for imgid in eimgidlist:
                imgid = int(imgid)
                eimgdict =  {'eid':eimg.eid,
                             'e_i_date':eimg.e_i_date,
                             'imgid':imgid
                            }
                columns = "eid, e_i_date, imgid"
                values = ":eid, :e_i_date, :imgid"
                log.info(values)
                model.meta.Session.execute("insert into img_event("+columns+") values("+values+");"
                                                , eimgdict, mapper=model.ImgEvent)
    def modifyEImg(self, eid):
        eimg = model.ImgEvent()
        #e = model.meta.Session.query(model.ImgEvent).filter_by(eid=eid)
        eimg.eid = int(eid)
        eimg.e_i_date = self.r.params['d1']
        eimg.imgid =self.r.params['graphs']
        eimgidlist = []
        if eimg.imgid:
            eimgidlist = eimg.imgid.split(',')
        if eimgidlist:   
            for imgid in eimgidlist:
                imgid = int(imgid)
                e = model.meta.Session.query(model.ImgEvent).filter_by(eid=eid).filter_by(imgid=imgid).first()
                if e:
                    e.eid = eimg.eid
                    e.e_i_date = self.r.params['d1']
                    e.imgid = imgid
                    model.meta.Session.add(e)
                    model.meta.Session.commit()
                else:
                    imgid = int(imgid)
                    eimgdict =  {'eid':eimg.eid,
                                 'e_i_date':eimg.e_i_date,
                                 'imgid':imgid
                                }
                    columns = "eid, e_i_date, imgid"
                    values = ":eid, :e_i_date, :imgid"
                    log.info(values)
                    model.meta.Session.execute("insert into img_event("+columns+") values("+values+");"
                                                    , eimgdict, mapper=model.ImgEvent)
            
    def modifyEvent(self,id):
        e = model.meta.Session.query(model.Events).filter_by(id=id).first()
        gh = _gh.GlobalHandle(self.r)
        e.evtitle = self.r.params['event_name']
        e.evdate = self.r.params['d1']+' '+self.r.params['h1']+':'+self.r.params['m1']
        e.dt2 = self.r.params['d2']+' '+self.r.params['h2']+':'+self.r.params['m2']
        e.dt3 = self.r.params['d3']+' '+self.r.params['h3']+':'+self.r.params['m3']
        e.dt4 = self.r.params['d4']+' '+self.r.params['h4']+':'+self.r.params['m4']
       # e.evtags = self.r.params['event_tags']
       # e.evtype = self.r.params['event_type']
       # e.evstatus = self.r.params['event_status']
       # e.evcause = self.r.params['event_cause']
       # e.evminutes = self.r.params['event_minutes']
       # e.evlosspv = self.r.params['event_losspv']
       # e.evdomain = self.r.params['event_domain']
       # e.evlasteditor = gh.getUID()
        e.evlastedit = gh.getCurrentDateTime()
       # e.evlasteditip = gh.getUserRealIP()
        e.evcontent = self.r.params['event_content']
        
        model.meta.Session.add(e)
        model.meta.Session.commit()
        
        return True
    
            
    def viewEvent(self,id):
        event = model.meta.Session.query(model.Events).filter_by(id=id).first()
        if event:
            gh = _gh.GlobalHandle(self.r)
            event.evreporter = gh.getUserName(event.evreporter)
        return event
    def viewGraphs(self,id):
        g = model.ImgEvent
        graphs = model.meta.Session.query(g).filter_by(eid=int(id))
        
        return graphs
    def viewMessages(self,id):
        messages = model.meta.Session.query(model.Messages).filter_by(eid = int(id)) 
        return messages 
    def addmsg(self):
        gh = _gh.GlobalHandle(self.r)
        msg = model.Messages
         
        #msg.msgsubject = self.r.params['msgsubject']
        msg.msgcontent = self.r.params['msgcontent']
        msg.eid = self.r.params['eventid']
        msg.msgdate = gh.getCurrentDateTime()
        msgdict = {
                    #'msgsubject':msg.msgsubject,
                    'msgcontent':msg.msgcontent,
                    'eid':msg.eid,
                    'msgdate':msg.msgdate
                    
                }
        columns ="msgcontent,eid,msgdate" 
        values = ":msgcontent, :eid, :msgdate"
        log.info(values)
        model.meta.Session.execute("insert into messages("+columns+") values("+values+");"
                                                    , msgdict, mapper=model.Messages)
    def searchEvent(self,ds):
        ev = model.Events
        if ds == "0000-00-00":
            events = model.meta.Session.query(model.Events).order_by(ev.id.desc())
        else:
            events = model.meta.Session.query(model.Events).filter_by(evdate=ds).order_by(ev.id.desc())
        return events
    def isExistEvent(self,ds):
        return  model.meta.Session.query(model.Events).filter_by(evdate=ds).count()