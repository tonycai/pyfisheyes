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


