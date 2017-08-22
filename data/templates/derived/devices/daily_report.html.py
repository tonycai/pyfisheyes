# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1322013869.0423911
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
            __M_writer(escape(c.info['hostname']))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'\t\t\t</span>\n\t\t</p>\n\t\t<div class="main">\n\t\t\t<div class="main_left devicechartlist" id="chartwrap">\n\t\t\t<div class=\'deviceinfo\' style="position:relative">\n\t\t\t\n\t\t\t        <table cellspacing=0 cellpadding = 0 border =0 id="deviceinfo" style="display:none;">\n\t\t\t        \n\t\t\t        <tr><th>\u4e3b\u673a\u540d\uff1a</th><td>')
        # SOURCE LINE 49
        __M_writer(escape(c.info['hostname']))
        __M_writer(u'</td><th>IP\uff1a</th><td><a style=\'color:red;\' href="http://')
        __M_writer(escape(c.info['inetaddr'][0]))
        __M_writer(u':27012/shockwave?f=html">')
        __M_writer(escape(c.info['inetaddr'][0]))
        __M_writer(u'</a></td></tr>\n\t\t\t        <tr><th>CPU\uff1a</th><td>')
        # SOURCE LINE 50
        __M_writer(escape(c.info['cpuinfo']))
        __M_writer(u'</td><th>\u5185\u5b58\uff1a</th><td>')
        __M_writer(escape(c.info['memsize']))
        __M_writer(u'</td></tr>\n\t\t\t        <tr><th>\u578b\u53f7\uff1a</th><td>')
        # SOURCE LINE 51
        __M_writer(escape(c.info['hardware']))
        __M_writer(u'</td><th>\u78c1\u76d8\uff1a</th><td>')
        __M_writer(escape(c.info['diskspace']))
        __M_writer(u'</td></tr>\n\t\t\t        <tr><th>\u5185\u6838\uff1a</th><td>')
        # SOURCE LINE 52
        __M_writer(escape(c.info['kernel_info']))
        __M_writer(u'</td><th>\u6240\u6709\u8005\uff1a</th>\n\t\t\t        <td>\n')
        # SOURCE LINE 54
        if c.info['customer']:
            # SOURCE LINE 55
            __M_writer(u"\t\t\t        <span id='customer'>")
            __M_writer(escape(c.info['customer']))
            __M_writer(u"</span> <span id='customerEdit' style='text-decoration:underline;color:#ccc;cursor:pointer'>\u70b9\u51fb\u4fee\u6539</span></td>\n")
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u"\t\t\t        <span id='customerEdit' style='text-decoration:underline;color:#ccc;cursor:pointer'>\u70b9\u51fb\u6dfb\u52a0</span>\n")
            pass
        # SOURCE LINE 59
        __M_writer(u"\t\t\t        </tr>\n\t\t\t        <tr><th>\u5907\u6ce8\uff1a</th>\n\t\t\t        \n\t\t\t        <td colspan='3'>\n")
        # SOURCE LINE 63
        if c.info['notes']:
            # SOURCE LINE 64
            __M_writer(u"\t\t\t        \n\t\t\t        <span id='notes'>")
            # SOURCE LINE 65
            __M_writer(escape(c.info['notes']))
            __M_writer(u"</span> <span id='notesEdit' style='text-decoration:underline;color:#ccc;cursor:pointer'>\u70b9\u51fb\u4fee\u6539</span>\n")
            # SOURCE LINE 66
        else:
            # SOURCE LINE 67
            __M_writer(u"\t\t\t        <span id='notesEdit' style='text-decoration:underline;color:#ccc;cursor:pointer'>\u70b9\u51fb\u6dfb\u52a0</span>\n")
            pass
        # SOURCE LINE 69
        __M_writer(u'\t\t\t        </td></tr>\n\t\t\t        </table>\n\t\t\t        <button id="slide" type=\'button\' style="cursor:pointer;position:absolute;top:0;right:0;width:16px;height:16px;padding:0;margin:0;background:url(\'/img/Arrow down.png\') no-repeat 0 0 transparent;border:0;"></button>\n\t\t\t</div>\n')
        # SOURCE LINE 73
        if c.pagename == 'deviceitems':
            # SOURCE LINE 74
            __M_writer(u'\t\t\t\n')
            # SOURCE LINE 75
            for x,t in enumerate(c.rows):
                # SOURCE LINE 76
                if c.rows[x]:
                    # SOURCE LINE 77
                    __M_writer(u'\t\t\t\t\t\t<dl class="dl1 floatl" id="')
                    __M_writer(escape(t.id))
                    __M_writer(u'">\n\t\t\t\t\t\t\t<dt>')
                    # SOURCE LINE 78
                    __M_writer(escape(x+1))
                    __M_writer(u') ')
                    __M_writer(escape(t.ditem))
                    __M_writer(u'</dt>\n\t\t\t\t\t\t\t<dd class="dd2 floatl">\n\t\t\t\t\t\t\t\t<img id=\'img_')
                    # SOURCE LINE 80
                    __M_writer(escape(x+1))
                    __M_writer(u'\' src="/devices/viewData/')
                    __M_writer(escape(t.id))
                    __M_writer(u'/')
                    __M_writer(escape(c.items[x]))
                    __M_writer(u'/')
                    __M_writer(escape(t.dname))
                    __M_writer(u'/')
                    __M_writer(escape(c.date))
                    __M_writer(u'/11.png" />\n\t\t\t\t\t\t\t\t<a class=\'cmp\' href="/devices/cmpItem?id=')
                    # SOURCE LINE 81
                    __M_writer(escape(t.id))
                    __M_writer(u'&item=')
                    __M_writer(escape(c.items[x]))
                    __M_writer(u'&d=')
                    __M_writer(escape(c.date))
                    __M_writer(u'&sn=')
                    __M_writer(escape(c.info['serial_no']))
                    __M_writer(u'&dn=')
                    __M_writer(escape(c.info['hostname']))
                    __M_writer(u'" title="\u5bf9\u6bd4"></a>\n\t\t\t\t\t\t\t\t<a class=\'top\' href="#" title="\u9876\u90e8"></a>\n\t\t\t\t\t\t\t</dd>\t\n\t\t\t\t\t\t</dl>\n')
                    pass
                pass
            pass
        # SOURCE LINE 88
        if c.pagename == 'cmpitem':
            # SOURCE LINE 89
            for x in c.dds:
                # SOURCE LINE 90
                __M_writer(u'\t\t\t\t\t\n\t\t\t\t\t\t<dl class="dl1 floatl" >\n\t\t\t\t\t\t\t<dt>')
                # SOURCE LINE 92
                __M_writer(escape(x))
                __M_writer(u'</dt>\n\t\t\t\t\t\t\t<dd class="dd2 floatl">\n\t\t\t\t\t\t\t\t<img src="/devices/viewData/')
                # SOURCE LINE 94
                __M_writer(escape(c.id))
                __M_writer(u'/')
                __M_writer(escape(c.item))
                __M_writer(u'/')
                __M_writer(escape(c.info['hostname']))
                __M_writer(u'/')
                __M_writer(escape(x))
                __M_writer(u'/11.png" />\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t</dd>\t\n\t\t\t\t\t\t</dl>\n\n')
                pass
            pass
        # SOURCE LINE 101
        __M_writer(u'\t\t\t</div><!-- end main_left -->\n\t\t\t\n\t\t\t<div class="main_right">\n')
        # SOURCE LINE 104
        if c.pagename == 'deviceitems':
            # SOURCE LINE 105
            __M_writer(u'\t\t\t\t\n\t\t\t\t<div class="slidebar">\t\n\t\t\t\t\t\t<h3 class="sbartitle">\u5feb\u901f\u641c\u7d22</h3>\t\n\t\t\t\t\t\t<form action="/devices" method="get">\t\t\n\t\t\t\t\t\t<input type="text" name="ds" value="" />\t\t\n\t\t\t\t\t\t<input type="submit" value="Go" />\n\t\t\t\t\t\t</form>\n\t\t\t\t</div>\n\t\t\t\t<div class="slidebar">\t\n\t\t\t\t\t\t<h3 class="sbartitle">\u5de5\u5177\u680f</h3>\n\t\t\t\t\t\t<ul class="sbarlist">\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t<li><a target=\'_blank\' href="/devices/devicerealtime">\u96f7\u8fbeII</a></li>\n\t\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t\t\n')
            pass
        # SOURCE LINE 122
        __M_writer(u'\t\t\t\t<div class="slidebar datepicker">\n\t\t\t\t\t<div id="datepicker"></div>\n\t\t\t\t\t<input type="hidden" id="actualDate" />\n')
        # SOURCE LINE 125
        if hasattr(c,'kw'):
            # SOURCE LINE 126
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="kw" value="')
            __M_writer(escape(c.kw))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 128
        if hasattr(c,'info'):
            # SOURCE LINE 129
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="dsn" value="')
            __M_writer(escape(c.info['serial_no']))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 131
        if hasattr(c,'info'):
            # SOURCE LINE 132
            __M_writer(u'\t\t\t\t\t\t<input type="hidden" name="kw" id="dn" value="')
            __M_writer(escape(c.info['hostname']))
            __M_writer(u'">\n')
            pass
        # SOURCE LINE 134
        __M_writer(u'\t\t\t\t</div>\n')
        # SOURCE LINE 135
        if c.pagename == 'deviceitems':
            # SOURCE LINE 136
            __M_writer(u'\t\t\t  <div class="slidebar">\t\n\t\t\t\t\t\t<h3 class="sbartitle">\u5feb\u901f\u5b9a\u4f4d</h3>\n\t\t\t\t\t\t<ul class="sbarlist">\n')
            # SOURCE LINE 139
            for x,t in enumerate(c.rows):
                # SOURCE LINE 140
                if c.rows[x]:
                    # SOURCE LINE 141
                    __M_writer(u'\t\t\t\t\t\t\t<li><a href="#')
                    __M_writer(escape(t.id))
                    __M_writer(u'">')
                    __M_writer(escape(t.ditem))
                    __M_writer(u'</a></li>\n')
                    pass
                pass
            # SOURCE LINE 144
            __M_writer(u'\t\t\t\t\t\t</ul>\n\t\t\t\t</div>\n\t\t\t   \n')
            pass
        # SOURCE LINE 148
        __M_writer(u'\t\t\t</div><!-- end main_right -->\n\t\t</div><!-- end main -->\n\t</div><!-- end wrap -->\n<script type="text/javascript" src="/jquery/js/jquery-1.4.4.min.js"></script>\n<script type="text/javascript" src="/jquery/js/jquery-ui-1.8.8.custom.min.js"></script>\n<script type="text/javascript" src="/js/CJL.0.1.min.js"></script>\n<script type="text/javascript" src="/js/LazyLoad.js"></script>\n<script type="text/javascript" src="/js/lazyLoadImg.js"></script>\n')
        # SOURCE LINE 156
        if c.pagename == 'deviceitems':
            # SOURCE LINE 157
            __M_writer(u'<script type="text/Javascript" src="/js/cdjcv.js"></script>\n\n<script>\n// \u5b9e\u66f4\u65b0\u56fe\u7247\uff0c\u4e00\u5206\u949f\u66f4\u65b0\u4e00\u6b21\nfunction updateDisplay()\n{\n    if (window.JsChartViewer)\n        for(x=1; x<=')
            # SOURCE LINE 164
            __M_writer(escape(c.total))
            __M_writer(u';x++)\n        JsChartViewer.get(\'img_\'+x).streamUpdate();\n}\nwindow.setInterval("updateDisplay()", 60000);\n</script>\n')
            pass
        # SOURCE LINE 170
        __M_writer(u'<script type="text/javascript">\n$(function(){\n\tvar oDate\n\tvar defaultdate = "')
        # SOURCE LINE 173
        __M_writer(escape(c.date))
        __M_writer(u'"\n\tvar kw = \'\'\n\tvar dns=\'\'\n\tvar dn=\'\'\n\tif (document.getElementById("kw"))\n\t\tkw = $("#kw").val()\n\tif (document.getElementById("dsn"))\n\t\tdsn = $("#dsn").val()\n\tif (document.getElementById("dn"))\n\t\tdn = $("#dn").val()\n\t\n\t$( "#datepicker" ).datepicker({\n\t\taltFormat: \'yy-mm-dd\',\n\t\taltField: \'#actualDate\',\n\t\tonSelect: function(dateText, inst) { \n\t\t\t\toDate = $("#actualDate").val();\n\t\t\t\tif(kw)\n\t\t\t\t\tlocation.href = "/devices/deviceItems?kw="+kw+"&d="+oDate;\n\t\t\t\t\t\n\t\t\t\telse\n\t\t\t\t\tlocation.href = "/devices/deviceItems?dsn="+dsn+"&dn="+dn+"&d="+oDate;\n\t\t\t\t    \n\t\t},\n\t\tdateFormat: \'yy-mm-dd\',\n\t\tdefaultDate:defaultdate\n\t\t\n\t});\n\t$("#slide").toggle(function(){\n\t\t\t\t$(\'#deviceinfo\').fadeIn()\n\t\t\t\t$(this).css("background-image","url(\'/img/Arrow up.png\')")\n\t\t},function(){\n\t\t\t\t\n\t\t\t\t$(\'#deviceinfo\').fadeOut()\n\t\t\t\t$(this).css("background-image","url(\'/img/Arrow down.png\')")\n\t\t});\n\t// \u4fee\u6539\u5907\u6ce8\n\t$(\'#notesEdit\').live(\'click\',function(){\n\t\ttextvalue = $(\'#notes\').text()\n\t\t$(this).before("<textarea id=\'addnotes\' style=\'width:70%;height:50px;\'>"+textvalue+"</textarea>")\n\t\t$(\'#notes\').remove();\n\t\t$(this).remove();\n\t\t$(\'#addnotes\').focus();\n\t});\n\t$(\'#addnotes\').live(\'blur\',function(){\n\t\tva = $(this).val()\n\t\ttd = $(this).parent(\'td\')\n\t\tif(va != \'\'){\n\t\t\t  \n\t\t\t$.ajax({\n\t\t\t\t\turl:"/devices/editdeviceinfo",\n\t\t\t\t\tdata:"sn=')
        # SOURCE LINE 223
        __M_writer(escape(c.info['serial_no']))
        __M_writer(u'&notes="+va,\n\t\t\t\t\tsuccess:function(html){\n\t\t\t\t\t\tif(html)\n\t\t\t\t\t\t{ \n\t\t\t\t\t\t\t$(td).append("<span id=\'notes\'>"+html+"</span> <span id=\'notesEdit\' style=\'text-decoration:underline;color:#ccc;cursor:pointer\'>\u70b9\u51fb\u4fee\u6539</span>")\t\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\n\t\t\t\t   });\n\t\t}\n\t\telse{\n\t\t\t\t$(this).before("<span id=\'notesEdit\' style=\'text-decoration:underline;color:#ccc;cursor:pointer\'>\u70b9\u51fb\u6dfb\u52a0</span>")\n\t\t\t}\n\t\t$(this).remove()\n\n\t\t\n     });\n\t//\u4fee\u6539\u6240\u6709\u8005\n\t$(\'#customerEdit\').live(\'click\',function(){\n\t\ttextvalue = $(\'#customer\').text()\n\t\t$(this).before("<input type=\'text\' value=\'"+textvalue+"\' id=\'addcustomer\' />")\n\t\t$(\'#customer\').remove()\n\t\t$(this).remove();\n\t\t$(\'#addcustomer\').focus()\n\t});\n\t$(\'#addcustomer\').live(\'blur\',function(){\n\t\tva = $(this).val()\n\t\ttd = $(this).parent(\'td\')\n\t\tif(va != \'\'){\n\t\t\t  \n\t\t\t$.ajax({\n\t\t\t\t\turl:"/devices/editdeviceinfo",\n\t\t\t\t\tdata:"sn=')
        # SOURCE LINE 255
        __M_writer(escape(c.info['serial_no']))
        __M_writer(u'&customer="+va,\n\t\t\t\t\tsuccess:function(html){\n\t\t\t\t\t\tif(html)\n\t\t\t\t\t\t{ \n\t\t\t\t\t\t\t$(td).append("<span id=\'customer\'>"+html+"</span> <span id=\'customerEdit\' style=\'text-decoration:underline;color:#ccc;cursor:pointer\'>\u70b9\u51fb\u4fee\u6539</span>")\t\n\t\t\t\t\t\t}\n\t\t\t\t\t}\n\t\t\n\t\t\t\t   });\n\t\t}\n\t\telse{\n\t\t\t\t$(this).before("<span id=\'customerEdit\' style=\'text-decoration:underline;color:#ccc;cursor:pointer\'>\u70b9\u51fb\u6dfb\u52a0</span>")\n\t\t\t}\n\t\t$(this).remove()\n\n\t\t\n     });\n    \n});\n</script>\t\n</body>\n</html>\n\n\n\n')
        # SOURCE LINE 288
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
        # SOURCE LINE 280
        __M_writer(u'\n    <div class="welcome">\n')
        # SOURCE LINE 282
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 283
            __M_writer(u'\t  \t\t<a href="/signin" class="login">\u767b\u5f55</a>\n')
            # SOURCE LINE 284
        else:
            # SOURCE LINE 285
            __M_writer(u'\t  \t\t\u4f60\u597d\uff0c')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u' <a href="/signout">\u9000\u51fa</a> | <a href="/template">\u914d\u7f6e</a> \n')
            pass
        # SOURCE LINE 287
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


