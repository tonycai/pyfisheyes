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


