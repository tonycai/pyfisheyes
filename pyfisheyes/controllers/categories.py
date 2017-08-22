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
