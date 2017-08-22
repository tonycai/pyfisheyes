# -*- coding: utf-8 -*-
import logging
from pyfisheyes import model
from pyfisheyes.model.utils import GlobalHandle as _gh
log = logging.getLogger(__name__)

class DeviceHandle():
    
    def __init__(self, request=None):
        self.r = request 
    def searchDevices(self,ds = ''):
        dv = model.DeviceBase
        if ds:
            devices = model.meta.Session.query(dv).filter_by(hostname=ds).order_by(dv.id.desc())
        else:
            devices = model.meta.Session.query(dv).order_by(dv.id.desc())
        return devices 