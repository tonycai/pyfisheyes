﻿== 可视化应用层级监控系统v1.0 ==

使用说明



下载
https://sourceforge.net/projects/pyfisheyes/


安装 - window

第一步：确定各程序版本
准备好三个程序,记录请下载windows版的：mod_python mod_python-3.3.1.win32-py2.5-Apache2.2.exe
		
		这个程序要看清楚选择，我用的是：mod_python-3.3.1.win32-py2.5-Apache2.2.exe，这个版本需要配套的python2.5(还只能用2.5版，比如说你要是用2.5.2的会出错！)+apache2.2.X

		python python-2.5.msi

		apache httpd-2.2.19-win32-x86-no_ssl.msi

第二步：安装apache

安装python

再安装mod_python，安装过程中会自动寻找python的安装目录,有一个过程是要你选择apache的位置，比如说我的“D:\Program Files\Apache Software Foundation\Apache2.2”。

第三步：安装好上面的三个软件后就要配置Apache来启动mod_python了。

打开Apache安装目录下的conf/httpd.conf，做如下修改：

找到“Dynamic Shared Object (DSO) Support”行，在这下面插入：

LoadModule python_module modules/mod_python.so
<Directory "D:/Program Files/Apache Software Foundation/Apache2.2/www">
    AllowOverride FileInfo
    AddHandler mod_python .py
    PythonHandler MyTest
    PythonDebug On
</Directory> 

第一行是将mod_python.so文件加载进来，可以在modules文件夹下查看到这个文件，安装完mod_python后会生成这个文件。
第二行 "D:/Program Files/Apache Software Foundation/Apache2.2/www" 为MyTest.py的目录，也是你的文档根目录，我是在Apache2.2下建了一个名为www文件夹，并且将它设为根目录，apache默认的根目录为htdocs。
要修改为你自已定义的根目录就要将httpd.conf文件夹中：

DocumentRoot "D:/Program Files/Apache Software Foundation/Apache2.2/htdocs"

行修改为：DocumentRoot "D:/Program Files/Apache Software Foundation/Apache2.2/www"

还有别忘了修改下面这行：

找到<Directory "D:/Program Files/Apache Software Foundation/Apache2.2/htdocs">行
然后将其修改为你的根目录。

第五行中“MyTest” 是缺省的文件，比如说我建的是MyTest.py，你也可以设置为hello.py,但是要将此处改为“PythonHandler hello.py”.

用文本编辑一个python文件命名为：Mytest.py

内容：

from mod_python import apache
def handler(req):
    req.write("Hello World!")
    return apache.OK

第四步：重新启动Apache服务，在浏览器中输入：
http://localhost/MyTest.py
如果能看到Hello World！说明mod_python工作正常。


注意事项：

将MyTest.py保存为utf-8的文件格式。否则可能会出现找不到MyTest这个handler

每修改httpd.conf重启apache的时候，不要直接重启，要右击“open service”然后从本地服务重启动服务。否则有可能会找不到文件。


第五步 安装pylons

C:\Python25\python.exe "D:\virtualenv-1.1\virtualenv.py" C:\env

C:\env\Scripts\easy_install.exe PasteDeploy

C:\env\Scripts\easy_install.exe "Pylons==0.9.7"

C:\env\Scripts\easy_install.exe "SQLAlchemy==0.5"

C:\env\Scripts\paster.exe serve D:\workspace\helloworld\development.ini

C:\env\Scripts\paster.exe --reload D:\workspace\helloworld\development.ini

C:\env\Scripts\activate.bat

cd D:\workspace\

(env) D:\workspace>C:\env\Scripts\paster.exe create -t pylons helloworld_mysql
Selected and implied templates:
  pylons#pylons  Pylons application template

Variables:
  egg:      helloworld2
  package:  helloworld2
  project:  helloworld2
Enter template_engine (mako/genshi/jinja2/etc: Template language) ['mako']:
Enter sqlalchemy (True/False: Include SQLAlchemy 0.5 configuration) [False]:
Creating template pylons
Creating directory .\helloworld2
  Recursing into +package+

cd helloworld_mysql
cd D:\workspace\helloworld2\
C:\env\Scripts\paster.exe serve --reload development.ini

C:\env\Scripts\easy_install.exe "Pylons==0.9.7"

第六步

开机后重启activate.bat：
打开cmd
C:\env\Scripts\activate.bat

C:\Documents and Settings\hyhe>C:\env\Scripts\activate.bat
(env) C:\Documents and Settings\hyhe>D:

(env) D:\>cd workspace

(env) D:\workspace>cd new_project

(env) D:\workspace\new_project>C:\env\Scripts\paster.exe serve --reload development.ini



安装 – Linux
源码安装
 $ tar -xzvf pyfisheyes-0.1dev-r388.tar.gz
 $ cd pyfisheyes-0.1dev-r388

$ easy_install .
Processing .
Running setup.py -q bdist_egg --dist-dir /home/tonycai/pyfisheyes-0.1dev-r388/egg-dist-tmp-S_jQ1y
Adding pyfisheyes 0.1dev-r388 to easy-install.pth file

Installed /home/tonycai/pylons/mydevenv/lib/python2.6/site-packages/pyfisheyes-0.1dev_r388-py2.6.egg
Processing dependencies for pyfisheyes==0.1dev-r388
Finished processing dependencies for pyfisheyes==0.1dev-r388


二进制文件安装
$ easy_install ./pyfisheyes-0.1dev_r392-py2.6.egg
Processing pyfisheyes-0.1dev_r392-py2.6.egg
creating /home/tonycai/pylons/mydevenv/lib/python2.6/site-packages/pyfisheyes-0.1dev_r392-py2.6.egg
Extracting pyfisheyes-0.1dev_r392-py2.6.egg to /home/tonycai/pylons/mydevenv/lib/python2.6/site-packages
Removing pyfisheyes 0.1dev-r391 from easy-install.pth file
Adding pyfisheyes 0.1dev-r392 to easy-install.pth file

Installed /home/tonycai/pylons/mydevenv/lib/python2.6/site-packages/pyfisheyes-0.1dev_r392-py2.6.egg
Processing dependencies for pyfisheyes==0.1dev-r392
Finished processing dependencies for pyfisheyes==0.1dev-r392

生成配置文件

$ paster make-config pyfisheyes production.ini


代码部分


##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/simplebar.py
##########################################
"""Simplebar model"""

from pychartdir import *

class Simplebar:
    def __init__(self):
        # The data for the bar chart
        self.data = [85, 156, 179.5, 211, 123]
        
        # The labels for the bar chart
        self.labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(250, 250)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(30, 20, 200, 200)
        
        # Add a bar chart layer using the given data
        self.c.addBarLayer(self.data)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(self.labels)

    def display(self):
        return self.c.makeChart2(PNG)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/__init__.py
##########################################
"""The application's model objects"""
from pyfisheyes.model.meta import Session, Base

from pyfisheyes.model.fisheyesdb.categories import Categories
from pyfisheyes.model.fisheyesdb.graphs import Graphs
from pyfisheyes.model.fisheyesdb.graphshour import GraphsHour
from pyfisheyes.model.fisheyesdb.graphshost import GraphsHost
from pyfisheyes.model.fisheyesdb.events import Events
from pyfisheyes.model.fisheyesdb.users import Users
from pyfisheyes.model.fisheyesdb.contacts import Contacts
from pyfisheyes.model.fisheyesdb.realtime import Realtime
from pyfisheyes.model.fisheyesdb.logstuff import Logstuff
from pyfisheyes.model.fisheyesdb.alarminfo import Alarminfo
from pyfisheyes.model.fisheyesdb.dateitems import Dateitems

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/ContactHandle.py
##########################################
# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh

log = logging.getLogger(__name__)

class ContactHandle():
    
    def __init__(self, request):
        self.r = request
        
        
    def createContact(self):
        p = model.Contacts()
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)        
        return qw
    
    def saveContact(self,id):
        p = model.meta.Session.query(model.Contacts).filter_by(id=id).first()       
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)
        return qw
    
            
    
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/EventHandle.py
##########################################
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
        e.evdate = self.r.params['event_date']
        e.evtags = self.r.params['event_tags']
        e.evtype = self.r.params['event_type']
        e.evstatus = self.r.params['event_status']
        e.evcause = self.r.params['event_cause']
        e.evminutes = self.r.params['event_minutes']
        e.evlosspv = self.r.params['event_losspv']
        e.evdomain = self.r.params['event_domain']
        gh = _gh.GlobalHandle(self.r)
        e.evreporter = gh.getUID()
        e.evcreatedate = gh.getCurrentDateTime()
        e.evreporterip = gh.getUserRealIP()
#        e.evlastedit = gh.getCurrentDateTime()
#        e.evlasteditor = 0       
        e.evcontent = self.r.params['event_content'] 
        #model.meta.Session.add(e)
        #result = model.meta.Session.commit()
        edict = {'evtitle':e.evtitle,
                 'evdate':e.evdate,
                 'evtags':e.evtags,
                 'evtype':e.evtype,
                 'evstatus':e.evstatus,
                 'evcause':e.evcause,
                 'evminutes':e.evminutes,
                 'evlosspv':e.evlosspv,
                 'evdomain':e.evdomain,
                 'evcontent':e.evcontent,
                 'evreporter':e.evreporter,
                 'evcreatedate':e.evcreatedate,
                 'evreporterip':e.evreporterip,                 
                 } 
        columns = "evtitle,evdate,evtags,evtype,evstatus,evcause,evminutes,evlosspv,evdomain,evcontent,evreporter,evcreatedate,evreporterip"
        values = ":evtitle,:evdate,:evtags,:evtype,:evstatus,:evcause,:evminutes,:evlosspv,:evdomain,:evcontent,:evreporter,:evcreatedate,:evreporterip"
        log.info(values)
        log.info(e.evreporter)
        result = model.meta.Session.execute("insert into events("+columns+") values("+values+");"
                                            , edict, mapper=model.Events)
        return result
    
    def modifyEvent(self,id):
        e = model.meta.Session.query(model.Events).filter_by(id=id).first()
        gh = _gh.GlobalHandle(self.r)
        e.evtitle = self.r.params['event_name']
        e.evdate = self.r.params['event_date']
        e.evtags = self.r.params['event_tags']
        e.evtype = self.r.params['event_type']
        e.evstatus = self.r.params['event_status']
        e.evcause = self.r.params['event_cause']
        e.evminutes = self.r.params['event_minutes']
        e.evlosspv = self.r.params['event_losspv']
        e.evdomain = self.r.params['event_domain']
        e.evlasteditor = gh.getUID()
        e.evlastedit = gh.getCurrentDateTime()
        e.evlasteditip = gh.getUserRealIP()
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
    
    def searchEvent(self,ds):
        ev = model.Events
        if ds == "0000-00-00":
            events = model.meta.Session.query(model.Events).order_by(ev.id.desc())
        else:
            events = model.meta.Session.query(model.Events).filter_by(evdate=ds).order_by(ev.id.desc())
        return events
    def isExistEvent(self,ds):
        return  model.meta.Session.query(model.Events).filter_by(evdate=ds).count()
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/GlobalHandle.py
##########################################
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

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/ViewHandle.py
##########################################
# -*- coding: utf-8 -*-

import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
from datetime import datetime, timedelta, date, time 

import time as my_time


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
        r = model.Realtime
        from sqlalchemy import and_
        if date1 == date2:
            rows = model.meta.Session.query(r).filter_by(tid=tid).filter_by(datei=date1).filter(and_(r.logtime >= datetime1, r.logtime <= datetime2)).order_by(r.id.asc())
        else:
            rows = model.meta.Session.query(r).filter_by(tid=tid).filter(and_(r.logtime >= datetime1, r.logtime <= datetime2)).order_by(r.id.asc())
            
        return rows
    
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
    


##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/WebAPI.py
##########################################
# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model

log = logging.getLogger(__name__)

class WebAPI():
    
    def __init__(self, template,request):
        self.t = template
        self.r = request
        self.date = "1999-01-01"
        self.host = ""
        self.hour = ""
        if "datei" in self.r.POST:
            self.date = self.r.POST['datei']
        if "houri" in self.r.POST:
            self.hour = self.r.POST['houri']
        if "host" in self.r.POST:
            self.host = self.r.POST['host']
        self.templateid = template.typeid
        self.gh = None
        self.message = ""
        log.info("self.date=" + self.date)
        log.info("self.hour=" + self.hour)
        log.info("self.templateid=" + str(self.templateid))
        #model.meta.Session.query(model.GraphsHou).filter_by(datei=self.date).filter_by(template_id=self.templateid).filter_by(houri=self.hour).first()
        
        
    def __CheckFormat__(self):
        items = self.t.items.split(",")
        for item in items:
            if item not in self.r.POST:
                self.message = "INVALID FORMAT"
                return False
            else:
                if self.r.POST[item] == "":
                    self.message = "%s : Content Feed Error" % item
                    return False
        return True

## Hour ##    
    def __isExistHour__(self):
        n = model.meta.Session.query(model.GraphsHour).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).count()
        if n > 0:
            return True
        else:
            return False
    
    def __setMediaData__(self):
        items = self.t.items.split(",")
        self.gh.mediadata = ""
        for item in items:
            if not len(self.gh.mediadata):
                self.gh.mediadata = self.r.POST[item]
            else:
                self.gh.mediadata += "," + self.r.POST[item]
        
    def SaveDataForGraphsHour(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsHourInsert()
        return self.message
    
    def SaveDataForGraphsHourUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.GraphsHour).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsHourInsert(self):
        if not self.__isExistHour__():
            try:
                items = self.t.items.split(",")
                self.gh = model.GraphsHour()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.houri = self.r.POST['houri']
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHourUpdate()                
        return True

## Day ##
    def SaveDataForGraphsDay(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsDayInsert()
        return self.message
    
    def SaveDataForGraphsDayUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.Graphs).filter_by(template_id=self.templateid).filter_by(datei=self.date).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsDayInsert(self):
        if not self.__isExistDay__():
            try:
                items = self.t.items.split(",")
                self.gh = model.Graphs()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']     
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsDayUpdate()                
        return True
    
    def __isExistDay__(self):
        n = model.meta.Session.query(model.Graphs).filter_by(template_id=self.templateid).filter_by(datei=self.date).count()
        if n > 0:
            return True
        else:
            return False
        
## Host ##
    def SaveDataForGraphsHost(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsHostInsert()
        return self.message
    
    def SaveDataForGraphsHostUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.GraphsHost).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(host=self.host).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsHostInsert(self):
        if not self.__isExistHost__():
            try:
                items = self.t.items.split(",")
                self.gh = model.GraphsHost()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.host = self.r.POST['host']
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHostUpdate()                
        return True
    
    def __isExistHost__(self):
        n = model.meta.Session.query(model.GraphsHost).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(host=self.host).count()
        if n > 0:
            return True
        else:
            return False
        
## Realtime ##
    def SaveDataForGraphsRealtime(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsRealtimeInsert()
        return self.message
    
    def SaveDataForGraphsRealtimeUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.Realtime).filter_by(tid=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).filter_by(minutei=self.minute).first()
            self.gh.valuei = self.r.POST['value']
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsRealtimeInsert(self):
        if not self.__isExistHost__():
            try:
                items = self.t.items.split(",")
                self.gh = model.Realtime()
                self.gh.tid = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.houri = self.r.POST['hour']
                self.gh.minutei = self.r.POST['minute']
                self.gh.valuei = self.r.POST['value']
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHostUpdate()                
        return True
    
    def __isExistRealtime__(self):
        n = model.meta.Session.query(model.Realtime).filter_by(tid=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).filter_by(minutei=self.minute).count()
        if n > 0:
            return True
        else:
            return False
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/utils/DailyReportHandle.py
##########################################
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
    def showsimitems(self, adate):
        t = model.Categories
        categories = model.meta.Session.query(t).filter_by(graphtype="realtime").filter_by(d_report=1).order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
        rows = paginate.Page(
            categories,
            page=int(request.params.get('page', 1)),
            #items_per_page = page_rows,
            items_per_page = 1000,
        )
        return rows
    

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/categories.py
##########################################
"""Categories model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base

class Categories(Base):
    __tablename__ = "categories"
   #c.categories = ['mysqlg1','apperrorlog','tmc']

    typeid = Column(Integer, primary_key=True)
    typename = Column(String(100))
    items = Column(String(100))
    titles = Column(String(200))
    classname = Column(String(100))
    labels = Column(Integer(2))
    disable = Column(Integer(1))
    orderby = Column(String(50))

    def __init__(self, datei='', _update=''):
        self.typeid = 0
        self.typename = ""
        self.classname = ""
        self.items = ""
        self.titles = ""
        self.labels = 0
        self.disable = 0
        self.orderby = ""
        

    def __repr__(self):
        return "<Categories('%s')" % self.typename
    
    def tostring(self):
        return "Categories('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.typeid,self.typename,self.items,self.titles,self.classname,self.labels,self.disable,self.orderby)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/multiline.py
##########################################
#coding=utf-8
"""Multiline model"""

"""四、中文处理

中文是非常重要的一点。而ChartDirector很好的支持了unicode，你可以使用utf-8编码的程序，在程序前加上：#coding=utf-8，并且保存程序为utf-8编码。有些方法提供对字体的设置，如addTitle(‘中文’, ’simsun.ttc’, 15)，第二个参数就是字体文件(simsun.ttc就是宋体字体的文件名)，它不使用字体名称。那么如果你想整个字体都为中文字体的话，可以使用：setDefaultFonts(’simsun.ttc’)，这样整个图都使用宋体了。
"""

from pychartdir import *
from datetime import date


class Multiline:
    def __init__(self,l,names,titles,opt="0"):
        # The data for the line chart
        #names = ['datei','com_update','com_insert','com_delete','com_replace']
        #names = ['datei','com_update','com_insert']

        #titles = ['数据库 - 写','queries per day','Jun 12, 2010']

        #for na in range(len(names)):
        #    print na,names[na],"test"
        opts = opt.split(',')
        data = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        i = 0
        
        try:
            for i,r in enumerate(l):
                mediadata = str(r.mediadata)
                ds =  mediadata.split(',')
                for na in range(len(names)):
                    data[str(na)].append(str(ds[na]))                
        except:
            data['0'] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
            data['1'] = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
            i = 24
        
        # The data for the line chart
        #self.data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
        #self.data1 = [50, 55, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73, 77, 84, 82, 80, 84, 98]
        #self.data2 = [36, 28, 25, 33, 38, 20, 22, 30, 25, 33, 30, 24, 28, 15, 21, 26, 46, 42, 48, 45, 43, 52, 64, 60, 70]
        
        # The labels for the line chart
        self.labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create an XYChart object of size 600 x 300 pixels, with a light blue (EEEEFF)
        # background, black border, 1 pxiel 3D border effect and rounded corners
        if i < 60:
            i = 60
        self.width = 700
        self.height = 250
        self.c = XYChart(self.width, self.height, 0xeeeeff, 0x000000, 1)
        self.c.setRoundedFrame()
        
        # Set the plotarea at (55, 58) and of size 520 x 195 pixels, with white background.
        # Turn on both horizontal and vertical grid lines with light grey color (0xcccccc)
        self.c.setPlotArea(80, 58, self.width-90, self.height-100, 0xffffff, -1, -1, 0xcccccc, 0xcccccc)
        
        # Add a legend box at (50, 30) (top of the chart) with horizontal layout. Use 9 pts
        # Arial Bold font. Set the background and border color to Transparent.
        self.c.addLegend(70, 30, 0, "arialbd.ttf", 9).setBackground(Transparent)
        
        # Add a title box to the chart using 15 pts Times Bold Italic font, on a light blue
        # (CCCCFF) background with glass effect. white (0xffffff) on a dark red (0x800000)
        # background, with a 1 pixel 3D border.
        #self.c.addTitle("Application Server Throughput", "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        self.c.addTitle(titles[0], "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(titles[1])
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data['0'])
        
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(20)
        
        # Add a title to the x axis
        d = date.today()

        self.c.xAxis().setTitle(str(d.strftime("%A %d. %B %Y")))
        
        # Add a line layer to the chart
        self.layer = self.c.addLineLayer2()
        
        # Set the default line width to 2 pixels
        self.layer.setLineWidth(2)
        
        # Add the three data sets to the line layer. For demo purpose, we use a dash line
        # color for the last line
        for na in range(len(names)):            
            if na > 0:
                if str(na) not in opts:
                    self.layer.addDataSet(data[str(na)], -1, names[na])


    def display(self):
        return self.c.makeChart2(PNG)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/apperrorlog.py
##########################################
"""Apperrorlog model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base

class Apperrorlog(Base):
    __tablename__ = "apperrorlog"
   

    id = Column(Integer, primary_key=True)
    datei = Column(Date)
    error = Column(Integer(10))
    

    def __init__(self, datei='', error=''):
        self.datei = datei
        self.error = error

    def __repr__(self):
        return "<Apperrorlog('%s')" % self.datei
    def tostring(self):
        return "Apperrorlog('%s','%s','%s')" % (self.id,self.datei,self.error)
"""
http://www.sqlalchemy.org/docs/05/mappers.html#customizing-column-properties
companies = Table('companies', metadata,
   Column('id', Integer, primary_key=True),
   Column('name', String(50)))

employees_table = Table('employees', metadata,
    Column('employee_id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('company_id', Integer, ForeignKey('companies.id'))
)

managers_table = Table('managers', metadata,
    Column('employee_id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('manager_data', String(50)),
    Column('company_id', Integer, ForeignKey('companies.id'))
)

engineers_table = Table('engineers', metadata,
    Column('employee_id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('engineer_info', String(50)),
    Column('company_id', Integer, ForeignKey('companies.id'))
)

mapper(Employee, employees_table, with_polymorphic=('*', pjoin), polymorphic_on=pjoin.c.type, polymorphic_identity='employee')
mapper(Manager, managers_table, inherits=employee_mapper, concrete=True, polymorphic_identity='manager')
mapper(Engineer, engineers_table, inherits=employee_mapper, concrete=True, polymorphic_identity='engineer')
mapper(Company, companies, properties={
    'employees': relation(Employee)
})


"""
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/mysqlg1.py
##########################################
"""Mysqlg1 model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base

class Mysqlg1(Base):
    __tablename__ = "mysqlg1"

    id = Column(Integer, primary_key=True)
    datei = Column(Date)
    com_update = Column(Integer(10))
    com_insert = Column(Integer(10))
    com_delete = Column(Integer(10))
    com_replace = Column(Integer(10))

    def __init__(self, datei='', com_update=''):
        self.datei = datei
        self.com_update = com_update

    def __repr__(self):
        return "<Mysqlg1('%s')" % self.datei

    def tostring(self):
        return "Mysqlg1('%s','%s','%s','%s','%s','%s')" % (self.id,self.datei,self.com_update,self.com_insert,self.com_delete,self.com_replace)



##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/graphs.py
##########################################
"""Apperrorlog model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base

import calendar

class Graphs(Base):
    __tablename__ = "graphs"
   

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    mediadata = Column(String(200))
    
    

    def __init__(self, datei='', m=''):
        self.datei = datei
        self.mediadata = m

    def __repr__(self):
        return "<Graphs('%s')" % self.datei
    
    def __numformat__(self,v):
        import re
        pattern = re.compile(r'(?<=\d)(?=(\d\d\d)+(?!\d))')
        return pattern.sub(',', str(v))
    def __dayname__(self,date):
        d = date.split('-')
        try:
            day_name = calendar.day_name[calendar.weekday(int(d[0]),int(d[1]),int(d[2]))]
        except:
            day_name = "None"
            
        
        return day_name[0:3]
    
    def tostring(self):
        return "Graphs('%s','%s','%s','%s')" % (self.id,self.template_id,self.datei,self.mediadata)
    
    def tostringlist(self):
        #unicode.isnumeric()
        #for x,item in enumerate(c.items):
        opts = self.mediadata.split(',')
        for x,item in enumerate(opts):
            if x == 0:
               opts[x] = opts[x] + " #" + self.__dayname__(opts[x])  + ""
            else:
                opts[x] = self.__numformat__(item)
        return opts
    
    def exporttoexcel(self):
        formatstr = ""
        opts = self.mediadata.split(',')
        for x,item in enumerate(opts):
            formatstr += "\t" + item
        return formatstr
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/simpleline.py
##########################################
"""Simpleline model"""

from pychartdir import *

class Simpleline:
    def __init__(self,l):
        # The data for the line chart
        data = []
        labels = []
        for r in l:
            data.append(r.com_update) 
            labels.append(str(r.datei)) 

        #self.data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 91, 60, 55, 53, 35, 50, 66, 56, 48, 52, 65, 62]
        #self.labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]


        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(950, 450)

        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(80, 20, 800, 250)

        # Add a line chart layer using the given data
        self.c.addLineLayer(data)

        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)

        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(3)

    def display(self):
        return self.c.makeChart2(PNG)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/meta.py
##########################################
"""SQLAlchemy Metadata and Session object"""
from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

__all__ = ['Session', 'metadata', 'Base']

# SQLAlchemy session manager. Updated by model.init_model()
Session = scoped_session(sessionmaker())

# Global metadata. If you have multiple databases with overlapping table
# names, you'll need a metadata for each database
metadata = MetaData()

# The declarative Base
Base = declarative_base()

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/PieChartWithLegend.py
##########################################
from pychartdir import *

class PieChartWithLegend:
    
    def __init__(self):
        # The data for the pie chart
        data = [25, 18, 15, 12, 8, 30, 35]
        
        # The labels for the pie chart
        labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
            "Production"]
        
        # Create a PieChart object of size 450 x 240 pixels
        self.c = PieChart(450, 240)
        
        # Set the center of the pie at (150, 100) and the radius to 80 pixels
        self.c.setPieSize(150, 100, 80)
        
        # Add a title at the bottom of the chart using Arial Bold Italic font
        self.c.addTitle2(Bottom, "Project Cost Breakdown", "arialbi.ttf")
        
        # Draw the pie in 3D
        self.c.set3D()
        
        # add a legend box where the top left corner is at (330, 40)
        self.c.addLegend(330, 40)
        
        # modify the label format for the sectors to $nnnK (pp.pp%)
        self.c.setLabelFormat("{label} ${value}K\n({percent}%)")
        
        # Set the pie data and the pie labels
        self.c.setData(data, labels)
        
        # Explode the 1st sector (index = 0)
        self.c.setExplode(0)
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/SimplePieChart.py
##########################################
from pychartdir import *

class SimplePieChart:
    
    def __init__(self):
        # The data for the pie chart
        data = [25, 18, 15, 12, 8, 30, 35]
        
        # The labels for the pie chart
        labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
            "Production"]
        
        # Create a PieChart object of size 360 x 300 pixels
        self.c = PieChart(360, 300)
        
        # Set the center of the pie at (180, 140) and the radius to 100 pixels
        self.c.setPieSize(180, 140, 100)
        
        # Set the pie data and the pie labels
        self.c.setData(data, labels)
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/StackedAreaChart.py
##########################################
from pychartdir import *

class StackedAreaChart:
    
    def __init__(self):
        # The data for the area chart
        data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70,
            76, 63, 67, 75, 64, 51]
        data1 = [50, 45, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73,
            77, 84, 82, 80, 84, 89]
        
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create a XYChart object of size 300 x 210 pixels. Set the background to pale yellow
        # (0xffffc0) with a black border (0x0)
        self.width = 700
        self.height = 250
        self.c = XYChart(self.width, self.height, 0xffffc0, 0x000000)
        
        # Set the plotarea at (50, 30) and of size 240 x 140 pixels. Use white (0xffffff)
        # background.
        self.c.setPlotArea(50, 30, self.width-60, self.height-70).setBackground(0xffffff)
        
        # Add a legend box at (50, 185) (below of plot area) using horizontal layout. Use 8
        # pts Arial font with Transparent background.
        self.c.addLegend(50, self.height-30, 0, "", 8).setBackground(Transparent)
        
        # Add a title box to the chart using 8 pts Arial Bold font, with yellow (0xffff40)
        # background and a black border (0x0)
        self.c.addTitle("Sales Volume", "arialbd.ttf", 8).setBackground(0xffff40, 0)
        
        # Set the y axis label format to US$nnnn
        self.c.yAxis().setLabelFormat("US${value}")
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)
        
        # Display 1 out of 2 labels on the x-axis. Show minor ticks for remaining labels.
        self.c.xAxis().setLabelStep(2, 1)
        
        # Add an stack area layer with three data sets
        layer = self.c.addAreaLayer2(Stack)
        layer.addDataSet(data0, 0x4040ff, "Store #1")
        layer.addDataSet(data1, 0xff4040, "Store #2")
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/XZoneColoring.py
##########################################
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class XZoneColoring:
    
    def __init__(self, et, ys=""):
        self.l1 = et[0] 
        self.l2 = et[1] 
        self.labs1 = et[2] 
        self.labs2 = et[3] 
        self.titles = et[4] 
        self.critical = et[5] 
        self.warning = et[6] 
        self.marks = et[7]
        self.line1_color = et[8]
        self.line2_color = et[9]
        self.r_mode = et[10]
        self.helth_range = et[11]
        self.f_width = et[12]
        self.f_height = et[13]
        self.ys = ys
        data1 = self.__datafact__(self.l1, self.labs1, True)
        data2 = self.__datafact__(self.l2, self.labs2, True)
        
        # Create a XYChart object of size 550 x 220 pixels
        self.width = self.f_width #660
        self.height = self.f_height #250
        
        self.c = XYChart(self.width, self.height)
        
        # Set the plot area at (50, 10) and of size 480 x 180 pixels. Enabled both vertical
        # and horizontal grids by setting their colors to light grey (cccccc)
        self.c.setPlotArea(60, 25, self.width - 70, self.height - 60).setGridColor(0xcccccc, 0xcccccc, 0xc0c0c0, 0xc0c0c0)
        
        # Add a legend box (50, 10) (top of plot area) using horizontal layout. Use 8 pts
        # Arial font. Disable bounding box (set border to transparent).
        legendBox = self.c.addLegend(60, 20, 0, "", 8)
        legendBox.setBackground(Transparent)
        
        # Add keys to the legend box to explain the color zones
        #legendBox.addKey("today", 0x333399)
        legendBox.addKey("Tolerant", self.line2_color) #tolerant Historical
        #legendBox.addKey("Forecast", 0xff9966)
        
        # Add a title to the y axis.
        self.c.addTitle(str(self.titles[0]), "timesbi.ttf", 14)
        self.c.yAxis().setTitle(str(self.titles[1]))        
        self.c.xAxis().setTitle(str(self.titles[2]) + " (" + str(self.width) + "x" + str(self.height) + ")")
        
        # Set the labels on the x axis
        #self.c.xAxis().setLabels2(data2['labels'])
        self.c.xAxis().setLabels(data2['labels'])
        
        # Set multi-style axis label formatting. Use Arial Bold font for yearly labels and
        # display them as "yyyy". Use default font for monthly labels and display them as
        # "mmm". Replace some labels with minor ticks to ensure the labels are at least 3
        # units apart.
        step = data2['n'] / ((self.width - 70) / 49)
        if step < 2:
            step = 2
        #self.c.xAxis().setMultiFormat(StartOfHourFilter(), "{value|hh:mm}", StartOfHourFilter(), "{value|hh:00}")
        self.c.xAxis().setLabelStep(step, step / 2)
        
        #self.c.xAxis().setLabelStep(step, step / 2)
        
        # Add a line layer to the chart
        layer = self.c.addLineLayer2()
        
        # Create the color to draw the data line. The line is blue (0x333399) to the left of
        # x = 18, and become a red (0xd04040) dash line to the right of x = 18.
        lineColor = layer.xZoneColor(1441, self.line1_color, self.c.dashLineColor(0xd04040, DashLine)) #0x333399
        
        # Add the data line
        layer.addDataSet(data1['data'], lineColor)
        
        # Create the color to draw the err zone. The color is semi-transparent blue
        # (0x809999ff) to the left of x = 18, and become semi-transparent red (0x80ff9966) to
        # the right of x = 18.
        errColor = layer.xZoneColor(1441, self.line2_color, 0x80ff9966L) #0x809999ffL
        
        # Add the upper border of the err zone
        layer.addDataSet(ArrayMath(data2['data']).add(data2['heldata']).result(), errColor)
        
        # Add the lower border of the err zone
        layer.addDataSet(ArrayMath(data2['data']).sub(data2['heldata']).result(), errColor)
        
        # Set the default line width to 2 pixels
        layer.setLineWidth(1)
        
        # Color the region between the err zone lines
        self.c.addInterLineLayer(layer.getLine(1), layer.getLine(2), errColor)       
        if self.ys:
            ys = int(self.ys)
            self.c.yAxis().setLinearScale(0, ys)
            self.c.setClipping()
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __datafact__(self, l1, labs, ulab):
        data = []
        labels = []
        heldata = []
        i = 0
        n = 0
        try:
            for i, r in enumerate(l1): 
                        
                hour = "%02d" % r.houri
                minute = "%02d" % r.minutei
                key = str(r.datei) + ":" + hour + ":" + minute
                #log.debug(key)       
                if key in labs.keys():
                    labs[key] = r.valuei
            if ulab:
                data = []
                labels = []
                heldata = []
                for k, v in sorted(labs.iteritems()):
                    #labels.append(chartTime(int(k[0:4]), int(k[5:7]), int(k[8:10]), k[11:13], k[14:16], 0))
                    labels.append(k[11:16])
                    data.append(v)
                    heldata.append(v * self.helth_range/100)
                    n += 1
                log.debug("n:" + str(n))
        except:
            log.error("valuei excetion")
        return {'data':data, 'heldata':heldata, 'labels':labels, 'n':n}

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/MarksAndZones2.py
##########################################
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class MarksAndZones2:
    def __init__(self, et, ys=""):        
        
        self.l1 = et[0] 
        self.l2 = et[1] 
        self.labs1 = et[2] 
        self.labs2 = et[3] 
        self.titles = et[4] 
        self.critical = et[5] 
        self.warning = et[6] 
        self.marks = et[7]
        self.line1_color = et[8]
        self.line2_color = et[9]
        self.r_mode = et[10]
        self.helth_range = et[11]
        self.f_width = et[12]
        self.f_height = et[13]
        self.ys = ys
        
        
        data1 = self.__datafact__(self.l1, self.labs1, True)
        data2 = self.__datafact__(self.l2, self.labs2, True)
        
        # Create a XYChart object of size 400 x 270 pixels
        self.width = self.f_width #660
        self.height = self.f_height #250
        self.c = XYChart(self.width, self.height)
        
        
        self.critical_color = 0xff0000
        self.warning_color = 0xff9900
        
        # Set the plotarea at (80, 25) and of size 300 x 200 pixels. Use alternate color
        # background (0xeeeeee) and (0xffffff). Set border and grid colors to grey
        # (0xc0c0c0).
        self.c.setPlotArea(60, 25, self.width - 70, self.height - 60, 0xeeeeee, 0xffffff, 0xc0c0c0, 0xc0c0c0, 0xc0c0c0)
        
        # Add a title to the chart using 14 pts Times Bold Italic font
        self.c.addTitle(str(self.titles[0]) , "timesbi.ttf", 14)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(self.titles[1]))
        self.c.xAxis().setTitle(str(self.titles[2]) + " (" + str(self.width) + "x" + str(self.height) + ")")
        
        # Set the y axis width to 2 pixels
        self.c.yAxis().setWidth(2)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        # Add a legend box (50, 10) (top of plot area) using horizontal layout. Use 8 pts
        # Arial font. Disable bounding box (set border to transparent).
        
        #legendBox = self.c.addLegend(60, 20, 0, "", 8)
        #legendBox.setBackground(Transparent)
        
        
        
        # Display 1 out of 3 labels on the x-axis. Show minor ticks for remaining labels.
        #(660 - 70) / 10
        #(6600 - 70) / 10
        
        step = data2['n'] / ((self.width - 70) / 49)
        if step < 2:
            step = 2
        self.c.xAxis().setLabelStep(step, step / 2)
        
        # Set the x axis width to 2 pixels
        self.c.xAxis().setWidth(2)
        
        if self.critical > 0:
            #Critical
            # Add a horizontal red (0x800080) mark line at y = 50000
            yMark2 = self.c.yAxis().addMark(self.critical, self.critical_color, "Critical Threshold Set Point")
            
            # Set the mark line width to 2 pixels
            yMark2.setLineWidth(2)
            
            # Put the mark label at the top center of the mark line
            yMark2.setAlignment(TopLeft)
        
        if self.warning > 0:
            #Warning
            # Add a horizontal red (0x800080) mark line at y = 30000
            yMark1 = self.c.yAxis().addMark(self.warning, self.warning_color, "Warning Threshold Set Point")
            
            # Set the mark line width to 2 pixels
            yMark1.setLineWidth(2)
            
            # Put the mark label at the top center of the mark line
            yMark1.setAlignment(TopLeft)
        
        if self.marks:
            
            # Add an orange (0xffcc66) zone from x = 18 to x = 20
            self.c.xAxis().addZone(18, 20, 0xffcc66)
            
            # Add a vertical brown (0x995500) mark line at x = 18
            xMark1 = self.c.xAxis().addMark(18, 0x995500, "Backup Start")
            
            # Set the mark line width to 2 pixels
            xMark1.setLineWidth(2)
            
            # Put the mark label at the left of the mark line
            xMark1.setAlignment(Left)
            
            # Rotate the mark label by 90 degrees so it draws vertically
            xMark1.setFontAngle(90)
            
            # Add a vertical brown (0x995500) mark line at x = 20
            xMark2 = self.c.xAxis().addMark(20, 0x995500, "Backup End")
            
            # Set the mark line width to 2 pixels
            xMark2.setLineWidth(2)
            
            # Put the mark label at the right of the mark line
            xMark2.setAlignment(Right)
            
            # Rotate the mark label by 90 degrees so it draws vertically
            xMark2.setFontAngle(90)
        
        # Add a green (0x00cc00) line layer with line width of 2 pixels
        self.c.addLineLayer(data1['data'], self.line1_color, 'today').setLineWidth(1)
        self.c.addLineLayer(data2['data'], self.line2_color, 'x').setLineWidth(1)
        #0x779C4F
        #0x999999
        if self.ys:
            ys = int(self.ys)
            self.c.yAxis().setLinearScale(0, ys)
            self.c.setClipping()
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __datafact__(self, l1, labs, ulab):
        data = []
        labels = []
        i = 0
        n = 0
        try:
            for i, r in enumerate(l1): 
                        
                hour = "%02d" % r.houri
                minute = "%02d" % r.minutei
                key = str(r.datei) + ":" + hour + ":" + minute
                #log.debug(key)       
                if key in labs.keys():
                    labs[key] = r.valuei
            if ulab:
                data = []
                labels = []
                for k, v in sorted(labs.iteritems()):
                    labels.append(k[11:16])
                    data.append(v)
                    n += 1
                log.debug("n:" + str(n))
        except:
            pass
        return {'data':data, 'labels':labels, 'n':n}

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/OverlappingBarChart.py
##########################################
from pychartdir import *

