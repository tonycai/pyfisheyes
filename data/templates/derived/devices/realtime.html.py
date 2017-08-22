# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1322013825.1052489
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/devices/realtime.html'
_template_uri='/derived/devices/realtime.html'
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
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<meta http-equiv="refresh" content="60" />\n<title>report</title>\n<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\n<link href="/css/report.css" rel="stylesheet" type="text/css" />\n<style type="text/css">\n*{\nfont-size:14px;\n}\nimg{\nmargin:5px 0;\n}\n.left{\nfloat:left;\n}\n.left input,.left select{\nfloat:left;\nmargin-left:10px;\ndisplay:inline;\n}\n.right{\nfloat:right\n}\n.right input{\nfloat:left;\nmargin-right:10px;\ndisplay:inline;\n}\n</style>\n</head>\n<body>\n<div style="padding:5px 0px;position:fixed;background-color:#aaa;width:100%;font-size:14px;text-align:center;vertical-align:middle;">\n<div class="left" style="float:left">\n <input id="back" type="button" value=" \u8fd4\u56de " style="float:left"/>\n <select id="items" style="width:100px;float:left;"><option value=\'loadavg\' selected>load</option><option value=\'util\'></>Utilization</option></select>\n <span style="line-height:25px;margin-left:5px;display:inline;color:#fff;"> \u65f6\u95f4\uff1a')
        # SOURCE LINE 39
        __M_writer(escape(c.rtime))
        __M_writer(u'</span>\n</div>\n<div class="right" style="float:right;">\n <input id=\'value\' type="text" value=\'')
        # SOURCE LINE 42
        __M_writer(escape(c.dname))
        __M_writer(u'\' />\n <input id=\'search\' type="button" value=" \u641c\u7d22 "/>\n <input id=\'clear\' type="button" value=" \u6e05\u9664 " style="display:none;"/>\n</div>\n</div>\n<div style="text-align:justify;padding:10px;padding-top:43px;">\n')
        # SOURCE LINE 48
        for x,t in enumerate(c.rows):
            # SOURCE LINE 49
            __M_writer(u'<a href="/devices/deviceItems?dsn=')
            __M_writer(escape(t.dsn))
            __M_writer(u'&dn=')
            __M_writer(escape(t.dname))
            __M_writer(u'#')
            __M_writer(escape(t.id))
            __M_writer(u'" title="')
            __M_writer(escape(t.dname))
            __M_writer(u'"><img id=\'img_')
            __M_writer(escape(x+1))
            __M_writer(u"' src='/devices/realtimeview/")
            __M_writer(escape(t.id))
            __M_writer(u'/')
            __M_writer(escape(t.dname))
            __M_writer(u'/')
            __M_writer(escape(t.ditem))
            __M_writer(u'/')
            __M_writer(escape(t.max_value))
            __M_writer(u"/12.png' /></a>\n")
            pass
        # SOURCE LINE 51
        __M_writer(u'</div>\n<!-- \n<script type="text/Javascript" src="/js/cdjcv.js"></script>\n\n<script>\n// The followings is executed once every second\n\nfunction updateDisplay()\n{\n    if (window.JsChartViewer)\n        for(x=1; x<=')
        # SOURCE LINE 61
        __M_writer(escape(c.total))
        __M_writer(u';x++)\n        JsChartViewer.get(\'img_\'+x).streamUpdate();\n}\nwindow.setInterval("updateDisplay()", 60000);\n</script>\n -->\n <script type="text/javascript" src="/jquery/js/jquery-1.6.2.min.js"></script>\n <script type="text/javascript">\n$(function(){\n$(\'#items\').change(function(){\n    item = $(this).val()\n    location.href="/devices/devicerealtime?hn=')
        # SOURCE LINE 72
        __M_writer(escape(c.dname))
        __M_writer(u'&item="+item\n});\n clear();\n $(\'#items\').val(\'')
        # SOURCE LINE 75
        __M_writer(escape(c.ditem))
        __M_writer(u'\');\n $(\'#search\').click(function(){\n\n\t\tif ($(\'#value\').val())\n\t\tlocation.href="/devices/devicerealtime?item=')
        # SOURCE LINE 79
        __M_writer(escape(c.ditem))
        __M_writer(u'&hn="+$(\'#value\').val()\n\t});\n$(\'#back\').click(function(){\n     location.href="/devices"\n\t\n});\n$(\'#value\').keypress(function(){\n\n\tclear();\n});\n \n});\n\nfunction clear(){\n\n\tif ($(\'#value\').val())\n        $("#clear").show()\n\telse\n\t    $("#clear").hide()\n\t\n}\n </script>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


