# -*- coding: utf-8 -*-

import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
from datetime import datetime, timedelta, date, time 
from sqlalchemy import schema
import time as my_time
from sqlalchemy import and_

log = logging.getLogger(__name__)

class ViewHandle():
    
    def __init__(self):
        pass     
        
    def __getDate__(self, df, interval=1):
        yesterday = datetime.now() - timedelta(days=interval)
        y = yesterday.strftime('%Y-%m-%d')
        if df == "":
            df = y
        return df
    
    def __getDateSub__(self, da, interval=1):
        log.debug("date:" + da)
        ds = da.split("-")
        d = date(
                     int(ds[0]),
                     int(ds[1]),
                     int(ds[2])
                     ) \
            - timedelta(days=interval)
        df = d.strftime('%Y-%m-%d')        
        return df
    
    def getTimeRange(self, m, d=0):
        now = datetime.now()
        interval = int(m) 
        interval2 = (1440 * int(d))
        start_time_point = now - timedelta(minutes=interval * 4) - timedelta(minutes=interval2)
        stop_time_point = now + timedelta(minutes=interval) - timedelta(minutes=interval2)
        
        return {'start_time_point':start_time_point, 'stop_time_point':stop_time_point}
    
    def getSharpDayMinute(self, date1, interval=0):
        if date1 == "":
            date1 = self.__getDate__("", 0)
        ds = date1.split("-")
        start_time_point = datetime(int(ds[0]), int(ds[1]), int(ds[2]), 0, 0) - timedelta(days=interval)
        stop_time_point = datetime(int(ds[0]), int(ds[1]), int(ds[2]), 23, 59) - timedelta(days=interval)
        
        return {'start_time_point':start_time_point, 'stop_time_point':stop_time_point}
    
    def makeLabels(self, dt):
        NoValue = 1.7E+308
        labels = {}
        start_time_point = dt['start_time_point']
        stop_time_point = dt['stop_time_point']
        td = stop_time_point - start_time_point
        if td.seconds >= 60:
            minutes = td.seconds / 60
        else:
            minutes = 0
            return labels
        for i in range(0, minutes + 1):
            ldate = start_time_point + timedelta(minutes=i)
            datestr = ldate.strftime('%Y-%m-%d')
            hour = "%02d" % ldate.hour
            minute = "%02d" % ldate.minute
            tagn = datestr + ":" + hour + ":" + minute
            labels[tagn] = NoValue
        #log.debug("labels: " + str(sorted(labels.keys())))
        return labels
    
    def hourlyLabels(self):
        NoValue = 1.7E+308
        labels = {'00':NoValue}
        for i in range(0, 24):
            hour = "%02d" % i            
            labels[hour] = NoValue
        log.debug("labels: " + str(sorted(labels.keys())))
        return labels
    
    def __getConfig__(self, id, accessed=1):
        t = model.meta.Session.query(model.Categories).filter_by(typeid=id).first()
        if t and accessed:
            t.accessed += accessed
            model.meta.Session.add(t)
            model.meta.Session.commit()
        return t    
    
    def update_alert_level(self, r, tt):        
    
        max_value = 0
        alert_level = 0
        for i, row in enumerate(r):
            if row.valuei > max_value:
                max_value = row.valuei
        
        if max_value > tt.warning and tt.warning > 0:
            alert_level = 1
        
        if max_value > tt.critical and tt.critical > 0:
            alert_level = 2
        log.debug("tt.warning:" + str(tt.warning))
        log.debug("tt.critical:" + str(tt.critical))
        log.debug("update_alert_level:" + str(alert_level))
        
        if tt and tt.alertlevel != alert_level:
            tt.alertlevel = alert_level
            model.meta.Session.add(tt)
            model.meta.Session.commit()
            log.debug("update_alert_level: update")
        return None 
    
    def exec_alarm_threshold(self, r1, r2, t):
        alert_list = [0, 0]
        if t.r_alert:
            if t.r_mode == 'a':
                alert_list = self.__analysis_a(r1, t.alarm_threshold)
            elif t.r_mode == 'b':
                alert_list = self.__analysis_b(r1, t.alarm_threshold)
            elif t.r_mode == 'c':
                alert_list = self.__analysis_c(r1, r2, t.alarm_threshold)
            elif t.r_mode == 'd':
                alert_list = self.__analysis_d(r1, r2, t.alarm_threshold)
        
        if t and t.alertlevel != int(alert_list[0]):
            t.alertlevel = int(alert_list[0])
            model.meta.Session.add(t)
            model.meta.Session.commit()
            log.debug("update_alert_level: update")
        return alert_list 
    
    def __analysis_a(self, r1, alarm_threshold):
        max_value = 0
        alert_level = 0      
        for i, row in enumerate(r1):
            if row.valuei > max_value:
                max_value = row.valuei
                
        atlt = eval(alarm_threshold)
        if max_value > int(atlt[2]) and int(atlt[2]) > 0:
            alert_level = 1
        
        if max_value > int(atlt[3]) and int(atlt[3]) > 0:
            alert_level = 2
            
        return [alert_level, max_value]
    
    def __analysis_b(self, r1, alarm_threshold):
        min_value = 1000000
        alert_level = 0      
        for i, row in enumerate(r1):
            if row.valuei < min_value:
                min_value = row.valuei
                
        atlt = eval(alarm_threshold)
        if min_value < int(atlt[1]) and int(atlt[1]) > 0:
            alert_level = 1
        
        if min_value < int(atlt[0]) and int(atlt[0]) > 0:
            alert_level = 2
            
        return [alert_level, min_value]
    
    def __analysis_c(self, r1, r2, alarm_threshold):
        alert_level = 0
        atlt = eval(alarm_threshold)
        
        v1 = self.avgValue(r1)
        v2 = self.avgValue(r2)
        
        
        if v1 <= 0:
            return [2, -100]
        if v2 <= 0:
            return [0, 0]
        
        ratio = (v1 - v2) * 100 / v2
        if ratio > 0:
            if ratio > atlt[6]:
                alert_level = 1
            if ratio > atlt[7]:
                alert_level = 2
        else:
            if abs(ratio) > atlt[5]:
                alert_level = 1
            if abs(ratio) > atlt[4]:
                alert_level = 2
        return [alert_level, ratio]
    
    def __analysis_d(self, r1, r2, alarm_threshold):
        # 09:00 - 23:30        
        min_time = my_time.strptime("09:00", "%H:%M")
        max_time = my_time.strptime("23:30", "%H:%M")
        D_max_time = self.__get_rowdata_max_time(r1)
        if min_time <= D_max_time <= max_time:
            return self.__analysis_c(r1, r2, alarm_threshold)
        else:
            return [0, 0]
    
    
    def __getTopic__(self, id, arrow="pre", type="day"):
        t_obj = model.Categories
        if arrow == "pre":
            t = model.meta.Session.query(t_obj).filter("typeid<" + str(id)).filter_by(graphtype=type).order_by(t_obj.typeid.desc()).first()
        else:
            t = model.meta.Session.query(t_obj).filter("typeid>" + str(id)).filter_by(graphtype=type).order_by(t_obj.typeid.asc()).first()                                                                                          
        return t
    
    def __get_rowdata_max_time(self, data):
        
        n = 0
        now = datetime.now()
        max_time = now.strftime('%H:%M')
        str_time = ""
        for i, d in enumerate(data):
           str_time = str(d.logtime)[11:16]
           if str_time > max_time:
               max_time = str_time
        return my_time.strptime(max_time, "%H:%M") 
        
            
    
    def getDataSet(self, cn, tid, order, w1="", sort=1, m="all"):
        
        if cn == 'Realtime':
            w2 = w1[11:21]
            rtid = int(tid[4:])
            table = self.realtimetablename(w2)
            metadata = model.meta.Base.metadata
            metadata.bind = model.meta.Session.bind
            r = schema.Table(table, metadata, autoload=True,include_columns=['id','tid','datei','houri','minutei','valuei','logtime','ts'],useexisting=True) 
            if sort:
                cgh = model.meta.Session.query(r).filter(and_(r.c.tid == rtid,r.c.datei == w2)).order_by(r.c.id.asc()).all()
            else:
                cgh = model.meta.Session.query(r).filter(and_(r.c.tid == rtid,r.c.datei == w2)).order_by(r.c.id.desc()).all()
            return cgh
        else:
            t_obj = getattr(model, cn)
            where = tid + " " + w1
            if sort:
                order_by = getattr(t_obj, order).asc()
            else:
                order_by = getattr(t_obj, order).desc()
            cgh = model.meta.Session.query(t_obj).filter(where).order_by(order_by)
            return getattr(cgh, m)()
    
    def getRowsData(self, gtype, tid, d1, d2 , s=1):
        if gtype == "day":            
            rows = self.getDataSet("Graphs", "template_id=" + str(tid), "datei", " and datei<='" + d2 + "' and datei>='" + d1 + "' ", s)                                                                              
        elif gtype == "hour":            
            rows = self.getDataSet("GraphsHour", "template_id=" + str(tid), "houri", "and datei='" + d2 + "'", s)
        elif gtype == "host":            
            rows = self.getDataSet("GraphsHost", "template_id=" + str(tid), "id", "and datei='" + d2 + "'", s)        
        elif gtype == "realtime":            
            rows = self.getDataSet("Realtime", "tid=" + str(tid), "id", "and datei='" + d2 + "'", s)
        else:
            rows = None
        return rows
    
    def getGraphData(self, gtype, r1, r2, names, titles, opt, d1, d2, d3):
        if gtype == "hour": 
            from pyfisheyes.model.chartobj import DepthAreaChart as _g
            labs = self.hourlyLabels()
            graph = _g.DepthAreaChart(r1, r2, names, titles, d2, d3, labs).display()
        elif gtype == "host":
            from pyfisheyes.model.chartobj import BorderlessBarChart as _g
            graph = _g.BorderlessBarChart(r1, names, titles, opt, d2).display()
        elif gtype == "day":
            from pyfisheyes.model.chartobj import MultiLineChart as _g
            graph = _g.MultiLineChart(r1, names, titles, opt, d1, d2).display()        
        else:
            graph = None
        return graph
    
    def getRealtimeRowsData(self, tid, timer):        
        start_time_point = timer['start_time_point']
        stop_time_point = timer['stop_time_point']
        datetime1 = start_time_point.strftime('%Y-%m-%d %H:%M:00')
        datetime2 = stop_time_point.strftime('%Y-%m-%d %H:%M:00')
        
        date1 = start_time_point.strftime('%Y-%m-%d')
        date2 = stop_time_point.strftime('%Y-%m-%d')
        log.debug("date1:" + datetime1)
        log.debug("date2:" + datetime2)
        #r = model.Realtime(tname='realtime_20110428')
        table = self.realtimetablename(date1)
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        r = schema.Table(table, metadata, autoload=True,include_columns=['id','tid','datei','houri','minutei','valuei','logtime','ts'],useexisting=True)

        if date1 == date2:
            rows = model.meta.Session.query(r).filter(r.c.tid==tid).filter(r.c.datei==date1).filter(and_(r.c.logtime >= datetime1, r.c.logtime <= datetime2)).order_by(r.c.id.asc())
        else:
            rows = model.meta.Session.query(r).filter(r.c.tid==tid).filter(and_(r.c.logtime >= datetime1, r.c.logtime <= datetime2)).order_by(r.c.id.asc())
            
        return rows
    def realtimetablename(self,date1):
        table = "realtime_"+''.join(date1.split('-'))
        
        return table
        
    def getRealtimeGraphData(self, e, gt, ys=""):
        graph = None
        if gt == "small":
            from pyfisheyes.model.chartobj import SimpleLineChart as _g
            graph = _g.SimpleLineChart(e).display()
        else:
            if e[10] in ['c','d']:
                from pyfisheyes.model.chartobj import XZoneColoring as _g
                graph = _g.XZoneColoring(e, ys).display()
            else:
                from pyfisheyes.model.chartobj import MarksAndZones2 as _g
                graph = _g.MarksAndZones2(e, ys).display()
        return graph
    
    def sumValue(self, data, n_format=True):
        v = 0
        for i, d in enumerate(data):
            v += d.valuei
        if n_format:
            return _gh.GlobalHandle().numformat(v)
        else:
            return v
        
    def avgValue(self, data):
        v = 0
        n = 0
        for i, d in enumerate(data):
            v += d.valuei
            n += 1
        if n == 0 or v == 0 :
            return 0
        return int(v/n)
    
    def getEvents(self,id,date):
        e = model.ImgEvent
        EventsId = model.meta.Session.query(e.eid).filter_by(imgid=id).filter_by(e_i_date=date)
        if EventsId:
            events = model.meta.Session.query(model.Events).filter(model.Events.id.in_(EventsId)).all()
            
        return events
        
        
        
        
          