class OverlappingBarChart:
    
    def __init__(self):
        # The data for the bar chart
        data0 = [100, 125, 156, 147, 87, 124, 178, 109, 140, 106, 192, 122, 100, 100, 100, 100, 110, 111, 123, 123]
        
        labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct","Nov", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec", "Dec"]
        
        self.width = 700
        self.height = 250
        # Create a XYChart object of size 580 x 280 pixels
        self.c = XYChart(self.width, self.height)
        
        # Add a title to the chart using 14 pts Arial Bold Italic font
        self.c.addTitle("DB Server", "arialbi.ttf", 14)
        
        # Set the plot area at (50, 50) and of size 500 x 200. Use two alternative background
        # colors (f8f8f8 and ffffff)
        self.c.setPlotArea(50, 50, 500, 200, 0xf8f8f8, 0xffffff)
        
        # Add a legend box at (50, 25) using horizontal layout. Use 8pts Arial as font, with
        # transparent background.
        self.c.addLegend(50, 25, 0, "arial.ttf", 8).setBackground(Transparent)
        
        # Set the x axis labels
        self.c.xAxis().setLabels(labels)
        
        # Draw the ticks between label positions (instead of at label positions)
        self.c.xAxis().setTickOffset(0.5)
        
        # Add a multi-bar layer with 3 data sets
        layer = self.c.addBarLayer2(Side)
        layer.addDataSet(data0, 0x8080ff, "select")
#        layer.addDataSet(data1, 0x80ff80, "Year 2004")
#        layer.addDataSet(data2, 0x8080ff, "Year 2005")
        
        # Set 50% overlap between bars
        layer.setOverlapRatio(0.5)
        
        # Add a title to the y-axis
        self.c.yAxis().setTitle("Revenue (USD in millions)")

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/MultiLineChart.py
##########################################
# -*- coding: utf-8 -*-
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class MultiLineChart:
    
    def __init__(self,l,names,titles,opt="0",d="",d2=""):
        # The data for the line chart
        #names = ['datei','com_update','com_insert','com_delete','com_replace']
        #names = ['datei','com_update','com_insert']

        #titles = ['','queries per day','Jun 12, 2010']

        #for na in range(len(names)):
        #    print na,names[na],"test"
        opts = opt.split(',')
        data = {'0':[],'1':[],'2':[],'3':[],'4':[],'5':[],'6':[],'7':[],'8':[],'9':[]}
        i = 0
        
        try:
            for i,r in enumerate(l):
                mediadata = str(r.mediadata)
                ds =  mediadata.split(',')
                for na in range(len(names)):
                    it = str(ds[na])
                    if it == "":
                        it = "0"
                    data[str(na)].append(it)                
        except:
            data['0'] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
            data['1'] = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
            i = 24
        
        # The data for the line chart
        #self.data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70, 76, 63, 67, 75, 64, 51]
        #self.data1 = [50, 55, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73, 77, 84, 82, 80, 84, 98]
        #self.data2 = [36, 28, 25, 33, 38, 20, 22, 30, 25, 33, 30, 24, 28, 15, 21, 26, 46, 42, 48, 45, 43, 52, 64, 60, 70]
        
        # The labels for the line chart
        self.labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create an XYChart object of size 600 x 300 pixels, with a light blue (EEEEFF)
        # background, black border, 1 pxiel 3D border effect and rounded corners
        
        self.width = 700
        self.height = 250
        
        self.c = XYChart(self.width, self.height, 0xeeeeff, 0x000000, 1)
        self.c.setRoundedFrame()
        
        # Set the plotarea at (55, 58) and of size 520 x 195 pixels, with white background.
        # Turn on both horizontal and vertical grid lines with light grey color (0xcccccc)
        self.c.setPlotArea(80, 58, self.width-120, self.height-100, 0xffffff, -1, -1, 0xcccccc, 0xcccccc)
        
        # Add a legend box at (50, 30) (top of the chart) with horizontal layout. Use 9 pts
        # Arial Bold font. Set the background and border color to Transparent.
        self.c.addLegend(70, 30, 0, "arialbd.ttf", 9).setBackground(Transparent)
        
        # Add a title box to the chart using 15 pts Times Bold Italic font, on a light blue
        # (CCCCFF) background with glass effect. white (0xffffff) on a dark red (0x800000)
        # background, with a 1 pixel 3D border.
        #self.c.addTitle("Application Server Throughput", "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        self.c.addTitle(str(titles[0]), "timesbi.ttf", 15).setBackground( 0xccccff, 0x000000, glassEffect())
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(titles[1]))
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data['0'])
        
        # Display 1 out of 3 labels on the x-axis.
        step = int( i / 6 )
        if step < 2:
            step = 2
        self.c.xAxis().setLabelStep(step, 0)
        
        # Add a title to the x axis
        

        self.c.xAxis().setTitle("From "+str(d)+" To "+str(d2))
        
        # Add a line layer to the chart
        self.layer = self.c.addLineLayer2()
        
        # Set the default line width to 2 pixels
        self.layer.setLineWidth(2)
        
        # Add the three data sets to the line layer. For demo purpose, we use a dash line
        # color for the last line
        for na in range(len(names)):            
            if na > 0:
                if str(na) not in opts:
                    try:
                        self.layer.addDataSet(data[str(na)], self.__colorsschema__(na), str(names[na]))
                    except:
                        log.info("data format error")
                        
        
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __colorsschema__(self,idx):
        v = "#3366FF"
        colors1 = [0x3366FF,0x6633FF,0xCC33FF,0xFF33CC,0x33CCFF,0x003DF5,0x002EB8,0xFF3366,0x33FFCC,0xB88A00,0xF5B800,0xFF6633]
        colors2 = [0x66CCFF,0xFF0000,0x00FF00,0x0000FF,0xCC00FF,0x6699FF,0x009999,0xCCCC00,0xFFCC33,0xFF9999,0x339900,0xCC0066]
        v = colors2[idx]
        return v
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/SimpleAreaChart.py
##########################################
from pychartdir import *

class SimpleAreaChart:
    
    def __init__(self):
        # The data for the area chart
        data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 89, 60, 55, 53, 35, 50,
            66, 56, 48, 52, 65, 62]
        
        # The labels for the area chart
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(250, 250)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(30, 20, 200, 200)
        
        # Add an area chart layer using the given data
        self.c.addAreaLayer(data)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)
        
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(3)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/TDPieChart.py
##########################################
from pychartdir import *

class TDPieChart:
    
    def __init__(self):
        # The data for the pie chart
        data = [25, 18, 15, 12, 8, 30, 35]
        
        # The labels for the pie chart
        labels = ["Labor", "Licenses", "Taxes", "Legal", "Insurance", "Facilities",
            "Production"]
        
        # Create a PieChart object of size 360 x 300 pixels
        self.c = PieChart(360, 300)
        
        # Set the center of the pie at (180, 140) and the radius to 100 pixels
        self.c.setPieSize(180, 140, 100)
        
        # Add a title to the pie chart
        self.c.addTitle("Project Cost Breakdown")
        
        # Draw the pie in 3D
        self.c.set3D()
        
        # Set the pie data and the pie labels
        self.c.setData(data, labels)
        
        # Explode the 1st sector (index = 0)
        self.c.setExplode(0)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/SimpleBarChart.py
##########################################
from pychartdir import *

class SimpleBarChart:
    
    def __init__(self):
        # The data for the bar chart
        data = [85, 156, 179.5, 211, 123]
        
        # The labels for the bar chart
        labels = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(250, 250)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(30, 20, 200, 200)
        
        # Add a bar chart layer using the given data
        self.c.addBarLayer(data)
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/SimpleLineChart.py
##########################################
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class SimpleLineChart:
    def __init__(self, et):
        #l1, l2, labs1, labs2, allt
        
        self.l1 = et[0]
        self.l2 = et[1]
        self.labs1 = et[2]
        self.labs2 = et[3]
        self.line1_color = et[4]
        self.line2_color = et[5]
        
        self.width = 300
        self.height = 160
        
        
        
        self.max_value = 0
        
        data1 = self.__datafact__(self.l1, self.labs1, True, True)
        data2 = self.__datafact__(self.l2, self.labs2, True)
        
        
        
        # Create a XYChart object of size 250 x 250 pixels
        self.c = XYChart(self.width, self.height)
        
        # Set the plotarea at (30, 20) and of size 200 x 200 pixels
        self.c.setPlotArea(50, 20, self.width - 80, self.height - 50)
        
        # Add a line chart layer using the given data
        self.c.addLineLayer(data1['data'], self.line1_color, 'today')
        self.c.addLineLayer(data2['data'], self.line2_color, 'yestoday')
        
        #layer.addDataSet(data0, 0xff0000, "Server #1")
        #layer.addDataSet(data1, 0x008800, "Server #2")
        #layer.addDataSet(data2, c.dashLineColor(0x3333ff, DashLine), "Server #3")
        
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        step = data2['n'] / 4
        if step < 2:
            step = 2
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(int(step))
        log.debug("step:" + str(step))

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
    
    def __datafact__(self, l1, labs, ulab, alert=False):
        data = []
        labels = []
        i = 0
        n = 0
        try:
            for i, r in enumerate(l1): 
                        
                hour = "%02d" % r.houri
                minute = "%02d" % r.minutei
                key = str(r.datei) + ":" + hour + ":" + minute
                #log.debug(key)       
                if key in labs.keys():
                    labs[key] = r.valuei
                    if r.valuei >= self.max_value and alert:
                        self.max_value = r.valuei
                    
            if ulab:
                data = []
                labels = []
                for k, v in sorted(labs.iteritems()):
                    labels.append(k[11:16])
                    data.append(v)
                    n += 1
                log.debug("n:" + str(n))
        except:
            pass
        return {'data':data, 'labels':labels, 'n':n}

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/BorderlessBarChart.py
##########################################
from pychartdir import *
import logging
log = logging.getLogger(__name__)

class BorderlessBarChart:
    
    def __init__(self,l,names,titles,opt="0",dset=""):
        # The data for the bar chart
#        data = [3.9, 8.1, 10.9, 14.2, 18.1, 19.0, 21.2, 23.2, 25.7, 36]
        
        # The labels for the bar chart
#        labels = ["Bastic Group", "Simpa", "YG Super", "CID", "Giga Tech", "Indo Digital","Supreme", "Electech", "THP Thunder", "Flash Light"]
        labels = []
        data = []
        i=0
        item_name_len = 0
        item_name_len_tmp = 0
        for i,r in enumerate(l):
            mediadata = str(r.mediadata)
            ds =  mediadata.split(',')
            labels.append(str(ds[1]))
            item_name_len_tmp = len(str(ds[1]))
            if item_name_len_tmp > item_name_len:
                item_name_len = item_name_len_tmp
            data.append(ds[2])            
                        
        self.width = 700
        self.height = 0
        if i > 30:
            self.steplength = 18
        else:
            self.steplength = 24
        self.height = self.steplength * ( i + 1 )
        # Create a XYChart object of size 600 x 250 pixels
        self.c = XYChart(self.width, self.height)
        
        # Add a title to the chart using Arial Bold Italic font
        self.c.addTitle(str(titles[0])+" - "+ str(dset), "arialbi.ttf")
        
        # Set the plotarea at (100, 30) and of size 400 x 200 pixels. Set the plotarea
        # border, background and grid lines to Transparent
        item_name_len = (item_name_len*9)
        log.debug("item_name_len: "+str(item_name_len))
        self.c.setPlotArea(item_name_len, 30, self.width-(item_name_len+100), self.height-50, Transparent, Transparent, Transparent, Transparent,Transparent)
        
        # Add a bar chart layer using the given data. Use a gradient color for the bars,
        # where the gradient is from dark green (0x008000) to white (0xffffff)
        layer = self.c.addBarLayer(data, self.c.gradientColor(item_name_len, 0, self.width-100, 0, 0x6666ff, 0xffffff))
        
        # Swap the axis so that the bars are drawn horizontally
        self.c.swapXY(1)
        
        # Set the bar gap to 10%
        layer.setBarGap(0.1)
        
        # Use the format "US$ xxx millions" as the bar label
        layer.setAggregateLabelFormat("q: {value}")
        
        # Set the bar label font to 10 pts Times Bold Italic/dark red (0x663300)
        layer.setAggregateLabelStyle("timesbi.ttf", 10, 0x663300)
        
        # Set the labels on the x axis
        textbox = self.c.xAxis().setLabels(labels)
        
        # Set the x axis label font to 10pt Arial Bold Italic
        textbox.setFontStyle("arialbi.ttf")
        textbox.setFontSize(10)
        
        # Set the x axis to Transparent, with labels in dark red (0x663300)
        self.c.xAxis().setColors(Transparent, 0x663300)
        
        # Set the y axis and labels to Transparent
        self.c.yAxis().setColors(Transparent, Transparent)
        
        

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/TDLineChart.py
##########################################
from pychartdir import *

class TDLineChart:
    
    def __init__(self):
        # The data for the line chart
        data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 91, 60, 55, 53, 35, 50,
            66, 56, 48, 52, 65, 62]
        
        # The labels for the line chart
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create a XYChart object of size 300 x 280 pixels
        self.c = XYChart(300, 280)
        
        # Set the plotarea at (45, 30) and of size 200 x 200 pixels
        self.c.setPlotArea(45, 30, 200, 200)
        
        # Add a title to the chart using 12 pts Arial Bold Italic font
        self.c.addTitle("Daily Server Utilization", "arialbi.ttf", 12)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle("MBytes")
        
        # Add a title to the x axis
        self.c.xAxis().setTitle("June 12, 2001")
        
        # Add a blue (0x6666ff) 3D line chart layer using the give data
        self.c.addLineLayer(data, 0x6666ff).set3D()
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)
        
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(3)
        
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/PercentageAreaChart.py
##########################################
#!/usr/bin/python
from pychartdir import *

# The data for the area chart
data0 = [42, 49, 33, 38, 51, 46, 29, 41, 44, 57, 59, 52, 37, 34, 51, 56, 56, 60, 70,
    76, 63, 67, 75, 64, 51]
data1 = [50, 55, 47, 34, 42, 49, 63, 62, 73, 59, 56, 50, 64, 60, 67, 67, 58, 59, 73,
    77, 84, 82, 80, 84, 98]
data2 = [87, 89, 85, 66, 53, 39, 24, 21, 37, 56, 37, 23, 21, 33, 13, 17, 14, 23, 16,
    25, 29, 30, 45, 47, 46]

# The timestamps on the x-axis
labels = [chartTime(1996, 1, 1), chartTime(1996, 4, 1), chartTime(1996, 7, 1),
    chartTime(1996, 10, 1), chartTime(1997, 1, 1), chartTime(1997, 4, 1), chartTime(
    1997, 7, 1), chartTime(1997, 10, 1), chartTime(1998, 1, 1), chartTime(1998, 4, 1
    ), chartTime(1998, 7, 1), chartTime(1998, 10, 1), chartTime(1999, 1, 1),
    chartTime(1999, 4, 1), chartTime(1999, 7, 1), chartTime(1999, 10, 1), chartTime(
    2000, 1, 1), chartTime(2000, 4, 1), chartTime(2000, 7, 1), chartTime(2000, 10, 1
    ), chartTime(2001, 1, 1), chartTime(2001, 4, 1), chartTime(2001, 7, 1),
    chartTime(2001, 10, 1), chartTime(2002, 1, 1)]

# Create a XYChart object of size 500 x 280 pixels, using 0xffffcc as background
# color, with a black border, and 1 pixel 3D border effect
c = XYChart(500, 280, 0xffffcc, 0, 1)

# Set directory for loading images to current script directory
# Need when running under Microsoft IIS
c.setSearchPath(os.path.dirname(sys.argv[0]))

# Set the plotarea at (50, 45) and of size 320 x 200 pixels with white background.
# Enable horizontal and vertical grid lines using the grey (0xc0c0c0) color.
c.setPlotArea(50, 45, 320, 200, 0xffffff).setGridColor(0xc0c0c0, 0xc0c0c0)

# Add a legend box at (370, 45) using vertical layout and 8 points Arial Bold font.
legendBox = c.addLegend(370, 45, 1, "arialbd.ttf", 8)

# Set the legend box background and border to transparent
legendBox.setBackground(Transparent, Transparent)

# Set the legend box icon size to 16 x 32 pixels to match with custom icon size
legendBox.setKeySize(16, 32)

# Add a title to the chart using 14 points Times Bold Itatic font and white font
# color, and 0x804020 as the background color
c.addTitle("Quarterly Product Sales", "timesbi.ttf", 14, 0xffffff).setBackground(
    0x804020)

# Set the labels on the x axis.
c.xAxis().setLabels2(labels)

# Set multi-style axis label formatting. Start of year labels are displayed as yyyy.
# For other labels, just show minor tick.
c.xAxis().setMultiFormat(StartOfYearFilter(), "{value|yyyy}", AllPassFilter(), "-")

# Add a percentage area layer to the chart
layer = c.addAreaLayer2(Percentage)

# Add the three data sets to the area layer, using icons images with labels as data
# set names
layer.addDataSet(data0, 0x40ddaa77,
    "<*block,valign=absmiddle*><*img=service.png*> Service<*/*>")
layer.addDataSet(data1, 0x40aadd77,
    "<*block,valign=absmiddle*><*img=software.png*> Software<*/*>")
layer.addDataSet(data2, 0x40aa77dd,
    "<*block,valign=absmiddle*><*img=computer.png*> Hardware<*/*>")

# For a vertical stacked chart with positive data only, the last data set is always
# on top. However, in a vertical legend box, the last data set is at the bottom. This
# can be reversed by using the setLegend method.
layer.setLegend(ReverseLegend)

# output the chart
print "Content-type: image/png\n"
binaryPrint(c.makeChart2(PNG))
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/CompactLineChart.py
##########################################
from pychartdir import *

class CompactLineChart:
    
    def __init__(self):
        #
        #    We use a random number generator to simulate the data from 9:30am to 4:30pm with
        #    one data point every 4 minutes. The total number of points during that period is
        #    106.  (7 hours x 15 points/hour + 1)
        #
        noOfPoints = 106
        
        # Assume we have not reached the end of the day yet, and only 85 points are
        # available. Create a random table object of 1 col x 85 rows, using 9 as seed.
        rantable = RanTable(9, 1, 85)
        
        # Set the 1st column to start with 1800 and with random delta from -5 to 5.
        rantable.setCol(0, 1800, -5, 5)
        
        # Get the data as the 1st column of the random table
        data = rantable.getCol(0)
        
        # The x-axis labels for the chart
        labels = ["-", "10am", "-", " ", "-", "12am", "-", " ", "-", "2pm", "-", " ", "-",
            "4pm", "-"]
        
        #
        #    Now we obtain the data into arrays, we can start to draw the chart using
        #    ChartDirector
        #
        
        # Create a XYChart object of size 180 x 180 pixels with a blue background (0x9c9cce)
        self.c = XYChart(180, 180, 0x9c9cce)
        
        # Add titles to the top and bottom of the chart using 7.5pt Arial font. The text is
        # white 0xffffff on a deep blue 0x31319C background.
        self.c.addTitle2(Top, "STAR TECH INDEX  2003-01-28", "arial.ttf", 7.5, 0xffffff, 0x31319c)
        self.c.addTitle2(Bottom, "LATEST  STI:1809.41 (+14.51)", "arial.ttf", 7.5, 0xffffff,
            0x31319c)
        
        # Set the plotarea at (31, 21) and of size 145 x 124 pixels, with a pale yellow
        # (0xffffc8) background.
        self.c.setPlotArea(31, 21, 145, 124, 0xffffc8)
        
        # Add custom text at (176, 21) (top right corner of plotarea) using 11pt Times Bold
        # Italic font/red (0xc09090) color
        self.c.addText(176, 21, "Chart Demo", "timesbi.ttf", 11, 0xc09090).setAlignment(TopRight)
        
        # Use 7.5 pts Arial as the y axis label font
        self.c.yAxis().setLabelStyle("", 7.5)
        
        # Set the labels on the x axis by spreading the labels evenly between the first point
        # (index = 0) and the last point (index = noOfPoints - 1)
        self.c.xAxis().setLinearScale(0, noOfPoints - 1, labels)
        
        # Use 7.5 pts Arial as the x axis label font
        self.c.xAxis().setLabelStyle("", 7.5)
        
        # Add a deep blue (0x000080) line layer to the chart
        self.c.addLineLayer(data, 0x000080)
        
    def display(self):
        # output the chart        
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/TDAreaChart.py
##########################################
from pychartdir import *

class TDAreaChart:
    
    def __init__(self):
        # The data for the area chart
        data = [30, 28, 40, 55, 75, 68, 54, 60, 50, 62, 75, 65, 75, 89, 60, 55, 53, 35, 50,
            66, 56, 48, 52, 65, 62]
        
        # The labels for the area chart
        labels = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
            "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"]
        
        # Create a XYChart object of size 300 x 300 pixels
        self.c = XYChart(300, 300)
        
        # Set the plotarea at (45, 30) and of size 200 x 200 pixels
        self.c.setPlotArea(45, 30, 200, 200)
        
        # Add a title to the chart using 12 pts Arial Bold Italic font
        self.c.addTitle("Daily Server Utilization", "arialbi.ttf", 12)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle("MBytes")
        
        # Add a title to the x axis
        self.c.xAxis().setTitle("June 12, 2001")
        
        # Add a green (0x00ff00) 3D area chart layer using the give data
        self.c.addAreaLayer(data, 0x00ff00).set3D()
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(labels)
        
        # Display 1 out of 3 labels on the x-axis.
        self.c.xAxis().setLabelStep(3)

    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/chartobj/DepthAreaChart.py
##########################################
# -*- coding: utf-8 -*-
from pychartdir import *

class DepthAreaChart:
    
    def __init__(self, l1, l2, names, titles, dset1, dset2, labs):
        # The data1 for the area chart
        
        
        data1 = self.datafact(l1, names, labs)
        data2 = self.datafact(l2, names, labs)
            
        self.width = 700
        self.height = 250
        # Create a XYChart object of size 350 x 230 pixels
        self.c = XYChart(self.width, self.height)
        self.c.setDefaultFonts("simsun.ttc");
        # Set the plotarea at (50, 30) and of size 250 x 150 pixels.
        self.c.setPlotArea(80, 30, self.width - 100, self.height - 80)
        
        # Add a legend box at (55, 0) (top of the chart) using 8 pts Arial Font. Set
        # background and border to Transparent.
        self.c.addLegend(55, 0, 0, "", 8).setBackground(Transparent)
        
        # Add a title to the x axis
        self.c.xAxis().setTitle(str(titles[0]) , "timesbi.ttf", 12)
        
        # Add a title to the y axis
        self.c.yAxis().setTitle(str(titles[1]))
        
        # Set the labels on the x axis.
        self.c.xAxis().setLabels(data2['labels'])
        
        # Display 1 out of 2 labels on the x-axis. Show minor ticks for remaining labels.
        self.c.xAxis().setLabelStep(2, 1)
        
        # Add three area layers, each representing one data1 set. The areas are drawn in
        # semi-transparent colors.
        
                
        self.c.addAreaLayer(data1['data'], 0x808080ffL, str(dset1), 3) #0x808080ffL
        self.c.addAreaLayer(data2['data'], 0x80ff0000L, '上周同一天', 2) #0x80ff0000L
                    #0x8000ff00L
    
    def datafact(self, l, names, labs):
        data = []
        labels = []
        i = 0
        n = 24
        try:
            for i, r in enumerate(l):
                key = "%02d" % r.houri
                mediadata = str(r.mediadata)
                ds = mediadata.split(',')                
                if key in labs.keys():
                    labs[key] = ds[len(ds)-1]
                    
            for k, v in sorted(labs.iteritems()):
                    labels.append(k)
                    data.append(v)
                    n +=1
            log.debug("n:"+str(n))
        except:
            pass
            
        return {'data':data, 'labels':labels, 'n':n}
    
    def display(self):
        # output the chart       
        return self.c.makeChart2(PNG)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/tmc.py
##########################################
"""TMC model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base

class Tmc(Base):
    __tablename__ = "tmc"
   

    id = Column(Integer, primary_key=True)
    datei = Column(Date)
    t = Column(Integer(10))
    

    def __init__(self, datei='', t=''):
        self.datei = datei
        self.t = t

    def __repr__(self):
        return "<Tmc('%s')" % self.datei
    
    def tostring(self):
        return "Tmc('%s','%s','%s')" % (self.id,self.datei,self.t)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/users.py
##########################################
"""Users model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text,DateTime
from pyfisheyes.model.meta import Base


class Users(Base):
    __tablename__ = "users"   

    uid = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    group_uid = Column(Integer)    

    def __init__(self):
        self.uid = 0
        self.username = ""
        self.password = ""
        self.group_uid = 0

    def __repr__(self):
        return "<Events('%s')" % self.username
    
    
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/dateitems.py
##########################################
"""DailyReport model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime, UnicodeText

from pyfisheyes.model.meta import Base


class Dateitems(Base):
    __tablename__ = "log_report_stuff"
    
    datei = Column(Date, primary_key=True)
    stuff = Column(UnicodeText)
    create_time = Column(DateTime)
    lastupdate_time = Column(DateTime)
    
    def __init__(self, datei="00-00-00" ,stuff="" , create_time="00-00-00 00:00:00", lastupdate_time="00-00-00 00:00:00"):
        
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')       
        if not isinstance(stuff, unicode):
            stuff = unicode(stuff, 'utf-8')        
        if not isinstance(create_time, unicode):
            create_time = unicode(create_time, 'utf-8')
        if not isinstance(lastupdate_time, unicode):
            lastupdate_time = unicode(lastupdate_time, 'utf-8')
        
        self.datei = datei       
        self.stuff = stuff
        self.create_time = create_time
        self.lastupdate_time = lastupdate_time
        

    #def __repr__(self):
        #return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    


##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/categories.py
##########################################
"""Categories model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, DateTime

from pyfisheyes.model.meta import Base
import re

class Categories(Base):
    __tablename__ = "categories"
   #c.categories = ['mysqlg1','apperrorlog','tmc']

    typeid = Column(Integer, primary_key=True)
    typename = Column(String(100))
    items = Column(String(100))
    titles = Column(String(200))
    classname = Column(String(100))
    labels = Column(Integer(2))
    disable = Column(Integer(1))
    orderby = Column(String(50))
    graphtype = Column(String(50))
    datasupport = Column(String(50))
    accessed =  Column(Integer)
    warning =  Column(Integer)
    critical =  Column(Integer)
    
    alertlevel =  Column(Integer)
    typecode =  Column(String(20))
    rankcode =  Column(Integer)    
    d_report = Column(Integer)
    r_alert = Column(Integer)
    r_weight = Column(Integer)
    r_mode = Column(String(10))
    r_snap = Column(DateTime)
    l_interval = Column(Integer)
    alarm_threshold = Column(String(200))
    baseface = Column(Date)
    u_baseface = Column(Integer)
    
    def __init__(self, datei='', _update=''):
        self.typeid = 0
        self.typename = ""
        self.classname = ""
        self.items = ""
        self.titles = ""
        self.labels = 0
        self.disable = 0
        self.orderby = ""
        self.graphtype = ""
        self.datasupport = ""
        self.accessed = 0
        self.warning = -1
        self.critical = -1        
        self.alertlevel = 0
        self.typecode = 0
        self.rankcode = 1000000
        self.d_report = 1
        self.r_alert = 0
        self.r_weight = 5
        self.r_mode = 'z'
        self.r_snap = '1970-01-01 00:00:00'
        self.l_interval = 300
        self.alarm_threshold = '[-1, -1, -1, -1, -1, -1, -1, -1]'
        self.baseface = '1970-01-01'
        self.u_baseface = 0
        

    def __repr__(self):
        return "<Categories('%s')" % self.typename
    
    def tostring(self):
        return "Categories('%s','%s','%s','%s','%s','%s','%s','%s')" % (self.typeid, self.typename, self.items, self.titles, self.classname, self.labels, self.disable, self.orderby)
    
    def search_highlight(self, sw):
        import pyfisheyes.lib.helpers as h
        p = re.compile(sw,re.IGNORECASE)
        return h.literal(p.sub( '<span class="sword">'+sw+"</span>", self.typename))
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/realtime.py
##########################################
"""realtime model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, DateTime

from pyfisheyes.model.meta import Base


class Realtime(Base):
    __tablename__ = "realtime"
    
    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    datei = Column(Date)
    houri = Column(Integer)
    minutei = Column(Integer)
    valuei = Column(Integer)
    logtime = Column(DateTime)
    
    def __init__(self, id=0, tid=0, datei='0000-00-00', houri=0, minutei=0, valuei=0):
        
        if not isinstance(id, unicode):
            id = unicode(id, 'utf-8')
        if not isinstance(tid, unicode):
            tid = unicode(tid, 'utf-8')
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')
        if not isinstance(houri, unicode):
            houri = unicode(houri, 'utf-8')
        if not isinstance(minutei, unicode):
            minutei = unicode(minutei, 'utf-8')
        if not isinstance(valuei, unicode):
            valuei = unicode(valuei, 'utf-8')
        if not isinstance(logtime, unicode):
            logtime = unicode(logtime, 'utf-8')
            
        self.id = id
        self.tid = tid
        self.datei = datei
        self.houri = houri
        self.minutei = minutei
        self.valuei = valuei
        self.logtime = logtime

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    def getLogstuff(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.getLogstuff(self.tid, self.datei, self.logtime)
    
    def time(self):
        time = ""
        logtime = str(self.logtime).split(' ')
        time = logtime[1]
        return time
    
    def exporttoexcel(self):        
        return u"\t %s \t %s \t %s" % (self.datei, str(self.logtime)[11:16], self.valuei)
    
    def formatValue(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.numformat(self.valuei)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/contacts.py
##########################################
"""Contacts model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base


class Contacts(Base):
    __tablename__ = "contacts"
   #c.categories = ['mysqlg1','apperrorlog','tmc']

    id = Column(Integer, primary_key=True)
    eid = Column(String(100))
    name = Column(String(100))
    ename = Column(String(200))
    title = Column(String(100))
    subtel = Column(Integer(2))
    mobile = Column(Integer(1))
    email = Column(String(50))
    forsearch = Column(String(50))

    def __init__(self, datei='', _update=''):
        self.id = 0
        self.eid = ""
        self.name = ""
        self.ename = ""
        self.title = ""
        self.subtel = ""
        self.mobile = ""
        self.email = ""
        self.forsearch = ""

    def __repr__(self):
        return "<Categories('%s')" % self.name
    
    
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/graphs.py
##########################################
"""Graph model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date
from pyfisheyes.model.meta import Base

class Graphs(Base):
    __tablename__ = "graphs"
   

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    mediadata = Column(String(200))

    def __init__(self, datei='', m=''):
        self.datei = datei
        self.mediadata = m

    def __repr__(self):
        return "<Graphs('%s')" % self.datei
    
    def tostring(self):
        return "Graphs('%s','%s','%s','%s')" % (self.id,self.template_id,self.datei,self.mediadata)
    
    def tostringlist(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.tostringlist(self.mediadata,True)
    
    def exporttoexcel(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.exporttoexcel(self.mediadata)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/alarminfo.py
##########################################
"""pyf_alarminfo model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date, Time, DateTime

from pyfisheyes.model.meta import Base


