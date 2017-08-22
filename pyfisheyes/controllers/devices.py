# -*- coding: utf-8 -*-

import logging

from pylons import config, request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
import re
from pyfisheyes.model.utils import DeviceHandle as _dh
from pyfisheyes import model
from webhelpers import paginate
from pyfisheyes.model.utils import ViewHandle as _vh
from datetime import datetime, timedelta, date, time
from sqlalchemy import *
from sqlalchemy import schema
from sqlalchemy.exc import NoSuchTableError
log = logging.getLogger(__name__)
#from sqlalchemy.sql import select
from pychartdir import *

class DevicesController(BaseController):
    
    def index(self):
        # Return a rendered template
        #return render('/devices.mako')
        # or, return a string
        return 'Hello World'
    def list(self):
        ds = u"请输入主机名或IP或负责人"
        
        dv = model.DeviceBase
        if 'ds' in request.params:
            ds = request.params['ds']
            log.info("________________")
            log.info(type(ds))
            log.info(ds)
            '''
            if ds == u'请输入主机名或IP或负责人':
                log.info("++++++++++++++++++++++")
                log.info(ds)
                ds = ''
                '''
        if ds and ds!=u"请输入主机名或IP或负责人":
            devices = model.meta.Session.query(dv).filter(dv.hidden==0).filter(dv.for_search.like('%'+ds+'%')).order_by(dv.hostname.asc()).all()
        else:
            devices = model.meta.Session.query(dv).filter(dv.hidden==0).order_by(dv.hostname.asc()).all()
        c.pagename = "devices"
        c.heading = "主机列表"
        for x,t in enumerate(devices):
            t.cpuinfo = self.cinfo_conv(t.cpuinfo, t.cpucore);
            t.memsize = self.num_scale(t.memsize, 1000)
            t.diskspace = self.num_scale(t.diskspace,1000)
            t.hardware = self.hinfo_conv(t.hardware)
        c.ds = ds
        c.rows = paginate.Page(
            devices,
            ds = ds,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        
        return render('/derived/devices/list.html')

    def deviceItems(self):
        import datetime
        today = str(datetime.date.today())
        d =  request.params.get("d",today)
        if 'kw' in request.params:
            ditem = request.params['kw']
            rows = model.meta.Session.query(model.Devices).filter(model.Devices.ditem.like('%'+ditem+'%')).order_by(model.Devices.ditem.asc())
            #log.info(rows)
            c.rows = rows
            c.ditem = ditem
            c.date = d
            c.kw = ditem
        else:
            dsn = request.params['dsn']
            dname = request.params['dn']
            c.date = d
            c.dsn = dsn
            c.dname = dname
            d = model.Devices
            dbase = model.DeviceBase
            info = self.deviceinfo(dsn,dname)
            
            rows = model.meta.Session.query(d).filter(and_(d.dsn==dsn,d.dname==dname)).order_by(d.ditem.asc()).all()
            itemsets = model.meta.Session.query(model.DeviceItemSets).all()
            items = {}
            total = len(rows)
            for x,t in enumerate(rows):
                t.ditem = unicode(t.ditem)
                items[x] = t.ditem
                for m,n in enumerate(itemsets):
                    if t.ditem == n.item_key:
                        t.ditem = n.location_name
            c.total = total
            c.items = items
            c.rows = rows
            c.imgpath = config["app_conf"]["img_path"]
            c.pagename = 'deviceitems'
        
            c.info = info
        return render('/derived/devices/daily_report.html')
    def deviceinfo(self,sn='',dn=''):
        dbase = model.DeviceBase
        info = model.meta.Session.query(dbase).filter(and_(dbase.serial_no == sn,dbase.hostname == dn)).first()
        deviceinfo={}
        deviceinfo['id'] = info.id
        deviceinfo['serial_no'] = info.serial_no
        deviceinfo['hostname'] = info.hostname
        deviceinfo['inetaddr'] = info.inetaddr
        deviceinfo['kernel_info'] = info.kernel_info
        deviceinfo['customer'] = info.customer
        deviceinfo['cpuinfo'] = info.cpuinfo
        deviceinfo['cpucore'] = info.cpucore
        deviceinfo['memsize'] = info.memsize
        deviceinfo['diskspace'] = info.diskspace
        deviceinfo['hardware'] = info.hardware
        deviceinfo['notes'] = info.notes
        
        deviceinfo['cpuinfo'] = self.cinfo_conv(deviceinfo['cpuinfo'], deviceinfo['cpucore']);
        deviceinfo['memsize'] = self.num_scale(deviceinfo['memsize'], 1000)
        deviceinfo['diskspace'] = self.num_scale(deviceinfo['diskspace'], 1000)
        deviceinfo['hardware'] = self.hinfo_conv(deviceinfo['hardware'])
        deviceinfo['inetaddr'] = self.inetaddr_conv(deviceinfo['inetaddr'])

        return deviceinfo
    def viewData(self, id=0,item='',hostname='',date1='0000-00-00'):
        if date1 == '0000-00-00' or id == 0:
            return "error"
        date2 = datetime.strptime(date1,'%Y-%m-%d').date()-timedelta(days=7)
        date2 = date2.strftime('%Y%m%d')
        #date1 = ''.join(date1.split('-'))
        table1 = 'device_realtime_'+''.join(date1.split('-'))
        table2 = 'device_realtime_'+date2
        realtime={}
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        try:
            realtime['device_realtime1'] = schema.Table(table1, metadata, autoload=True,include_columns=['did','dthour','dtvalue'],useexisting=True)
            realtime['device_realtime2'] = schema.Table(table2, metadata, autoload=True,include_columns=['did','dthour','dtvalue'],useexisting=True)
        except NoSuchTableError:
            pass
        finally:
            chart = {}
            chart['labels'] = []
            chart['data1'] = []
            chart['data2'] = []
            chart['fmt'] =''
            chart['hostname'] = hostname
            labelsdatas1 = self.makeChartInit('00:00','23:59')
            labelsdatas2 = self.makeChartInit('00:00','23:59')
            if 'device_realtime1' in realtime:
            #if realtime.has_key('device_realtime1'):
                #device_realtime1 = schema.Table(table1, metadata, autoload=True,include_columns=['did','dthour','dtvalue'],useexisting=True)
                result1 = model.meta.Session.query(realtime['device_realtime1']).filter(realtime['device_realtime1'].c.did==int(id)).all()
                
                for x,t in enumerate(result1):
                    labelsdatas1[self.timeFormat(str(t.dthour))] = t.dtvalue
            for k,v in sorted(labelsdatas1.iteritems()):
                chart['labels'].append(k)
                if v >= 0:
                    chart['data1'].append(v)
            if 'device_realtime2' in realtime:
            #if realtime.has_key('device_realtime2'):
                #device_realtime2 = schema.Table(table2, metadata, autoload=True,include_columns=['did','dthour','dtvalue'],useexisting=True)
                result2 = model.meta.Session.query(realtime['device_realtime2']).filter(realtime['device_realtime2'].c.did==int(id)).all()
                
                for x, t in enumerate(result2):
                    labelsdatas2[self.timeFormat(str(t.dthour))] = t.dtvalue
            for k, v in sorted(labelsdatas2.iteritems()):
                if v >= 0:
                    chart['data2'].append(v)
            item_sets = model.meta.Session.query(model.DeviceItemSets).filter_by(item_key=str(item)).first()
            l = 0
            if item_sets:
                for i in range(1440):
                    if chart['data1'][i] != 1.7E+308:
                        chart['data1'][i] = chart['data1'][i] * item_sets.adjustv
                        l = max(len(str(chart['data1'][i])),l)
                    if chart['data2'][i] != 1.7E+308:
                        chart['data2'][i] = chart['data2'][i] * item_sets.adjustv
                        l = max(len(str(chart['data1'][i])),l) 
                if item_sets.short_scale:
                    if 4 <= l <7:
                        chart['fmt'] = 'K'
                        for i in range(len(chart['data1'])):
                            if chart['data1'][i] != 1.7E+308:
                                chart['data1'][i] = chart['data1'][i] / 1000.0
                            if chart['data2'][i] != 1.7E+308:
                                chart['data2'][i] = chart['data2'][i] / 1000.0
                    if 7 <= l <10:
                        chart['fmt'] = 'M'
                        for i in range(len(chart['data1'])):
                            if chart['data1'][i] != 1.7E+308:
                                chart['data1'][i] = chart['data1'][i] / 1000000.0
                            if chart['data2'][i] != 1.7E+308:
                                chart['data2'][i] = chart['data2'][i] / 1000000.0
                    if 10 <= l:
                        chart['fmt'] = 'G'
                        for i in range(len(chart['data1'])):
                            if chart['data1'][i] != 1.7E+308:
                                chart['data1'][i] = chart['data1'][i] / 1000000000.0
                            if chart['data2'][i] != 1.7E+308:
                                chart['data2'][i] = chart['data2'][i] / 1000000000.0
                if item_sets.title2 == 'percent':
                    chart['fmt'] = '%'
                    for i in range( len(chart['data1'])):
                        if chart['data1'][i] != 1.7E+308:
                            chart['data1'][i] = chart['data1'][i] / 100.0
                        if chart['data2'][i] != 1.7E+308:
                            chart['data2'][i] = chart['data2'][i] / 100.0
                chart['title1'] = item_sets.title1
                chart['title2'] = item_sets.title2
                chart['title3'] = item_sets.title3 % (date1 + ' 00:00',' 23:59')
                chart['line_color'] = item_sets.line_color
                chart['line_color2'] = 0x999999
                chart['nice_name'] = item_sets.nice_name
            else:
                chart['title1'] = item
                chart['title2'] = ''
                chart['title3'] = 'from ' + date1 + ' 00:00 to 23:59'
                chart['line_color'] = 0x336699
                chart['line_color2'] = 0x999999
                chart['nice_name'] = ''
            graph = self.makeChart(chart=chart)
                        
            response.headers['Content-type'] = 'image/png'
            return graph
    def cmpItem(self):
        c.pagename="cmpitem" 
        id = request.params['id']
        d = request.params['d']
        item = request.params['item']
        dn = request.params['dn']
        dsn = request.params['sn']
        dd = datetime.strptime(d,'%Y-%m-%d')
        dds = []
        for x in range(7):
            
            odate = dd - timedelta(days=x)
            oweekday = odate.date().weekday()
            if oweekday == 0:
                oweekday = "星期一"
            elif oweekday == 1:
                oweekday = "星期二"
            elif oweekday == 2:
                oweekday = "星期三"
            elif oweekday == 3:
                oweekday = "星期四"
            elif oweekday == 4:
                oweekday = "星期五"
            elif oweekday == 5:
                oweekday = "星期六"
            elif oweekday == 6:
                oweekday = "星期日"
            dateweek = [str(odate.date()),oweekday]
            dds.append(dateweek)
        c.dds = dds
        c.id = id
        c.item = item
        info = self.deviceinfo(dsn,dn)
        c.date = d
        c.info = info
        #c.ds =''
        return render('/derived/devices/daily_report.html')
    def devicerealtime(self):
        if 'item' in request.params:
            ditem = request.params['item']
        else:
            ditem = 'loadavg'
        if 'hn' in request.params:
            dname = request.params['hn']
        else:
            dname = ''
        c.ditem = ditem
        c.dname=''
        d = model.Devices
        if dname:
            rows = model.meta.Session.query(d).filter(and_(d.ditem.like('%'+ditem+'%'),d.dname.like('%'+dname+'%'),d.max_value>0)).order_by(d.rank.desc())
        else:
            rows = model.meta.Session.query(d).filter(and_(d.ditem.like('%'+ditem+'%'),d.max_value>0)).order_by(d.rank.desc())
        rs = rows.all()
        c.dname = dname
        c.total = rows.count()
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        d = str(datetime.now().date())
        table = ''.join(d.split('-'))
        table = 'device_realtime_'+table
        flag = 1
        c.rtime = ''
        import time
        c.reflash = ''.join(str(time.time()).split('.'))
        dt = int((datetime.now()-timedelta(minutes=15)).strftime('%H%M'))
        for x,t in enumerate(rs):
            r = schema.Table(table, metadata, autoload=True,include_columns=['id','did','dthour','dtvalue'],useexisting=True)
            result = model.meta.Session.query(r).filter(and_(r.c.did==t.id,r.c.dthour >= dt)).order_by(r.c.dthour.desc()).first()
            if result:
                while flag:
                    if len(str(result.dthour)) <4:
                        c.rtime = str(result.dthour)[0:1]+':'+str(result.dthour)[1:]
                    else:
                        c.rtime = str(result.dthour)[0:2]+':'+str(result.dthour)[2:]
                    flag = 0
                t.rank =result.dtvalue*100.0/t.max_value
                t.rank = round(t.rank,2)
            else:
                t.rank = -1
        c.rows = sorted(rs,key=lambda d:d.rank,reverse=True)
        return render('/derived/devices/realtime.html')
    def realtimeview(self, id = 0,dname ='',ditem='',maxvalue=''):
        d = str(datetime.now().date())
        table = ''.join(d.split('-'))
        table = 'device_realtime_'+table
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        dt = int((datetime.now()-timedelta(minutes=15)).strftime('%H%M'))
        try:
            t = schema.Table(table, metadata, autoload=True,include_columns=['id','did','dthour','dtvalue'],useexisting=True)
            result = model.meta.Session.query(t).filter(and_(t.c.did==id,t.c.dthour >= dt)).order_by(t.c.dthour.desc()).first()
            if result:
                
                curvalue = result.dtvalue
                graph = self.makeChart_Semi(curvalue=curvalue, dname=dname, ditem=ditem, maxvalue=maxvalue)
                response.headers['Content-type'] = 'image/png'
                return graph
            else:
                graph = self.makeChart_Semi(curvalue=0, dname=dname, ditem=ditem, maxvalue=maxvalue,nodata=True)
                response.headers['Content-type'] = 'image/png'
                return graph
        except NoSuchTableError:
            return 'no such table' 
    def editdeviceinfo(self):
        sn = request.params['sn']
        d = model.DeviceBase
        info = model.meta.Session.query(d).filter_by(serial_no=sn).first()
        if 'notes' in request.params:
            notes = request.params['notes']
            info.notes = notes
            model.meta.Session.add(info)
            model.meta.Session.commit()
            return notes
        if 'customer' in request.params:
            customer = request.params['customer']
            info.customer = customer
            model.meta.Session.add(info)
            model.meta.Session.commit()
            return customer
                  
    def searchItems(self,kw):
        kw = request.params['kw']
                  
    def timeFormat(self, t):
        #time = str(time)
        if len(t) < 4:
            c = 4 - len(t)
            b = "0" * c + t
            b = b[0:2] + ':' + b[2:4]
        else:
            b = t[0:2] + ':' + t[2:4]
        return b
    def makeChart_Semi(self,**params):
       # self.round()
        maxvalue = int(params['maxvalue'])
        value = int(params['curvalue'])*100.0/maxvalue
        text = str(params['ditem'])
        toptitle = str(params['dname'])
        if value < 60:
            m = AngularMeter(200, 125, silverColor(), 0x000000, 2)
        elif 60<= value <=80:
            m = AngularMeter(200, 125, 0xFFFF99, 0x000000, 2)
        else:
            m = AngularMeter(200, 125, 0xFFCCCC, 0x000000, 2)
        m.setMeter(100, 110, 85, -90, 90)
        m.addTitle(toptitle,'timesbi.ttf',14,0)
        # Set 0 - 60 as green (66FF66) zone
        if 'nodata' not in params:
            
            m.addZone(0, 60, 0, 85, 0x66ff66)
            
            # Set 60 - 80 as yellow (FFFF33) zone
            m.addZone(60,80 , 0, 85, 0xffff33)
            
            # Set 80 - 100 as red (FF6666) zone
            m.addZone(80, 100, 0, 85, 0xff6666)

        m.setRoundedFrame()
        
        m.setScale(0, 100, 20, 10, 5)
        m.addText(100, 80, text , "arialbd.ttf", 12, TextColor, Center)
        m.addText(156, 8, m.formatValue(value, "2"), "arial.ttf", 8, 0xffffff).setBackground(0x000000, 0, -1)
        if value<100:
            m.addPointer(value, 0x40666699, 0x000000)
        else:
            value=100
            m.addPointer(value, 0x40666699, 0x000000)
        return m.makeChart2(PNG)
    def round(self):
        import math

        #
        # Data to draw the chart. In this demo, the data buffer will be filled by a random
        # data generator. In real life, the data is probably stored in a buffer (eg. a
        # database table, a text file, or some global memory) and updated by other means.
        #
        
        # We use a data buffer to emulate the last 240 samples.
        sampleSize = 240
        dataSeries1 = [0] * sampleSize
        dataSeries2 = [0] * sampleSize
        dataSeries3 = [0] * sampleSize
        timeStamps = [0] * sampleSize
        
        # Our pseudo random number generator
        firstDate = chartTime2(time.time()) - len(timeStamps)
        for i in range(0, len(timeStamps)) :
            p = firstDate + i
            timeStamps[i] = p
            dataSeries1[i] = math.cos(p * 7 * 18463) * 10 + 1 / (math.cos(p) * math.cos(p
                ) + 0.01) + 20
            dataSeries2[i] = 100 * math.sin(p / 27.7) * math.sin(p / 10.1) + 150
            dataSeries3[i] = 100 * math.cos(p / 6.7) * math.cos(p / 11.9) + 150
    def makeChart(self, **params):
        self.round()
        c = XYChart(660,280,0xF1F1F1,0)
        plotarea = c.setPlotArea(60, 35, 550, 195,0xffffff).setGridColor(0xc0c0c0, 0xc0c0c0)
        c.addLegend(60, 255, 0, "", 8).setBackground(Transparent)
        layer = c.addLineLayer2()
       
        layer.addDataSet(params['chart']['data1'],params['chart']['line_color'],'')
        layer.addDataSet(params['chart']['data2'],params['chart']['line_color2'],'')
        c.xAxis().setLabels(params['chart']['labels'])
        c.xAxis().setLabelStyle("arial.ttf")
        c.xAxis().setLabelStep(120,60)
        c.yAxis().setWidth(2)
        c.xAxis().setWidth(2)
        c.addTitle(str(params['chart']['hostname'])+' : '+str(params['chart']['title1']),'timesbi.ttf',14,0)
        c.yAxis().setTitle(str(params['chart']['title2']))
        c.xAxis().setTitle(str(params['chart']['title3']))
        c.yAxis().setLabelFormat("{value} "+str(params['chart']['fmt']))
        return c.makeChart2(PNG)
    def makeChartInit(self,st,et):
        st = datetime.strptime(st,"%H:%M")
        et = datetime.strptime(et,"%H:%M")
        NoValue = 1.7E+308
        labelsdatas = {}
        rt = et - st
        if rt.seconds > 60:
            
            rt = rt.seconds/60
            
            for i in range(0, rt + 1):
                labelt = st + timedelta(minutes=i)
                
                label = labelt.strftime('%H:%M')
                
                labelsdatas[label] = NoValue
                
        return labelsdatas

    def num_scale(self, num, unit):
        symbol = ['','K','M','G','T','P','E','Z','Y','?']
        n = 0
        num = num * unit
        while (num > 1000):
           num = round(num / 1000, 2)
           n += 1
        if n > 9:
           n = 9  
        if n <=3:
           num = int(num)
        return str(num) + symbol[n]

    def hinfo_conv(self, h_str):
        h_str = str(h_str)
        h_str = h_str.replace("PowerEdge","")  
        h_str = h_str.replace("VMware Virtual Platform","VM")  
        h_str = h_str.strip()
        return h_str

    def cinfo_conv(self, c_str, n):
        c_str = str(c_str)
        c_str = c_str.replace("Intel(R) Xeon(R) CPU","")  
        c_str = c_str.replace("Intel(R) Core(TM) i3 CPU","")  
        c_str = c_str.strip()
        return c_str + " x " + str(n)

    def inetaddr_conv(self, addr_str):
        ips = addr_str.split(',')
        ip_1 = "0.0.0.0"
        ip_2 = ""
        for i in ips:
            if re.match("^10\.(?:10|11|0)\.\d+\.\d+$", i):
                ip_1 = i
        return [ip_1, addr_str]
    def deviceaddhtml(self):
        if 'edit' in request.params:
            c.heading = "编辑主机"
            c.pagename = "editdevice"
        else:
            c.heading ="添加主机"
            c.pagename = "adddevice"
        if 'id' in request.params:
            info = model.meta.Session.query(model.DeviceBase).filter(model.DeviceBase.id==request.params['id']).first()
            c.info = info
            log.info('++++++++++++++=')
            log.info(c.info)
        return render("/derived/devices/add.html")
    def deviceadd(self):
        if request.params['hostname'] and request.params['serial_no'] and request.params['source_ip']:
            try:
                d = model.DeviceBase
                columns = "hostname,serial_no,source_ip,domain,hardware,cpuinfo,cpucore,memsize,diskspace,netcard,inetaddr,purchased,os_info,customer,in_service,kernel_info,building, hidden,roles,rack_pos,for_search,ship_date,notes"
                values = ":hostname,:serial_no,:source_ip,:domain,:hardware,:cpuinfo,:cpucore,:memsize,:diskspace,:netcard,:inetaddr,:purchased,:os_info,:customer,:in_service,:kernel_info,:building, :hidden,:roles,:rack_pos,:for_search,:ship_date,:notes"
                result = model.meta.Session.execute("insert into device_base("+columns+") values("+values+");"
                                               , request.params, mapper=model.DeviceBase)
                redirect('/devices/list')
            except Exception,e:
                return e
        else:
            c.error = u"必填项未填！"
            c.pagename = "adddevice"
            c.heading = "添加主机"
            #return "error"
            return render('/derived/devices/add.html')
    
    def deviceedit(self):
          # d = model.DeviceBase
           d = model.meta.Session.query(model.DeviceBase).filter_by(id=request.params['id']).first()
           #d.hostname = request.params['hostname']
           #d.serial_no = request.params['serial_no']
           #d.source_ip = request.params['source_ip']
           #d.domain = request.params['domain']
           
          # d.hardware = request.params['hardware']
           #d.cpucore = request.params['cpucore']
          # d.memsize = request.params['memsize']
          # d.diskspace = request.params['diskspace']
           #d.netcard = request.params['netcard']
          # d.inetaddr = request.params['inetaddr']
          # d.purchased = request.params['purchased']
          # d.os_info = request.params['os_info']
           d.customer = request.params['customer']
          # d.in_service = request.params['in_service']
          # d.kernel_info = request.params['kernel_info']
           d.building = request.params['building']
           
          # d.hidden = request.params['hidden']
           #d.roles = request.params['roles']
           d.rack_pos = request.params['rack_pos']
          # d.for_search = request.params['for_search']
          # d.ship_date = request.params['ship_date']
           d.notes = request.params['notes']
           model.meta.Session.add(d)
           model.meta.Session.commit()
           log.info(request.params)
           redirect ('/devices/deviceItems?dsn='+request.params['serial_no_1']+'&dn='+request.params['hostname_1'])
           
           
            
