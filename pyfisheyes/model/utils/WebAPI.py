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