class Alarminfo(Base):
    __tablename__ = "pyf_alarminfo"
    
    
    id = Column(Integer, primary_key=True) #0
    t_name = Column(String(100))           #1
    tid = Column(Integer)                  #2
    datei = Column(Date)                   #3
    t_status = Column(String(250))         #4
    r_weight = Column(Integer)             #5
    r_mode = Column(String(20))            #6
    start_time = Column(Time)              #7
    end_time = Column(Time)                #8
    t_threshold = Column(Integer)          #9
    a_level = Column(String(50))           #10
    logtime = Column(DateTime)             #11
    
    def __init__(self, arr):
        
        t_name1 = arr[1]
        if not isinstance(arr[1], unicode):
            t_name1 = unicode(arr[1], 'utf-8')
        
        t_status1 = arr[4]
        if not isinstance(arr[4], unicode):
            t_status1 = unicode(arr[4], 'utf-8')
        
        r_mode1 = arr[6]
        if not isinstance(arr[6], unicode):
            r_mode1 = unicode(arr[6], 'utf-8')
               
        a_level1 = arr[10]   
        if not isinstance(arr[10], unicode):
            a_level1 = unicode(arr[10], 'utf-8')    
            
        #self.id = arr[0]
        self.t_name = t_name1
        self.tid = arr[2]
        self.datei = arr[3]
        self.t_status = t_status1
        self.r_weight = arr[5]
        self.r_mode = r_mode1
        self.start_time = arr[7]
        self.end_time = arr[8]
        self.t_threshold = arr[9]
        self.a_level = a_level1
        self.logtime = arr[11]

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.t_name)
    
    def t_name_urlencode(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.urlencode( self.t_name.encode('utf-8'))
    
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/logstuff.py
##########################################
"""realtime model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text, DateTime

from pyfisheyes.model.meta import Base


class Logstuff(Base):
    __tablename__ = "logstuff"
    
    id = Column(Integer, primary_key=True)
    tid = Column(Integer)
    datei = Column(Date)
    stuff = Column(Text)
    logtime = Column(DateTime)
    
    def __init__(self, id=0, tid=0, datei='0000-00-00', houri=0, minutei=0, valuei=0):
        
        if not isinstance(id, unicode):
            id = unicode(id, 'utf-8')
        if not isinstance(tid, unicode):
            tid = unicode(tid, 'utf-8') 
        if not isinstance(datei, unicode):
            datei = unicode(datei, 'utf-8')       
        if not isinstance(stuff, unicode):
            stuff = unicode(stuff, 'utf-8')        
        if not isinstance(logtime, unicode):
            logtime = unicode(logtime, 'utf-8')
        
        self.id = id
        self.tid = tid
        self.datei = datei       
        self.stuff = stuff
        self.logtime = logtime

    def __repr__(self):
        return u"<Realteam('%s, %s')" % (self.id, self.datei)
    
    


##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/graphshour.py
##########################################
"""graphs model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base


class GraphsHour(Base):
    __tablename__ = "graphshour"
    
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    houri = Column(Integer)
    mediadata = Column(String(200))
    
    def __init__(self, id='', template_id='', datei='', houri='', mediadata=''):
        
        if not isinstance( template_id, unicode ):
            template_id = unicode( template_id, 'utf-8' )
        if not isinstance( datei, unicode ):
            datei = unicode( datei, 'utf-8' )
        if not isinstance( houri, unicode ):
            houri = unicode( houri, 'utf-8' )
        if not isinstance( mediadata, unicode ):
            mediadata = unicode( mediadata, 'utf-8' )
        if not isinstance( id, unicode ):
            id  = unicode( id, 'utf-8' )

        self.id = id
        self.template_id = template_id
        self.datei = datei
        self.houri = houri
        self.mediadata = mediadata

    def __repr__(self):
        return u"<GraphsHour('%s, %s')" % (self.id, self.datei)
    
    def tostringlist(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.tostringlist(self.mediadata,False)
    
    def exporttoexcel(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.exporttoexcel(self.mediadata)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/events.py
##########################################
"""Events model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date,Text,DateTime

from pyfisheyes.model.meta import Base
import pyfisheyes.lib.helpers as h
import textile


class Events(Base):
    __tablename__ = "events"
   

    id = Column(Integer, primary_key=True)
    evtitle = Column(String(200))
    evdate = Column(Date)
    evtags = Column(String(100))
    evtype = Column(String(20))
    evstatus = Column(String(20))
    evcause = Column(String(100))
    evminutes = Column(Integer)
    evlosspv = Column(Integer)
    evdomain = Column(String(50))
    evreporter = Column(Integer)
    evcreatedate = Column(DateTime)
    evreporterip = Column(String(20))
    evlastedit = Column(DateTime)
    evlasteditor = Column(Integer)
    evlasteditip = Column(String(20))
    evcontent = Column(Text)
    tid = Column(Integer)
    

    def __init__(self):
        self.id = 0
        self.evtitle = ""
        self.evdate = "0000-00-00"
        self.evtags = ""
        self.evtype = ""
        self.evstatus = ""
        self.evcause = ""
        self.evminutes = 0
        self.evlosspv = 0
        self.evdomain = ""
        self.evreporter = 0
        self.evcreatedate = "0000-00-00 00:00:00"
        self.evlastedit = "0000-00-00 00:00:00"
        self.evlasteditor = 0
        self.evcontent = ""
        self.evreporterip = ""
        self.evlasteditip = ""
        self.tid = 0

    def __repr__(self):
        return "<Events('%s')" % self.evtitle
    
    def getEvContent(self):
        try:
            content = h.literal(textile.textile(self.evcontent))
        except:
            content = ""
        return content
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/model/fisheyesdb/graphshost.py
##########################################
"""graphs model"""
from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Date

from pyfisheyes.model.meta import Base


class GraphsHost(Base):
    __tablename__ = "graphshost"
    
    id = Column(Integer, primary_key=True)
    template_id = Column(Integer)
    datei = Column(Date)
    host = Column(String(50))
    mediadata = Column(String(200))
    
    def __init__(self, id='', template_id='', datei='', host='', mediadata=''):
        
        if not isinstance( template_id, unicode ):
            template_id = unicode( template_id, 'utf-8' )
        if not isinstance( datei, unicode ):
            datei = unicode( datei, 'utf-8' )
        if not isinstance( host, unicode ):
            host = unicode( host, 'utf-8' )
        if not isinstance( mediadata, unicode ):
            mediadata = unicode( mediadata, 'utf-8' )
        if not isinstance( id, unicode ):
            id  = unicode( id, 'utf-8' )

        self.id = id
        self.template_id = template_id
        self.datei = datei
        self.host = host
        self.mediadata = mediadata

    def __repr__(self):
        return u"<GraphsHost('%s, %s')" % (self.id, self.datei)    

    def tostringlist(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()        
        return gh.tostringlist(self.mediadata,False)
    
    def exporttoexcel(self):
        from pyfisheyes.model.utils import GlobalHandle as _gh
        gh = _gh.GlobalHandle()   
        return gh.exporttoexcel(self.mediadata)
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/base.py
##########################################
"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons import app_globals, cache, config, request, response, session
from pylons import app_globals as g
from pylons.controllers.util import redirect
from pylons import url

from pyfisheyes.model.meta import Session


class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/archivefile.py
##########################################
import os, zipfile, tarfile, shutil

def extractall(archive, dstdir):
    """ extract zip or tar content to dstdir"""

    if zipfile.is_zipfile(archive):
        z = zipfile.ZipFile(archive)
        for name in z.namelist():
            targetname = name
            # directories ends with '/' (on Windows as well)
            if targetname.endswith('/'):
                targetname = targetname[:-1]

            # don't include leading "/" from file name if present
            if targetname.startswith(os.path.sep):
                targetname = os.path.join(dstdir, targetname[1:])
            else:
                targetname = os.path.join(dstdir, targetname)
            targetname = os.path.normpath(targetname)

            # Create all upper directories if necessary.    
            upperdirs = os.path.dirname(targetname)
            if upperdirs and not os.path.exists(upperdirs):
                os.makedirs(upperdirs)

            # directories ends with '/' (on Windows as well)
            if not name.endswith('/'):
                # copy file
                file(targetname, 'wb').write(z.read(name))

    elif tarfile.is_tarfile(archive):
        tar = tarfile.open(archive)
        tar.extractall(path=dstdir)

    else:
        # seems to be a single file, save it
        shutil.copyfile(archive, os.path.join(dstdir, os.path.basename(archive)))
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/app_globals.py
##########################################
"""The application's Globals object"""
import atexit
from turbomail import interface
from turbomail.adapters import tm_pylons

from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

class Globals(object):
    """Globals acts as a container for objects available throughout the
    life of the application

    """

    def __init__(self, config):
        """One instance of Globals is created during application
        initialization and is available during requests via the
        'app_globals' variable

        """
        self.cache = CacheManager(**parse_cache_config_options(config))
        atexit.register(tm_pylons.shutdown_extension)
        interface.start(tm_pylons.FakeConfigObj(config))

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/auth.py
##########################################
from authkit.permissions import ValidAuthKitUser
from authkit.permissions import HasAuthKitRole
from authkit.authorize.pylons_adaptors import authorized
from pylons.templating import render_mako as render
from authkit.authorize.pylons_adaptors import authorize

is_valid_user = ValidAuthKitUser()
has_delete_role = HasAuthKitRole(['delete'])

def render_signin():
    return render('/derived/account/signin.html').encode('utf-8')

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/helpers.py
##########################################
"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
import os
import hashlib

from webhelpers.html import escape, HTML, literal, url_escape, literal
from webhelpers.html.tags import *
from pylons import url
from pylons.controllers.util import redirect

from formbuild.helpers import field
from formbuild import start_with_layout as form_start, end_with_layout as form_end
from formbuild.helpers import checkbox_group

from routes import url_for

from pyfisheyes.lib import auth

from types import StringType, UnicodeType

def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return unicode(md5.hexdigest())

def unchroot_path(path, chroot):
    if type(path) != StringType and type(path) != UnicodeType:
        raise Exception('Bad path (type is not string)')
    while path.startswith(os.sep):
        path = path[len(os.sep):]
    if not path.startswith(os.path.basename(chroot)):
        raise Exception('Bad path (no chroot prefix)')

    uri = os.path.normpath(path[len(os.path.basename(chroot)):])
    while uri.startswith(os.sep):
        uri = uri[len(os.sep):]
    unchrooted = os.path.normpath(os.path.join(chroot, uri))

    if not unchrooted.startswith(chroot):
        raise Exception('Bad path (chroot protected)')
    if not os.path.exists(unchrooted):
        raise Exception('Bad path (does not exist): %s' %unchrooted)

    return (unchrooted, uri)

def remove_empty_dirs(root):
    # remove empty directories
    for dirpath, dirs, files in os.walk(root, topdown=False):
        for subdirname in dirs:
            try:
                os.rmdir(os.path.join(dirpath, subdirname))
            except OSError:
                pass

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/lib/imageprocessing.py
##########################################
# -*- coding: utf-8 -*-
import os
import datetime
import shutil
import logging
import string
from random import choice
log = logging.getLogger(__name__)

# CONSTANTS
ORIG = "orig"
SCALED = "scaled"

class ImageProcessing:

    def __init__(self,
                 src_dir,
                 dest_dir,
                 crop_dimension=700,
                 crop_quality=80):
        self.src_dir = src_dir
        self.dest_dir = dest_dir
        self.abs_orig_dest_dir = os.path.join(self.dest_dir, ORIG)
        self.abs_scaled_dest_dir = os.path.join(self.dest_dir, SCALED)
        self.dimension = crop_dimension
        self.quality = crop_quality


    def copy_orig(self, uri, dest_uri=None):
        """
        Copy the original image to orig dest directory
        """
        src = os.path.join(self.src_dir, uri)
        dest_uri = uri if dest_uri is None else dest_uri
        dest = os.path.join(self.abs_orig_dest_dir, dest_uri)

        self._check_paths(src, dest)

        # copy original photo
        dirpath = os.path.dirname(dest)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath, 0755)
        shutil.copy2(src, dest)
        log.info("Copied: %s" % dest)


    def unlink(self, uri):
        """
        Remove the original image from disk
        """
        src = os.path.join(self.src_dir, uri)

        self._check_paths(src)

        # unlink original photo
        os.unlink(src)
        log.info("Removed: %s" % src)


    def process_image(self, uri):
        """
        Standard processing for the given image:
        Built the destination relative path based on image timestamp
        Copy the original image to orig dest directory
        Copy the scaled and rotated image to scaled dest directory
        Remove the original image from disk
        """
        date = self._get_datetime(uri)
        ext = os.path.splitext(uri)[1].lower()
        genstr = self._filenamegenerator()
        filename = genstr + ext
        dest_uri = os.path.join(
            date.strftime("%Y"),
            date.strftime("%m"),
            date.strftime("%d"),
            os.path.basename(os.path.join(self.src_dir, filename))
        )
        log.debug("process_image::uri:"+ uri)
        self.copy_orig(uri, dest_uri)
        
        self.unlink(uri)
        return (date, dest_uri)


    def _get_datetime(self, uri):
        """
        Built the destination relative path based on image timestamp
        """
        date = datetime.datetime.today()
        return date


    def _check_paths(self, src, dest=None):
        """
        Checks validity of src and/or dest paths
        """
        # abort if src photo does not exist
        if not os.path.exists(src):
            raise Exception("Source image does not exists")        

        # abort if dest photo already exists
        if dest is not None and os.path.exists(dest):
            raise Exception("Destination image already exists")
        
    def _filenamegenerator(self,size=24):
        s = ''.join([choice(string.letters + string.digits) for i in range(size)])
        ss = s.lower()
        return ss


##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/alert.py
##########################################
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
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/speed.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SpeedController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/speed.mako')
        # or, return a string
        c.pagename = "speed"
        return render("/derived/speed/index.html")

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/security.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SecurityController(BaseController):
    def index(self):
        """
        Show login form. Submits to login/submit
        """
        return render('/login.mako')

    def submit(self):
        """
        Verify username and password
        """
        auth_passed = False
        # Both fields filled?
        username = request.params.get('username')
        password = request.params.get('password')

        #for auth in cfg.auth:
        #    if auth(username=username, password=password, config=cfg):
        if username == "test":
            auth_passed = True
        #        break

        # Mark user as logged in
        if auth_passed:
            session['user'] = username
            log.info(u"User %s logged in" % session['user'])
            session.save()

            # Send user back to the page he originally wanted to get to
            if session.get('path_before_login'):
                redirect(url(session['path_before_login']))
            else: # if previous target is unknown just send the user to a welcome page
                redirect('/')
        else:
            log.error("User %s login failed from host [%s]" % ( username, request.remote_addr))
            session.clear()
            session.save()
            return render('/login.mako')

    def logout(self):
        """
        Logout the user and display a confirmation message
        """
        if 'user' in session:
            log.info("User %s logged out" % session['user'])
            del session['user']
            session.save()
        redirect(url("login"))

    def failed(self):
        return render('/auth_failed.mako')

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/session.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SessionController(BaseController):

    def _index(self):
        # Return a rendered template
        #return render('/session.mako')
        # or, return a string
        return 'Hello World'

    def index(self):
        name = session.get('name', 'NULL')
        return 'session name=%s' % name

    def setsession(self):
        session['name'] = 'tony'
        session.save()
        return "save session ok"

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/example.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class ExampleController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/example.mako')
        # or, return a string
        #return 'Hello World'
        return render('/example.mako')

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/categories.py
##########################################
# -*- coding: utf-8 -*-
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from webhelpers import paginate
from pyfisheyes import model

import pyfisheyes.lib.helpers as h

log = logging.getLogger(__name__)

class CategoriesController(BaseController):
    
    graphtype = ['noset', 'day', 'hour', 'host', 'realtime']
    labels = ['noset', 14, 30, 60, 120, 180]
    orderby = ['noset', 'datei', 'houri', 'host']
    r_mode = ['a', 'b', 'c', 'd', 'z']
    r_weight = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    l_interval = [300, 600, 900]
    r_snap = [0, 3600, 10800, 28800, 86400]
    r_typecode = {u'稳定':'10000', u'功能':'20000', u'速度':'30000'}
    

    @h.auth.authorize(h.auth.is_valid_user)   
    def index(self):             
        c.topic = "Templates"
        c.rows = paginate.Page(
        model.meta.Session.query(model.Categories).order_by(model.Categories.typeid.desc()),
        page=int(request.params.get('page', 1)),
        items_per_page=20)        
        return render('/derived/categories/list.html')
    
    @h.auth.authorize(h.auth.has_delete_role)
    def edit(self, id):
        assert id and isinstance(id, basestring)
#        return "id="+str(id)
        c.cate = model.meta.Session.query(model.Categories).filter_by(typeid=id).first()
        c.id = id
        c.action = "submit"
        c.id = 0
        c.heading = "Edit Template"
        c.graphtype = self.graphtype
        c.labels = self.labels
        c.orderby = self.orderby
        
        c.r_mode = self.r_mode
        c.r_weight = self.r_weight
        c.l_interval = self.l_interval
        c.r_snap = self.r_snap
        c.list_alarm_threshold = eval(c.cate.alarm_threshold)
        c.r_typecode = self.r_typecode
        
        return render('/derived/categories/edit.html')
    
    @h.auth.authorize(h.auth.has_delete_role)
    def copy(self, id):
        assert id and isinstance(id, basestring)
#        return "id="+str(id)
        c.cate = model.meta.Session.query(model.Categories).filter_by(typeid=id).first()
        c.id = id
        c.action = "submitadd"
        c.id = 0
        c.heading = "Copy Template"
        c.graphtype = self.graphtype
        c.labels = self.labels
        c.orderby = self.orderby
        c.r_mode = self.r_mode
        c.r_weight = self.r_weight
        c.l_interval = self.l_interval
        c.r_snap = self.r_snap
        c.list_alarm_threshold = eval(c.cate.alarm_threshold)
        c.r_typecode = self.r_typecode
        return render('/derived/categories/edit.html')

    @h.auth.authorize(h.auth.has_delete_role)
    def add(self):
        c.action = "submitadd"
        c.cate = model.Categories()
        c.heading = "Add Template"
        c.graphtype = self.graphtype
        c.labels = self.labels
        c.orderby = self.orderby
        return render('/derived/categories/edit.html')
    
    @h.auth.authorize(h.auth.has_delete_role)
    def submitadd(self):
        ca = model.Categories()
        ca.typename = request.params.get('typename', '')
        ca.classname = request.params.get('classname', '')
        ca.items = request.params.get('items', '')
        ca.titles = request.params.get('titles', '')
        ca.labels = request.params.get('labels', '')
        ca.disable = request.params.get('disable', '')
        ca.orderby = request.params.get('orderby', '')
        ca.graphtype = request.params.get('graphtype', '')
        ca.datasupport = request.params.get('datasupport', '')
        
        ca.typecode = request.params.get('typecode', '')
        ca.rankcode = request.params.get('rankcode', '')
        
        ca.warning = int(request.params.get('warning', '-1'))
        ca.critical = int(request.params.get('critical', '-1'))
        
        ca.d_report = int(request.params.get('d_report', '1'))
        ca.r_alert = int(request.params.get('r_alert', '0'))
        ca.r_weight = int(request.params.get('r_weight', '0'))
        ca.r_mode = request.params.get('r_mode', 'z')
        #ca.r_snap = int(request.params.get('r_snap',''))
        ca.l_interval = int(request.params.get('l_interval', '1'))
        ca.alarm_threshold = "[" \
                            + str(int(request.params.get('x_thr_0', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_1', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_2', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_3', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_4', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_5', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_6', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_7', '-1'))) + "," \
                            + "]"       
        ca.baseface = request.params.get('baseface', '1970-01-01')
        ca.u_baseface = request.params.get('usebaseface', '0')
        model.meta.Session.add(ca)
        model.meta.Session.commit()
        redirect('/template')
        return ""
    
    @h.auth.authorize(h.auth.has_delete_role)
    def submit(self):
        request.charset = 'utf8'
        typeid = int(request.params.get('typeid', 0))
        ca = model.meta.Session.query(model.Categories).filter_by(typeid=typeid).first()
        ca.typename = request.params.get('typename', '')
        ca.classname = request.params.get('classname', '')
        ca.items = request.params.get('items', '')
        ca.titles = request.params.get('titles', '')
        ca.labels = request.params.get('labels', '')
        ca.disable = request.params.get('disable', '')
        ca.orderby = request.params.get('orderby', '')
        ca.graphtype = request.params.get('graphtype', '')
        ca.datasupport = request.params.get('datasupport', '')
        
        ca.typecode = request.params.get('typecode', '')
        ca.rankcode = request.params.get('rankcode', '')
        
        ca.warning = int(request.params.get('warning', '-1'))
        ca.critical = int(request.params.get('critical', '-1'))
        
        ca.d_report = int(request.params.get('d_report', '1'))
        ca.r_alert = int(request.params.get('r_alert', '0'))
        ca.r_weight = int(request.params.get('r_weight', '1'))
        ca.r_mode = request.params.get('r_mode', 'z')
        #ca.r_snap = int(request.params.get('r_snap',''))
        ca.l_interval = int(request.params.get('l_interval', '0'))
        ca.alarm_threshold = "[" \
                            + str(int(request.params.get('x_thr_0', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_1', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_2', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_3', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_4', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_5', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_6', '-1'))) + "," \
                             + str(int(request.params.get('x_thr_7', '-1'))) + "," \
                            + "]"       
        ca.baseface = request.params.get('baseface', '1970-01-01')
        ca.u_baseface = request.params.get('usebaseface', '0')
        model.meta.Session.add(ca)
        model.meta.Session.commit()
        
        redirect('/view/data/' + str(typeid))

        return ""
    
    @h.auth.authorize(h.auth.has_delete_role)
    def delete(self, id=None):
        if id is None:
            abort(404)
        assert id and isinstance(id, basestring)
        ca = model.meta.Session.query(model.Categories).filter_by(typeid=id).first()
        if ca is None:
            abort(404)
        model.meta.Session.delete(ca)
        model.meta.Session.commit()
        return render('/derived/categories/deleted.html')

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/daily_report.py
##########################################
# -*- coding: utf-8 -*-
import logging
import json

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
        clearcache = request.params.get('clear','')
        disabledlazy = request.params.get('unlazy','')
        c.disabledlazy = disabledlazy
        adate = datetime.strptime(odate,'%Y-%m-%d')
        c.odate = odate
        c.imgpath = config["app_conf"]["img_path"]
        dateitems = model.meta.Session.query(i).filter_by(datei=adate).first()
        if dateitems is None:
            #items = drh.createitems(odate)
            items = drh.showsimitems(adate)
            c.rows=items
            c.simp = 1
             
            
        elif clearcache:
            items = drh.createitems(odate)
            items = drh.updateitems(adate)
        else:
            items = json.loads(dateitems.stuff)
            c.items = items
            c.simp = 0
            #return dateitems.stuff
            #return render("/derived/list/daily_report.html")
        return render("/derived/list/daily_report.html")

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/apperrorlog.py
##########################################
#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model import multiline as _m

log = logging.getLogger(__name__)

class ApperrorlogController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/apperrorlog.mako')
        # or, return a string
        return 'Hello World'

    def data(self):        
        c.topic = "AppErrorLog"
        try :
            page_set = int(request.params['page'])
        except:
            page_set = 1 
        c.rows = paginate.Page(
        model.meta.Session.query(model.Apperrorlog),
        page = page_set,
        items_per_page = 10)
        
        return render('/displaydata.mako')

    def graph(self):
        response.headers['Content-type'] = 'image/png'

        names = ['datei','error']
        titles = ['生产环境中的错误日志','errors per day','Jun 12, 2010']

        rows = model.meta.Session.query(model.Apperrorlog).all()

        return _m.Multiline(rows,names,titles).display()
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/list.py
##########################################
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
            if request.cookies.has_key('disrf'):
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

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/account.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
import pyfisheyes.lib.helpers as h

log = logging.getLogger(__name__)

class AccountController(BaseController):

    def signin(self):
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            return render('/derived/account/signedin.html')

    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return render('/derived/account/signedout.html')

    def signinagain(self):
        request.environ['paste.auth_tkt.logout_user']()
        return render('/derived/account/signin.html').replace('%s', h.url_for('signin'))

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/mysqlg1.py
##########################################
#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model import multiline as _m


log = logging.getLogger(__name__)

class Mysqlg1Controller(BaseController):   
    
        
    def data(self):
        try :
            page_set = int(request.params['page'])
        except:
            page_set = 1
        
        c.topic = "MySQLG1"
        #c.rows = model.meta.Session.query(model.Mysqlg1).all()
        c.rows = paginate.Page(
        model.meta.Session.query(model.Mysqlg1),
        page = page_set,
        items_per_page = 10)

        return render('/displaydata.mako')

    def graph(self):
        response.headers['Content-type'] = 'image/png'

        names = ['datei','com_update','com_insert','com_delete','com_replace']
        titles = ['数据库 - 写','queries per day','Jun 12, 2010']

        rows = model.meta.Session.query(model.Mysqlg1).all()

        return _m.Multiline(rows,names,titles).display()

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/wsgiapp.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class WsgiappController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/wsgiapp.mako')
        # or, return a string
        return 'Hello World'

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/contacts.py
##########################################
# -*- coding: utf-8 -*-
import logging

from pylons import config,request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from pyfisheyes import model
from webhelpers import paginate
import pyfisheyes.lib.helpers as h
from pyfisheyes.model.utils import ContactHandle as _ch
from turbomail import Message


log = logging.getLogger(__name__)

class ContactsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/contacts.mako')
        # or, return a string
        return 'Hello World'
    
    def list(self):
        c.pagename = "contacts"
        c.heading = "Contacts::List"
        c.qw = ""        
        log.info(config['app_conf']['my_contacts'])
        my_contacts = config['app_conf']['my_contacts']
        if len(my_contacts)>2:
            c.my_contacts = my_contacts.split(',')
        else:
            c.my_contacts = []
            
        if "qw" in request.params:
            qw = request.params['qw']
        else:
            qw = "nothing"
        c.qw = qw
        
        con = model.Contacts
        contacts = model.meta.Session.query(model.Contacts).filter(con.forsearch.like('%'+qw+'%')).order_by(con.id.asc())

        c.contacts = paginate.Page(
            contacts,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        )
        
        return render('/derived/contacts/list.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def edit(self,id):
        assert id and isinstance(id, basestring)     
        c.pagename = "contacts"
        c.heading = "Contacts::Edit"
        c.act = 'edit'
        c.contact_id = id
        c.contact = model.meta.Session.query(model.Contacts).filter_by(id=id).first()
        return render('/derived/contacts/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def editsubmit(self,id):
        assert id and isinstance(id, basestring)
        ch = _ch.ContactHandle(request)
        qw = ""
        qw = ch.saveContact(id)
        redirect('/contacts/list/1?qw='+qw)      
        return ''
    
    @h.auth.authorize(h.auth.is_valid_user)
    def new(self):        
        c.pagename = "contacts"
        c.heading = "Contacts::New"
        c.contact = model.Contacts()     
        return render('/derived/contacts/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def newsubmit(self):
        ch = _ch.ContactHandle(request)
        qw = ch.createContact()
        redirect('/contacts/list/1?qw='+qw)     
        return ''

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/chart.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes.model.chartobj import XZoneColoring as _g


log = logging.getLogger(__name__)

class ChartController(BaseController):

    def __before__(self):
        response.headers['Content-type'] = 'image/png'


    def index(self):
        return _g.XZoneColoring().display()

   

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/cookie.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class CookieController(BaseController):

    def _index(self):
        # Return a rendered template
        #return render('/cookie.mako')
        # or, return a string
        return 'Hello World'

    def index(self):
        name = 'NULL'
        if request.cookies.has_key('name'):
            name = request.cookies['name']
        return 'cookie name=%s' % name

    def setcookie(self):
        response.set_cookie("name", "tony")
        #response.set_cookie(self, key, value='', max_age=None, path='/', domain=None, secure=None,
        #         httponly=False, version=None, comment=None, expires=None, overwrite=False)
        return "write cookie ok"

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/view.py
##########################################
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
        if request.cookies.has_key('set_default_day') and 'd2' not in request.params:
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
        if request.cookies.has_key('set_default_day'):
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
        if 'partial' in request.params:                
            return render('/derived/view/onlydata.html')
        else:
            return render('/derived/view/view.html')

    def graph(self, id, opt="0", date="", date2="", big=False):       
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
                fsize = date2
                gp = self.rtgrap_big(t, vh, fsize, titles, date, hidden, ys)
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
        else :
            exp = timedelta(seconds=315360000)
            now = datetime.utcnow()
            response.headers['Cache-Control'] = 'max-age=315360000'
            response.headers['Expires'] = (now + exp).strftime('%a, %d %b %Y %H:%M:%S GMT')
        return gp
    
    def graph2(self, id, opt, date, fsize):       
        assert id and isinstance(id, basestring)
        assert opt and isinstance(opt, basestring)
        assert date and isinstance(date, basestring)
        assert fsize and isinstance(fsize, basestring)
        #/view/graph2/100/1/2011-04-16/660x250/1.png
        #/view/graph2/100/1/2011-04-16/7126x250/2.png
        gp = self.graph(id, opt, date, fsize, True)
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
            
        e_tup = (rows1, rows2, lables1, lables2, line1_color, line2_color)
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
    def test(self):
        self.data(self,119,)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/form.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

import os
import shutil
from pylons import config

log = logging.getLogger(__name__)

class FormController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/form.mako')
        # or, return a string
        #return 'Hello World'
        return render('/form.mako')

    def submit(self):
        return "hello, name: %s" % request.params['name']

    def upload(self):
        name   = request.POST['name']
        myfile = request.POST['file']
        local_name = os.path.join(config['app_conf']['upload_dir'], myfile.filename)
        local_file = open(local_name, "wb")
        shutil.copyfileobj(myfile.file, local_file)
        myfile.file.close()
        local_file.close()
        return "hello, name: %s, upload: %s" % (name, myfile.filename)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/database.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes import model

log = logging.getLogger(__name__)

class DatabaseController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/database.mako')
        # or, return a string
        #return 'Hello World'
        c.msgs = model.meta.Session.query(model.Msg).all()
        return render('/database.mako')

    def add(self):
        content = request.POST['content']
        msg = model.Msg()
        msg.content = content
        model.meta.Session.add(msg)
        model.meta.Session.commit()
        return "add %s ok..." % content

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/error.py
##########################################
import cgi

from paste.urlparser import PkgResourcesParser
from pylons.middleware import error_document_template
from webhelpers.html.builder import literal

from pyfisheyes.lib.base import BaseController

from pylons import tmpl_context as c
from pyfisheyes.lib.base import render


class ErrorController(BaseController):
    """Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.

    """
    def document2(self):
        """Render the error document"""
        request = self._py_object.request
        resp = request.environ.get('pylons.original_response')
        content = literal(resp.body) or cgi.escape(request.GET.get('message', ''))
        page = error_document_template % \
            dict(prefix=request.environ.get('SCRIPT_NAME', ''),
                 code=cgi.escape(request.GET.get('code', str(resp.status_int))),
                 message=content)
        return page
    
    def document(self):
        """Render the error document"""
        request = self._py_object.request
        resp = request.environ.get('pylons.original_response')
        code = cgi.escape(request.GET.get('code', ''))
        content = cgi.escape(request.GET.get('message', ''))
        if resp:
            content = literal(resp.status)
            code = code or cgi.escape(str(resp.status_int))
        if not code:
            raise Exception('No status code was found')
        c.code = code
        c.message = content
        return render('/derived/error/document.html')

    def img(self, id):
        """Serve Pylons' stock images"""
        return self._serve_file('/'.join(['media/img', id]))

    def style(self, id):
        """Serve Pylons' stock stylesheets"""
        return self._serve_file('/'.join(['media/style', id]))

    def _serve_file(self, path):
        """Call Paste's FileApp (a WSGI application) to serve the file
        at the specified path
        """
        request = self._py_object.request
        request.environ['PATH_INFO'] = '/%s' % path
        return PkgResourcesParser('pylons', 'pylons')(request.environ, self.start_response)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/logstuffshow.py
##########################################
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

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/tmc.py
##########################################
#coding=utf-8
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render
from webhelpers import paginate
from pyfisheyes import model
from pyfisheyes.model import multiline as _m

log = logging.getLogger(__name__)

class TmcController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/apperrorlog.mako')
        # or, return a string
        return 'Hello World'

    def data(self):        
        c.topic = "Too Many Connections"
        try :
            page_set = int(request.params['page'])
        except:
            page_set = 1 
        c.rows = paginate.Page(
        model.meta.Session.query(model.Tmc),
        page = page_set,
        items_per_page = 10)
        
        return render('/displaydata.mako')

    def graph(self):
        response.headers['Content-type'] = 'image/png'

        names = ['datei','t']
        titles = ['生产环境中的tmc','tmc per day','Jun 12, 2010']

        rows = model.meta.Session.query(model.Tmc).all()

        return _m.Multiline(rows,names,titles).display()
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/home.py
##########################################
import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from webhelpers import paginate
from pyfisheyes import model

log = logging.getLogger(__name__)

class HomeController(BaseController):
    requires_auth = False

    def index(self):
        c.pagename = "homepage"
        
        
        return render('/derived/homepage/home.html')

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/controllers/events.py
##########################################
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
import textile
from pyfisheyes.lib.archivefile import extractall

log = logging.getLogger(__name__)


class EventsController(BaseController):

    
    def index(self):
        c.pagename = "events"
        # Return a rendered template
        #return render('/events.mako')
        # or, return a string        
        return "404"
    
    def list(self,id="0000-00-00"):
        assert id and isinstance(id, basestring)
        c.pagename = "events"
        c.heading = "Events::List"
        eh = _eh.EventHandle(request)
        events = eh.searchEvent(id)

        c.events = paginate.Page(
            events,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        ) 
        return render('/derived/events/list.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def new(self,id="0000-00-00"):
        assert id and isinstance(id, basestring)
        c.pagename = "events"
        c.event = model.Events()
        c.event.evdate = id
        c.heading = "Events::New"     
        log.debug("new::upload")
        self.__initValue__()
        return render('/derived/events/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def edit(self,id):
        c.pagename = "events"
        c.heading = "Events::Edit"
        assert id and isinstance(id, basestring)        
        c.event = model.meta.Session.query(model.Events).filter_by(id=id).first()
        c.id = id
        
        self.__initValue__()     
        return render('/derived/events/new.html')
    
    @h.auth.authorize(h.auth.is_valid_user)
    def newsubmit(self):
        eh = _eh.EventHandle(request)
        result = eh.createEvent()
        redirect('/events/detail/' + str(result.lastrowid))            
        return ""
    
    @h.auth.authorize(h.auth.is_valid_user)
    def editsubmit(self,id):
        assert id and isinstance(id, basestring)        
        eh = _eh.EventHandle(request)
        eh.modifyEvent(id)        
        
        redirect('/events/detail/'+id)      
            
        return ""
    
    def detail(self,id):
        c.pagename = "events"
        c.heading = "Events::Detail"
        assert id and isinstance(id, basestring)
        eh = _eh.EventHandle(request)
        c.event = eh.viewEvent(id)
        if not c.event:
            abort(404)
        return render('/derived/events/detail.html')
    
    def preview(self):
        return h.literal(textile.textile(request.params['data']))
    
    def __initValue__(self):
        c.event_type = ['noset','Story','Failure']
        c.event_status = ['noset','New','Open','Closed']
        c.event_cause = ['noset','Physical Disaster','Component Failure','Capacity Planning','Operator Error or Malicious Users/Code','Planned Administration & Maintenance','Software Bug or Crash']
        c.event_domain = ['noset','yoursite.com','yoursite1.com','yoursite2.com','bbs','mobileapi','all','other']
        
    def upload(self):
        log.debug("events::upload")
        """POST /photos/upload: Upload archive of photo"""
        # url(controller='import', action='upload')

        # gp.fileupload stores uploaded filename in fieldstorage
        fieldstorage = request.params.get('file', u'')
        if fieldstorage == u'':
            log.debug("Nothing uploaded")
            abort(400)
        filepath = os.path.join(
            config['global_conf']['upload_dir'],
            fieldstorage.file.read().strip(" \n\r"))
        log.debug("File has been downloaded to %s" %(filepath))
        fieldstorage.file.close()
        res = {
            "status": False,
            "msg": '',
            "dest_uri": ''
        }
        try:
            # extract archive to "import" directory
            extractall(filepath, config['app_conf']['import_dir'])

            # walk in import directory to delete all files that are not photos
            for dirpath, dirs, files in os.walk(
                config['app_conf']['import_dir'], topdown=False):
                for filename in files:
                    abspath = os.path.join(dirpath, filename)
                    log.debug("walk on file: %s" %abspath)
                    
                    if os.path.splitext(abspath)[1].lower() not in ['.jpg', '.jpeg', '.png']:
                        log.debug("Remove non jpeg file: %s" %abspath)
                        os.remove(abspath)
                    else:
                        log.debug("json:" + os.path.split(abspath)[1])
                        log.debug("import_dir:"+config['app_conf']['import_dir'])
                        res = self._createImage('/import/'+os.path.split(abspath)[1])                       
                        
                for subdirname in dirs:
                    abspath = os.path.join(dirpath, subdirname)
                    log.debug("walk on dir: %s" %abspath)
                    try:
                        os.rmdir(abspath)
                    except OSError:
                        log.debug('directory is not empty')
            log.debug("Extraction to %s has succeeded" %(config['app_conf']['import_dir']))
        except Exception, e:
            # TODO: log error in session (flash message)
            log.error(e)
#            raise e
        # delete the uploaded archive if no exception is raised
        os.remove(filepath)
        
        if res['status']:            
            return '/' + config['app_conf']['photos_public_dir'] + '/orig/' + str(res['dest_uri'])
        else:
            return str(res['msg'])
        
    def _createImage(self,path=None):
        """POST /photos: Create a new item"""
        # url('photos')
        
        abspath, uri = unchroot_path(
            path,
            config['app_conf']['import_dir'])
        
        ip = ImageProcessing(
            config['app_conf']['import_dir'],
            os.path.join(
                config['pylons.paths']['static_files'],
                config['app_conf']['photos_public_dir']))

        error = False
        msg = None
        dest_uri = None
        try:
            # check same image has not already been imported
#            f = open(abspath)
#            try:
#                hash = md5_for_file(f)
#            finally:
#                f.close()
#            photo = Session.query(PyGallPhoto).filter_by(md5sum=hash)
#            if photo.count() > 0:
#                raise Exception("Same md5sum already exists in database")

            # process and import photos to public/data/photos dir
            date, dest_uri = ip.process_image(uri)
            # import image in db
#            photo = PyGallPhoto()
#            photo.uri = dest_uri
#            photo.md5sum = hash
#            photo.time = date
#            Session.add(photo)
#            Session.commit()

#            remove_empty_dirs(config['app_conf']['import_dir'])
        except Exception, e:
            error = True
            msg = "%s [%s]" %(str(e), path)
            log.error(msg)

        return {
            "status": not error,
            "msg": msg,
            "dest_uri": dest_uri
        }

    
##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/__init__.py
##########################################
"""Pylons application test package

This package assumes the Pylons environment is already loaded, such as
when this script is imported from the `nosetests --with-pylons=test.ini`
command.

This module initializes the application via ``websetup`` (`paster
setup-app`) and provides the base testing objects.
"""
from unittest import TestCase
import os
import sys

import pylons
from pylons.i18n.translation import _get_translator
from paste.deploy import loadapp
from pylons import url
from paste.script.appinstall import SetupCommand
from routes.util import URLGenerator
from webtest import TestApp

from pyfisheyes.config.environment import load_environment

__all__ = ['environ', 'url', 'TestController']

environ = {}
here_dir = os.path.dirname(os.path.abspath(__file__))
conf_dir = os.path.dirname(os.path.dirname(here_dir))

sys.path.insert(0, conf_dir)


class TestController(TestCase):
    def __init__(self, *args, **kwargs):
        wsgiapp = loadapp('config:test.ini', relative_to=conf_dir)
        config = wsgiapp.config
        pylons.app_globals._push_object(config['pylons.app_globals'])
        pylons.config._push_object(config)
        
        # Initialize a translator for tests that utilize i18n
        translator = _get_translator(pylons.config.get('lang'))
        pylons.translator._push_object(translator)
        
        url._push_object(URLGenerator(config['routes.map'], environ))
        self.app = TestApp(wsgiapp)
        TestCase.__init__(self, *args, **kwargs)

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/test_models.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_apperrorlog.py
##########################################
from pyfisheyes.tests import *

class TestApperrorlogController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='apperrorlog', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_example.py
##########################################
from pyfisheyes.tests import *

class TestExampleController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='example', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_account.py
##########################################
from pyfisheyes.tests import *

class TestAccountController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='account', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_security.py
##########################################
from pyfisheyes.tests import *

class TestSecurityController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='security', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_events.py
##########################################
from pyfisheyes.tests import *

class TestEventsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='events', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_categories.py
##########################################
from pyfisheyes.tests import *

class TestCategoriesController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='categories', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_session.py
##########################################
from pyfisheyes.tests import *

class TestSessionController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='session', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_daily_report.py
##########################################
from pyfisheyes.tests import *

class TestDailyReportController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='daily_report', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_view.py
##########################################
from pyfisheyes.tests import *

class TestViewController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='view', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_home.py
##########################################
from pyfisheyes.tests import *

class TestHomeController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='home', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_wsgiapp.py
##########################################
from pyfisheyes.tests import *

class TestWsgiappController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='wsgiapp', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_tmc.py
##########################################
from pyfisheyes.tests import *

class TestTmcController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='tmc', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_logstuffshow.py
##########################################
from pyfisheyes.tests import *

class TestLogstuffshowController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='logstuffshow', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_alert.py
##########################################
from pyfisheyes.tests import *

class TestAlertController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='alert', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_speed.py
##########################################
from pyfisheyes.tests import *

class TestSpeedController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='speed', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_chart.py
##########################################
from pyfisheyes.tests import *

class TestChartController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='chart', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_database.py
##########################################
from pyfisheyes.tests import *

class TestDatabaseController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='database', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_contacts.py
##########################################
from pyfisheyes.tests import *

class TestContactsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='contacts', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_cookie.py
##########################################
from pyfisheyes.tests import *

class TestCookieController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='cookie', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_mysqlg1.py
##########################################
from pyfisheyes.tests import *

class TestMysqlg1Controller(TestController):

    def test_index(self):
        response = self.app.get(url(controller='mysqlg1', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_form.py
##########################################
from pyfisheyes.tests import *

class TestFormController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='form', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/tests/functional/test_list.py
##########################################
from pyfisheyes.tests import *

class TestListController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='list', action='index'))
        # Test response...

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/config/routing.py
##########################################
"""Routes configuration

The more specific and detailed routes should be defined first so they
may take precedent over the more generic routes. For more information
refer to the routes manual at http://routes.groovie.org/docs/
"""
from routes import Mapper

def make_map(config):
    """Create, configure and return the routes Mapper"""
    map = Mapper(directory=config['pylons.paths']['controllers'],
                 always_scan=config['debug'])
    map.minimization = False
    map.explicit = False

    # The ErrorController route (handles 404/500 error pages); it should
    # likely stay at the top, ensuring it can always be resolved
    map.connect('/error/{action}', controller='error')
    map.connect('/error/{action}/{id}', controller='error')

    # CUSTOM ROUTES HERE
    map.connect('home', '/', controller='home', action='index')
    
    map.connect('signout', '/signout', controller='account', action='signout')
    map.connect('signin', '/signin', controller='account', action='signin')
    map.connect('signinagain', '/signinagain', controller='account', action='signinagain')

    map.connect('template', '/template', controller='categories', action='index')
    map.connect('events', '/events', controller='events', action='list')
    map.connect('alert', '/alert', controller='alert', action='list')
    map.connect('contacts', '/contacts', controller='contacts', action='list')
    map.connect('logstuffshow', '/logstuffshow', controller='logstuffshow', action='index')
    map.connect('speed', '/speed', controller='speed', action='index')
    
    map.connect('/{controller}/{action}')
    map.connect('/{controller}/{action}/{id}')
    map.connect('/{controller}/{action}/{id}/{page}')
    map.connect('/{controller}/{action}/{tid}/{datei}/{timei}')
    map.connect('/{controller}/{action}/{id}/{page}/{date}/{date2}')
    
    map.connect('/{controller}/{action}/{id}/{opt}/{date}/{date2}/1.png')
    map.connect('/{controller}/{action}/{id}/{opt}/{date}/{fsize}/2.png')
    

    return map

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/config/__init__.py
##########################################

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/config/middleware.py
##########################################
"""Pylons middleware initialization"""
from beaker.middleware import SessionMiddleware
from paste.cascade import Cascade
from paste.registry import RegistryManager
from paste.urlparser import StaticURLParser
from paste.deploy.converters import asbool
from pylons.middleware import ErrorHandler, StatusCodeRedirect
from pylons.wsgiapp import PylonsApp
from routes.middleware import RoutesMiddleware

import authkit.authenticate

from pyfisheyes.config.environment import load_environment

def make_app(global_conf, full_stack=True, static_files=True, **app_conf):
    """Create a Pylons WSGI application and return it

    ``global_conf``
        The inherited configuration for this application. Normally from
        the [DEFAULT] section of the Paste ini file.

    ``full_stack``
        Whether this application provides a full WSGI stack (by default,
        meaning it handles its own exceptions and errors). Disable
        full_stack when this application is "managed" by another WSGI
        middleware.

    ``static_files``
        Whether this application serves its own static files; disable
        when another web server is responsible for serving them.

    ``app_conf``
        The application's local configuration. Normally specified in
        the [app:<name>] section of the Paste ini file (where <name>
        defaults to main).

    """
    # Configure the Pylons environment
    config = load_environment(global_conf, app_conf)

    # The Pylons WSGI app
    app = PylonsApp(config=config)

    # Routing/Session Middleware
    # If set singleton=False, proxy-filter failed to work.
    #app = RoutesMiddleware(app, config['routes.map'], singleton=False)
    app = RoutesMiddleware(app, config['routes.map'])
    app = SessionMiddleware(app, config)

    # CUSTOM MIDDLEWARE HERE (filtered by error handling middlewares)

    if asbool(full_stack):
        # Handle Python exceptions
        app = ErrorHandler(app, global_conf, **config['pylons.errorware'])
        
        app = authkit.authenticate.middleware(app, app_conf)

        # Display error documents for 401, 403, 404 status codes (and
        # 500 when debug is disabled)
        if asbool(config['debug']):
            app = StatusCodeRedirect(app)
        else:
            app = StatusCodeRedirect(app, [400, 401, 403, 404, 500])

    # Establish the Registry for this application
    app = RegistryManager(app)

    if asbool(static_files):
        # Serve static files
        static_app = StaticURLParser(config['pylons.paths']['static_files'])
        app = Cascade([static_app, app])
    app.config = config
    return app

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/config/environment.py
##########################################
"""Pylons environment configuration"""
import os

from mako.lookup import TemplateLookup
from pylons.configuration import PylonsConfig
from pylons.error import handle_mako_error
from sqlalchemy import engine_from_config

import pyfisheyes.lib.app_globals as app_globals
import pyfisheyes.lib.helpers
from pyfisheyes.config.routing import make_map
from pyfisheyes.model import init_model

def load_environment(global_conf, app_conf):
    """Configure the Pylons environment via the ``pylons.config``
    object
    """
    config = PylonsConfig()
    
    # Pylons paths
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = dict(root=root,
                 controllers=os.path.join(root, 'controllers'),
                 static_files=os.path.join(root, 'public'),
                 templates=[os.path.join(root, 'templates')])

    # Initialize config with the basic options
    config.init_app(global_conf, app_conf, package='pyfisheyes', paths=paths)

    config['routes.map'] = make_map(config)
    config['pylons.app_globals'] = app_globals.Globals(config)
    config['pylons.h'] = pyfisheyes.lib.helpers
    
    # Setup cache object as early as possible
    import pylons
    pylons.cache._push_object(config['pylons.app_globals'].cache)
    


    # Create the Mako TemplateLookup, with the default auto-escaping
    config['pylons.app_globals'].mako_lookup = TemplateLookup(
        directories=paths['templates'],
        error_handler=handle_mako_error,
        module_directory=os.path.join(app_conf['cache_dir'], 'templates'),
        input_encoding='utf-8', output_encoding='utf-8',
        imports=['from webhelpers.html import escape'],
        default_filters=['escape'])


    # Setup the SQLAlchemy database engine
    engine = engine_from_config(config, 'sqlalchemy.')
#    syslogdb_engine = engine_from_config(config, 'syslogdb.')
    init_model(engine)
#    tmpl_options['mako.default_filters']= ['decode.utf8']
    # CONFIGURATION OPTIONS HERE (note: all config options will override
    # any Pylons config options)
    
    return config

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/jobs/alter_message.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib,urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

#conf = appconfig('config:' + '/home/tonycai/pyfisheyes/production.ini')
conf = appconfig('config:' + '/home/tonycai/pyfisheyes/production_20110128.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

from datetime import datetime, timedelta, date

__usage__ = \
"""

    Usage: 
    python ./alter_message.py --action=lookup
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags   = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def lookup_system():
     t = model.Categories
     categories = model.meta.Session.query(t).filter_by(graphtype="realtime").order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
     for i,d in enumerate(categories):
	#print d.typename
	compare_background_data(d)
     return None

def send_mail(level, title, id, status, t1, t2, d2):

        vh = _vh.ViewHandle()
	attach_dir = "/home/tonycai/pyfisheyes/jobs/attach_files"

	mail_subject = "[" + level + "] " + title + " - " + status
        start_time = u"开始时间: "
        stop_time = u"结束时间: "
        detail = u"详细内容:"
	site_url = "http://pyfisheyes.corp.yoursite.com"
	t_url = site_url + "/view/data/" + str(id) + "/1/" + d2 + "/" + d2

	text_part = u" 时间: " + d2 + " (" +  t1 + "  -  " + t2 +  ")"

        html_part = "<html><header/><body><h1>Look,</h1> "
        html_part += "<h1>" + title + "</h1>"
        html_part += "<p>" + status + " (" +  t1 + " - " + t2 + ")</p>"
        html_part += "<p>" + detail + " <a href=" + t_url + " >" + t_url + "</a> </p>"
        html_part += "<p>this mail sent by PyFisheyes</p></body></html> "

        message = Message("noreply@yoursite.com","xxxxxx@yoursite.com",mail_subject)
        message.encoding = "utf-8"
        message.plain = text_part
        message.rich = html_part        
        message.cc = "xxxxxx@yoursite.com"

        timestamp = time.time()

	url1 = "/view/realtimegraph/"+str(id)+"/1.png"
        img1 = attach_dir + "/realtimegraph." + str(id) + "." + str(timestamp) + ".png"

	if download_file(url1,img1):
        	message.attach(img1)

        message.send()

def compare_background_data(t , min=4):
        
        vh = _vh.ViewHandle()
            
        timerange1 = vh.getTimeRange(min, 0)
        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
	day_name = u"同比上周同一天"
        
        timerange2 = vh.getTimeRange(min, 7)
	if t.u_baseface and t.baseface:
	    day_name = u"相比" + str(t.baseface)
            td = vh.__getDate__("",0).split("-")
            bf =str(t.baseface).split("-")
            days = (date(int(td[0]), int(td[1]), int(td[2])) - date(int(bf[0]), int(bf[1]), int(bf[2]))).days 
            timerange2 = vh.getTimeRange(min, days)
        else:
            timerange2 = vh.getTimeRange(min, 7)

        rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)

	level = None
        status = ""
        time_range = ""

        start_time_point = timerange1['start_time_point']
        stop_time_point = timerange1['stop_time_point']
        datetime1 = start_time_point.strftime('%H:%M')
        datetime2 = stop_time_point.strftime('%H:%M')
        date2 = start_time_point.strftime('%Y-%m-%d')

        allt = vh.exec_alarm_threshold(rows1, rows2, t)

        if t.r_mode == 'a':
	   	status = u"突然升至: " + str(int(allt[1])) + u"次/分钟"

        if t.r_mode == 'b':
	   	status = u"突然降至: " + str(int(allt[1])) + u"次/分钟"

        if t.r_mode in ['c', 'd']:
		if int(allt[1]) < 0 :
	   		status = day_name + u"下跌: " + str(abs(int(allt[1]))) + "%"
		else:
	   		status = day_name  + u"上涨: " + str(int(allt[1])) + "%"

        if int(allt[0]) == 1:
		level = "Warning"
        if int(allt[0]) == 2:
		level = "Critical"

	if level == "Critical" and t.r_weight>5:
		send_mail(level, t.typename, t.typeid, status, datetime1, datetime2, date2)

        #return {'level':level,'ratio':dv_ratio,'2':[],'3':[]}
        return level

def sumValue(data):
        v = 0
        for i,d in enumerate(data):
            v += d.valuei
        return v

def download_file(url, local_file):
	isExist = False
	try:
        	conn=httplib.HTTPConnection("127.0.0.1:8000")
        	conn.request("GET",url)
        	response = conn.getresponse()
        	data = response.read()
        	f = open(local_file, "w")
		f.write(data)
		f.close()
		isExist = True
     	except:
         	print "except"
	return isExist

    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('action') or flags.has_key('help'):
        print __usage__
    else:
        if flags['action'] == 'lookup':
            lookup_system()
        if flags['action'] == 'mail':
            send_mail()

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/jobs/daily_report.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib,urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

#conf = appconfig('config:' + '/home/tonycai/pyfisheyes/production.ini')
conf = appconfig('config:' + '/home/tonycai/pyfisheyes/production_20110128.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

__usage__ = \
"""

    Usage: 
    python ./daily_report.py --action=lookup
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags   = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def lookup_system():
     t = model.Categories
     items = []
     categories = model.meta.Session.query(t).filter_by(graphtype="realtime").filter_by(d_report=1).order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
     for i,d in enumerate(categories):
	#print d.typename
	items.append(compare_background_data(d))
     #items = items.sort(t_cmp)
     items.sort(my_cmp)
     #print items
     send_reports(items)
     return None

def send_reports(its):
        vh = _vh.ViewHandle()
	date1 = vh.__getDate__("", 1)
	attach_dir = "/home/tonycai/pyfisheyes/jobs/attach_files"

	mail_subject = "Site System Daily Report " + date1 + " - PyFisheyes"
        start_time = u"开始时间:"
        stop_time = u"结束时间:"
	time_range = u"时间范围:"
	u1 = (u"芙妹",'EVA')
	u2 = (u"秀才",'Wall-E')
	site_url = "http://pyfisheyes.corp.yoursite.com"
	attach_dir = "/home/tonycai/pyfisheyes/jobs/attach_files"
        message = Message("noreply@yoursite.com","xxxxxx@yoursite.com",mail_subject)
        #message = Message("noreply@yoursite.com","xxxxxx@yoursite.com",mail_subject)
        message.encoding = "utf-8"

	text_part = ""

        html_part = "<html><header/> <body> <h1>Look,</h1> " + u1[1]
        #html_part += "<p>" + u"今天09:30发出的报告数据有误，特此更正!" + "</p>"
	html_section = ""
	timestamp = time.time()
	timestamp1 = str(timestamp)
        for x, E in enumerate(its):
		item = checkItems(E[0], E[1], E[2], E[3], E[4], E[5], E[6], E[7])
		level = item.level
		typename = item.typename
		typeid = item.typeid
		typeid = str(typeid)
		status = item.status
		level = item.level
		d1 = item.d1
		d2 = item.d2
		if level != "Norml":
			url2 = "/view/graph/"+typeid+"/0/"+date1+"/"+date1+"/1.png"
			t_url = site_url + "/view/data/" + typeid + "/1/" + date1 + "/" + date1
			img2 = attach_dir + "/graph." + typeid + "." + timestamp1 + ".png"

			html_section += "<h2>" + str(x+1) + ") " + typename + " <a href=\""+ t_url + "\">#" + typeid +  "</a></h2>" 
			html_section += "<p>" + status + "</p>" 
			html_section += "<p>" + time_range + d1 + " - " + d2 + "</p>" 
		
			html_section += "<p><img src=\"" + site_url + url2 + "\" alt=\""+typename+"\"></p>"
			#html_section += "<p>" + t_url + "</p>" 
			html_section += "<p>---section end---</p>" 
			#print "%s %s %s" % (typename, typeid, status)
			# add attach
			#if download_file(url2,img2):
                	#	message.attach(img2)

        html_footer = "<p> Sent by " + u2[1] + " </p> </body> </html>"

        message.plain = typename + status
        message.rich = html_part + html_section + html_footer
        message.cc = "xxxxxx@yoursite.com"

        message.send()

def compare_background_data(t , min=4):
        
        vh = _vh.ViewHandle()

        date1 = vh.__getDate__("", 1)
            
        timerange1 = vh.getSharpDayMinute(date1)

        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
	sum1 = sumValue(rows1)
        
        timerange2 = vh.getSharpDayMinute(date1, 7)

        rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)
	sum2 = sumValue(rows2)

	dv_ratio = 0
	level = "Norml"
        status = ""
        time_range = ""

        start_time_point = timerange1['start_time_point']
        stop_time_point = timerange1['stop_time_point']
        datetime1 = start_time_point.strftime('%Y-%m-%d %H:%M:00')
        datetime2 = stop_time_point.strftime('%Y-%m-%d %H:%M:00')

        try:
        	dv_ratio = (sum2 - sum1)*100 / sum2
		if dv_ratio > 0 :
		   status = u"同比上周同一天下跌:<strong>" + str(abs(dv_ratio)) + "%</strong>"
		else:
		   status = u"同比上周同一天上涨:<strong>" + str(abs(dv_ratio)) + "%</strong>"
        except:
		print "ZeroDivisionError"

        if abs(dv_ratio) > 10:
		level = "Warning"
        if abs(dv_ratio) > 20:
		level = "Critical"

        return (level, t.typename, t.typeid, status, datetime1, datetime2, t.r_weight, abs(dv_ratio))

def sumValue(data):
        v = 0
        for i,d in enumerate(data):
            v += d.valuei
        return v

def download_file(url, local_file):
	isExist = False
	try:
        	conn=httplib.HTTPConnection("127.0.0.1:8000")
        	conn.request("GET",url)
        	response = conn.getresponse()
        	data = response.read()
        	f = open(local_file, "w")
		f.write(data)
		f.close()
		isExist = True
     	except:
         	print "except"
	return isExist

def my_cmp(E1, E2):
    #print 'E1:', E1[7], 'E2:', E2[7]
    return -cmp(E1[7], E2[7])


class checkItems:
	def __init__(self, level, typename, typeid, status, d1, d2, w, m):
        	self.level = level
        	self.typename = typename
        	self.typeid = typeid
        	self.status = status
        	self.d1 = d1
        	self.d2 = d2
        	self.weight = w
        	self.margin = m


    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('action') or flags.has_key('help'):
        print __usage__
    else:
        if flags['action'] == 'lookup':
            lookup_system()
        if flags['action'] == 'mail':
            send_mail()

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/jobs/graphs_job.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/tonycai/pyfisheyes/production_20110128.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model

__usage__ = \
"""

    Usage: 
    python ./graphs_job.py --template=tmc --action=delete --values=2010-12-16
    python ./graphs_job.py --template=tmc --action=show
    python ./graphs_job.py --template=tmc --action=update --values=2010-12-16,4
    python ./graphs_job.py --template=tmc --action=add --values=2010-12-16,4
    
    clean
    s=1;e=400;for i in `seq $s $e`;do x=$(($e-$i)); d=`date +%F -d "$x days ago"`;echo -n "$d : "; python ./graphs_job.py --template=tmc --action=delete --values=$d; done
    
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags   = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def __config__(cn):
    ca = model.meta.Session.query(model.Categories).filter_by(classname=cn).first()
    return ca

def __CheckStringFormat__(cn,values):
#NULL
    ca = __config__(cn)
    vlist = values.split(',')
    items = ca.items.split(',')
    if "NULL" in vlist:
        return False
    if len(vlist) == len(items):
        return True
    else:
        return False

def update(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        d = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).first()
        d.mediadata = values
        model.meta.Session.add(d)
        model.meta.Session.commit()
        return "UPDATE SUCCESS"
    else:
        return "Fail"

def add(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    #n = model.meta.Session.query(model.Graphs).filter_by(and_(datei=vlist[0], template_id=ca.typeid)).count()    
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        return update(cn,values)
    else:        
#        t = model.Apperrorlog()
        t = model.Graphs()
#        print t.__class__
        t.template_id = ca.typeid
        t.datei = vlist[0]
        t.mediadata = values
        model.meta.Session.add(t)
        model.meta.Session.commit()
        return "ADD SUCCESS"

def show(cn):
    ca = __config__(cn)
    return model.meta.Session.query(model.Graphs).filter_by(template_id=ca.typeid).all()
     

def delete(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        d = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).first()    
        model.meta.Session.delete(d)
        model.meta.Session.commit()
        return "SUCCESS"
    else:
        return "Fail"
     
    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('template') or flags.has_key('help'):
        print __usage__
    else:
        
        if flags['action'] == 'add':
#            try:
                print add(flags['template'],flags['values'])            
#            except:
#                print "Fail"
                
        if flags['action'] == 'show':
            rows = show(flags['template'])
            for row in rows:
                print row.tostring()
            
        if flags['action'] == 'delete':
            try:
                print delete(flags['template'],flags['values'])
            except:
                print "Fail"
                
        if flags['action'] == 'update':
            try:
                print update(flags['template'],flags['values'])
            except:
                print "Fail"
    

##########################################
####file_name: ./build/lib.linux-i686-2.6/pyfisheyes/websetup.py
##########################################
"""Setup the pyfisheyes application"""
import logging

from pyfisheyes.config.environment import load_environment
from pyfisheyes.model.meta import Session, Base

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup helloworld2 here"""
    # Don't reload the app if it was loaded under the testing environment
    load_environment(conf.global_conf, conf.local_conf)

    # Create the tables if they don't already exist
    Base.metadata.create_all(bind=Session.bind)

##########################################
####file_name: ./jobs/tmc_jobs.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/tonycai/workspace/pyfisheyes/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model

__usage__ = \
"""
    Usage: 
    python ./tmc_jobs.py --action=delete --date=2010-12-30
    python ./tmc_jobs.py --action=show
    python ./tmc_jobs.py --action=update --date=2010-12-16 --tmc=2
    python ./tmc_jobs.py --action=add --date=2010-12-16 --tmc=2
    
    clean
    s=1;e=400;for i in `seq $s $e`;do x=$(($e-$i)); d=`date +%F -d "$x days ago"`;echo -n "$d : "; python ./tmc_jobs.py --action=delete --date=$d; done
    
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags   = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def __config__(cn):
        ca = model.meta.Session.query(model.Categories).filter_by(classname=cn).first()
        return ca

def add(cn,values):
    ca = __config__(cn)
    vlist = values.split(',')
    vcols = ca.items.split(',')
    
    n = model.meta.Session.query(getattr(model,ca.classname)).filter_by(datei=vlist[0]).count()    
    if n > 0:
        return "Fail"
    else:        
#        t = model.Apperrorlog()
        
        t = getattr(model,ca.classname)()
#        print t.__class__
        i = 0
        for col in vcols:
            setattr(t,col,vlist[i])
            i += 1
        model.meta.Session.add(t)
        model.meta.Session.commit()
        return "SUCCESS"

def show(cn):
    ca = __config__(cn)
    return model.meta.Session.query(getattr(model,ca.classname))
     

def delete(datei):
    n = model.meta.Session.query(model.Tmc).filter_by(datei=datei).count()
    if n > 0:
        d = model.meta.Session.query(model.Tmc).filter_by(datei=datei).first()
        model.meta.Session.delete(d)
        model.meta.Session.commit()
        return "SUCCESS"
    else:
        return "Fail"
     
def update(datei,t):
    n = model.meta.Session.query(model.Tmc).filter_by(datei=datei).count()
    if n > 0:
        d = model.meta.Session.query(model.Tmc).filter_by(datei=datei).first()    
        d.t = t    
        model.meta.Session.add(d)
        model.meta.Session.commit()
        return "SUCCESS"
    else:
        return "Fail"
    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('action') or flags.has_key('help'):
        print __usage__
    else:
        
        if flags['action'] == 'add':
#            try:
                print add(flags['classname'],flags['values'])            
#            except:
#                print "Fail"
                
        if flags['action'] == 'show':
            rows = show(flags['classname'])
            for row in rows:
                print row.tostring()
            
        if flags['action'] == 'delete':
            try:
                print delete(flags['classname'],flags['values'])
            except:
                print "Fail"
                
        if flags['action'] == 'update':
            try:
                print update(flags['classname'],flags['values'])
            except:
                print "Fail"
    
##########################################
####file_name: ./jobs/hello.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib, urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/jobs/production_20110128.ini')
#conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/development_20.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

from datetime import datetime, timedelta, date
from pyfisheyes.model.utils import DailyReportHandle as _dh
from pyfisheyes.model.utils import GlobalHandle as _gh
def hello(abc):
    print abc
def hello2():
    hello("12345")

if __name__== '__main__':

    hello2()

##########################################
####file_name: ./jobs/daily_report_hyhe.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib, urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/tonycai/workspace/pyfisheyes/jobs/production_20110128.ini')
#conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

from datetime import datetime, timedelta, date
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import DailyReportHandle as _drh


def index(self):
        # Return a rendered template
        #return render('/daily_report.mako')
        # or, return a string
	return 'Hello World'   
def lookup_system(d=""):
	drh = _drh.DailyReportHandle() 
	i = model.Dateitems
        yesterday = datetime.now() - timedelta(1)
        y = yesterday.strftime('%Y-%m-%d')
        if d:
           y = d
        oy = datetime.strptime(y,'%Y-%m-%d')
	#odate = request.params.get('odate',y)
        #clearcache = request.params.get('clearcache','')
	#disabledlazy = request.params.get('disabledlazy','')
        #c.disabledlazy = disabledlazy
        #adate = datetime.strptime(odate,'%Y-%m-%d')
        #c.odate = odate
        dateitems = model.meta.Session.query(i).filter_by(datei=oy).first()
        if dateitems is None:
		#items = drh.createitems(odate)
		drh.saveitems(oy)
        #elif clearcache:
            #items = drh.createitems(odate)
            #drh.updateitem(adate, items) 
        else:
            #items = json.loads(dateitems.stuff)
		#items = drh.createitems(odate)
		drh.updateitems(oy)
        #c.items = items
        #return render("/derived/list/daily_report.html")
	return None
if __name__== '__main__':

    flags = ProcessCommandFlags(sys.argv[1:])

    if not flags or not flags.has_key('action') or flags.has_key('help'):
        print __usage__
    else:
        if flags['date']:
            lookup_system(flags['date'])

##########################################
####file_name: ./jobs/alert_message.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib, urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/jobs/production.ini')
#conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

from datetime import datetime, timedelta, date

__usage__ = \
"""

    Usage: 
    python ./alter_message.py --action=lookup
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def lookup_system():
     t = model.Categories
     categories = model.meta.Session.query(t).filter_by(graphtype="realtime").order_by(t.alertlevel.desc()).order_by(t.rankcode.asc())
     for i, d in enumerate(categories):
      #print d.typename
      compare_background_data(d)
     return None

def send_mail(level, title, id, status, t1, t2, d2):

        vh = _vh.ViewHandle()
        attach_dir = "/home/tonycai/pyfisheyes/jobs/attach_files"

        mail_subject = "[" + level + "] " + title + " - " + status
        start_time = u"开始时间: "
        stop_time = u"结束时间: "
        detail = u"详细内容:"
        site_url = "http://pyfisheyes.corp.yoursite.com"
        t_url = site_url + "/view/data/" + str(id) + "/1/" + d2 + "/" + d2

        text_part = u" 时间: " + d2 + " (" + t1 + "  -  " + t2 + ")"
        #mail_subject += text_part

        html_part = "<html><header/><body><h1>Look,</h1> "
        html_part += "<h1>" + title + "</h1>"
        html_part += "<p>" + status + " (" + t1 + " - " + t2 + ")</p>"
        html_part += "<p>" + detail + " <a href=" + t_url + " >" + t_url + "</a> </p>"
        html_part += "<p>this mail sent by PyFisheyes</p></body></html> "

        message = Message("noreply@yoursite.com", "xxxxxx@yoursite.com", mail_subject)
        message.encoding = "utf-8"
        message.plain = text_part
        message.rich = html_part        
        message.cc = "xxxxxx@yoursite.com"

        timestamp = time.time()

        url1 = "/view/realtimegraph/" + str(id) + "/1.png"
        img1 = attach_dir + "/realtimegraph." + str(id) + "." + str(timestamp) + ".png"
        if download_file(url1, img1):
            message.attach(img1)

        message.send()

def compare_background_data(t , min=4):
        
        vh = _vh.ViewHandle()
            
        timerange1 = vh.getTimeRange(min, 0)
        rows1 = vh.getRealtimeRowsData(t.typeid, timerange1)
        day_name = u"同比上周同一天"
        
        timerange2 = vh.getTimeRange(min, 7)
        if t.u_baseface and t.baseface:
            day_name = u"相比" + str(t.baseface)
            td = vh.__getDate__("", 0).split("-")
            bf = str(t.baseface).split("-")
            days = (date(int(td[0]), int(td[1]), int(td[2])) - date(int(bf[0]), int(bf[1]), int(bf[2]))).days 
            timerange2 = vh.getTimeRange(min, days)
        else:
            timerange2 = vh.getTimeRange(min, 7)

        rows2 = vh.getRealtimeRowsData(t.typeid, timerange2)
        level = None
        status = ""
        time_range = ""

        start_time_point = timerange1['start_time_point']
        stop_time_point = timerange1['stop_time_point']
        datetime1 = start_time_point.strftime('%H:%M')
        datetime2 = stop_time_point.strftime('%H:%M')
        date2 = start_time_point.strftime('%Y-%m-%d')

        allt = vh.exec_alarm_threshold(rows1, rows2, t)

        if t.r_mode == 'a':
           status = u"突然升至: " + str(int(allt[1])) + u"次/分钟"

        if t.r_mode == 'b':
           status = u"突然降至: " + str(int(allt[1])) + u"次/分钟"

        if t.r_mode in ['c', 'd']:
            if int(allt[1]) < 0 :
               status = day_name + u"下跌: " + str(abs(int(allt[1]))) + "%"
            else:
               status = day_name + u"上涨: " + str(int(allt[1])) + "%"

        if int(allt[0]) == 1:
            level = "Warning"
        if int(allt[0]) == 2:
            level = "Critical"

        if not isexist_same_alarm_log(t, int(allt[1]), 18):
            if level == "Critical" and t.r_weight > 5:
                send_mail(level, t.typename, t.typeid, status, datetime1, datetime2, date2)
            if level != None:
                alarm_logger(level, t, status, datetime1, datetime2, int(allt[1]))
            return level

def sumValue(data):
        v = 0
        for i, d in enumerate(data):
            v += d.valuei
        return v

def download_file(url, local_file):
    isExist = False
    try:
            conn = httplib.HTTPConnection("127.0.0.1:8000")
            conn.request("GET", url)
            response = conn.getresponse()
            data = response.read()
            f = open(local_file, "w")
            f.write(data)
            f.close()
            isExist = True
    except:
             print "except"
    return isExist

def alarm_logger(lev, t, stat, t1, t2, v):
    op = False
    try:
        now = datetime.now()
        datei = now.strftime('%Y-%m-%d')
        logtime = now.strftime('%Y-%m-%d %H:%M:%S')
        et = (0, t.typename, t.typeid, datei, stat, t.r_weight, t.r_mode, t1, t2, v, lev, logtime)
        al = model.Alarminfo(et)
        model.meta.Session.add(al)
        model.meta.Session.commit()
        op = True
    except:
        print "except"
    return op

def isexist_same_alarm_log(t, v, m):
    b = False
    try:
        now = datetime.now()
        itime = now - timedelta(minutes=m)
        logtime = itime.strftime('%Y-%m-%d %H:%M:%S')
        date_str = itime.strftime('%Y-%m-%d')
        al = model.Alarminfo
            #af = model.meta.Session.query(al).filter_by(tid=t.typeid).filter_by(datei=date_str).filter_by(t_threshold=v).filter(al.logtime>=logtime).first()
        af = model.meta.Session.query(al).filter_by(tid=t.typeid).filter(al.logtime > logtime).first()
        if af :
            b = True
    except:
          print "except"
    return b

    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('action') or flags.has_key('help'):
        print __usage__
    else:
        if flags['action'] == 'lookup':
            lookup_system()
        if flags['action'] == 'mail':
            send_mail()

##########################################
####file_name: ./jobs/daily_report.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging
import time
import httplib, urllib

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/tonycai/workspace/pyfisheyes/jobs/production_20110128.ini')
#conf = appconfig('config:' + '/home/hyhe/workspace/pyfisheyes/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model
from turbomail import Message
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import ViewHandle as _vh

from datetime import datetime, timedelta, date
from pyfisheyes.model.utils import GlobalHandle as _gh
from pyfisheyes.model.utils import DailyReportHandle as _drh


def index(self):
        # Return a rendered template
        #return render('/daily_report.mako')
        # or, return a string
	return 'Hello World'   
def lookup_system():
	drh = _drh.DailyReportHandle() 
	i = model.Dateitems
        yesterday = datetime.now() - timedelta(1)
        y = yesterday.strftime('%Y-%m-%d')
        oy = datetime.strptime(y,'%Y-%m-%d')
	#odate = request.params.get('odate',y)
        #clearcache = request.params.get('clearcache','')
	#disabledlazy = request.params.get('disabledlazy','')
        #c.disabledlazy = disabledlazy
        #adate = datetime.strptime(odate,'%Y-%m-%d')
        #c.odate = odate
        dateitems = model.meta.Session.query(i).filter_by(datei=oy).first()
        if dateitems is None:
		#items = drh.createitems(odate)
		drh.saveitems(oy)
        #elif clearcache:
            #items = drh.createitems(odate)
            #drh.updateitem(adate, items) 
        else:
            #items = json.loads(dateitems.stuff)
		#items = drh.createitems(odate)
		drh.updateitems(oy)
        #c.items = items
        #return render("/derived/list/daily_report.html")
	return None
if __name__== '__main__':
	lookup_system()

    

##########################################
####file_name: ./jobs/graphs_job.py
##########################################
#!/usr/bin/env python
#coding=utf-8

import sys
import re
import logging

from paste.deploy import appconfig
from pylons import config

from pyfisheyes.config.environment import load_environment

conf = appconfig('config:' + '/home/tonycai/workspace/pyfisheyes/development.ini')
load_environment(conf.global_conf, conf.local_conf)

from pyfisheyes import model

__usage__ = \
"""

    Usage: 
    python ./graphs_job.py --template=tmc --action=delete --values=2010-12-16
    python ./graphs_job.py --template=tmc --action=show
    python ./graphs_job.py --template=tmc --action=update --values=2010-12-16,4
    python ./graphs_job.py --template=tmc --action=add --values=2010-12-16,4
    
    clean
    s=1;e=400;for i in `seq $s $e`;do x=$(($e-$i)); d=`date +%F -d "$x days ago"`;echo -n "$d : "; python ./graphs_job.py --template=tmc --action=delete --values=$d; done
    
    
"""

def ProcessCommandFlags(args):
  """
  Parse command line flags per specified usage, pick off key, value pairs
  All flags of type "--key=value" will be processed as __flags[key] = value,
                    "--option" will be processed as __flags[option] = option
  """
 
  flags   = {}
  rkeyval = '--(?P<key>\S*)[=](?P<value>\S*)' # --key=val
  roption = '--(?P<option>\S*)'               # --key
  r = '(' + rkeyval + ')|(' + roption + ')'
  rc = re.compile(r)
  for a in args:
    try:
      rcg = rc.search(a).groupdict()
      if rcg.has_key('key'):
        flags[rcg['key']] = rcg['value']
      if rcg.has_key('option'):
        flags[rcg['option']] = rcg['option']
    except AttributeError:
      return None
  return flags
#end def ProcessCommandFlags

def __config__(cn):
    ca = model.meta.Session.query(model.Categories).filter_by(classname=cn).first()
    return ca

def __CheckStringFormat__(cn,values):
    ca = __config__(cn)
    vlist = values.split(',')
    items = ca.items.split(',')
    if len(vlist) == len(items):
        return True
    else:
        return False

def update(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        d = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).first()
        d.mediadata = values
        model.meta.Session.add(d)
        model.meta.Session.commit()
        return "UPDATE SUCCESS"
    else:
        return "Fail"

def add(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    #n = model.meta.Session.query(model.Graphs).filter_by(and_(datei=vlist[0], template_id=ca.typeid)).count()    
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        return update(cn,values)
    else:        
#        t = model.Apperrorlog()
        t = model.Graphs()
#        print t.__class__
        t.template_id = ca.typeid
        t.datei = vlist[0]
        t.mediadata = values
        model.meta.Session.add(t)
        model.meta.Session.commit()
        return "ADD SUCCESS"

def show(cn):
    ca = __config__(cn)
    return model.meta.Session.query(model.Graphs).filter_by(template_id=ca.typeid).all()
     

def delete(cn,values):
    if not  __CheckStringFormat__(cn,values):
        return "Fail : CheckStringFormat Error!"
    ca = __config__(cn)
    vlist = values.split(',')
    n = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).count()    
    if n > 0:
        d = model.meta.Session.query(model.Graphs).filter_by(datei=vlist[0]).filter_by(template_id=ca.typeid).first()    
        model.meta.Session.delete(d)
        model.meta.Session.commit()
        return "SUCCESS"
    else:
        return "Fail"
     
    
if __name__ == "__main__":
    flags = ProcessCommandFlags(sys.argv[1:])
    
    if not flags or not flags.has_key('template') or flags.has_key('help'):
        print __usage__
    else:
        
        if flags['action'] == 'add':
#            try:
                print add(flags['template'],flags['values'])            
#            except:
#                print "Fail"
                
        if flags['action'] == 'show':
            rows = show(flags['template'])
            for row in rows:
                print row.tostring()
            
        if flags['action'] == 'delete':
            try:
                print delete(flags['template'],flags['values'])
            except:
                print "Fail"
                
        if flags['action'] == 'update':
            try:
                print update(flags['template'],flags['values'])
            except:
                print "Fail"
    

##########################################
####file_name: ./data/templates/base/index.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320473803.8443329
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/base/index.html'
_template_uri=u'/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['profile', 'script', 'title', 'head_tags', 'toolbox', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'navigation', context._clean_inheritance_tokens(), templateuri=u'/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        navigation = _mako_get_namespace(context, 'navigation')
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n  \t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n\t<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">\n  \t<title>pyfisheyes - ')
        # SOURCE LINE 9
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n\t<meta name="keywords" content="pyfisheyes" />\n\t<meta name="description" content="" />\n\t')
        # SOURCE LINE 12
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/report.css'))))
        __M_writer(u'\n\t')
        # SOURCE LINE 13
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n\t')
        # SOURCE LINE 14
        __M_writer(escape(self.script()))
        __M_writer(u'\n\t\n</head>\n<body>\n\n<div class="wrap">\n\n\t<div class="header">\n\t    <div class="header_top">\n\t\t\t<a href="/" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\n\t\t\t')
        # SOURCE LINE 24
        __M_writer(escape(self.profile()))
        __M_writer(u'\n\t\t</div>\n\t\n\t   <!-- <div id="description">{toolkit}</div> --> \n')
        # SOURCE LINE 28
        if hasattr(c,'pagename') and c.pagename:
            # SOURCE LINE 29
            __M_writer(u'\t\t\t')
            __M_writer(escape(navigation.menu(c.pagename)))
            __M_writer(u'\n')
            # SOURCE LINE 30
        else:
            # SOURCE LINE 31
            __M_writer(u'\t\t\t')
            __M_writer(escape(navigation.menu("")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 33
        __M_writer(u'\t    \n\t</div><!-- end header -->\n\t\n\t<div class="main">\n\t    <div class="main_left">\n\t\t    \t')
        # SOURCE LINE 38
        __M_writer(escape(self.heading()))
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 39
        __M_writer(escape(next.body()))
        __M_writer(u'\n\t    </div> <!-- end #content-inner, #content -->\n\t\t<div class="main_right">\t\n\t\t\t')
        # SOURCE LINE 42
        __M_writer(escape(self.toolbox()))
        __M_writer(u'\t\n\t\t</div> <!-- end #sidebar -->\n\t</div> <!-- end main -->\n\n\t<div class="footer">\n\t    <div class="footer_pypowered"><a href="http://www.python.org/" title="The Python Language Site"><img src="/img/python-logo.gif" width="88" height="30" alt="Python" class="pypowered" /></a></div>\n\t    <p class="copyright">Website content copyright &copy; by YourSiteInc-OPSTeam. All rights reserved. tonycai321(&amp;)gmail.com</p>\n\t</div>\n\n\n</div> <!-- end wrap --> \n</body>\n</html>\n\n')
        # SOURCE LINE 64
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        # SOURCE LINE 68
        __M_writer(u'\n\n')
        # SOURCE LINE 70
        __M_writer(u'\n\n')
        # SOURCE LINE 79
        __M_writer(u'\n\n')
        # SOURCE LINE 81
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_profile(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n    <div class="welcome">\n')
        # SOURCE LINE 58
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 59
            __M_writer(u'\t  \t\t<a href="/signin" class="login">\u767b\u5f55</a>\n')
            # SOURCE LINE 60
        else:
            # SOURCE LINE 61
            __M_writer(u'\t  \t\t\u4f60\u597d\uff0c')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u' <a href="/signout">\u9000\u51fa</a> | <a href="/template">\u914d\u7f6e</a> \n')
            pass
        # SOURCE LINE 63
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 72
        __M_writer(u'\n\t<div class="slidebar news">\t\n\t\t<h3 class="sbartitle">News</h3>\t\n\t\t<ul class="sbarlist">\n\t\t\t<li><a href="#">Itme</a></li>\n\t\t</ul>\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/view/onlydata.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318557074.136194
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/view/onlydata.html'
_template_uri=u'/derived/view/onlydata.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'/component/pagination.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'pagination')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        pagination = _mako_get_namespace(context, 'pagination')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(escape(pagination.pagin(c, True)))
        __M_writer(u'\n\n<div class="viewdata">\n\t<table>\n\t\t<tr>\n')
        # SOURCE LINE 8
        if c.pagename == "realtime" :
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<th width="30">')
            __M_writer(escape(u"编号"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 10
            __M_writer(escape(u"日期"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 11
            __M_writer(escape(u"小时"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 12
            __M_writer(escape(u"分钟"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 13
            __M_writer(escape(u"键值"))
            __M_writer(u'</th>\t\t\n')
            # SOURCE LINE 14
        else:
            # SOURCE LINE 15
            __M_writer(u'\t\t\t<th>N</th>\n')
            # SOURCE LINE 16
            for y,item in enumerate(c.items):
                # SOURCE LINE 17
                __M_writer(u'\t\t\t\t<th>')
                __M_writer(escape(item))
                __M_writer(u'</th>\n')
                pass
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t</tr>\t\n')
        # SOURCE LINE 21
        for y,row in enumerate(c.rows):
            # SOURCE LINE 22
            if c.pagename == "realtime" :
                # SOURCE LINE 23
                __M_writer(u'\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 24
                __M_writer(escape(y+1))
                __M_writer(u'</td>\t\t\t\t\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 25
                __M_writer(escape(row.datei))
                __M_writer(u'</td>\t\t\t\t\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 26
                __M_writer(escape(row.houri))
                __M_writer(u'</td>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 27
                __M_writer(escape(row.minutei))
                __M_writer(u'</td>\n\t\t\t\t\t\t<td><a onclick="load_logstuff(\'/logstuffshow/index/')
                # SOURCE LINE 28
                __M_writer(escape(row.tid))
                __M_writer(u'/')
                __M_writer(escape(row.datei))
                __M_writer(u'/')
                __M_writer(escape(row.time()))
                __M_writer(u'\')">')
                __M_writer(escape(row.formatValue()))
                __M_writer(u'</a></td>\n\t\t\t\t\t</tr>\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                __M_writer(u'\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 32
                __M_writer(escape(y+1))
                __M_writer(u'</td>\t\n')
                # SOURCE LINE 33
                for x,opt in enumerate(row.tostringlist()):				
                    # SOURCE LINE 34
                    __M_writer(u'\t\t\t\t\t\t\t<td>')
                    __M_writer(escape(opt))
                    __M_writer(u'</td>\t\t\t\t\n')
                    pass
                # SOURCE LINE 36
                __M_writer(u'\t\t\t\t\t</tr>\n')
                pass
            pass
        # SOURCE LINE 39
        __M_writer(u'\t</table>\n</div>\n')
        # SOURCE LINE 41
        __M_writer(escape(pagination.pagin(c, True)))
        __M_writer(u'\n<script type="text/javascript">\n$(function(){\n\tvar src = $("#img").attr("src");\n\t$("#ysizeok").click(function(){\n\t\t    var graphs = $("#img");\n\t\t    var img1 = $("#imglink");\n\t\t    var img2 = $(".scale");\n\t\t    var img3 = $(".zoomWrapperImage");\n\t\t\tvar ysize = parseInt($("#ysize").val());\n\t\t\tif(ysize){\n\t\t\t\tvar src2 = $("#imglink").attr("href");\n\t\t\t\t\tvar index = src.lastIndexOf("?");\n\t\t\t\t\tvar index2 = src.lastIndexOf("?ys=");\n\t\t\t\t\tvar index3 = src.lastIndexOf("&ys=");\n\t\t\t\t\tvar oindex1 = src2.lastIndexOf("?");\n\t\t\t\t\tvar oindex2 = src2.lastIndexOf("?ys=");\n\t\t\t\t\tvar oindex3 = src2.lastIndexOf("&ys=");\n\t\t\t\t\tif (index == -1 ){\n\t\t\t\t\t\tvar src2 = src2+"?ys="+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",src+"?ys="+ysize);\n\t\t\t\t\t\t$(img1).attr("href",src2);\n\t\t\t\t\t\t$(img2).css("background-img","url("+src2+")");\n\t\t\t\t\t\t$(img3).attr("src",src2);\n\t\t\t\t\t}\n\t\t\t\t\telse if(index2 != -1){\n\t\t\t\t\t\tstr1 = src.substring(0,index2)+src.substr(index2,4)+ysize;\n\t\t\t\t\t\tstr11 = src2.substring(0,index21)+src2.substr(index21,4)+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",str1);\n\t\t\t\t\t}else if(index3 != -1){\n\t\t\t\t\t\tstr2 = src.substring(0,index3)+src.substr(index3,4)+ysize;\n\t\t\t\t\t\tstr22 = src2.substring(0,index31)+src2.substr(index31,4)+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",str2);\t\t\t\t\t\t\n\t\t\t\t\t}else{\n\t\t\t\t\t\t$(graphs).attr("src",src+"&ys="+ysize);\n\t\t\t\t\t}\n\t\t\t\t\t\n\t\t\t\t}\n\t\t\t\n\t\t\t\n\t\t});\n\t$("#ysizeclear").click(function(){\n\t\tvar graphs = $("#portfolio_0 a img");\n\t\tvar src = $(graphs).attr("src");\n\t\tvar index2 = src.lastIndexOf("?ys=");\n\t\tvar index3 = src.lastIndexOf("&ys=");\n\t\tvar str4;\n\t\tif(index2 != -1)\n\t\t\tstr4 = src.substring(0,index2)\n\t\telse if(index3 != -1)\n\t\t\tstr4 = src.substring(0,index3)\n\t\t$(graphs).attr("src",str4);\n\t\t\t$("#ysize").val("");\n\t\t});\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/view/view.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320386372.2915189
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/view/view.html'
_template_uri='/derived/view/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['script', 'toolbox', 'title', 'heading', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        if c.pagename == "realtime":	
            # SOURCE LINE 44
            __M_writer(u'\t<div class="container">\t\t\t\n\t\t    <ul class="tabs">\n\t\t        <li><a href="#tab1">\u56fe\u8868</a></li>\t\t        \n\t\t        <li><a href="#tab2">\u8bbe\u7f6e</a></li>\n\t\t        <li><a href="#tab3">\u884c\u52a8</a></li>\n\t\t    </ul>\t    \n\t    <div class="tab_container">\n\t        <div id="tab1" class="tab_content" style="text-align:center;">            \n\t            <p id="portfolio_0">\n')
            # SOURCE LINE 53
            if c.pweekday == '1':
                # SOURCE LINE 54
                __M_writer(u'\t\t            \t<a class="largeimg floatl" rel="gal1" href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'" id="imglink">\n\t\t            \t<img id="img" src="')
                # SOURCE LINE 55
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/0000-00-00/')
                __M_writer(escape(c.date2))
                __M_writer(u'/1.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'" />\n\t\t            \t</a>\n')
                # SOURCE LINE 57
            else:
                # SOURCE LINE 58
                __M_writer(u'\t\t            \t<a class="largeimg floatl" rel="gal1" href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png" id="imglink">\n\t\t            \t<img id="img" src="')
                # SOURCE LINE 59
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/0000-00-00/')
                __M_writer(escape(c.date2))
                __M_writer(u'/1.png" />\n\t\t            \t</a>\n')
                pass
            # SOURCE LINE 62
            __M_writer(u'\t\t                <p class="fguide">\n\t\t\t\t\t\t\t\t<a title="\u5bf9\u6bd4" href="/list/realtime?viewmdays&typeid=')
            # SOURCE LINE 63
            __M_writer(escape(c.template_id))
            __M_writer(u'&typename=')
            __M_writer(escape(c.topic))
            __M_writer(u'&odate=')
            __M_writer(escape(c.date2))
            __M_writer(u'" class="fl a1">\u5bf9\u6bd4</a>\n\t\t\t\t\t\t\t\t<a title="\u653e\u5927" href="')
            # SOURCE LINE 64
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph2/')
            __M_writer(escape(c.template_id))
            __M_writer(u'/')
            __M_writer(escape(c.opt))
            __M_writer(u'/')
            __M_writer(escape(c.date2))
            __M_writer(u'/7126x350/2.png" class="fl a2">\u653e\u5927</a>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t</p> \n\t            </p>\n\t        </div>\n\t        <div id="tab2" class="tab_content">\n\t            <ul>\n\t            \t\n\t            \t<li><i>\u65e5\u62a5 </i>\n')
            # SOURCE LINE 73
            if c.t.d_report:
                # SOURCE LINE 74
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 75
            else:
                # SOURCE LINE 76
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 78
            __M_writer(u'\t            \t</li>\n\t            \t<li><i>\u63d0\u9192 </i>\n')
            # SOURCE LINE 80
            if c.t.r_alert:
                # SOURCE LINE 81
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 82
            else:
                # SOURCE LINE 83
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 85
            __M_writer(u'\t            \t</li>\n\t            \t<li><i>\u6743\u91cd </i>')
            # SOURCE LINE 86
            __M_writer(escape(c.t.r_weight))
            __M_writer(u'</li>\n\t            \t<li><i>\u53c2\u8003\u7ebf </i>\n')
            # SOURCE LINE 88
            if c.t.u_baseface:	            		       	
                # SOURCE LINE 89
                __M_writer(u'\t            \t\t\u5f00\u542f (')
                __M_writer(escape(c.t.baseface))
                __M_writer(u')\n')
                # SOURCE LINE 90
            else:
                # SOURCE LINE 91
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 93
            __M_writer(u'\t            \t</li>\n\t            \t\n\t            \t<li><i>\u77ed\u4fe1\u901a\u77e5 </i>\n')
            # SOURCE LINE 96
            if c.t.r_weight>5 and c.t.r_alert:
                # SOURCE LINE 97
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 98
            else:
                # SOURCE LINE 99
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 101
            __M_writer(u'\t\t\t\t\t</li>\n\t            \t<li><i>\u5206\u6790\u6a21\u578b </i>')
            # SOURCE LINE 102
            __M_writer(escape(c.t.r_mode))
            __M_writer(u'\u7c7b</li>\n\t            \t<li><i>\u62a5\u8b66\u9600\u503c </i>\n')
            # SOURCE LINE 104
            if c.t.r_mode == 'a':
                # SOURCE LINE 105
                __M_writer(u'\t\t\t\t\t\t\u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[2]))
                __M_writer(u' , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[3]))
                __M_writer(u'\n')
                # SOURCE LINE 106
            elif c.t.r_mode == 'b':            	
                # SOURCE LINE 107
                __M_writer(u'\t\t\t\t\t\t\u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[1]))
                __M_writer(u' , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[0]))
                __M_writer(u'\n')
                # SOURCE LINE 108
            elif c.t.r_mode in ['c','d']:
                # SOURCE LINE 109
                __M_writer(u'\t\t\t\t\t\t\u5d29\u6f70 -')
                __M_writer(escape(c.list_alarm_threshold[4]))
                __M_writer(u'% , \u8b66\u544a -')
                __M_writer(escape(c.list_alarm_threshold[5]))
                __M_writer(u'% , \u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[6]))
                __M_writer(u'% , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[7]))
                __M_writer(u'%\n')
                # SOURCE LINE 110
            else:
                # SOURCE LINE 111
                __M_writer(u'\t\t\t\t\t   noset\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'\t            \t</li>\n\t            \t\n\t            </ul>       \n\t        </div>\n\t        <div id="tab3" class="tab_content">\t            \n\t            <p></p>\n\t        </div>\n\t    </div>\n\t</div>\n')
            # SOURCE LINE 122
        else:
            # SOURCE LINE 123
            __M_writer(u'\t<div class="graph">\n\t<p id="portfolio_0"><img src="')
            # SOURCE LINE 124
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph/')
            __M_writer(escape(c.template_id))
            __M_writer(u'/')
            __M_writer(escape(c.opt))
            __M_writer(u'/')
            __M_writer(escape(c.date))
            __M_writer(u'/')
            __M_writer(escape(c.date2))
            __M_writer(u'/1.png" /></p>\n\t</div>\n')
            pass
        # SOURCE LINE 127
        __M_writer(u'\n\n<div id="dialog" title="')
        # SOURCE LINE 129
        __M_writer(escape(c.topic))
        __M_writer(u'">\n\t<p id="dialog_content"></p>\n</div>\n\n')
        # SOURCE LINE 133
        if c.pagename == "realtime":	
            # SOURCE LINE 134
            __M_writer(u'<div class="clear">\t            \n\t<p><strong>\u5408\u8ba1</strong>\uff1a')
            # SOURCE LINE 135
            __M_writer(escape(c.sumvalue))
            __M_writer(u'\u3000\u9650\u5236\uff39\u8f74\u6700\u5927\u503c\uff1a<input type="text" id="ysize" style=\'width:80px;\' /> <input type="button" id="ysizeok" value="\u786e\u5b9a"/> <input type="button" id="ysizeclear" value="\u6e05\u9664"/>\n\t</p>\n</div>\n')
            pass
        # SOURCE LINE 139
        if c.pagename == "realtime":
            # SOURCE LINE 140
            if c.events:
                # SOURCE LINE 141
                __M_writer(u'<div ><h3 style="line-height:30px;font-weight:bold;border-bottom:1px solid orange;margin-top:5px;font-size:14px;color:#FF9933">\u4e8b\u4ef6</h3>\n')
                # SOURCE LINE 142
                for x,t in enumerate(c.events):
                    # SOURCE LINE 143
                    __M_writer(u'\t<dl style="line-height:24px;border-bottom:1px dashed orange;"><dt><a href="/events/detail/')
                    __M_writer(escape(t.id))
                    __M_writer(u'" style="color:#333;">')
                    __M_writer(escape(t.evtitle))
                    __M_writer(u'</a></dt><dd>')
                    __M_writer(escape(t.evcontent))
                    __M_writer(u'</dd><dl>\t\n')
                    pass
                # SOURCE LINE 145
                __M_writer(u'</div>\n')
                pass
            pass
        # SOURCE LINE 148
        __M_writer(u'<div id="page-area">')
        runtime._include_file(context, u'onlydata.html', _template_uri)
        __M_writer(u'</div>\n\n\n')
        # SOURCE LINE 245
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n<script>\nvar opt = "')
        # SOURCE LINE 18
        __M_writer(escape(c.opt))
        __M_writer(u'";\nvar date = "')
        # SOURCE LINE 19
        __M_writer(escape(c.date))
        __M_writer(u'";\nvar date2 = "')
        # SOURCE LINE 20
        __M_writer(escape(c.date2))
        __M_writer(u'";\nvar tid = "')
        # SOURCE LINE 21
        __M_writer(escape(c.template_id))
        __M_writer(u'";\nvar pagename = "')
        # SOURCE LINE 22
        __M_writer(escape(c.pagename))
        __M_writer(u'";\nvar imgpath = "')
        # SOURCE LINE 23
        __M_writer(escape(c.imgpath))
        __M_writer(u'";\nvar ck = "')
        # SOURCE LINE 24
        __M_writer(escape(c.ck))
        __M_writer(u'"\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 151
        __M_writer(u'\n')
        # SOURCE LINE 152
        if c.pagename == "realtime":
            # SOURCE LINE 153
            __M_writer(u'<div class="box">\t\n\t\t<h3>')
            # SOURCE LINE 154
            __M_writer(escape("Search"))
            __M_writer(u'</h3>\t\n\t\t<form action="/list/realtime?montoring" method="get">\n\t\t\t<input type="hidden" name="montoring" value=1 />\n\t\t\t<input type="text" name="s" value="')
            # SOURCE LINE 157
            __M_writer(escape(c.sw))
            __M_writer(u'" />\t\n\t\t\t<input type="submit" value="Go" />\n\t\t\n\t\t</form>\n\t</div>\n')
            pass
        # SOURCE LINE 163
        __M_writer(u'\n<div class="box">\n\n')
        # SOURCE LINE 166
        if c.pagename == "day":
            # SOURCE LINE 167
            __M_writer(u'\t<h3>\u5f00\u59cb\u65e5\u671f:</h3>\n\t<div id="datepicker"></div>\n\t<h3></h3>\n\t<h3>\u7ed3\u675f\u65e5\u671f:</h3>\n\t<div id="datepicker2"></div>\n')
            # SOURCE LINE 172
        else:	
            # SOURCE LINE 173
            __M_writer(u'\t<h3>\u9009\u62e9\u65e5\u671f <input type="checkbox" name="onlyshowyester" id="osy"  value="')
            __M_writer(escape(c.yesterday))
            __M_writer(u'" ')
            __M_writer(escape(c.set_default_day))
            __M_writer(u' /><label style="font-size:10px" for="osy">\u8bb0\u4f4f</label></h3>\n\t\n\t<div id="datepicker2"></div>\n')
            pass
        # SOURCE LINE 177
        __M_writer(u'\n</div>\n\n\n')
        # SOURCE LINE 181
        if len(c.items)>2 and c.pagename == "day":
            # SOURCE LINE 182
            __M_writer(u'<div class="box">\n\t<h3>\u9690\u85cf</h3>\n\t<ul style="float:left;">\n')
            # SOURCE LINE 185
            for x,item in enumerate(c.items):
                # SOURCE LINE 186
                if x > 0:
                    # SOURCE LINE 187
                    __M_writer(u'\t\t\t<li style="float:left;"><input type="checkbox" name="item" id="item_')
                    __M_writer(escape(x))
                    __M_writer(u'"  value="')
                    __M_writer(escape(x))
                    __M_writer(u'" /><label for="item_')
                    __M_writer(escape(x))
                    __M_writer(u'">')
                    __M_writer(escape(item))
                    __M_writer(u'</label></li>\n')
                    pass
                pass
            # SOURCE LINE 190
            __M_writer(u'\t<br style="clear:both;"></br>\n\t</ul>\n</div>\n')
            pass
        # SOURCE LINE 194
        __M_writer(u'\n')
        # SOURCE LINE 195
        if len(c.items)>2 and c.pagename == "realtime":
            # SOURCE LINE 196
            __M_writer(u'<div class="box">\n\t<h3>\u9690\u85cf</h3>\n\t<ul>\n\t\t<li><input type="checkbox" name="pweekday" id="ritem_1"  value="1" checked/><label for="ritem_1">\u4e0a\u5468\u540c\u4e00\u5929</label></li>\t\t\n\t</ul>\n</div>\n')
            pass
        # SOURCE LINE 203
        __M_writer(u'\n<div class="box">\n\n<h3>\u5de5\u5177\u7bb1</h3>\n\n<ul>\n')
        # SOURCE LINE 209
        if c.pagename == "realtime":
            # SOURCE LINE 210
            __M_writer(u'\t<li><a href="/events/new?d1=')
            __M_writer(escape(c.date2))
            __M_writer(u'&graphs=')
            __M_writer(escape(c.template_id))
            __M_writer(u'" title="Report">New Event</a></li>\n\t<li>\n')
            # SOURCE LINE 212
            if c.pweekday == '1':
                # SOURCE LINE 213
                __M_writer(u'\t\t<a href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'">\u67e5\u770b\u5927\u56fe</a>\n')
                # SOURCE LINE 214
            else:
                # SOURCE LINE 215
                __M_writer(u'\t\t<a href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png">\u67e5\u770b\u5927\u56fe</a>\n')
                pass
            # SOURCE LINE 217
            __M_writer(u'    </li>\n')
            pass
        # SOURCE LINE 219
        __M_writer(u'\t<li><a href="')
        __M_writer(escape(h.url(controller="view", action="exporttoexcel",id=c.template_id)))
        __M_writer(u'" id="ExporttoExcel">\u5bfc\u51faExcel</a></li>\n\t<li><a href="')
        # SOURCE LINE 220
        __M_writer(escape(h.url(controller="view", action="webapi",id=c.template_id)))
        __M_writer(u'">\u5199\u5165\u63a5\u53e3</a></li>\n')
        # SOURCE LINE 221
        if c.pagename == "realtime":
            # SOURCE LINE 222
            __M_writer(u'\t<li><a href="/list/realtime?montoring" title="\u6bcf\u5206\u949f\u5237\u65b0\u4e00\u6b21" >\u76d1\u63a7\u6a21\u5f0f</a></li>\n\t<li><a href="/list/realtime?fullscreen" title="\u4e0d\u5237\u65b0" >\u5168\u5c4f\u6a21\u5f0f</a></li>\n\t<li><a href="/daily_report/lookup_system" title="Report">Report</a></li>\n\t\n')
            pass
        # SOURCE LINE 227
        __M_writer(u'\t\n</ul>\n\n</div>\n\n<div class="box">\n\n<h3>\u4fe1\u606f</h3>\n\n<ul>\n')
        # SOURCE LINE 237
        if c.datasupport != "":
            # SOURCE LINE 238
            __M_writer(u'\t<li>\u6570\u636e\u652f\u6301\uff1a <a href="/contacts/list/1?qw=')
            __M_writer(escape(c.datasupport))
            __M_writer(u'">')
            __M_writer(escape(c.datasupport))
            __M_writer(u'</a></li>\n')
            pass
        # SOURCE LINE 240
        __M_writer(u'\t<li>\u8bbf\u95ee\u91cf\uff1a ')
        __M_writer(escape(c.accessed))
        __M_writer(u' \u6b21</li>\n</ul>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(escape(c.topic))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n<p class="pageguide floatl">\n')
        # SOURCE LINE 29
        if c.pre_topic:
            # SOURCE LINE 30
            __M_writer(u'<a class="pre" href="')
            __M_writer(escape(c.pre_topic.typeid))
            __M_writer(u'">&lt;&lt;&nbsp;')
            __M_writer(escape(c.pre_topic.typename))
            __M_writer(u'</a>\n')
            pass
        # SOURCE LINE 32
        if c.next_topic:
            # SOURCE LINE 33
            __M_writer(u'<a class="next" href="')
            __M_writer(escape(c.next_topic.typeid))
            __M_writer(u'">')
            __M_writer(escape(c.next_topic.typename))
            __M_writer(u'&nbsp;&gt;&gt;</a>\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</p>\n<h1 class="clear">\n')
        # SOURCE LINE 37
        __M_writer(escape(c.topic))
        __M_writer(u' #')
        __M_writer(escape(c.template_id))
        __M_writer(u'\n')
        # SOURCE LINE 38
        if request.environ.get('REMOTE_USER'):
            # SOURCE LINE 39
            __M_writer(u'\t <a href="/categories/edit/')
            __M_writer(escape(c.template_id))
            __M_writer(u'">\u7f16\u8f91</a>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-1.6.2.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-ui-1.8.8.custom.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/development-bundle/ui/i18n/jquery.ui.datepicker-zh-CN.js'))))
        __M_writer(u'  \n')
        # SOURCE LINE 7
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/development-bundle/external/jquery.cookie.js '))))
        __M_writer(u'  \n')
        # SOURCE LINE 8
        __M_writer(escape(h.stylesheet_link(h.url_for('/jquery/development-bundle/themes/pepper-grinder/jquery.ui.all.css'))))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/view.css'))))
        __M_writer(u'\n')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link(h.url_for('/lib/jqzoom/css/jquery.jqzoom.css'))))
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(escape(h.javascript_link(h.url_for('/js/view.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(escape(h.javascript_link(h.url_for('/lib/jqzoom/js/jquery.jqzoom-core.js'))))
        __M_writer(u' \n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/list/report_7days.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320386381.6502471
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/list/report_7days.html'
_template_uri='/derived/list/report_7days.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['profile']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'navigation', context._clean_inheritance_tokens(), templateuri=u'/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        navigation = _mako_get_namespace(context, 'navigation')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\r\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n<title>report</title>\r\n<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\r\n<link href="/css/report.css" media="all" rel="stylesheet" type="text/css" />\r\n<script type="text/javascript" src="/jquery/js/jquery-1.6.2.min.js"></script>\r\n<script type="text/javascript" src="/jquery/js/jquery-ui-1.8.8.custom.min.js"></script>\r\n<script src="/js/CJL.0.1.min.js"></script>\r\n<script src="/js/LazyLoad.js"></script>\r\n<script src="/js/lazyLoadImg.js"></script>\r\n<script type="text/javascript">\r\n$(function(){\r\n\t$("#dvalue").focus(function(){\r\n\t\t\tif($(this).val() == "\u8f93\u5165\u5929\u6570")\r\n\t\t\t\t$(this).val("");\r\n\t\t});\r\n\t$("#dvalue").blur(function(){\r\n\t\tif($(this).val() == ""||$(this).val() == null)\r\n\t\t\t$(this).val("\u8f93\u5165\u5929\u6570");\r\n\t});\r\n});\r\n</script>\r\n</head>\r\n<body>\r\n\t<div class="wrap">\r\n\t\t<div class="header">\r\n\t\t    <div class="header_top">\r\n\t\t\t\t<a href="/" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\r\n\t\t\t\t')
        # SOURCE LINE 32
        __M_writer(escape(self.profile()))
        __M_writer(u'\r\n\t\t\t</div>\r\n\t\t\r\n\t\t   <!-- <div id="description">{toolkit}</div> --> \r\n')
        # SOURCE LINE 36
        if hasattr(c,'pagename') and c.pagename:
            # SOURCE LINE 37
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(navigation.menu(c.pagename)))
            __M_writer(u'\r\n')
            # SOURCE LINE 38
        else:
            # SOURCE LINE 39
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(navigation.menu("")))
            __M_writer(u'\r\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\t\t    \r\n\t\t</div><!-- end header -->\r\n\t\t<p class="pageguide"><a href="/">\u9996\u9875</a>&nbsp;&gt;&gt;&nbsp;<a href="/list/realtime">\u76d1\u63a7</a>&nbsp;&gt;&gt;&nbsp;<a href="/daily_report/lookup_system">Report</a>&nbsp;&gt;&gt;&nbsp;')
        # SOURCE LINE 43
        __M_writer(escape(c.t2))
        __M_writer(u' ( ')
        __M_writer(escape(c.rdate[6]))
        __M_writer(u'--')
        __M_writer(escape(c.rdate[0]))
        __M_writer(u' ) </p>\r\n\t\t<div class="main">\r\n\t\t\t<div class="main_left" id="chartwrap">\r\n')
        # SOURCE LINE 46
        for x in c.rdate:
            # SOURCE LINE 47
            __M_writer(u'\t\t\t\t<dl class="dl1 floatl">\r\n\t\t\t\t\t<dt>')
            # SOURCE LINE 48
            __M_writer(escape(x))
            __M_writer(u'</dt>\r\n\t\t\t\t\t<dd class="dd2 floatl">\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<a class="largeimg floatl" href="/view/data/')
            # SOURCE LINE 51
            __M_writer(escape(c.t1))
            __M_writer(u'?d=')
            __M_writer(escape(x))
            __M_writer(u'"><img _lazysrc="')
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph/')
            __M_writer(escape(c.t1))
            __M_writer(u'/0/0000-00-00/')
            __M_writer(escape(x))
            __M_writer(u'/1.png" alt="')
            __M_writer(escape(c.t2))
            __M_writer(u'" /></a>\r\n\t\t\t\t\t\t\r\n\t\t\t\t\t\t<p class="fguide">\r\n\t\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t\t\t<a class="fl a2" href="')
            # SOURCE LINE 55
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph2/')
            __M_writer(escape(c.t1))
            __M_writer(u'/0/')
            __M_writer(escape(x))
            __M_writer(u'/7126x650/2.png" title="\u653e\u5927">\u653e\u5927</a>\r\n\t\t\t\t\t\t\t\t<a class="fl a3" href="/view/data/')
            # SOURCE LINE 56
            __M_writer(escape(c.t1))
            __M_writer(u'?d=')
            __M_writer(escape(x))
            __M_writer(u'" title="\u5355\u9875">\u5355\u9875</a>\r\n\t\t\t\t\t\t\t\r\n\t\t\t\t\t\t</p>\r\n\t\t\t\t\t</dd>\r\n\t\t\t\t</dl>\r\n')
            pass
        # SOURCE LINE 62
        __M_writer(u'\t\t\t</div>\r\n\t\t\t<div class="main_right">\r\n\t\t\t\t<div class="slidebar">\r\n\t\t\t\t\t<h3 class="sbartitle">\u5de5\u5177\u7bb1</h3>\r\n\t\t\t\t\t<form action="/list/realtime" method="get" >\r\n\t\t\t\t\t\t<input id="dvalue" type="text" value="\u8f93\u5165\u5929\u6570" name="dys"/>&nbsp;<input type="submit" value="GO" />\r\n\t\t\t\t\t\t<input type="hidden" name="typeid" value="')
        # SOURCE LINE 68
        __M_writer(escape(c.t1))
        __M_writer(u'" />\r\n\t\t\t\t\t\t<input type="hidden" name="typename" value="')
        # SOURCE LINE 69
        __M_writer(escape(c.t2))
        __M_writer(u'">\r\n\t\t\t\t\t\t<input type="hidden" name="odate" value="')
        # SOURCE LINE 70
        __M_writer(escape(c.odate))
        __M_writer(u'">\r\n\t\t\t\t\t\t<input type="hidden" name="viewmdays" />\r\n\t\t\t\t\t</form>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n<script>\r\nfunction lazy(){\r\nvar lazy = new ImagesLazyLoad({\r\n\t\tcontainer: window, mode: "vertical",\r\n\t\tholder: "/img/o_dot.gif"\r\n\t});\r\n}\r\nlazy();\r\n</script>\r\n</body>\r\n</html>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_profile(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 89
        __M_writer(u'\r\n    <div class="welcome">\r\n')
        # SOURCE LINE 91
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 92
            __M_writer(u'\t  \t\t<a href="/signin" class="login">\u767b\u5f55</a>\r\n')
            # SOURCE LINE 93
        else:
            # SOURCE LINE 94
            __M_writer(u'\t  \t\t\u4f60\u597d\uff0c')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u' <a href="/signout">\u9000\u51fa</a> | <a href="/template">\u914d\u7f6e</a> \r\n')
            pass
        # SOURCE LINE 96
        __M_writer(u'    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/list/list.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320378303.429302
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/list/list.html'
_template_uri='/derived/list/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'/component/pagination.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<table class="atable" cellspacing="0" border="0" cellpadding="0">\n')
        # SOURCE LINE 8
        for x,category in enumerate(c.rows):
            # SOURCE LINE 9
            __M_writer(u'\t<tr>\n\t\t<td class="first">')
            # SOURCE LINE 10
            __M_writer(escape(x+1))
            __M_writer(u'</td>\n\t\t<td> <a href="')
            # SOURCE LINE 11
            __M_writer(escape(h.url_for('/view/data/'+ str(category.typeid))))
            __M_writer(u'">')
            __M_writer(escape(category.typename))
            __M_writer(u'</a></a></td>\n\t\t<td class="last"><a href="/view/data/')
            # SOURCE LINE 12
            __M_writer(escape(category.typeid))
            __M_writer(u'">')
            __M_writer(escape("view"))
            __M_writer(u'</a></td>\n\t</tr>\n')
            pass
        # SOURCE LINE 15
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 17
        __M_writer(escape(pagination.pagin(c, False)))
        __M_writer(u'\n\n')
        # SOURCE LINE 66
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 20
        if c.pagename == "realtime":
            # SOURCE LINE 21
            __M_writer(u'   <div class="slidebar">\t\n\t\t<h3 class="sbartitle">')
            # SOURCE LINE 22
            __M_writer(escape("Search"))
            __M_writer(u'</h3>\t\n\t\t<form action="/list/realtime?montoring" method="get">\n\t\t<input type="hidden" name="fullscreen" value=1 />\t\t\n\t\t\t<input type="text" name="s" value="" />\t\t\n\t\t\t<input type="submit" value="Go" />\n\t\n\t\t</form>\n\t</div>\n\t\n\t<div class="slidebar">\t\n\t\t\t<h3 class="sbartitle">')
            # SOURCE LINE 32
            __M_writer(escape("usefully"))
            __M_writer(u'</h3>\n\t\t\t<p>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=mysql">mysql</a> \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=vpn">vpn</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=ct">ct</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cnc">cnc</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cdn">cdn</a> \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=solr">solr</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=\u5b9e\u65f6\u8bf7\u6c42">\u5b9e\u65f6\u8bf7\u6c42</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=\u6162\u8bf7\u6c42">\u5b9e\u65f6\u6162\u8bf7\u6c42</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=connections">connections</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cache">cache</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=release">release</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite">yoursite</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite1">yoursite1</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite2">yoursite2</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=500">500</a>  \n\t\t\t</p>\n\t</div>\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\n\t<div class="slidebar">\n\t\t<h3 class="sbartitle">\u5de5\u5177\u7bb1</h3>\n\t\t<ul class="sbarlist">\n')
        # SOURCE LINE 56
        if c.pagename == "realtime":
            # SOURCE LINE 57
            __M_writer(u'\t\t\t<li><a href="/list/realtime?montoring" title="\u6bcf\u5206\u949f\u5237\u65b0\u4e00\u6b21" >\u76d1\u63a7\u6a21\u5f0f</a></li>\n\t\t\t<li><a href="/list/realtime?fullscreen" title="\u4e0d\u5237\u65b0" >\u5168\u5c4f\u6a21\u5f0f</a></li>\n\t\t\t<li style="display:none;"><a href="/list/realtime?report" title="Report">Report</a></li>\n\t\t\t<li><a href="/daily_report/lookup_system" title="Report">Report</a></li>\n\t\t\t<li><a href="/html/vip_justin.html" title="">vip_Justin</a></li>\n')
            pass
        # SOURCE LINE 63
        __M_writer(u'\t\t</ul>\n\t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.pagename))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(escape(c.pagename))
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/list/realtime.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320378310.6910701
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/list/realtime.html'
_template_uri='/derived/list/realtime.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'search', context._clean_inheritance_tokens(), templateuri=u'/component/search.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'search')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        search = _mako_get_namespace(context, 'search')
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"> \n \n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en"> \n<head>\n<style type="text/css">\n<!-- @import url(/gp.fileupload.static/fileupload.css); -->\n</style> \n  \t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/> \n\t<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon" /> \n\t<link href="/css/realtime.css" rel="stylesheet" type="text/css" />\n  \t<title>pyfisheyes - Realtime</title> \n\t<meta name="keywords" content="pyfisheyes" /> \n\t<meta name="description" content="" /> \n')
        # SOURCE LINE 15
        if hasattr(c,"refresh") and c.refresh and c.disrf=='false':
            # SOURCE LINE 16
            __M_writer(u'\t\t<meta http-equiv="refresh" content="10" />\n')
            pass
        # SOURCE LINE 18
        __M_writer(u'<style type="text/css">\n*html,*html body{background-image:url(about:blank);background-attachment:fixed;}\n\n*html .clickbar{position:absolute;right:auto;left:expression(eval(document.documentElement.scrollLeft+document.documentElement.clientWidth-this.offsetWidth)-(parseInt(this.currentStyle.marginLeft,10)||0)-(parseInt(this.currentStyle.marginRight,10)||0));}\n.alert{\nbackground-color:yellow;\n}\n</style>\n<script src="/jquery/js/jquery-1.4.4.min.js" type="text/javascript"></script>\n<script src="/js/CJL.0.1.min.js"></script>\n<script src="/js/LazyLoad.js"></script>\n<script src="/js/lazyLoadImg.js"></script>\n<script src="/js/jquery.cookie.js"></script>\n</head> \n<body>\n<div class="clickbar" id="oClick">\u70b9\u51fb\u663e\u793a</div>\n<div class="wrap">\n\t\n\t<div id="rtimeHeader" style="padding-top:5px;display:none;">\n\t\t<div class="top">\n\t\t\t<p class="navbar">\n\t\t\t\t<a href="/">\u9996\u9875</a>\n\t\t\t\t<a href="/list/day">\u6bcf\u5929</a>\n\t\t\t\t<a href="/list/hour">\u5c0f\u65f6</a>\n\t\t\t\t<a href="/list/host">\u5206\u7ec4</a>\n\t\t\t\t<a href="/list/realtime">\u76d1\u63a7</a>\n\t\t\t\t<a href="/events">\u4e8b\u4ef6</a>\n\t\t\t\t<a href="/alert">\u62a5\u8b66</a>\n\t\t\t\t<a href="/contacts">\u8054\u7cfb\u4eba</a>\n\t\t\t\t<a href="#" onclick="javascript:void(0);">\u8fc7\u6ee4</a>\t\n\t\t\t</p>\n\t\t\t<span class="updatetime">\u66f4\u65b0: ')
        # SOURCE LINE 49
        __M_writer(escape(c.currentdatetime))
        __M_writer(u'</span><span class="updatetime">\u5171\u8ba1: ')
        __M_writer(escape(c.count))
        __M_writer(u'\u6761</span>\n\t\t\t<!-- \u5934\u90e8\u641c\u7d22\u6846 -->\n\t\t\t')
        # SOURCE LINE 51
        __M_writer(escape(search.bar("/list/realtime", c.view_mode)))
        __M_writer(u'\n\t\t</div>\n\t\t<div class="checkwrap">\n')
        # SOURCE LINE 54
        for typecode_k, typecode_v in c.r_typecode.iteritems():
            # SOURCE LINE 55
            if typecode_v in c.filter_list:
                # SOURCE LINE 56
                __M_writer(u'\t\t\t\t\t<input type="checkbox" name="filter" id="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'"  value="')
                __M_writer(escape(typecode_v))
                __M_writer(u'" checked="checked"/><label for="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'">')
                __M_writer(escape(typecode_k))
                __M_writer(u'</label>\n')
                # SOURCE LINE 57
            else:
                # SOURCE LINE 58
                __M_writer(u'\t\t\t\t\t<input type="checkbox" name="filter" id="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'"  value="')
                __M_writer(escape(typecode_v))
                __M_writer(u'"  /><label for="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'">')
                __M_writer(escape(typecode_k))
                __M_writer(u'</label>\n')
                pass
            pass
        # SOURCE LINE 61
        __M_writer(u'\t\t</div>\n\t</div>\n\t<div class="chartwrap">\n\t\t<ul class="chartlist" id="chartlist">\n')
        # SOURCE LINE 65
        for x,t in enumerate(c.rows):
            # SOURCE LINE 66
            if t.alertlevel == 2 and t.r_weight > 5:
                # SOURCE LINE 67
                __M_writer(u'\t\t\t<li>\n\t\t\t\t<p class="chatname alert">\n\t\t\t\t\t\t<span class="sn">#')
                # SOURCE LINE 69
                __M_writer(escape(t.typeid))
                __M_writer(u'</span>\n')
                # SOURCE LINE 70
                if c.sw:
                    # SOURCE LINE 71
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.search_highlight(c.sw)))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 72
                else:
                    # SOURCE LINE 73
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.typename))
                    __M_writer(u'</span>\n')
                    pass
                # SOURCE LINE 75
                __M_writer(u'\t\t\t\t</p>\n\t\t\t\t<div class="imgbox">\n\t\t\t\t\t<a href="/view/data/')
                # SOURCE LINE 77
                __M_writer(escape(t.typeid))
                __M_writer(u'?s=')
                __M_writer(escape(c.sw))
                __M_writer(u'">\n\t\t\t\t\t\n\t\t\t\t\t<!-- <img alt="')
                # SOURCE LINE 79
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(h.url_for('/view/realtimegraph/'+str(t.typeid),host='')))
                __M_writer(u'/1.png"/>  -->\n\t\t\t\t\t\n\t\t\t\t\t<img class="alert" alt="')
                # SOURCE LINE 81
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/realtimegraph/')
                __M_writer(escape(t.typeid))
                __M_writer(u'/1.png"/>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t</li>\n')
                pass
            pass
        # SOURCE LINE 87
        for x,t in enumerate(c.rows):	
            # SOURCE LINE 88
            if t.alertlevel !=2 or t.r_weight <= 5:
                # SOURCE LINE 89
                __M_writer(u'\t\t\t<li>\n\t\t\t\t<p class="chatname">\n\t\t\t\t\t\t<span class="sn">#')
                # SOURCE LINE 91
                __M_writer(escape(t.typeid))
                __M_writer(u'</span>\n')
                # SOURCE LINE 92
                if c.sw:
                    # SOURCE LINE 93
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.search_highlight(c.sw)))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 94
                else:
                    # SOURCE LINE 95
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.typename))
                    __M_writer(u'</span>\n')
                    pass
                # SOURCE LINE 97
                __M_writer(u'\t\t\t\t</p>\n\t\t\t\t<div class="imgbox">\n\t\t\t\t\t<a href="/view/data/')
                # SOURCE LINE 99
                __M_writer(escape(t.typeid))
                __M_writer(u'?s=')
                __M_writer(escape(c.sw))
                __M_writer(u'">\n\t\t\t\t\t\n\t\t\t\t\t<!-- <img alt="')
                # SOURCE LINE 101
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(h.url_for('/view/realtimegraph/'+str(t.typeid),host='')))
                __M_writer(u'/1.png"/>  -->\n\t\t\t\t\t\n\t\t\t\t\t<img alt="')
                # SOURCE LINE 103
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/realtimegraph/')
                __M_writer(escape(t.typeid))
                __M_writer(u'/1.png"/>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t</li>\n')
                pass
            pass
        # SOURCE LINE 109
        __M_writer(u'\t\t</ul>\n\t</div>\n</div>\n<script>\nfunction lazy(){\nvar lazy = new ImagesLazyLoad({\n\t\tcontainer: window, mode: "vertical",\n\t\tholder: "/img/o_dot.gif"\n\t});\n}\nlazy();\n</script>\n<script type="text/javascript"> \n\tvar filter = "";\t\n\t$("document").ready(function(){\n\t\tslide();\n\t\tvar disrf = $.cookie("disrf");\n\t\tif(disrf == \'true\'){\n\t\t\tdocument.getElementById("disreflash").checked=true;\n\t\t}else{\n\t\t\tdocument.getElementById("disreflash").checked=false;\n\t\t\tdocument.getElementById("disreflash").defaultChecked=false;\n\t\t}\n\t\t/*hidden line*/\n\t\t  $("[name=\'filter\']").bind("click",function(){\n\t\t\t  filter="";\n\t\t\t\t  $("[name=\'filter\']").each(function(){\n\t\t\t\t\t\tif ($(this).attr("checked")==true){\n\t\t\t\t\t\t\t\tif (filter==""){\n\t\t\t\t\t\t\t\t\tfilter=$(this).val();\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\telse\n\t\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t\tfilter+=","+$(this).val();\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t    })\n\t\t\t\t  if (filter == ""){filter=0}\n\t\t\t\t  \n\t\t\t\t  filterSelect(filter);\n\t\t\t  });\n\t\t\t/*$("#oClick").toggle(function(){\n\t\t\t\t$("#rtimeHeader").slideDown();\n\t\t\t\t$(this).html("\u70b9\u51fb\u9690\u85cf");\n\t\t\t},function(){\n\t\t\t\t$("#rtimeHeader").slideUp();\n\t\t\t\t$(this).html("\u70b9\u51fb\u663e\u793a");\n\t\t\t});*/\n\t\t\t\n\t\t\t\n\t\t\t$("#oClick").click(function(){\n\t\t\t\t\tif($("#rtimeHeader").css("display") == "none")\n\t\t\t\t\t{\n\t\t\t\t\t\t$("#rtimeHeader").slideDown();\n\t\t\t\t\t    $(this).html("\u70b9\u51fb\u9690\u85cf");\n\t\t\t\t\t    $.cookie(\'sk\',\'true\');\n\t\t\t\t\t}\n\t\t\t\t\telse\n\t\t\t\t\t{\n\t\t\t\t\t\t$("#rtimeHeader").slideUp();\n\t\t\t\t\t    $(this).html("\u70b9\u51fb\u663e\u793a");\n\t\t\t\t\t    $.cookie(\'sk\',\'false\');\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t$("#disreflash").click(function(){\n\t\t\t\t\tif (document.getElementById("disreflash").checked==true){\n\t\t\t\t\t\t$.cookie("disrf",true);\n\t\t\t\t\t\t}else{\n\t\t\t\t\t\t\t$.cookie("disrf",false);\n\t\t\t\t\t}\n\t\t\t\t\tlocation.reload();\n\t\t\t\t\t\n\t\t\t\t});\n\t});\n\tfunction filterSelect(fi) {\n\t\t  \t\n\t\t  \t\twindow.location = "?montoring=1&filter="+ fi; \n\t\t  \t\n\t}\n\tfunction slide(){\n\t\t\n\t\tif($.cookie(\'sk\') == \'true\'){\n\t\t\t\t$("#rtimeHeader").show();\n\t\t\t\t$("#oClick").html("\u70b9\u51fb\u9690\u85cf");\n\t\t}else{\n\t\t\t\t$("#rtimeHeader").hide();\n\t\t\t\t$("#oClick").html("\u70b9\u51fb\u663e\u793a");\n\t\t}\n\t}\n\t\n</script> \n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/list/daily_report.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1311746666.0695801
_template_filename='/home/hyhe/workspace/pyfisheyes/pyfisheyes/templates/derived/list/daily_report.html'
_template_uri='/derived/list/daily_report.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n<title>report</title>\r\n<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\r\n<link href="/css/report.css" media="all" rel="stylesheet" type="text/css" />\r\n<script type="text/javascript" src="/jquery/js/jquery-1.4.4.min.js"></script>\r\n<script type="text/javascript" src="/jquery/js/jquery-ui-1.8.8.custom.min.js"></script>\r\n<script src="/js/CJL.0.1.min.js"></script>\r\n<script src="/js/LazyLoad.js"></script>\r\n<script src="/js/lazyLoadImg.js"></script>\r\n<script type="text/javascript">\r\n$(function(){\r\n\tvar oDate\r\n\tvar defaultdate = $("#odate").text()\r\n\t$( "#datepicker" ).datepicker({\r\n\t\taltFormat: \'yy-mm-dd\',\r\n\t\taltField: \'#actualDate\',\r\n\t\tonSelect: function(dateText, inst) { \r\n\t\t\t\toDate = $("#actualDate").val();\r\n\t\t\t\tlocation.href = "/daily_report/lookup_system?odate="+oDate;\r\n\t\t},\r\n\t\tdateFormat: \'yy-mm-dd\',\r\n\t\tdefaultDate:defaultdate\r\n\t\t\r\n\t});\r\n\t$("#clearcache").click(function(){\r\n\t\tlocation.href = "/daily_report/lookup_system?odate=')
        # SOURCE LINE 29
        __M_writer(escape(c.odate))
        __M_writer(u'&cr=cr";\r\n\t});\r\n\t$("#disabledlazy").click(function(){\r\n\t\tlocation.href = "/daily_report/lookup_system?odate=')
        # SOURCE LINE 32
        __M_writer(escape(c.odate))
        __M_writer(u'&unlazy=unlazy";\r\n\t});\r\n\t\r\n});\r\n</script>\r\n</head>\r\n<body>\r\n\t<div class="wrap">\r\n\t\t<div class="header">\r\n\t\t\t<a href="#" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\r\n\t\t\t<ul class="nav">\r\n\t\t\t\t<li><a href="/" class="active">\u9996\u9875</a></li>\r\n\t\t\t\t<li><a href="/list/day">\u6bcf\u5929</a></li>\r\n\t\t\t\t<li><a href="/list/hour">\u5c0f\u65f6</a></li>\r\n\t\t\t\t<li><a href="/list/host">\u5206\u7ec4</a></li>\r\n\t\t\t\t<li><a href="/list/realtime">\u76d1\u63a7</a></li>\r\n\t\t\t\t<li><a href="/speed">\u901f\u5ea6</a></li>\r\n\t\t\t\t<li><a href="/events">\u4e8b\u4ef6</a></li>\r\n\t\t\t\t<li><a href="/alert">\u62a5\u8b66</a></li>\r\n\t\t\t\t<li><a href="/contacts">\u8054\u7cfb\u4eba</a></li>\r\n\t\t\t</ul>\r\n\t\t</div>\r\n\t\t<p class="pageguide"><a href="/">\u9996\u9875</a>&nbsp;&gt;&gt;&nbsp;<a href="/list/realtime">\u76d1\u63a7</a>&nbsp;&gt;&gt;&nbsp;<span>Report</span>&nbsp;&gt;&gt;&nbsp;<span id="odate">')
        # SOURCE LINE 54
        __M_writer(escape(c.odate))
        __M_writer(u'</span></p>\r\n\t\t<div class="main">\r\n\t\t\t<div class="main_left" id="chartwrap">\r\n')
        # SOURCE LINE 57
        if c.simp == 0:
            # SOURCE LINE 58
            for x,t in enumerate(c.items):
                # SOURCE LINE 59
                __M_writer(u'\t\t\t\t\r\n\t\t\t\t<dl class="dl1">\r\n\t\t\t\t\t<dt>')
                # SOURCE LINE 61
                __M_writer(escape(x+1))
                __M_writer(u') ')
                __M_writer(escape(t[1]))
                __M_writer(u' #')
                __M_writer(escape(t[2]))
                __M_writer(u'</dt>\r\n\t\t\t\t\t<dd>')
                # SOURCE LINE 62
                __M_writer(escape(t[3]))
                __M_writer(u' <strong>')
                __M_writer(escape(t[7]))
                __M_writer(u'%</strong>&nbsp;&nbsp;<span>\u603b\u8ba1\uff1a</span><strong>')
                __M_writer(escape(t[8]))
                __M_writer(u'</strong></dd>\r\n\t\t\t\t\t<dd>\u65f6\u95f4\u8303\u56f4\uff1a')
                # SOURCE LINE 63
                __M_writer(escape(t[4]))
                __M_writer(u' - ')
                __M_writer(escape(t[5]))
                __M_writer(u'</dd>\r\n\t\t\t\t\t<dd class="dd2">\r\n\t\t\t\t\t\t<div style="display:inline-block;width:660px;background-color:#fff;text-align:center;">\r\n\t\t\t\t\t\t<a href="/list/realtime?viewmdays&typeid=')
                # SOURCE LINE 66
                __M_writer(escape(t[2]))
                __M_writer(u'&typename=')
                __M_writer(escape(t[1]))
                __M_writer(u'&odate=')
                __M_writer(escape(c.odate))
                __M_writer(u'">\r\n')
                # SOURCE LINE 67
                if c.disabledlazy:
                    # SOURCE LINE 68
                    __M_writer(u'\t\t\t\t\t\t\r\n\t\t\t\t\t\t<img class="lazyimage" src="')
                    # SOURCE LINE 69
                    __M_writer(escape(c.imgpath))
                    __M_writer(u'/view/graph/')
                    __M_writer(escape(t[2]))
                    __M_writer(u'/0/')
                    __M_writer(escape(t[4][0:10]))
                    __M_writer(u'/')
                    __M_writer(escape(t[5][0:10]))
                    __M_writer(u'/1.png" alt="{t[1]}" />\r\n\t\t\t\t\t\t\r\n')
                    # SOURCE LINE 71
                else:
                    # SOURCE LINE 72
                    __M_writer(u'\t\r\n\t\t\t\t\t\t<img class="lazyimage" _lazysrc="')
                    # SOURCE LINE 73
                    __M_writer(escape(c.imgpath))
                    __M_writer(u'/view/graph/')
                    __M_writer(escape(t[2]))
                    __M_writer(u'/0/')
                    __M_writer(escape(t[4][0:10]))
                    __M_writer(u'/')
                    __M_writer(escape(t[5][0:10]))
                    __M_writer(u'/1.png" alt="{t[1]}" />\r\n')
                    pass
                # SOURCE LINE 75
                __M_writer(u'\t\t\t\t\t\t</a>\r\n\t\t\t\t\t\t</div>\r\n\t\t\t\t\t</dd>\r\n\t\t\t\t</dl>\r\n\t\t\t\t\r\n')
                pass
            pass
        # SOURCE LINE 82
        __M_writer(u'\t\t\t\r\n\t\t\t\r\n')
        # SOURCE LINE 84
        if c.simp == 1 :
            # SOURCE LINE 85
            for x,t in enumerate(c.rows):
                # SOURCE LINE 86
                __M_writer(u'\t\t\t\t<dl class="dl1">\r\n\t\t\t\t\t<dt>')
                # SOURCE LINE 87
                __M_writer(escape(x+1))
                __M_writer(u') ')
                __M_writer(escape(t.typename))
                __M_writer(u' #')
                __M_writer(escape(t.typeid))
                __M_writer(u'</dt>\r\n\t\t\t\t\t<dd class="dd2">\r\n\t\t\t\t\t<a href="/list/realtime?viewmdays&typeid=')
                # SOURCE LINE 89
                __M_writer(escape(t.typeid))
                __M_writer(u'&typename=')
                __M_writer(escape(t.typename))
                __M_writer(u'&odate=')
                __M_writer(escape(c.odate))
                __M_writer(u'">\r\n')
                # SOURCE LINE 90
                if c.disabledlazy:
                    # SOURCE LINE 91
                    __M_writer(u'\t\t\t\t\t<img class="lazyimage" src="')
                    __M_writer(escape(c.imgpath))
                    __M_writer(u'/view/graph/')
                    __M_writer(escape(t.typeid))
                    __M_writer(u'/0/2011-04-28/')
                    __M_writer(escape(c.odate))
                    __M_writer(u'/1.png" alt="')
                    __M_writer(escape(t.typename))
                    __M_writer(u'" />\r\n')
                    # SOURCE LINE 92
                else:
                    # SOURCE LINE 93
                    __M_writer(u'\t\t\t\t\t<img class="lazyimage" _lazysrc="')
                    __M_writer(escape(c.imgpath))
                    __M_writer(u'/view/graph/')
                    __M_writer(escape(t.typeid))
                    __M_writer(u'/0/2011-04-28/')
                    __M_writer(escape(c.odate))
                    __M_writer(u'/1.png" alt="')
                    __M_writer(escape(t.typename))
                    __M_writer(u'" />\r\n')
                    pass
                # SOURCE LINE 95
                __M_writer(u'\t\t\t\t\t</a>\r\n\t\t\t\t\t</dd>\t\r\n\t\t\t\t</dl>\r\n')
                pass
            pass
        # SOURCE LINE 100
        __M_writer(u'\t\t\t</div>\r\n\t\t\t\r\n\t\t\t<div class="main_right">\r\n\t\t\t\t<div class="slidebar datepicker">\r\n\t\t\t\t\t<div id="datepicker"></div>\r\n\t\t\t\t\t<input type="hidden" id="actualDate" />\r\n\t\t\t\t</div>\r\n\t\t\t\t<div style="display:none;" id="clearcache" class="clearcache">\u6e05\u9664\u7f13\u5b58</div>\r\n\t\t\t\t<div id="disabledlazy" class="disabledlazy">\u7981\u7528\u5ef6\u8f7d\u56fe\u7247</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n\r\n')
        # SOURCE LINE 113
        if not c.disabledlazy:
            # SOURCE LINE 114
            __M_writer(u'<script type="text/javascript">\r\nfunction lazy(){\r\nvar lazy = new ImagesLazyLoad({\r\n\t\tcontainer: window, mode: "vertical",\r\n\t\tholder: "/img/o_dot.gif"\r\n\t});\r\n}\r\nlazy();\r\n</script>\r\n')
            pass
        # SOURCE LINE 124
        __M_writer(u'</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/list/report.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1311143560.21628
_template_filename='/home/hyhe/workspace/pyfisheyes/pyfisheyes/templates/derived/list/report.html'
_template_uri='/derived/list/report.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\r\n<title>report</title>\r\n<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\r\n<link href="/css/report.css" media="all" rel="stylesheet" type="text/css" />\r\n<script type="text/javascript" src="/jquery/js/jquery-1.4.4.min.js"></script>\r\n<script type="text/javascript" src="/jquery/js/jquery-ui-1.8.8.custom.min.js"></script>\r\n<script src="/js/CJL.0.1.min.js"></script>\r\n<script src="/js/LazyLoad.js"></script>\r\n<script src="/js/lazyLoadImg.js"></script>\r\n<script type="text/javascript">\r\n$(function(){\r\n\t$( "#datepicker" ).datepicker({\r\n\taltFormat: \'yy-mm-dd\',\r\n\taltField: \'#actualDate\',\r\n\tonSelect: function(dateText, inst) { \r\n\tvar oDate = $("#actualDate").val();\r\n\t\t\tlocation.href = "/daily_report/lookup_system?odate="+oDate;\r\n\t\t}\r\n\t});\r\n});\r\n</script>\r\n</head>\r\n<body>\r\n\t<div class="wrap">\r\n\t\t<div class="header">\r\n\t\t\t<a href="#" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\r\n\t\t\t<ul class="nav">\r\n\t\t\t\t<li><a href="/" class="active">\u9996\u9875</a></li>\r\n\t\t\t\t<li><a href="/list/day">\u6bcf\u5929</a></li>\r\n\t\t\t\t<li><a href="/list/hour">\u5c0f\u65f6</a></li>\r\n\t\t\t\t<li><a href="/list/host">\u5206\u7ec4</a></li>\r\n\t\t\t\t<li><a href="/list/realtime">\u76d1\u63a7</a></li>\r\n\t\t\t\t<li><a href="/speed">\u901f\u5ea6</a></li>\r\n\t\t\t\t<li><a href="/events">\u4e8b\u4ef6</a></li>\r\n\t\t\t\t<li><a href="/alert">\u62a5\u8b66</a></li>\r\n\t\t\t\t<li><a href="/contacts">\u8054\u7cfb\u4eba</a></li>\r\n\t\t\t</ul>\r\n\t\t</div>\r\n\t\t<p class="pageguide"><a href="/">\u9996\u9875</a>&nbsp;&gt;&gt;&nbsp;<a href="/list/realtime">\u76d1\u63a7</a>&nbsp;&gt;&gt;&nbsp;<span>Report</span>&nbsp;&gt;&gt;&nbsp;')
        # SOURCE LINE 42
        __M_writer(escape(c.odate))
        __M_writer(u'</p>\r\n\t\t<div class="main">\r\n\t\t\t<div class="main_left" id="chartwrap">\r\n')
        # SOURCE LINE 45
        for x,t in enumerate(c.rows):
            # SOURCE LINE 46
            __M_writer(u'\t\t\t\t<dl class="dl1">\r\n\t\t\t\t\t<dt>')
            # SOURCE LINE 47
            __M_writer(escape(x+1))
            __M_writer(u') ')
            __M_writer(escape(t.typename))
            __M_writer(u' #')
            __M_writer(escape(t.typeid))
            __M_writer(u'</dt>\r\n\t\t\t\t\t<dd style="display:none;">\u540c\u6bd4\u4e0a\u5468\u540c\u4e00\u5929\u4e0a\u6da8:169%</dd>\r\n\t\t\t\t\t<dd class="dd2"><a href="/list/realtime?viewmdays&typeid=')
            # SOURCE LINE 49
            __M_writer(escape(t.typeid))
            __M_writer(u'&typename=')
            __M_writer(escape(t.typename))
            __M_writer(u'&odate=')
            __M_writer(escape(c.odate))
            __M_writer(u'" style="display:inline-block;width:660px;background-color:#fff;text-align:center;"><img class="lazyimage" _lazysrc="/view/graph/')
            __M_writer(escape(t.typeid))
            __M_writer(u'/0/2011-04-28/')
            __M_writer(escape(c.odate))
            __M_writer(u'/1.png" alt="')
            __M_writer(escape(t.typename))
            __M_writer(u'" /></a></dd>\r\n\t\t\t\t</dl>\r\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\t\t\t</div>\r\n\t\t\t\r\n\t\t\t<div class="main_right">\r\n\t\t\t\t<div class="slidebar datepicker">\r\n\t\t\t\t\t<div id="datepicker"></div>\r\n\t\t\t\t\t<input type="hidden" id="actualDate" />\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n<script>\r\nfunction lazy(){\r\nvar lazy = new ImagesLazyLoad({\r\n\t\tcontainer: window, mode: "vertical",\r\n\t\tholder: "/img/o_dot.gif"\r\n\t});\r\n}\r\nlazy();\r\n</script>\r\n</body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/events/detail.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318562283.686466
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/events/detail.html'
_template_uri='/derived/events/detail.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'script', 'heading', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        str = context.get('str', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n\n\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n<table class="detail_event_t" cellspacing=\'0\'>\n<tr><th>\u4e3b\u9898</th><td>')
        # SOURCE LINE 54
        __M_writer(escape(c.event.evtitle))
        __M_writer(u' @')
        __M_writer(escape(str(c.event.evdate)[0:10]))
        __M_writer(u' #')
        __M_writer(escape(c.event.id))
        __M_writer(u'</td></tr>\n<tr><th>\u6807\u7b7e</th><td>')
        # SOURCE LINE 55
        __M_writer(escape(c.event.evtags))
        __M_writer(u'</td></tr>\n<tr><th>\u53d1\u751f\u65f6\u95f4</th><td>')
        # SOURCE LINE 56
        __M_writer(escape(str(c.event.evdate)[0:16]))
        __M_writer(u'</td></tr>\n<tr><th>\u53d1\u73b0\u65f6\u95f4</th><td>')
        # SOURCE LINE 57
        __M_writer(escape(str(c.event.dt2)[0:16]))
        __M_writer(u'</td></tr>\n<tr><th>\u627e\u5230\u65b9\u5411</th><td>')
        # SOURCE LINE 58
        __M_writer(escape(str(c.event.dt3)[0:16]))
        __M_writer(u'</td></tr>\n<!-- <tr><th>\u4e8b\u4ef6\u89e3\u51b3\u65f6\u95f4</th><td>')
        # SOURCE LINE 59
        __M_writer(escape(str(c.event.dt4)[0:16]))
        __M_writer(u'</td></tr> -->\n<tr><th>\u6700\u540e\u4fee\u6539\u65f6\u95f4</th><td>')
        # SOURCE LINE 60
        __M_writer(escape(c.event.evlastedit))
        __M_writer(u'</td></tr>\n<tr><th>\u5185\u5bb9</th><td>')
        # SOURCE LINE 61
        __M_writer(escape(c.event.getEvContent()))
        __M_writer(u'</td></tr>\n<tr><th>\u4e8b\u4ef6\u56fe\u7247</th><td>\n')
        # SOURCE LINE 63
        for x,g in enumerate(c.graphs):
            # SOURCE LINE 64
            if g.imgid:
                # SOURCE LINE 65
                __M_writer(u'<a href="/view/data/')
                __M_writer(escape(g.imgid))
                __M_writer(u'?d2=')
                __M_writer(escape(str(c.event.evdate)[0:10]))
                __M_writer(u'">')
                __M_writer(escape(g.imgid))
                __M_writer(u'</a>&nbsp;\n')
                pass
            pass
        # SOURCE LINE 68
        __M_writer(u'</td></tr>\n<!-- \n\n<tr><th>type</th><td>')
        # SOURCE LINE 71
        __M_writer(escape(c.event.evtype))
        __M_writer(u'</td></tr>\n')
        # SOURCE LINE 72
        if c.event.evtype == "Failure":
            # SOURCE LINE 73
            __M_writer(u"<tr><td colspan='2'>\n<p>\n\t<strong>status:</strong> ")
            # SOURCE LINE 75
            __M_writer(escape(c.event.evstatus))
            __M_writer(u' \n\t<strong>cause:</strong> ')
            # SOURCE LINE 76
            __M_writer(escape(c.event.evcause))
            __M_writer(u' \n\t<strong>minutes:</strong> ')
            # SOURCE LINE 77
            __M_writer(escape(c.event.evminutes))
            __M_writer(u' \n\t</p>\n\t<p>\n\t<strong>losspv:</strong> ')
            # SOURCE LINE 80
            __M_writer(escape(c.event.evlosspv))
            __M_writer(u' \n\t<strong>domain:</strong> ')
            # SOURCE LINE 81
            __M_writer(escape(c.event.evdomain))
            __M_writer(u' \n\t<strong>reporter:</strong> ')
            # SOURCE LINE 82
            __M_writer(escape(c.event.evreporter))
            __M_writer(u' \n\t</p></td>\n\t</tr>\n')
            pass
        # SOURCE LINE 86
        __M_writer(u'\n -->\n\n\n\n</table>\n\n\n\n<!--  \n<div style="border-top:1px solid #ccc;">\n<div style="line-height:24px;">\n<h2 id="card-short-description" style="line-height:25px;">\n')
        # SOURCE LINE 99
        __M_writer(escape(c.event.evtitle))
        __M_writer(u' @')
        __M_writer(escape(c.event.evdate))
        __M_writer(u' #')
        __M_writer(escape(c.event.id))
        __M_writer(u'\n</h2>\n\n<p><strong>tags:</strong> ')
        # SOURCE LINE 102
        __M_writer(escape(c.event.evtags))
        __M_writer(u'</p>\n<p><strong>modified:</strong> ')
        # SOURCE LINE 103
        __M_writer(escape(c.event.evlastedit))
        __M_writer(u'</p>\n</div>\n\n<div class="card_cantain" style="PADDING-RIGHT:10px;OVERFLOW-Y:auto;PADDING-LEFT:10px;SCROLLBAR- FACE-COLOR:#ffffff;FONT-SIZE:11pt;PADDING-BOTTOM:0px;SCROLLBAR- HIGHLIGHT-COLOR:#ffffff;OVERFLOW:auto;WIDTH:100%;SCROLLBAR-SHADOW- COLOR:#919192;SCROLLBAR-3DLIGHT-COLOR:#ffffff;LINE- HEIGHT:100%;SCROLLBAR-ARROW-COLOR:#919192;PADDING-TOP:0px;SCROLLBAR- TRACK-COLOR:#ffffff;SCROLLBAR-DARKSHADOW- COLOR:#ffffff;LETTER-SPACING:1pt;TEXT-ALIGN:left">\n')
        # SOURCE LINE 107
        __M_writer(escape(c.event.getEvContent()))
        __M_writer(u'\n</div>\n\n<div style="line-height:24px;">\n<p class="graphlist"><strong>graphs: </strong>\n')
        # SOURCE LINE 112
        for x,g in enumerate(c.graphs):
            # SOURCE LINE 113
            if g.imgid:
                # SOURCE LINE 114
                __M_writer(u'<a href="/view/data/')
                __M_writer(escape(g.imgid))
                __M_writer(u'?d2=')
                __M_writer(escape(c.event.evdate))
                __M_writer(u'">')
                __M_writer(escape(g.imgid))
                __M_writer(u'</a>&nbsp;\n')
                pass
            pass
        # SOURCE LINE 117
        __M_writer(u'\n</p>\n<p><strong>type:</strong>')
        # SOURCE LINE 119
        __M_writer(escape(c.event.evtype))
        __M_writer(u'</p>\n')
        # SOURCE LINE 120
        if c.event.evtype == "Failure":
            # SOURCE LINE 121
            __M_writer(u'\t<p>\n\t<strong>status:</strong> ')
            # SOURCE LINE 122
            __M_writer(escape(c.event.evstatus))
            __M_writer(u' \n\t<strong>cause:</strong> ')
            # SOURCE LINE 123
            __M_writer(escape(c.event.evcause))
            __M_writer(u' \n\t<strong>minutes:</strong> ')
            # SOURCE LINE 124
            __M_writer(escape(c.event.evminutes))
            __M_writer(u' \n\t</p>\n\t<p>\n\t<strong>losspv:</strong> ')
            # SOURCE LINE 127
            __M_writer(escape(c.event.evlosspv))
            __M_writer(u' \n\t<strong>domain:</strong> ')
            # SOURCE LINE 128
            __M_writer(escape(c.event.evdomain))
            __M_writer(u' \n\t<strong>reporter:</strong> ')
            # SOURCE LINE 129
            __M_writer(escape(c.event.evreporter))
            __M_writer(u' \n\t</p>\n')
            pass
        # SOURCE LINE 132
        __M_writer(u'</div>\n\n')
        # SOURCE LINE 134
        __M_writer(u'\n\t<div>\n\t<p><a href="/events/edit/')
        # SOURCE LINE 136
        __M_writer(escape(c.event.id))
        __M_writer(u'">')
        __M_writer(escape("Edit"))
        __M_writer(u'</a>\n\t</p>\n\t</div>\n\n\n\n</div>\n-->\n<div class="notice" style="margin-top:10px;">\n\t<div style="float:right;padding-bottom:10px;color:#777"><a href="#addmsgform">\u56de\u590d</a></div>\n  <ol style="clear:both;">\n')
        # SOURCE LINE 147
        for x,m in enumerate(c.messages):
            # SOURCE LINE 148
            __M_writer(u'  \t<li>\n  \t\t<div class="userinfo">\n  \t\t\t<img alt="tony" src="http://192.168.1.118:40080/statusnet-0.9.5/avatar/1-48-20101101075218.png" /><div class="name">guest</div>\n  \t\t</div>\n  \t\t<div class="right">\n  \t\n\t\t\t  \t<p class="p1" ><span class="fw">')
            # SOURCE LINE 154
            __M_writer(escape(m.msgsubject))
            __M_writer(u'</span></p>\n\t\t\t  \t<p class="p2" >\u53d1\u8868\u4e8e\uff1a')
            # SOURCE LINE 155
            __M_writer(escape(m.msgdate))
            __M_writer(u'</p>\n\t\t\t  \t<p class="p3">')
            # SOURCE LINE 156
            __M_writer(escape(m.msgcontent))
            __M_writer(u'</p>\n  \t\t</div>\n  \t</li>\n')
            pass
        # SOURCE LINE 160
        __M_writer(u'  </ol>\n</div>\n<div class="addmsg">\n\t<h3><a name="addmsgform">\u56de\u590d</a></h3>\n\t<form action="/events/addmsgsubmit" method="post" onsubmit="return validate()">\n\t\t<!-- <div class="row"><label>\u6807\u9898\uff1a</label><input type="text" class="require" id="addmsgS" name="msgsubject"/></div> -->\n\t\t<div class="row"><label>\u5185\u5bb9\uff1a</label><textarea class="require" id="addmsgC" name="msgcontent"></textarea></div>\n\t\t<input type="hidden" value="')
        # SOURCE LINE 167
        __M_writer(escape(c.event.id))
        __M_writer(u'" name=\'eventid\' />\n\t\t<input type="submit" value="\u63d0\u4ea4" style="margin-left:50px;"/> <span id="error">(\u5185\u5bb9\u957f\u5ea61~200\u4e2a\u5b57\u7b26)</span>\n\t</form>\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 172
        __M_writer(u'\n\t<div class="slidebar">\t\n\t\t<h3 class="sbartitle">')
        # SOURCE LINE 174
        __M_writer(escape("Assistant"))
        __M_writer(u'</h3>\t\n\t\t<ul class="sbarlist">\n\t\t\t<li><a href="/events/new">New Event</a></li>\n\t\t</ul>\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n<script type="text/javascript">\nfunction validate(){\n    // \u9a8c\u8bc1\u5fc5\u586b\u9879\u662f\u5426\u5b58\u5728\n\t  $(".require").each(function(){\n\t\t\t\tif($(this).val() == \'\'){\n\t\t\t   \t\t\t$("#error").html("\u5185\u5bb9\u4e0d\u80fd\u4e3a\u7a7a!").addClass("error");\n\t\t\t   \t\t}\n\t\t\t\telse if\t($(this).val().length > 100){\n\t\t   \t\t\t$("#error").html("\u5185\u5bb9\u8fc7\u957f!").addClass("error");\n\t\t   \t\t}\n\t\t\t\telse{\n\t\t\t\t\t$("#error").html("(\u5185\u5bb9\u957f\u5ea61~100\u4e2a\u5b57\u7b26)").removeClass("error");\n\t\t\t\t\t}\n\t\t});\n\t\tif($(".error").length > 0){\n\t\t\treturn false;\n\t\t\t\n\t\t}else{\n\t\t\treturn true;\n\t\t\t\n\t\t}\n\n} \n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n<h1>')
        # SOURCE LINE 35
        __M_writer(escape(c.heading))
        __M_writer(u'\n')
        # SOURCE LINE 36
        __M_writer(u'\n<a style="" href="/events/edit/')
        # SOURCE LINE 37
        __M_writer(escape(c.event.id))
        __M_writer(u'">Edit</a>\n')
        # SOURCE LINE 38
        __M_writer(u'\n</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-1.4.4.min.js'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/events/list.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318562374.226258
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/events/list.html'
_template_uri='/derived/events/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<div class="pagination">\n\t')
        # SOURCE LINE 6
        __M_writer(escape(c.events.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n\t')
        # SOURCE LINE 9
        __M_writer(u'\n</div>\n\n<table class="atable" cellspacing="0" border="0" cellpadding="0">\n<tr>\n\t<td>id</td>\n\t<td width="70%">name</td>\n\t<td>date</td>\n</tr>\n')
        # SOURCE LINE 18
        for x,e in enumerate(c.events):
            # SOURCE LINE 19
            __M_writer(u'\t<tr>\n\t\t<td><a href="/events/detail/')
            # SOURCE LINE 20
            __M_writer(escape(e.id))
            __M_writer(u'">#')
            __M_writer(escape(e.id))
            __M_writer(u'</a></td>\n\t\t<td>')
            # SOURCE LINE 21
            __M_writer(escape(e.evtitle))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 22
            __M_writer(escape(e.evdate))
            __M_writer(u'</td>\n\t\t\n\t</tr>\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'</table>\n\n<div class="pagination">\n\t')
        # SOURCE LINE 29
        __M_writer(escape(c.events.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n\t<div class="slidebar">\t\n\t\t<h3 class="sbartitle">')
        # SOURCE LINE 34
        __M_writer(escape("Assistant"))
        __M_writer(u'</h3>\t\n\t\t<ul class="sbarlist">\n\t\t\t<li><a href="/events/new">New Event</a></li>\n\t\t</ul>\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/events/new.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318562261.3755701
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/events/new.html'
_template_uri='/derived/events/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['script', 'toolbox', 'title', 'heading', 'head_tags']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        str = context.get('str', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 129
        __M_writer(u'\n\n\n<div>\n')
        # SOURCE LINE 133
        if hasattr(c,'id') and c.id:
            # SOURCE LINE 134
            __M_writer(u'\t<form action="/events/editsubmit/')
            __M_writer(escape(c.id))
            __M_writer(u'" method="post" enctype="multipart/form-data" onsubmit="return validate()">\n')
            # SOURCE LINE 135
        else:
            # SOURCE LINE 136
            __M_writer(u'\t<form action="/events/newsubmit" method="post" enctype="multipart/form-data" onsubmit="return validate()">\n')
            pass
        # SOURCE LINE 138
        __M_writer(u'\t\t<table class="newevent">\n\t\t\t<tr class="field"><td valign="top" colspan="2"><input name="submit" type="submit" value="Save" /></td></tr>\n\t\t\t<tr class="field"><td valign="top" colspan="2"><label for="event_name"><span style="color:red;">\uff0a</span> \u4e3b\u9898:</label> <input class="require" id="event_name" name="event_name" type="text" value="')
        # SOURCE LINE 140
        __M_writer(escape(c.event.evtitle))
        __M_writer(u'" size="80" style="width:400px;" /> #')
        __M_writer(escape(c.event.id))
        __M_writer(u'</td>\n\t\t</tr>\n\t\t    <tr class="field"><td valign="top" colspan="2"> <label for="event_date"><span style="color:red;">\uff0a</span> \u53d1\u751f\u65f6\u95f4:</label>\n')
        # SOURCE LINE 143
        if hasattr(c,'d1'):
            # SOURCE LINE 144
            __M_writer(u'\t\t    <input class="require date datetime" id="event_date" name="d1" type="text" value ="')
            __M_writer(escape(c.d1))
            __M_writer(u'" /> \n')
            # SOURCE LINE 145
        else:
            # SOURCE LINE 146
            __M_writer(u'\t\t    <input class="require date datetime" id="event_date" name="d1" type="text" value ="')
            __M_writer(escape(str(c.event.evdate)[0:10]))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 148
        __M_writer(u'\t\t    <input class="require h datetime" value ="')
        __M_writer(escape(str(c.event.evdate)[11:13]))
        __M_writer(u'" name=\'h1\' type="text" style="width:40px;" maxlength="2" /> : <input class="require m datetime" name=\'m1\' type="text" style="width:40px;" maxlength="2" value="')
        __M_writer(escape(str(c.event.evdate)[14:16]))
        __M_writer(u'" /> </td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u53d1\u73b0\u65f6\u95f4: </label> <input class=" date datetime" name="d2" type="text" value ="')
        # SOURCE LINE 150
        __M_writer(escape(str(c.event.dt2)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h2\' style="width:40px;" class="h datetime" maxlength="2"  value="')
        __M_writer(escape(str(c.event.dt2)[11:13]))
        __M_writer(u'"/> : <input value="')
        __M_writer(escape(str(c.event.dt2)[14:16]))
        __M_writer(u'" name=\'m2\' type="text" style="width:40px;" maxlength="2" class="m datetime" /></td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u67e5\u660e\u539f\u56e0\u65f6\u95f4: </label> <input class="date datetime" name="d3" type="text" value ="')
        # SOURCE LINE 152
        __M_writer(escape(str(c.event.dt3)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h3\' style="width:40px;" class="h datetime"  maxlength="2" value="')
        __M_writer(escape(str(c.event.dt3)[11:13]))
        __M_writer(u'" /> : <input value="')
        __M_writer(escape(str(c.event.dt3)[14:16]))
        __M_writer(u'" type="text" name=\'m3\' class="m datetime" style="width:40px;" maxlength="2" /></td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u89e3\u51b3\u95ee\u9898\u65f6\u95f4: </label> <input class="date datetime" name="d4" type="text" value ="')
        # SOURCE LINE 154
        __M_writer(escape(str(c.event.dt4)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h4\' style="width:40px;" class="h datetime"  maxlength="2" value="')
        __M_writer(escape(str(c.event.dt4)[11:13]))
        __M_writer(u'" /> : <input value="')
        __M_writer(escape(str(c.event.dt4)[14:16]))
        __M_writer(u'" type="text" name=\'m4\' class="m datetime" style="width:40px;" maxlength="2" /></td>\n\t\t</tr>\n\t\t\t<tr><td><label>\u4e8b\u4ef6\u56fe\u7247:</label>\n')
        # SOURCE LINE 157
        if hasattr(c,'imgid'):
            # SOURCE LINE 158
            __M_writer(u'\t\t\t<input type="text" value="')
            __M_writer(escape(c.imgid))
            __M_writer(u'" name="graphs"/>\n')
            # SOURCE LINE 159
        else:
            # SOURCE LINE 160
            __M_writer(u'\t\t\t<input type="text" value="')
            __M_writer(escape(c.graphs))
            __M_writer(u'" name="graphs"/> \n')
            pass
        # SOURCE LINE 162
        __M_writer(u'\t\t\t<span>\u591a\u5f20\u56fe\u7247\u8bf7\u4ee5\u9017\u53f7","\u76f8\u9694</span></td></tr>\n\t\t\t<tr class="field"><td valign="top" colspan="2"><textarea id="ftextile" cols="80" name="event_content" rows="20">')
        # SOURCE LINE 163
        __M_writer(escape(c.event.evcontent))
        __M_writer(u'</textarea>\n\t\t</td></tr>\n\t\t\t<tr><td valign="top" colspan="2">\n\t\t\t\t\t\ttags:<input id="event_tags" name="event_tags" type="text" value ="')
        # SOURCE LINE 166
        __M_writer(escape(c.event.evtags))
        __M_writer(u'" size=15 />\n\t\t\t\t\t\tmin:<input id="event_minutes" name="event_minutes" type="text" value ="')
        # SOURCE LINE 167
        __M_writer(escape(c.event.evminutes))
        __M_writer(u'" size=3 />\n\t\t\t\t\t\tlosspv:<input id="event_losspv" name="event_losspv" type="text" value ="')
        # SOURCE LINE 168
        __M_writer(escape(c.event.evlosspv))
        __M_writer(u'" size=3 />\n\t\t\t\t\t\tcause:<select id="event_cause" name="event_cause">\n')
        # SOURCE LINE 170
        for cause in c.event_cause:  
            # SOURCE LINE 171
            if cause == c.event.evcause:
                # SOURCE LINE 172
                __M_writer(u'\t\t\t\t\t\t\t\t\t  \t\t<option value="')
                __M_writer(escape(cause))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(cause))
                __M_writer(u'</option>\n')
                # SOURCE LINE 173
            else:
                # SOURCE LINE 174
                __M_writer(u'\t\t\t\t\t\t\t\t\t  \t\t<option value="')
                __M_writer(escape(cause))
                __M_writer(u'">')
                __M_writer(escape(cause))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 177
        __M_writer(u'\t\t\t\t\t\t\t</select>\n\t\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr><td>\n\t\t\t\ttype:<select  id="event_type" name="event_type">\n')
        # SOURCE LINE 182
        for evtype in c.event_type:
            # SOURCE LINE 183
            if evtype == c.event.evtype:
                # SOURCE LINE 184
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(evtype))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(evtype))
                __M_writer(u'</option>\n')
                # SOURCE LINE 185
            else:
                # SOURCE LINE 186
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(evtype))
                __M_writer(u'">')
                __M_writer(escape(evtype))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 189
        __M_writer(u'\t\t\t\t</select>\n\t\t\t\t\n\t\t\t\tstatus:<select id="event_status" name="event_status">\n')
        # SOURCE LINE 192
        for status in c.event_status:
            # SOURCE LINE 193
            if status == c.event.evstatus:
                # SOURCE LINE 194
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(status))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(status))
                __M_writer(u'</option>\n')
                # SOURCE LINE 195
            else:
                # SOURCE LINE 196
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(status))
                __M_writer(u'">')
                __M_writer(escape(status))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 199
        __M_writer(u'\t\t\t\t</select>\n\t\t\t\tdomain:<select  id="event_domain" name="event_domain">\n')
        # SOURCE LINE 201
        for domain in c.event_domain:
            # SOURCE LINE 202
            __M_writer(u'\t\t\t\t  \n')
            # SOURCE LINE 203
            if domain == c.event.evdomain:
                # SOURCE LINE 204
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(domain))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(domain))
                __M_writer(u'</option>\n')
                # SOURCE LINE 205
            else:
                # SOURCE LINE 206
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(domain))
                __M_writer(u'">')
                __M_writer(escape(domain))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 209
        __M_writer(u'\t\t</select>\n\t\t\n\t\t\t</td>\n\t\t\t</tr>\n\t\t\n\t\t\t<tr class="field">\n\t\t\t<td valign="top" colspan="2"><input id="submit" name="submit" type="submit" value="Save" /></td>\n\t\t\t</tr>\n\t\t</table>\n\t</form>\n</div>\n<div id="flash"></div>\n<!-- <div id="upload"></div> -->\n\n\n')
        # SOURCE LINE 232
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n  \t<script type="text/javascript">\t\t\n\t\t$("document").ready(function(){\n\t\t\t\n\t\t\t$(function() {\n\t\t\t\t$( ".date" ).datepicker({ dateFormat: \'yy-mm-dd\' });\t\t\t\t\n\t\t\t});\n\n\t\t\t$(\'#ftextile\').markItUp(myTextileSettings);\n\n\t\t\t/* jQuery(\'#forms\').fileUpload({action:\'/\', field_name:\'file_field\',submit_label:\'upload\',use_iframes:true}) */\n\t\t\t\n\t\t\t/* \u9a8c\u8bc1\u56fe\u7247ID\u662f\u5426\u5b58\u5728 */\n\t\t\t\n\t\t\t$("input[name=\'graphs\']").blur(function(){\n\t\t\t\t  \n\t\t\t\t  if($(this).val() != \'\'){\n\t\t\t\t\t\t$.ajax({\n\t\t\t\t\t\t\t\turl:"/events/checkImgid",\n\t\t\t\t\t\t\t\tdata:"graphs="+$(this).val(),\n\t\t\t\t\t\t\t\tsuccess:function(html){\n\t\t\t\t\t\t\t\t\t$("input[name=\'graphs\']").siblings(".error").remove();\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tif(html)\n\t\t\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t$("input[name=\'graphs\']").after("<span class=\'error\'> \u56fe\u7247ID"+html+"\u4e0d\u5b58\u5728! </span>");\t\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\n\t\t\t\t\t\t\t   });\n\t\t\t\t\t}\n\n\t\t\t\t});\n\n\n\t\t\t/* \u9a8c\u8bc1\u65e5\u671f\u4e0e\u65f6\u95f4\u7684\u683c\u5f0f */\n\n\t\t\t$(".datetime").blur(function(){\n\t\t\t\t\n\t\t\t\t\tvar patt1=/\\d{4}\\-\\d{2}\\-\\d{2}/\n\t\t\t\t\tvar patt2=/\\d{2}/\n\t\t\t\t\n\t\t\t\t\tif($(this).hasClass("date")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt1.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte ){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65e5\u671f\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}else if($(this).hasClass("h")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt2.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte || parseInt($(this).val())>24){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65f6\u95f4\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}else if($(this).hasClass("m")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt2.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte || parseInt($(this).val())>60){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65f6\u95f4\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t$(".require").blur(function(){\n\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\tif($(this).val()==""){\n\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u5fc5\u586b\u9879\u4e0d\u80fd\u4e3a\u7a7a</span>");\n\t\t\t\t}\n\t\t\t\t\t\n\t\t  \t    });\n\t\t\t\t\t\t\t\t\t\n\t\t  });\n\t\t  \n\t\t  $("document").ready(App.Upload.init);\t\n\t\t  \n\t\t  function validate(){\n\t\t\t  \t  \n\t\t\t      // \u9a8c\u8bc1\u5fc5\u586b\u9879\u662f\u5426\u5b58\u5728\n\t\t\t\t  $(".require").each(function(){\n\t\t\t\t\t  \t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\t\tif($(this).val() == \'\'){\n\t\t\t\t\t\t   \t\t\t$(this).parent("td").append("<span class=\'error\'> \u5fc5\u586b\u9879\u4e0d\u80fd\u4e3a\u7a7a</span>");\n\t\t\t\t\t\t   \t\t}\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t});\n\t\t\t\t\tif($(".error").length > 0){\n\t\t\t\t\t\t\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t\n\t\t\t\t\t}else{\n\t\t\t\t\t\t\n\t\t\t\t\t\treturn true;\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\n\t\t\t  } \n\t\t  \n\t</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 224
        __M_writer(u'\n\t<div class="box">\t\n\t\t<h3>')
        # SOURCE LINE 226
        __M_writer(escape("Assistant"))
        __M_writer(u'</h3>\t\n\t\t<ul>\n\t\t\t<li><a href="/events/new">New Event</a></li>\n\t\t\t<li><a href="http://redcloth.org/hobix.com/textile/" target="_blank">Textile Reference</a></li>\n\t\t</ul>\t\n\t</div>\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(escape(c.heading))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<h1>')
        # SOURCE LINE 4
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-1.4.4.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-ui-1.8.8.custom.min.js'))))
        __M_writer(u'    \n')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link(h.url_for('/jquery/development-bundle/themes/pepper-grinder/jquery.ui.all.css'))))
        __M_writer(u'\n<script type="text/javascript" src="/markitup/jquery.markitup.js"></script>\n<script type="text/javascript" src="/markitup/sets/textile/set.js"></script>\n<!-- <script src="')
        # SOURCE LINE 13
        __M_writer(escape(url('/js/App.Upload.js')))
        __M_writer(u'" type="text/javascript"></script> -->\n<link rel="stylesheet" type="text/css" href="/markitup/skins/markitup/style.css" />\n<link rel="stylesheet" type="text/css" href="/markitup/sets/textile/style.css" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/devices/list.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320476325.1164241
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/devices/list.html'
_template_uri='/derived/devices/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading', 'script']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n\n<div class="pagination">\n\t')
        # SOURCE LINE 6
        __M_writer(escape(c.devices.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n\t')
        # SOURCE LINE 9
        __M_writer(u'\n</div>\n\n<table class="atable" cellspacing="0" border="0" cellpadding="0" id="deviceList">\n<thead>\n<tr>\n\t\n\t<th>\u4e3b\u673a\u540d</th><th>\u5904\u7406\u5668</th><th>\u5185\u5b58</th><th>\u78c1\u76d8</th><th>\u578b\u53f7</th><th>\u5185\u6838</th>\n\t\n\t\n</tr>\n</thead>\n<tbody>\n')
        # SOURCE LINE 22
        for x,d in enumerate(c.devices):
            # SOURCE LINE 23
            __M_writer(u'\t<tr>\n\t\t<td><a class=\'link\' href="/devices/deviceItems?dsn=')
            # SOURCE LINE 24
            __M_writer(escape(d.serial_no))
            __M_writer(u'&dn=')
            __M_writer(escape(d.hostname))
            __M_writer(u'">')
            __M_writer(escape(d.hostname))
            __M_writer(u'</a></td>\n\t\t<td>')
            # SOURCE LINE 25
            __M_writer(escape(d.cpuinfo))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 26
            __M_writer(escape(d.memsize))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 27
            __M_writer(escape(d.diskspace))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 28
            __M_writer(escape(d.hardware))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 29
            __M_writer(escape(d.kernel_info))
            __M_writer(u'</td>\n\t\t\n\t</tr>\n')
            pass
        # SOURCE LINE 33
        __M_writer(u'</tbody>\n</table>\n\n<div class="pagination">\n\t')
        # SOURCE LINE 37
        __M_writer(escape(c.devices.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n</div>\n\n')
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 75
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 40
        __M_writer(u'\n\t<div class="slidebar">\t\n\t\t<h3 class="sbartitle">\u5feb\u901f\u641c\u7d22</h3>\t\n\t\t<form action="/devices" method="get">\t\t\n\t\t<input type="text" name="ds" value="" />\t\t\n\t\t<input type="submit" value="Go" />\n\t\t</form>\n\t</div>\n\t\n\t<div class="slidebar">\t\n\t\t\t<h3 class="sbartitle">\u70ed\u95e8\u641c\u7d22</h3>\n\t\t\t<p>\n\t\t\t\t<a href="/devices?ds=app">app</a> \n\t\t\t</p>\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'\n<script type="text/javascript" src="/jquery/js/jquery-1.6.2.min.js"></script>\n<script type="text/javascript">\n$(function(){\n$("#deviceList tbody tr").hover(function(){\n\t$(this).children(\'td\').css({\'background-color\':\'#778877\',cursor:\'pointer\',color:\'#fff\'})\n\t\n},function(){\n\t$(this).children(\'td\').css({\'background-color\':\'#fff\',cursor:\'auto\',color:\'#000\'})\n\t\n});\n$("#deviceList tbody tr").click(function(){\n\th = $(this).find(\'.link\').attr(\'href\')\n\tlocation.href = h;\n\t\n});\n\t\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/devices/daily_report.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320473820.9946859
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/devices/daily_report.html'
_template_uri='/derived/devices/daily_report.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['profile']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'navigation', context._clean_inheritance_tokens(), templateuri=u'/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        navigation = _mako_get_namespace(context, 'navigation')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<title>report</title>\n<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\n<link href="/css/report.css" rel="stylesheet" type="text/css" />\n<style type="text/css">\n\n#chartwrap dl{\nborder:none;\n}\n\n</style>\n</head>\n<body>\n\t<div class="wrap">\n\t\t<div class="header">\n\t\t    <div class="header_top">\n\t\t\t\t<a href="/" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\n\t\t\t\t')
        # SOURCE LINE 22
        __M_writer(escape(self.profile()))
        __M_writer(u'\n\t\t\t</div>\n\t\t\n\t\t   <!-- <div id="description">{toolkit}</div> --> \n')
        # SOURCE LINE 26
        if hasattr(c,'pagename') and c.pagename:
            # SOURCE LINE 27
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(navigation.menu(c.pagename)))
            __M_writer(u'\n')
            # SOURCE LINE 28
        else:
            # SOURCE LINE 29
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(navigation.menu("")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 31
        __M_writer(u'\t\t    \n\t\t</div><!-- end header -->\n\t\t<p class="pageguide">\n\t\t\t<a href="/">\u9996\u9875</a>&nbsp;&gt;&gt;&nbsp;<a href="/devices">\u4e3b\u673a</a>&nbsp;&gt;&gt;&nbsp;\n\t\t\t<span id="oname">\n')
        # SOURCE LINE 36
        if hasattr(c,'ditem'):
            # SOURCE LINE 37
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(c.ditem))
            __M_writer(u'\n')
            # SOURCE LINE 38
        else:
            # SOURCE LINE 39
            __M_writer(u'\t\t\t\t')
            __M_writer(escape(c.info.hostname))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\t\t\t</span>\n\t\t</p>\n\t\t<div class="main">\n\t\t\t<div class="main_left devicechartlist" id="chartwrap">\n\t\t\t<div class=\'deviceinfo\' style="position:relative">\n\t\t\t\n\t\t\t        <table cellspacing=0 cellpadding = 0 border =0 id="deviceinfo">\n\t\t\t        \n\t\t\t        <tr><th>\u4e3b\u673a\u540d\uff1a</th><td>')
        # SOURCE LINE 49
        __M_writer(escape(c.info.hostname))
        __M_writer(u'</td><th>IP\uff1a</th><td>')
        __M_writer(escape(c.info.inetaddr))
        __M_writer(u'</td></tr>\n\t\t\t        <tr><th>CPU\uff1a</th><td>')
        # SOURCE LINE 50
        __M_writer(escape(c.info.cpuinfo))
        __M_writer(u'</td><th>\u5185\u5b58\uff1a</th><td>')
        __M_writer(escape(c.info.memsize))
        __M_writer(u'</td></tr>\n\t\t\t        <tr><th>\u578b\u53f7\uff1a</th><td>')
        # SOURCE LINE 51
        __M_writer(escape(c.info.hardware))
        __M_writer(u'</td><th>\u78c1\u76d8\uff1a</th><td>')
        __M_writer(escape(c.info.diskspace))
        __M_writer(u'</td></tr>\n\t\t\t        <tr><th>\u5185\u6838\uff1a</th><td>')
        # SOURCE LINE 52
        __M_writer(escape(c.info.kernel_info))
        __M_writer(u'</td><th>\u6240\u6709\u8005\uff1a</th><td>')
        __M_writer(escape(c.info.customer))
        __M_writer(u'</td></tr>\n\t\t\t        </table>\n\t\t\t        <button id="slide" type=\'button\' style="cursor:pointer;position:absolute;top:0;right:0;width:16px;height:16px;padding:0;margin:0;background:url(\'/img/Arrow up.png\') no-repeat 0 0 transparent;border:0;"></button>\n\t\t\t</div>\n')
        # SOURCE LINE 56
        if c.pagename == 'deviceitems':
            # SOURCE LINE 57
            __M_writer(u'\t\t\t\n')
            # SOURCE LINE 58
            for x,t in enumerate(c.rows):
                # SOURCE LINE 59
                if c.rows[x]:
                    # SOURCE LINE 60
                    __M_writer(u'\t\t\t\t\t\t<dl class="dl1 floatl" id="')
                    __M_writer(escape(t.id))
                    __M_writer(u'">\n\t\t\t\t\t\t\t<dt>')
                    # SOURCE LINE 61
                    __M_writer(escape(x+1))
                    __M_writer(u') ')
                    __M_writer(escape(t.ditem))
                    __M_writer(u'</dt>\n\t\t\t\t\t\t\t<dd class="dd2 floatl">\n\t\t\t\t\t\t\t\t<img src="/devices/viewData/')
                    # SOURCE LINE 63
                    __M_writer(escape(t.id))
                    __M_writer(u'/')
                    __M_writer(escape(c.date))
                    __M_writer(u'/1.png" />\n\t\t\t\t\t\t\t\t<a class=\'cmp\' href="/devices/cmpItem?id=')
                    # SOURCE LINE 64
                    __M_writer(escape(t.id))
                    __M_writer(u'&d=')
                    __M_writer(escape(c.date))
                    __M_writer(u'&sn=')
                    __M_writer(escape(c.info.serial_no))
                    __M_writer(u'" title="\u5bf9\u6bd4"></a>\n\t\t\t\t\t\t\t\t<a class=\'top\' href="#" title="\u9876\u90e8"></a>\n\t\t\t\t\t\t\t</dd>\t\n\t\t\t\t\t\t</dl>\n')
                    pass
                pass
            pass
        # SOURCE LINE 71
        if c.pagename == 'cmpitem':
            # SOURCE LINE 72
            for x in c.dds:
                # SOURCE LINE 73
                __M_writer(u'\t\t\t\t\t\n\t\t\t\t\t\t<dl class="dl1 floatl" >\n\t\t\t\t\t\t\t<dt>')
                # SOURCE LINE 75
                __M_writer(escape(x))
                __M_writer(u'</dt>\n\t\t\t\t\t\t\t<dd class="dd2 floatl">\n\t\t\t\t\t\t\t\t<img src="/devices/viewData/')
                # SOURCE LINE 77
                __M_writer(escape(c.id))
                __M_writer(u'/')
                __M_writer(escape(x))
                __M_writer(u'/1.png" />\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</dd>\t\n\t\t\t\t\t\t</dl>\n\n')
                pass
            pass
        # SOURCE LINE 84
        __M_writer(u'\t\t\t</div><!-- end main_left -->\n\t\t\t\n\t\t\t<div class="main_right">\n')
        # SOURCE LINE 87
        if c.pagename == 'deviceitems':
            # SOURCE LINE 88
            __M_writer(u'\t\t\t\t<div class="slidebar">\t\n\t\t\t\t\t\t<h3 class="sbartitle">\u5feb\u901f\u5b9a\u4f4d</h3>\n\t\t\t\t\t\t<ul class="sbarlist">\n')
            # SOURCE LINE 91
            for x,t in enumerate(c.rows):
                # SOURCE LINE 92
                if c.rows[x]:
                    # SOURCE LINE 93
                    __M_writer(u'\t\t\t\t\t\t\t<li><a href="#')
                    __M_writer(escape(t.id))
                    __M_writer(u'">')
                    __M_writer(escape(t.ditem))
                    __M_writer(u'</a></li>\n')
                    pass
                pass
            # SOURCE LINE 96
            __M_writer(u'\t\t\t\t\t\t</ul>\n\t\t\t\t</div>\n')
            pass
        # SOURCE LINE 99
        __M_writer(u'\t\t\t\t<div class="slidebar datepicker">\n\t\t\t\t\t<div id="datepicker"></div>\n\t\t\t\t\t<input type="hidden" id="actualDate" />\n')
        # SOURCE LINE 102
        if hasattr(c,'kw'):
            # SOURCE LINE 103
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="kw" value="')
            __M_writer(escape(c.kw))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 105
        if hasattr(c,'info'):
            # SOURCE LINE 106
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="dsn" value="')
            __M_writer(escape(c.info.serial_no))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 108
        if hasattr(c,'info'):
            # SOURCE LINE 109
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="dn" value="')
            __M_writer(escape(c.info.hostname))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 111
        __M_writer(u'\t\t\t\t</div>\n\t\t\t\t\n\t\t\t\n\t\t\t</div><!-- end main_right -->\n\t\t</div><!-- end main -->\n\t</div><!-- end wrap -->\n<script type="text/javascript" src="/jquery/js/jquery-1.4.4.min.js"></script>\n<script type="text/javascript" src="/jquery/js/jquery-ui-1.8.8.custom.min.js"></script>\n<script type="text/javascript" src="/js/CJL.0.1.min.js"></script>\n<script type="text/javascript" src="/js/LazyLoad.js"></script>\n<script type="text/javascript" src="/js/lazyLoadImg.js"></script>\n<script type="text/javascript">\n$(function(){\n\tvar oDate\n\tvar defaultdate = "')
        # SOURCE LINE 125
        __M_writer(escape(c.date))
        __M_writer(u'"\n\tvar kw = \'\'\n\tvar dns=\'\'\n\tvar dn=\'\'\n\tif (document.getElementById("kw"))\n\t\tkw = $("#kw").val()\n\tif (document.getElementById("dsn"))\n\t\tdsn = $("#dsn").val()\n\tif (document.getElementById("dn"))\n\t\tdn = $("#dn").val()\n\t\n\t$( "#datepicker" ).datepicker({\n\t\taltFormat: \'yy-mm-dd\',\n\t\taltField: \'#actualDate\',\n\t\tonSelect: function(dateText, inst) { \n\t\t\t\toDate = $("#actualDate").val();\n\t\t\t\tif(kw)\n\t\t\t\t\tlocation.href = "/devices/deviceItems?kw="+kw+"&d="+oDate;\n\t\t\t\t\t\n\t\t\t\telse\n\t\t\t\t\tlocation.href = "/devices/deviceItems?dsn="+dsn+"&dn="+dn+"&d="+oDate;\n\t\t\t\t    \n\t\t},\n\t\tdateFormat: \'yy-mm-dd\',\n\t\tdefaultDate:defaultdate\n\t\t\n\t});\n\t$("#slide").toggle(function(){\n\t\t\t\t$(\'#deviceinfo\').fadeOut(\'slow\')\n\t\t\t\t$(this).css("background-image","url(\'/img/Arrow down.png\')")\n\t\t},function(){\n\t\t\t\t$(\'#deviceinfo\').fadeIn(\'slow\')\n\t\t\t\t$(this).css("background-image","url(\'/img/Arrow up.png\')")\n\t\t});\n});\n</script>\t\n</body>\n</html>\n')
        # SOURCE LINE 171
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_profile(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 163
        __M_writer(u'\n    <div class="welcome">\n')
        # SOURCE LINE 165
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 166
            __M_writer(u'\t  \t\t<a href="/signin" class="login">\u767b\u5f55</a>\n')
            # SOURCE LINE 167
        else:
            # SOURCE LINE 168
            __M_writer(u'\t  \t\t\u4f60\u597d\uff0c')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u' <a href="/signout">\u9000\u51fa</a> | <a href="/template">\u914d\u7f6e</a> \n')
            pass
        # SOURCE LINE 170
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/speed/index.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1312871421.282233
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/speed/index.html'
_template_uri='/derived/speed/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'/component/pagination.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n<div style="border-top:1px solid #ccc;">\n\u6b63\u5728\u8bbe\u8ba1\u4e2d\uff0c\u9884\u8ba1\u57286\u6708\u4e2d\u65ec\u5f00\u653e\u3002\u656c\u8bf7\u5173\u6ce8\uff5e\n</div>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.pagename))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(escape(c.pagename))
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/account/signedin.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1314759878.2835391
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/account/signedin.html'
_template_uri='/derived/account/signedin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n<p>You are signed in as ')
        # SOURCE LINE 6
        __M_writer(escape(request.environ['REMOTE_USER']))
        __M_writer(u'.\n<a href="')
        # SOURCE LINE 7
        __M_writer(escape(h.url_for(controller='account', action='signout')))
        __M_writer(u'">Sign out</a></p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>Signed In</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Signed In')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/account/signin.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1314759794.1874571
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/account/signin.html'
_template_uri='/derived/account/signin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n<!-- ')
        # SOURCE LINE 19
        __M_writer(escape(h.form_start('%s', method="post")))
        __M_writer(u'-->\n<form class="signinform" action="/signin" method="post">\n\t<div><label for="username"> Username:</label><input id="username" name="username" type="text" /></div>\n\t<div><label for="password"> Password:</label><input id="password" name="password" type="password" /></div>\n\t<div><input id="submit" name="submit" type="submit" value="Sign in" /></div>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">Sign In</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Sign In')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/categories/edit.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1315195500.4765401
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/categories/edit.html'
_template_uri='/derived/categories/edit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n<form action="/categories/')
        # SOURCE LINE 20
        __M_writer(escape(c.action))
        __M_writer(u'" method="post">\n<table style="width:100%;border: 1px solid #ccc;">\n<tr>\n    <td colspan="2" style="text-align:center;background-color:#eee;"><strong>')
        # SOURCE LINE 23
        __M_writer(escape(u"基础信息"))
        __M_writer(u'</strong></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 26
        __M_writer(escape(u"名称"))
        __M_writer(u'</td><td><input type="text" name="typename" value=\'')
        __M_writer(escape(c.cate.typename))
        __M_writer(u'\' class="input_text" /></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 29
        __M_writer(escape(u"类名"))
        __M_writer(u'</td><td><input type="text" name="classname" value=\'')
        __M_writer(escape(c.cate.classname))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 33
        __M_writer(escape(u"数据项"))
        __M_writer(u'</td><td><input type="text" name="items" value=\'')
        __M_writer(escape(c.cate.items))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 36
        __M_writer(escape(u"图标题"))
        __M_writer(u'</td><td><input type="text" name="titles" value=\'')
        __M_writer(escape(c.cate.titles))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 39
        __M_writer(escape(u"显示天数"))
        __M_writer(u'</td><td>\n    <select  id="labels" name="labels">\n')
        # SOURCE LINE 41
        for labels in c.labels:
            # SOURCE LINE 42
            if labels == c.cate.labels:
                # SOURCE LINE 43
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(labels))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(labels))
                __M_writer(u'</option>\n')
                # SOURCE LINE 44
            else:
                # SOURCE LINE 45
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(labels))
                __M_writer(u'">')
                __M_writer(escape(labels))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 48
        __M_writer(u'</select>\n    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 52
        __M_writer(escape(u"隐藏"))
        __M_writer(u'</td><td>\n')
        # SOURCE LINE 53
        if c.cate.disable == 0:
            # SOURCE LINE 54
            __M_writer(u'\t    <input type="radio" name="disable" value="0" checked> No\n\t\t<input type="radio" name="disable" value="1"> Yes\t\n')
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u'    \t    <input type="radio" name="disable" value="0"> No\n\t\t\t<input type="radio" name="disable" value="1" checked> Yes\t\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 63
        __M_writer(escape(u"排序字段"))
        __M_writer(u'</td>\n    <td>\n\t    <select  id="orderby" name="orderby">\n')
        # SOURCE LINE 66
        for orderby in c.orderby:
            # SOURCE LINE 67
            if orderby == c.cate.orderby:
                # SOURCE LINE 68
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(orderby))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(orderby))
                __M_writer(u'</option>\n')
                # SOURCE LINE 69
            else:
                # SOURCE LINE 70
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(orderby))
                __M_writer(u'">')
                __M_writer(escape(orderby))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 73
        __M_writer(u'</select>\n\t    <input type="hidden" name="typeid" value=\'')
        # SOURCE LINE 74
        __M_writer(escape(c.cate.typeid))
        __M_writer(u'\' /> \n    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 78
        __M_writer(escape(u"图形"))
        __M_writer(u'</td><td>\n    <select  id="graphtype" name="graphtype">\n')
        # SOURCE LINE 80
        for graphtype in c.graphtype:
            # SOURCE LINE 81
            if graphtype == c.cate.graphtype:
                # SOURCE LINE 82
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(graphtype))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(graphtype))
                __M_writer(u'</option>\n')
                # SOURCE LINE 83
            else:
                # SOURCE LINE 84
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(graphtype))
                __M_writer(u'">')
                __M_writer(escape(graphtype))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 87
        __M_writer(u'</select>\n    \n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 93
        __M_writer(escape(u"排序"))
        __M_writer(u'</td><td><input type="text" name="rankcode" value=\'')
        __M_writer(escape(c.cate.rankcode))
        __M_writer(u'\' class="input_text_short" /></td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 97
        __M_writer(escape(u"数据支持"))
        __M_writer(u'</td><td><input type="text" name="datasupport" value=\'')
        __M_writer(escape(c.cate.datasupport))
        __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n\n')
        # SOURCE LINE 100
        if c.cate.graphtype == "realtime":
            # SOURCE LINE 101
            __M_writer(u'<tr>\n    <td colspan="2" style="text-align:center;background-color:#eee;"><strong>')
            # SOURCE LINE 102
            __M_writer(escape(u"实时监控"))
            __M_writer(u'</strong></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 105
            __M_writer(escape(u"分类"))
            __M_writer(u'</td><td>\n<select  id="typecode" name="typecode">\n')
            # SOURCE LINE 107
            for typecode_k, typecode_v in c.r_typecode.iteritems():
                # SOURCE LINE 108
                if typecode_v == c.cate.typecode:
                    # SOURCE LINE 109
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(typecode_v))
                    __M_writer(u'" selected="selected">')
                    __M_writer(escape(typecode_k))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 110
                else:
                    # SOURCE LINE 111
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(typecode_v))
                    __M_writer(u'">')
                    __M_writer(escape(typecode_k))
                    __M_writer(u'</option>\n')
                    pass
                pass
            # SOURCE LINE 114
            __M_writer(u'</select>\n </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 118
            __M_writer(escape(u"警告"))
            __M_writer(u'</td><td><input type="text" name="warning" value=\'')
            __M_writer(escape(c.cate.warning))
            __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 121
            __M_writer(escape(u"崩潰"))
            __M_writer(u'</td><td><input type="text" name="critical" value=\'')
            __M_writer(escape(c.cate.critical))
            __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 125
            __M_writer(escape(u"日报"))
            __M_writer(u'</td><td>\n')
            # SOURCE LINE 126
            if c.cate.d_report == 0:
                # SOURCE LINE 127
                __M_writer(u'\t    <input type="radio" name="d_report" value="0" checked> No\n\t\t<input type="radio" name="d_report" value="1"> Yes\t\n')
                # SOURCE LINE 129
            else:
                # SOURCE LINE 130
                __M_writer(u'    \t    <input type="radio" name="d_report" value="0"> No\n\t\t\t<input type="radio" name="d_report" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 133
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 137
            __M_writer(escape(u"报警"))
            __M_writer(u'</td><td>   \n')
            # SOURCE LINE 138
            if c.cate.r_alert == 0:
                # SOURCE LINE 139
                __M_writer(u'\t    <input type="radio" name="r_alert" value="0" checked> No\n\t\t<input type="radio" name="r_alert" value="1"> Yes\t\n')
                # SOURCE LINE 141
            else:
                # SOURCE LINE 142
                __M_writer(u'    \t    <input type="radio" name="r_alert" value="0"> No\n\t\t\t<input type="radio" name="r_alert" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 145
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 149
            __M_writer(escape(u"权重"))
            __M_writer(u'</td><td>\n    <select  id="r_weight" name="r_weight">\n')
            # SOURCE LINE 151
            for r_weight in c.r_weight:
                # SOURCE LINE 152
                if r_weight == c.cate.r_weight:
                    # SOURCE LINE 153
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(r_weight))
                    __M_writer(u'" selected="selected">')
                    __M_writer(escape(r_weight))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 154
                else:
                    # SOURCE LINE 155
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(r_weight))
                    __M_writer(u'">')
                    __M_writer(escape(r_weight))
                    __M_writer(u'</option>\n')
                    pass
                pass
            # SOURCE LINE 158
            __M_writer(u'</select>\n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 163
            __M_writer(escape(u"分析模型"))
            __M_writer(u'</td><td>\n    \n')
            # SOURCE LINE 165
            for r_mode in c.r_mode:
                # SOURCE LINE 166
                if r_mode == c.cate.r_mode:
                    # SOURCE LINE 167
                    __M_writer(u'  \t\t<input type="radio" name="r_mode" value="')
                    __M_writer(escape(r_mode))
                    __M_writer(u'" checked> ')
                    __M_writer(escape(r_mode))
                    __M_writer(u'\n')
                    # SOURCE LINE 168
                else:
                    # SOURCE LINE 169
                    __M_writer(u'  \t\t<input type="radio" name="r_mode" value="')
                    __M_writer(escape(r_mode))
                    __M_writer(u'" > ')
                    __M_writer(escape(r_mode))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 172
            __M_writer(u'<span class="intro">\u8bf4\u660e\uff1aa:A, b:V, c:<> d:.<>.</span>\n    </td>\n</tr>\n')
            # SOURCE LINE 187
            __M_writer(u'\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 189
            __M_writer(escape(u"报警周期"))
            __M_writer(u'</td><td>\n')
            # SOURCE LINE 190
            for l_interval in c.l_interval:
                # SOURCE LINE 191
                if l_interval == c.cate.l_interval:
                    # SOURCE LINE 192
                    __M_writer(u'\t  \t\t<input type="radio" name="l_interval" value="')
                    __M_writer(escape(l_interval))
                    __M_writer(u'" checked> ')
                    __M_writer(escape(l_interval))
                    __M_writer(u'\n')
                    # SOURCE LINE 193
                else:
                    # SOURCE LINE 194
                    __M_writer(u'\t  \t\t<input type="radio" name="l_interval" value="')
                    __M_writer(escape(l_interval))
                    __M_writer(u'" > ')
                    __M_writer(escape(l_interval))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 197
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 201
            __M_writer(escape(u"报警阀值"))
            __M_writer(u'</td><td class="tab_td2">\n    ')
            # SOURCE LINE 207
            __M_writer(u'\n    <lu>\n\t    <li><i>')
            # SOURCE LINE 209
            __M_writer(escape(u"最小值"))
            __M_writer(u'</i> <input type="text" name="x_thr_0" value=\'')
            __M_writer(escape(c.list_alarm_threshold[0]))
            __M_writer(u'\' class="input_text_short" /></li>\n\t   \t<li><i>')
            # SOURCE LINE 210
            __M_writer(escape(u"稍小值"))
            __M_writer(u'</i> <input type="text" name="x_thr_1" value=\'')
            __M_writer(escape(c.list_alarm_threshold[1]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 211
            __M_writer(escape(u"稍大值"))
            __M_writer(u'</i> <input type="text" name="x_thr_2" value=\'')
            __M_writer(escape(c.list_alarm_threshold[2]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 212
            __M_writer(escape(u"最大值"))
            __M_writer(u'</i> <input type="text" name="x_thr_3" value=\'')
            __M_writer(escape(c.list_alarm_threshold[3]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 213
            __M_writer(escape(u"最小百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_4" value=\'')
            __M_writer(escape(c.list_alarm_threshold[4]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 214
            __M_writer(escape(u"稍小最分百"))
            __M_writer(u'</i> <input type="text" name="x_thr_5" value=\'')
            __M_writer(escape(c.list_alarm_threshold[5]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 215
            __M_writer(escape(u"稍大百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_6" value=\'')
            __M_writer(escape(c.list_alarm_threshold[6]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 216
            __M_writer(escape(u"最大百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_7" value=\'')
            __M_writer(escape(c.list_alarm_threshold[7]))
            __M_writer(u'\' class="input_text_short" />% </li>\n   \t</lu>\n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 222
            __M_writer(escape(u"参考线"))
            __M_writer(u'</td><td>   \n\t    <input type="text" name="baseface" value="')
            # SOURCE LINE 223
            __M_writer(escape(c.cate.baseface))
            __M_writer(u'" />\n')
            # SOURCE LINE 224
            if c.cate.u_baseface == 0:
                # SOURCE LINE 225
                __M_writer(u'\t    <input type="radio" name="usebaseface" value="0" checked> No\n\t\t<input type="radio" name="usebaseface" value="1"> Yes\t\n')
                # SOURCE LINE 227
            else:
                # SOURCE LINE 228
                __M_writer(u'    \t    <input type="radio" name="usebaseface" value="0"> No\n\t\t\t<input type="radio" name="usebaseface" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 231
            __M_writer(u'\t    \n    </td>\n</tr>\n\n')
            pass
        # SOURCE LINE 236
        __M_writer(u'\n<tr>\n    <td colspan="2" style="text-align:center;">    \n    <input type="submit" value="')
        # SOURCE LINE 239
        __M_writer(escape(u"保存"))
        __M_writer(u'" />\n')
        # SOURCE LINE 240
        if c.action == "submit":
            # SOURCE LINE 241
            __M_writer(u'    <input type="button" value="')
            __M_writer(escape(u'克隆'))
            __M_writer(u'" onclick="window.location.href=\'/categories/copy/')
            __M_writer(escape(c.cate.typeid))
            __M_writer(u'\'" /> \n')
            pass
        # SOURCE LINE 243
        __M_writer(u'    \n    </td>\n</tr>\n</table>\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n<div class="box">\n\n<h3>toolbox</h3>\n\n<ul>\n\t<li><a href="/categories/add">new template</a></li>\n</ul>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <h1>')
        # SOURCE LINE 4
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/error/document.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1309775327.1553421
_template_filename='/home/hyhe/workspace/pyfisheyes/pyfisheyes/templates/derived/error/document.html'
_template_uri='/derived/error/document.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        if c.code == '403':
            # SOURCE LINE 7
            __M_writer(u'<p>You do not have sufficient permissions to access this page. Please\n<a href="')
            # SOURCE LINE 8
            __M_writer(escape(h.url_for('signinagain')))
            __M_writer(u'">sign in</a> as a different user.</p>\n')
            # SOURCE LINE 9
        else:
            # SOURCE LINE 10
            __M_writer(u'<p>')
            __M_writer(escape(c.message))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 12
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>Error ')
        __M_writer(escape(c.code))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Server Error ')
        __M_writer(escape(c.code))
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/derived/homepage/home.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320650871.534734
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/homepage/home.html'
_template_uri='/derived/homepage/home.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n<div class="graph"> \n\t<img src="http://imgpyfisheyes.corp.yoursite.com/view/graph/23/0/2011-07-24/2011-10-24/1.png" id="graphs" /> \n</div> \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n <h1 class="heading">\u9996\u9875</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'homepage')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/component/pagination.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1309775314.3182449
_template_filename=u'/home/hyhe/workspace/pyfisheyes/pyfisheyes/templates/component/pagination.html'
_template_uri=u'/component/pagination.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['pagin']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagin(context,cp,is_ajax):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div class="pagination">\n')
        # SOURCE LINE 3
        if is_ajax:
            # SOURCE LINE 4
            __M_writer(u'\t')
            __M_writer(escape(cp.rows.pager('$link_previous ~4~ $link_next ',symbol_first=u'首页', symbol_last=u'末页', symbol_previous=u'上一页', symbol_next=u'下一页',onclick="$('#page-area').load('%s',function(){}); return false;")))
            __M_writer(u'\n')
            # SOURCE LINE 5
        else:
            # SOURCE LINE 6
            __M_writer(u'\t')
            __M_writer(escape(cp.rows.pager('Page $page: $link_previous ~4~ $link_next', symbol_last=u'末页', symbol_previous=u'上一页', symbol_next=u'下一页')))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/component/navigation.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320230902.121417
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/component/navigation.html'
_template_uri=u'/component/navigation.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,selected):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\t    <ul class="nav">\n')
        # SOURCE LINE 3
        if selected == "homepage":
            # SOURCE LINE 4
            __M_writer(u'\t\t\t<li><a class="active" href="/">\u9996\u9875</a></li>\n')
            # SOURCE LINE 5
        else:
            # SOURCE LINE 6
            __M_writer(u'\t\t    <li><a href="/">\u9996\u9875</a></li>\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\t\t\n')
        # SOURCE LINE 9
        if selected == "day":
            # SOURCE LINE 10
            __M_writer(u'\t\t\t<li><a class="active" href="/list/day">\u6bcf\u5929</a></li>\n')
            # SOURCE LINE 11
        else:
            # SOURCE LINE 12
            __M_writer(u'\t\t\t<li><a href="/list/day">\u6bcf\u5929</a></li>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\t\t\n')
        # SOURCE LINE 15
        if selected == "hour":
            # SOURCE LINE 16
            __M_writer(u'\t\t\t<li><a class="active" href="/list/hour">\u5c0f\u65f6</a></li>\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'\t\t\t<li><a href="/list/hour">\u5c0f\u65f6</a></li>\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t\n')
        # SOURCE LINE 21
        if selected == "host":
            # SOURCE LINE 22
            __M_writer(u'\t\t\t<li><a class="active" href="/list/host">\u5206\u7ec4</a></li>\n')
            # SOURCE LINE 23
        else:
            # SOURCE LINE 24
            __M_writer(u'\t\t\t<li><a href="/list/host">\u5206\u7ec4</a></li>\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'\t\t\n')
        # SOURCE LINE 27
        if selected == "realtime":
            # SOURCE LINE 28
            __M_writer(u'\t\t\t<li><a class="active" href="/list/realtime">\u76d1\u63a7</a></li>\n')
            # SOURCE LINE 29
        else:
            # SOURCE LINE 30
            __M_writer(u'\t\t\t<li><a href="/list/realtime">\u76d1\u63a7</a></li>\n')
            pass
        # SOURCE LINE 32
        if selected == "devices":
            # SOURCE LINE 33
            __M_writer(u'\t\t\t<li><a class="active" href="/devices">\u4e3b\u673a</a></li>\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer(u'\t\t\t<li><a href="/devices">\u4e3b\u673a</a></li>\n')
            pass
        # SOURCE LINE 37
        __M_writer(u'\t\t\n')
        # SOURCE LINE 38
        if selected == "speed":
            # SOURCE LINE 39
            __M_writer(u'\t\t\t<li><a class="active" href="/speed" style="display:none;">\u901f\u5ea6</a></li>\n')
            # SOURCE LINE 40
        else:
            # SOURCE LINE 41
            __M_writer(u'\t\t\t<li><a href="/speed" style="display:none;">\u901f\u5ea6</a></li>\n')
            pass
        # SOURCE LINE 43
        __M_writer(u'\t\t\n')
        # SOURCE LINE 44
        if selected == "events":
            # SOURCE LINE 45
            __M_writer(u'\t\t\t<li><a class="active" href="/events">\u4e8b\u4ef6</a></li>\n')
            # SOURCE LINE 46
        else:
            # SOURCE LINE 47
            __M_writer(u'\t\t\t<li><a href="/events">\u4e8b\u4ef6</a></li>\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'\t\t\n')
        # SOURCE LINE 50
        if selected == "alert":
            # SOURCE LINE 51
            __M_writer(u'\t\t\t<li><a class="active" href="/alert">\u62a5\u8b66</a></li>\n')
            # SOURCE LINE 52
        else:
            # SOURCE LINE 53
            __M_writer(u'\t\t\t<li><a href="/alert">\u62a5\u8b66</a></li>\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'\t\t\n')
        # SOURCE LINE 56
        if selected == "contacts":
            # SOURCE LINE 57
            __M_writer(u'\t\t\t<li><a class="active" href="/contacts">\u8054\u7cfb\u4eba</a></li>\n')
            # SOURCE LINE 58
        else:
            # SOURCE LINE 59
            __M_writer(u'\t\t\t<li><a href="/contacts">\u8054\u7cfb\u4eba</a></li>\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'\t    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./data/templates/component/search.html.py
##########################################
# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318555661.594269
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/component/search.html'
_template_uri=u'/component/search.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['bar']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,url,mode):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div class="searchwrap">\n\t\t<p style="float:left;line-height:20px;"><input type="checkbox" id="disreflash" style="vertical-align:middle;" name="disrf" />&nbsp;<lable for="disreflash" style="color:#990000;">\u7981\u6b62\u5237\u65b0</lable>&nbsp;</p>\n\t\t<form action="')
        # SOURCE LINE 4
        __M_writer(escape(url))
        __M_writer(u'" class="searchform floatl">\n\t\t\t<input type="hidden" name="')
        # SOURCE LINE 5
        __M_writer(escape(mode))
        __M_writer(u'" value=1 />\n\t\t\t<input type="text" name="s" value="')
        # SOURCE LINE 6
        __M_writer(escape(c.sw))
        __M_writer(u'" class="searchkey" id="searchkey" /> \n\t\t\t<input type="submit" value="\u641c\u7d22" />\n')
        # SOURCE LINE 8
        if c.sw:
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<input type="button" value="\u64a4\u9500" onclick="window.location.href=\'')
            __M_writer(escape(url))
            __M_writer(u'?')
            __M_writer(escape(mode))
            __M_writer(u'\'" /> \n')
            pass
        # SOURCE LINE 11
        __M_writer(u'\t\t</form>\t\t\t\t\n\t\t<p class="hotkey floatl">\n\t\t\t\u70ed\u70b9: \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 14
        __M_writer(escape(mode))
        __M_writer(u'=1&s=dfs">dfs</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 15
        __M_writer(escape(mode))
        __M_writer(u'=1&s=my">my</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 16
        __M_writer(escape(mode))
        __M_writer(u'=1&s=cache">cache</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 17
        __M_writer(escape(mode))
        __M_writer(u'=1&s=500">500</a>\n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 18
        __M_writer(escape(mode))
        __M_writer(u'=1&s=solr">solr</a> \n\t\t</p>\n\t\t<div class="clear"></div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()



##########################################
####file_name: ./ez_setup.py
##########################################
#!python
"""Bootstrap setuptools installation

If you want to use setuptools in your package's setup.py, just include this
file in the same directory with it, and add this to the top of your setup.py::

    from ez_setup import use_setuptools
    use_setuptools()

If you want to require a specific version of setuptools, set a download
mirror, or use an alternate download directory, you can do so by supplying
the appropriate options to ``use_setuptools()``.

This file can also be run as a script to install or upgrade setuptools.
"""
import sys
DEFAULT_VERSION = "0.6c9"
DEFAULT_URL     = "http://pypi.python.org/packages/%s/s/setuptools/" % sys.version[:3]

md5_data = {
    'setuptools-0.6b1-py2.3.egg': '8822caf901250d848b996b7f25c6e6ca',
    'setuptools-0.6b1-py2.4.egg': 'b79a8a403e4502fbb85ee3f1941735cb',
    'setuptools-0.6b2-py2.3.egg': '5657759d8a6d8fc44070a9d07272d99b',
    'setuptools-0.6b2-py2.4.egg': '4996a8d169d2be661fa32a6e52e4f82a',
    'setuptools-0.6b3-py2.3.egg': 'bb31c0fc7399a63579975cad9f5a0618',
    'setuptools-0.6b3-py2.4.egg': '38a8c6b3d6ecd22247f179f7da669fac',
    'setuptools-0.6b4-py2.3.egg': '62045a24ed4e1ebc77fe039aa4e6f7e5',
    'setuptools-0.6b4-py2.4.egg': '4cb2a185d228dacffb2d17f103b3b1c4',
    'setuptools-0.6c1-py2.3.egg': 'b3f2b5539d65cb7f74ad79127f1a908c',
    'setuptools-0.6c1-py2.4.egg': 'b45adeda0667d2d2ffe14009364f2a4b',
    'setuptools-0.6c2-py2.3.egg': 'f0064bf6aa2b7d0f3ba0b43f20817c27',
    'setuptools-0.6c2-py2.4.egg': '616192eec35f47e8ea16cd6a122b7277',
    'setuptools-0.6c3-py2.3.egg': 'f181fa125dfe85a259c9cd6f1d7b78fa',
    'setuptools-0.6c3-py2.4.egg': 'e0ed74682c998bfb73bf803a50e7b71e',
    'setuptools-0.6c3-py2.5.egg': 'abef16fdd61955514841c7c6bd98965e',
    'setuptools-0.6c4-py2.3.egg': 'b0b9131acab32022bfac7f44c5d7971f',
    'setuptools-0.6c4-py2.4.egg': '2a1f9656d4fbf3c97bf946c0a124e6e2',
    'setuptools-0.6c4-py2.5.egg': '8f5a052e32cdb9c72bcf4b5526f28afc',
    'setuptools-0.6c5-py2.3.egg': 'ee9fd80965da04f2f3e6b3576e9d8167',
    'setuptools-0.6c5-py2.4.egg': 'afe2adf1c01701ee841761f5bcd8aa64',
    'setuptools-0.6c5-py2.5.egg': 'a8d3f61494ccaa8714dfed37bccd3d5d',
    'setuptools-0.6c6-py2.3.egg': '35686b78116a668847237b69d549ec20',
    'setuptools-0.6c6-py2.4.egg': '3c56af57be3225019260a644430065ab',
    'setuptools-0.6c6-py2.5.egg': 'b2f8a7520709a5b34f80946de5f02f53',
    'setuptools-0.6c7-py2.3.egg': '209fdf9adc3a615e5115b725658e13e2',
    'setuptools-0.6c7-py2.4.egg': '5a8f954807d46a0fb67cf1f26c55a82e',
    'setuptools-0.6c7-py2.5.egg': '45d2ad28f9750e7434111fde831e8372',
    'setuptools-0.6c8-py2.3.egg': '50759d29b349db8cfd807ba8303f1902',
    'setuptools-0.6c8-py2.4.egg': 'cba38d74f7d483c06e9daa6070cce6de',
    'setuptools-0.6c8-py2.5.egg': '1721747ee329dc150590a58b3e1ac95b',
    'setuptools-0.6c9-py2.3.egg': 'a83c4020414807b496e4cfbe08507c03',
    'setuptools-0.6c9-py2.4.egg': '260a2be2e5388d66bdaee06abec6342a',
    'setuptools-0.6c9-py2.5.egg': 'fe67c3e5a17b12c0e7c541b7ea43a8e6',
    'setuptools-0.6c9-py2.6.egg': 'ca37b1ff16fa2ede6e19383e7b59245a',
}

import sys, os
try: from hashlib import md5
except ImportError: from md5 import md5

def _validate_md5(egg_name, data):
    if egg_name in md5_data:
        digest = md5(data).hexdigest()
        if digest != md5_data[egg_name]:
            print >>sys.stderr, (
                "md5 validation of %s failed!  (Possible download problem?)"
                % egg_name
            )
            sys.exit(2)
    return data

def use_setuptools(
    version=DEFAULT_VERSION, download_base=DEFAULT_URL, to_dir=os.curdir,
    download_delay=15
):
    """Automatically find/download setuptools and make it available on sys.path

    `version` should be a valid setuptools version number that is available
    as an egg for download under the `download_base` URL (which should end with
    a '/').  `to_dir` is the directory where setuptools will be downloaded, if
    it is not already available.  If `download_delay` is specified, it should
    be the number of seconds that will be paused before initiating a download,
    should one be required.  If an older version of setuptools is installed,
    this routine will print a message to ``sys.stderr`` and raise SystemExit in
    an attempt to abort the calling script.
    """
    was_imported = 'pkg_resources' in sys.modules or 'setuptools' in sys.modules
    def do_download():
        egg = download_setuptools(version, download_base, to_dir, download_delay)
        sys.path.insert(0, egg)
        import setuptools; setuptools.bootstrap_install_from = egg
    try:
        import pkg_resources
    except ImportError:
        return do_download()       
    try:
        pkg_resources.require("setuptools>="+version); return
    except pkg_resources.VersionConflict, e:
        if was_imported:
            print >>sys.stderr, (
            "The required version of setuptools (>=%s) is not available, and\n"
            "can't be installed while this script is running. Please install\n"
            " a more recent version first, using 'easy_install -U setuptools'."
            "\n\n(Currently using %r)"
            ) % (version, e.args[0])
            sys.exit(2)
        else:
            del pkg_resources, sys.modules['pkg_resources']    # reload ok
            return do_download()
    except pkg_resources.DistributionNotFound:
        return do_download()

def download_setuptools(
    version=DEFAULT_VERSION, download_base=DEFAULT_URL, to_dir=os.curdir,
    delay = 15
):
    """Download setuptools from a specified location and return its filename

    `version` should be a valid setuptools version number that is available
    as an egg for download under the `download_base` URL (which should end
    with a '/'). `to_dir` is the directory where the egg will be downloaded.
    `delay` is the number of seconds to pause before an actual download attempt.
    """
    import urllib2, shutil
    egg_name = "setuptools-%s-py%s.egg" % (version,sys.version[:3])
    url = download_base + egg_name
    saveto = os.path.join(to_dir, egg_name)
    src = dst = None
    if not os.path.exists(saveto):  # Avoid repeated downloads
        try:
            from distutils import log
            if delay:
                log.warn("""
---------------------------------------------------------------------------
This script requires setuptools version %s to run (even to display
help).  I will attempt to download it for you (from
%s), but
you may need to enable firewall access for this script first.
I will start the download in %d seconds.

(Note: if this machine does not have network access, please obtain the file

   %s

and place it in this directory before rerunning this script.)
---------------------------------------------------------------------------""",
                    version, download_base, delay, url
                ); from time import sleep; sleep(delay)
            log.warn("Downloading %s", url)
            src = urllib2.urlopen(url)
            # Read/write all in one block, so we don't create a corrupt file
            # if the download is interrupted.
            data = _validate_md5(egg_name, src.read())
            dst = open(saveto,"wb"); dst.write(data)
        finally:
            if src: src.close()
            if dst: dst.close()
    return os.path.realpath(saveto)




































def main(argv, version=DEFAULT_VERSION):
    """Install or upgrade setuptools and EasyInstall"""
    try:
        import setuptools
    except ImportError:
        egg = None
        try:
            egg = download_setuptools(version, delay=0)
            sys.path.insert(0,egg)
            from setuptools.command.easy_install import main
            return main(list(argv)+[egg])   # we're done here
        finally:
            if egg and os.path.exists(egg):
                os.unlink(egg)
    else:
        if setuptools.__version__ == '0.0.1':
            print >>sys.stderr, (
            "You have an obsolete version of setuptools installed.  Please\n"
            "remove it from your system entirely before rerunning this script."
            )
            sys.exit(2)

    req = "setuptools>="+version
    import pkg_resources
    try:
        pkg_resources.require(req)
    except pkg_resources.VersionConflict:
        try:
            from setuptools.command.easy_install import main
        except ImportError:
            from easy_install import main
        main(list(argv)+[download_setuptools(delay=0)])
        sys.exit(0) # try to force an exit
    else:
        if argv:
            from setuptools.command.easy_install import main
            main(argv)
        else:
            print "Setuptools version",version,"or greater has been installed."
            print '(Run "ez_setup.py -U setuptools" to reinstall or upgrade.)'

def update_md5(filenames):
    """Update our built-in md5 registry"""

    import re

    for name in filenames:
        base = os.path.basename(name)
        f = open(name,'rb')
        md5_data[base] = md5(f.read()).hexdigest()
        f.close()

    data = ["    %r: %r,\n" % it for it in md5_data.items()]
    data.sort()
    repl = "".join(data)

    import inspect
    srcfile = inspect.getsourcefile(sys.modules[__name__])
    f = open(srcfile, 'rb'); src = f.read(); f.close()

    match = re.search("\nmd5_data = {\n([^}]+)}", src)
    if not match:
        print >>sys.stderr, "Internal error!"
        sys.exit(2)

    src = src[:match.start(1)] + repl + src[match.end(1):]
    f = open(srcfile,'w')
    f.write(src)
    f.close()


if __name__=='__main__':
    if len(sys.argv)>2 and sys.argv[1]=='--md5update':
        update_md5(sys.argv[2:])
    else:
        main(sys.argv[1:])







##########################################
####file_name: ./pyfisheyes/__init__.py
##########################################

##########################################
####file_name: ./pyfisheyes/model/__init__.py
##########################################
"""The application's model objects"""
from pyfisheyes.model.meta import Session, Base

from pyfisheyes.model.fisheyesdb.categories import Categories
from pyfisheyes.model.fisheyesdb.graphs import Graphs
from pyfisheyes.model.fisheyesdb.graphshour import GraphsHour
from pyfisheyes.model.fisheyesdb.graphshost import GraphsHost
from pyfisheyes.model.fisheyesdb.events import Events
from pyfisheyes.model.fisheyesdb.users import Users
from pyfisheyes.model.fisheyesdb.contacts import Contacts
from pyfisheyes.model.fisheyesdb.realtime import Realtime
from pyfisheyes.model.fisheyesdb.logstuff import Logstuff
from pyfisheyes.model.fisheyesdb.alarminfo import Alarminfo
from pyfisheyes.model.fisheyesdb.dateitems import Dateitems
from pyfisheyes.model.fisheyesdb.img_event import ImgEvent
from pyfisheyes.model.fisheyesdb.messages import Messages
from pyfisheyes.model.fisheyesdb.devices import Devices
from pyfisheyes.model.fisheyesdb.chartstyle import ChartStyle
from pyfisheyes.model.fisheyesdb.devicebase import DeviceBase
from pyfisheyes.model.fisheyesdb.deviceitemsets import DeviceItemSets
from pyfisheyes.model.fisheyesdb.deviceitemgroup import DeviceItemGroup
#from pyfisheyes.model.fisheyesdb.devices_realtime import DevicesRealtime
def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

##########################################
####file_name: ./pyfisheyes/model/utils/__init__.py
##########################################

##########################################
####file_name: ./pyfisheyes/model/utils/ContactHandle.py
##########################################
# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh

log = logging.getLogger(__name__)

class ContactHandle():
    
    def __init__(self, request):
        self.r = request
        
        
    def createContact(self):
        p = model.Contacts()
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)        
        return qw
    
    def saveContact(self,id):
        p = model.meta.Session.query(model.Contacts).filter_by(id=id).first()       
        p.eid = self.r.params['contact_eid']
        p.name = self.r.params['contact_name']
        p.ename = self.r.params['contact_ename']
        p.title = self.r.params['contact_title']
        p.subtel = self.r.params['contact_subtel']
        p.mobile = self.r.params['contact_mobile']
        p.email = self.r.params['contact_email']
        p.forsearch = self.r.params['contact_tags'] + ";" + p.eid + ";" + p.name + ";" + p.ename + ";" + p.title \
        + ";" + p.email
        qw = p.eid + ";" + p.name
        qw = qw.encode('utf-8')
        model.meta.Session.add(p)
        model.meta.Session.commit()
        qw = _gh.GlobalHandle(self.r).urlencode(qw)
        return qw
    
            
    
##########################################
####file_name: ./pyfisheyes/model/utils/EventHandle.py
##########################################
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
        e.evtags = self.r.params['event_tags']
        e.evtype = self.r.params['event_type']
        e.evstatus = self.r.params['event_status']
        e.evcause = self.r.params['event_cause']
        e.evminutes = self.r.params['event_minutes']
        e.evlosspv = self.r.params['event_losspv']
        e.evdomain = self.r.params['event_domain']
        gh = _gh.GlobalHandle(self.r)
        e.evreporter = gh.getUID()
        e.evcreatedate = gh.getCurrentDateTime()
        e.evreporterip = gh.getUserRealIP()
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
                 'evtags':e.evtags,
                 'evtype':e.evtype,
                 'evstatus':e.evstatus,
                 'evcause':e.evcause,
                 'evminutes':e.evminutes,
                 'evlosspv':e.evlosspv,
                 'evdomain':e.evdomain,
                 'evcontent':e.evcontent,
                 'evreporter':e.evreporter,
                 'evcreatedate':e.evcreatedate,
                 'evreporterip':e.evreporterip,                 
                 } 
        columns = "evtitle,evdate,dt2,dt3,dt4,evtags,evtype,evstatus,evcause,evminutes,evlosspv,evdomain,evcontent,evreporter,evcreatedate,evreporterip"
        values = ":evtitle,:evdate,:dt2,:dt3,:dt4,:evtags,:evtype,:evstatus,:evcause,:evminutes,:evlosspv,:evdomain,:evcontent,:evreporter,:evcreatedate,:evreporterip"
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
        e.evtags = self.r.params['event_tags']
        e.evtype = self.r.params['event_type']
        e.evstatus = self.r.params['event_status']
        e.evcause = self.r.params['event_cause']
        e.evminutes = self.r.params['event_minutes']
        e.evlosspv = self.r.params['event_losspv']
        e.evdomain = self.r.params['event_domain']
        e.evlasteditor = gh.getUID()
        e.evlastedit = gh.getCurrentDateTime()
        e.evlasteditip = gh.getUserRealIP()
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
##########################################
####file_name: ./pyfisheyes/model/utils/GlobalHandle.py
##########################################
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

##########################################
####file_name: ./pyfisheyes/model/utils/ViewHandle.py
##########################################
# -*- coding: utf-8 -*-

import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
from datetime import datetime, timedelta, date, time 

import time as my_time


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
        r = model.Realtime
        from sqlalchemy import and_
        if date1 == date2:
            rows = model.meta.Session.query(r).filter_by(tid=tid).filter_by(datei=date1).filter(and_(r.logtime >= datetime1, r.logtime <= datetime2)).order_by(r.id.asc())
        else:
            rows = model.meta.Session.query(r).filter_by(tid=tid).filter(and_(r.logtime >= datetime1, r.logtime <= datetime2)).order_by(r.id.asc())
            
        return rows
    
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
            events = model.meta.Session.query(model.Events).filter(model.Events.id.in_(EventsId))
        
        return events
        
        
        
        
          

##########################################
####file_name: ./pyfisheyes/model/utils/WebAPI.py
##########################################
# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model

log = logging.getLogger(__name__)

class WebAPI():
    
    def __init__(self, template,request):
        self.t = template
        self.r = request
        self.date = "1999-01-01"
        self.host = ""
        self.hour = ""
        if "datei" in self.r.POST:
            self.date = self.r.POST['datei']
        if "houri" in self.r.POST:
            self.hour = self.r.POST['houri']
        if "host" in self.r.POST:
            self.host = self.r.POST['host']
        self.templateid = template.typeid
        self.gh = None
        self.message = ""
        log.info("self.date=" + self.date)
        log.info("self.hour=" + self.hour)
        log.info("self.templateid=" + str(self.templateid))
        #model.meta.Session.query(model.GraphsHou).filter_by(datei=self.date).filter_by(template_id=self.templateid).filter_by(houri=self.hour).first()
        
        
    def __CheckFormat__(self):
        items = self.t.items.split(",")
        for item in items:
            if item not in self.r.POST:
                self.message = "INVALID FORMAT"
                return False
            else:
                if self.r.POST[item] == "":
                    self.message = "%s : Content Feed Error" % item
                    return False
        return True

## Hour ##    
    def __isExistHour__(self):
        n = model.meta.Session.query(model.GraphsHour).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).count()
        if n > 0:
            return True
        else:
            return False
    
    def __setMediaData__(self):
        items = self.t.items.split(",")
        self.gh.mediadata = ""
        for item in items:
            if not len(self.gh.mediadata):
                self.gh.mediadata = self.r.POST[item]
            else:
                self.gh.mediadata += "," + self.r.POST[item]
        
    def SaveDataForGraphsHour(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsHourInsert()
        return self.message
    
    def SaveDataForGraphsHourUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.GraphsHour).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsHourInsert(self):
        if not self.__isExistHour__():
            try:
                items = self.t.items.split(",")
                self.gh = model.GraphsHour()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.houri = self.r.POST['houri']
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHourUpdate()                
        return True

## Day ##
    def SaveDataForGraphsDay(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsDayInsert()
        return self.message
    
    def SaveDataForGraphsDayUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.Graphs).filter_by(template_id=self.templateid).filter_by(datei=self.date).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsDayInsert(self):
        if not self.__isExistDay__():
            try:
                items = self.t.items.split(",")
                self.gh = model.Graphs()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']     
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsDayUpdate()                
        return True
    
    def __isExistDay__(self):
        n = model.meta.Session.query(model.Graphs).filter_by(template_id=self.templateid).filter_by(datei=self.date).count()
        if n > 0:
            return True
        else:
            return False
        
## Host ##
    def SaveDataForGraphsHost(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsHostInsert()
        return self.message
    
    def SaveDataForGraphsHostUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.GraphsHost).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(host=self.host).first()
            self.__setMediaData__()
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsHostInsert(self):
        if not self.__isExistHost__():
            try:
                items = self.t.items.split(",")
                self.gh = model.GraphsHost()
                self.gh.template_id = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.host = self.r.POST['host']
                self.__setMediaData__()
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHostUpdate()                
        return True
    
    def __isExistHost__(self):
        n = model.meta.Session.query(model.GraphsHost).filter_by(template_id=self.templateid).filter_by(datei=self.date).filter_by(host=self.host).count()
        if n > 0:
            return True
        else:
            return False
        
## Realtime ##
    def SaveDataForGraphsRealtime(self):
        if self.__CheckFormat__():                
            self.SaveDataForGraphsRealtimeInsert()
        return self.message
    
    def SaveDataForGraphsRealtimeUpdate(self):
        try:      
            self.gh = model.meta.Session.query(model.Realtime).filter_by(tid=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).filter_by(minutei=self.minute).first()
            self.gh.valuei = self.r.POST['value']
            model.meta.Session.add(self.gh)
            model.meta.Session.commit()
        except:
            return False
        return True        
        
    def SaveDataForGraphsRealtimeInsert(self):
        if not self.__isExistHost__():
            try:
                items = self.t.items.split(",")
                self.gh = model.Realtime()
                self.gh.tid = self.templateid
                self.gh.datei = self.r.POST['datei']
                self.gh.houri = self.r.POST['hour']
                self.gh.minutei = self.r.POST['minute']
                self.gh.valuei = self.r.POST['value']
                model.meta.Session.add(self.gh)
                model.meta.Session.commit()
            except:
                return False
        else:
            self.SaveDataForGraphsHostUpdate()                
        return True
    
    def __isExistRealtime__(self):
        n = model.meta.Session.query(model.Realtime).filter_by(tid=self.templateid).filter_by(datei=self.date).filter_by(houri=self.hour).filter_by(minutei=self.minute).count()
        if n > 0:
            return True
        else:
            return False
##########################################
####file_name: ./pyfisheyes/model/utils/DailyReportHandle.py
##########################################
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
        datetime2 = stop_time_point.str
