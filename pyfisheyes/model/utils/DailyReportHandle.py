# -*- coding: utf-8 -*-
import logging
import json
from datetime import datetime

from pylons import request
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh
from webhelpers import paginate
log = logging.getLogger(__name__)

class DailyReportHandle():
    
    def compare_background_data(self,t,odate, min=4):
       
        vh = _vh.ViewHandle()
        date1 = vh.__getDate__(odate, 1)
                    
        timerange1 = vh.getSharpDayMinute(date1)

        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
        sum1 = self.sumValue(rows1)
                
        timerange2 = vh.getSharpDayMinute(date1, 7)

        rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)
        sum2 = self.sumValue(rows2)

        dv_ratio = 0
        level = "Norml"
        status = "同比上周同一天上涨:"
        status_n = ""
        time_range = ""

        start_time_point = timerange1['start_time_point']
        stop_time_point = timerange1['stop_time_point']
        datetime1 = start_time_point.strftime('%Y-%m-%d %H:%M:00')
        datetime2 = stop_time_point.strftime('%Y-%m-%d %H:%M:00')

        try:
            ssum = sum2 - sum1
            if ssum:
                dv_ratio = (sum2 - sum1)*100 / sum2
            else:
                dv_ratio = 0
            if dv_ratio > 0 :
                status = u"同比上周同一天下跌:"
            else:
                status = u"同比上周同一天上涨:"
        except:
            print "ZeroDivisionError"

        if abs(dv_ratio) > 10:
            level = "Warning"
        if abs(dv_ratio) > 20:
            level = "Critical"
        return (level, t.typename, t.typeid, status, datetime1, datetime2, t.r_weight, abs(dv_ratio) ,sum1)
    def my_cmp(self, E1, E2):

        return -cmp(E1[7], E2[7])
    def sumValue(self, data):
        v = 0
        for i,d in enumerate(data):
            v += d.valuei
        return v 
    def creatitems(self, odate):
        t = model.Categories
        items = []
        categories = model.meta.Session.query(t).filter_by(graphtype="realtime").order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
        for i,d in enumerate(categories):
            items.append(self.compare_background_data(d,odate))
        items.sort(self.my_cmp)
        return items 
    def saveitems(self, adate):
        odate = adate.strftime('%Y-%m-%d')
        items = self.creatitems(odate)
        j = model.Dateitems()
        j.stuff = json.dumps(items)
        j.datei = adate
        j.create_time = datetime.now()
        model.meta.Session.add(j)
        model.meta.Session.commit()
        return items
    def updateitems(self, adate):
        odate = adate.strftime('%Y-%m-%d')
        i = model.Dateitems
        dateitems = model.meta.Session.query(i).filter_by(datei=adate).first()
        items = self.creatitems(odate)
        setattr(dateitems,'stuff' ,json.dumps(items))
        setattr(dateitems,'lastupdate_time' ,datetime.now())
        model.meta.Session.commit()
        return items
    def showsimitems(self, adate, sort):
        t = model.Categories
        categories = model.meta.Session.query(t).filter_by(graphtype="realtime").filter_by(d_report=1).order_by(t.r_weight.desc()).order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
        if sort == '2':
            
            categories = model.meta.Session.query(t).filter_by(graphtype="realtime").filter_by(d_report=1).order_by(t.typeid.desc()).order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
        elif sort == '1':
            categories = model.meta.Session.query(t).filter_by(graphtype="realtime").filter_by(d_report=1).order_by(t.typeid.asc()).order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
        else:
            pass  
        rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            #items_per_page = page_rows,
            items_per_page = 1000,
        )
        return rows
    
