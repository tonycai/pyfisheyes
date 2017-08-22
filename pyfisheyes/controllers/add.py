import logging

from pylons import request, response, session, tmpl_context as c, url

from pyfisheyes.lib.base import BaseController, render

from sqlalchemy import schema, types, Column
from sqlalchemy.engine import create_engine
from sqlalchemy.exc import NoSuchTableError, IntegrityError
from pyfisheyes import model
from sqlalchemy import and_
from sqlalchemy import sql
from sqlalchemy import func
import re
import json
log = logging.getLogger(__name__)

class AddController(BaseController):
    def index(self):
        if 'ditem' in request.params and 'dtype' in request.params:
            ditem = request.params['ditem']
            dtype = request.params['dtype']
        else:
            return 'error'
        if dtype == '1':
            dname = request.params['dname']
            dsn = request.params['dsn']
            odatetime = request.params['odatetime']
            ovalue = request.params['ovalue']
            p = re.compile('^[0-9]+$')
            odate = ''.join(odatetime[0:10].split('-'))
            otime = ''.join(odatetime[11:16].split(':'))
            if ovalue:
                if p.match(ovalue):
                    pass
                else:
                    return "value is not a number"
                oid = self.device_check(dname, ditem, dsn)
                if oid:
                    device_realtime = creat_d_table(odate)
                    model.meta.Session.bind.execute(device_realtime.insert(),did=oid,dtvalue=ovalue,dthour=int(otime))
                    
        if dtype == '2':
            try:
                '''
                ditem_list = ditem.split('/')
                
                for x in ditem_list:
                    insert_values = []
                    x = json.loads(x)
                    insert_value = {}
                    
                    if 'hn' in x and 'dt' in x and 'sn' in x:
                        dname = x['hn']
                        del x['hn']
                        odatetime = x['dt']
                        del x['dt']
                        dsn = x['sn']
                        del x['sn']
                        insert_values.append(x)
                    else:
                        return 'error'
                    
                    
                    
                    
                    
                for t in new_ditem_list:
                    for key in t:
                        insert_val = {}
                        ids = model.meta.Session.query(model.Devices.id).filter(and_(model.Devices.ditem==key,model.Devices.dname==dname, model.Devices.dsn==dsn)).first()
                        if ids:
                            oid = ids[0]
                        else:
                            d = model.Devices()
                            d.dname = dname
                            d.ditem = key
                            d.dsn = dsn
                            d_dict = {"dname":d.dname, "ditem":d.ditem, "dsn":d.dsn}
                            columns = "dname,ditem,dsn"
                            values = ":dname,:ditem,:dsn"
                            result = model.meta.Session.execute("insert into devices("+columns+") values("+values+");"
                                                        ,d_dict, mapper=model.Devices)
                            oid = result.lastrowid
                        insert_val['did'] = oid
                        insert_val['dthour'] = int(otime)
                        insert_val['dtvalue'] = t[key]
                        insert_values.append(insert_val)
                odate = ''.join(odatetime[0:10].split('-')) 
                ''' 
                insert_list = []
                val_list = ditem.split('/')
                odatetime = json.loads(val_list[0])['dt']
                odate = ''.join(odatetime[0:10].split('-'))
                log.info(odate)
                device_realtime = self.creat_d_table(odate)
                for x in val_list:
                    insert_vals_1 = []
                    vals = json.loads(x)
                    hostname = vals['hn']
                    del vals['hn']
                    odatetime = vals['dt']
                    del vals['dt']
                    dsn = vals['sn']
                    del vals['sn']
                    otime = ''.join(odatetime[11:16].split(':'))
                    for key in vals:
                        insert_val={}
                        oid = self.device_check(hostname, key, dsn)
                        insert_val['did'] = oid
                        insert_val['dtvalue'] = vals[key]
                        insert_val['dthour'] = int(otime)
                        insert_vals_1.append(insert_val)
                    insert_list=insert_list + insert_vals_1 
                try:
                    log.info(insert_list)
                    model.meta.Session.bind.execute(device_realtime.insert(),insert_list)
                except IntegrityError:
                    pass        
            except Exception,e:
                log.error(e)
                log.error(ditem)
    def device_check(self,dname,ditem,dsn):
        if dname and ditem and dsn:
            ids = model.meta.Session.query(model.Devices.id).filter(and_(model.Devices.ditem==ditem,model.Devices.dname==dname, model.Devices.dsn==dsn)).first()
            if ids:
                oid = ids[0]
            else:
                d = model.Devices()
                d.dname = dname
                d.ditem = ditem
                d.dsn = dsn
                d_dict = {"dname":d.dname, "ditem":d.ditem, "dsn":d.dsn}
                columns = "dname,ditem,dsn"
                values = ":dname,:ditem,:dsn"
                result = model.meta.Session.execute("insert into devices("+columns+") values("+values+");"
                                            ,d_dict, mapper=model.Devices)
                oid = result.lastrowid
            return oid
        else:
            log.info("dname,ditem,dsn not value")
            return 0
        
        
    def creat_d_table(self,odate):
        otable = "device_realtime_"+odate
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
      
        device_realtime = schema.Table(otable, metadata)
        et = device_realtime.exists(bind=model.meta.Session.bind)
        if not et:
            device_realtime = schema.Table(otable, metadata,
                                        Column('id', types.Integer, primary_key = True, autoincrement = True),
                                        Column('did', types.Integer, primary_key = True),
                                        Column('dthour', types.Integer, primary_key = True),
                                        Column('dtvalue', types.Integer),
                                        schema.UniqueConstraint("did","dthour"),
                                        useexisting = True
                                        )
            device_realtime.create()
        else:
            device_realtime.get_children(column_collections=True,schema_visitor=True)
        return device_realtime
    def addrealtime(self):
        values = request.params['values']
        
        values = json.loads(values)
        tid = str(values['tid'])
        datei = str(values['datei'])
        houri= str(values['houri'])
        minutei = str(values['minutei'])
        valuei = str(values['valuei'])
        logtime = str(values['logtime'])
        odate = ''.join(values['datei'].split('-'))
        otable = "realtime_"+odate
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        try: 
            realtime = schema.Table(otable, metadata, autoload=True)
            realtime.insert().execute(tid=int(tid), datei =datei, houri=int(houri),minutei=int(minutei),valuei = int(valuei),logtime=logtime)
        except NoSuchTableError:
            realtime = schema.Table(otable, metadata,
                                        Column('id', types.Integer(11),autoincrement = True, primary_key = True),
                                        Column('tid', types.Integer, default = 0),
                                        Column('datei', types.Date, default = "0000-00-00"),
                                        Column('houri', types.Integer(2)),
                                        Column('minutei', types.Integer(2)),
                                        Column('valuei', types.Integer),
                                        Column('logtime', types.DateTime, default = "0000-00-00 00:00:00"),
                                        Column('ts', types.TIMESTAMP),
                                        schema.UniqueConstraint("tid","datei","houri","minutei"),
                                        )
            schema.Index('logtime',realtime.c.logtime)
            realtime.create()
            #realtime = schema.Table(otable, metadata, autoload=True)
            realtime.insert().execute(tid=int(tid), datei =datei, houri=int(houri),minutei=int(minutei),valuei = int(valuei),logtime=logtime)
            
    def v_add(self):
        insert_list = []
        vals = request.params['vals']
        val_list = vals.split('/')
        odatetime = json.loads(val_list[0])['dt']
        odate = ''.join(odatetime[0:10].split('-'))
        log.info(odate)
        otable = self.create_v_device_table(odate)
        log.info(type(otable))
        for x in val_list:
            insert_vals_1 = []
            vals = json.loads(x)
            hostname = vals['hn']
            del vals['hn']
            odatetime = vals['dt']
            del vals['dt']
            otime = ''.join(odatetime[11:16].split(':'))
            for key in vals:
                insert_val={}
                exist = model.meta.Session.query(model.V_Devices.id).filter(and_(model.V_Devices.dname==hostname,model.V_Devices.ditem==key)).first()
                if not exist:
                    d = model.V_Devices()
                    d.dname = hostname
                    d.ditem = key
                    v_d_dict = {
                                "dname":d.dname,
                                "ditem":d.ditem
                                }
                    columns = "dname,ditem"
                    values = ":dname,:ditem"
                    result = model.meta.Session.execute("insert into v_devices("+columns+") values("+values+");"
                                                , v_d_dict, mapper=model.V_Devices)
                    lid = result.lastrowid
                else:
                    lid = exist[0] 
                insert_val['did'] = lid
                insert_val['dtvalue'] = vals[key]
                insert_val['dthour'] = int(otime)
                insert_vals_1.append(insert_val)
            insert_list=insert_list + insert_vals_1 
        try:
            log.info(insert_list)
            model.meta.Session.bind.execute(otable.insert(),insert_list)
        except IntegrityError:
            pass        
        '''        
                
                
                
        log.info('++++++++++++++++++++')
        log.info(new_list)
        v_devices = model.V_Devices
        
        insert_vals = []
        insert_val = {}
        for x in new_list:
            for key in x:
                exist = model.meta.Session.query(v_devices.id).filter(and_(v_devices.dname==hostname,v_devices.ditem==key)).first()
                if not exist:
                    d = model.V_Devices()
                    d.dname = hostname
                    d.ditem = key
                    v_d_dict = {
                                "dname":d.dname,
                                "ditem":d.ditem
                                }
                    columns = "dname,ditem"
                    values = ":dname,:ditem"
                    result = model.meta.Session.execute("insert into v_devices("+columns+") values("+values+");"
                                                , v_d_dict, mapper=model.V_Devices)
                    lid = result.lastrowid
                else:
                    lid = exist[0]
                insert_val['did'] = int(lid)
                insert_val['dtvalue'] = x[key]
                insert_val['dthour'] = int(otime)
            #device_realtime = schema.Table(otable, metadata, autoload=True)
            
            
                insert_vals.append(insert_val)
        #conn = engine.connect()
        ins = 
        log.info("++++++++++++++++++++++")
        log.info(insert_vals)
        '''
        #realtime.insert().execute(did=int(lid), dthour=int(otime), dtvalue=int(vals[key]))
        return "OK"
    def create_v_device_table(self,odate):
        otable = "v_device_realtime_"+odate
        metadata = model.meta.Base.metadata
        metadata.bind = model.meta.Session.bind
        realtime = schema.Table(otable, metadata)
        et = realtime.exists(bind=model.meta.Session.bind)
        log.info('++++++++++++++++++++++++++')
        log.info(et)
        if not et:
            realtime = schema.Table(otable, metadata,
                                        Column('id', types.Integer, primary_key = True, autoincrement = True),
                                        Column('did', types.Integer,primary_key = True),
                                        Column('dthour', types.Integer,primary_key = True),
                                        Column('dtvalue', types.Integer),
                                        schema.UniqueConstraint("did","dthour"),
                                        useexisting=True
                                        )
            realtime.create()
        else:
            realtime.get_children(column_collections=True,schema_visitor=True)
        return realtime  
            
            
            
        
         