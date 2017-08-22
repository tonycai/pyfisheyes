# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1322205501.2692111
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
        __M_writer(u'<style type="text/css">\n*html,*html body{background-image:url(about:blank);background-attachment:fixed;}\n\n*html .clickbar{position:absolute;right:auto;left:expression(eval(document.documentElement.scrollLeft+document.documentElement.clientWidth-this.offsetWidth)-(parseInt(this.currentStyle.marginLeft,10)||0)-(parseInt(this.currentStyle.marginRight,10)||0));}\n.alert{\nbackground-color:yellow;\n}\n</style>\n<script src="/jquery/js/jquery-1.4.4.min.js" type="text/javascript"></script>\n<script src="/js/CJL.0.1.min.js"></script>\n<script src="/js/LazyLoad.js"></script>\n<script src="/js/lazyLoadImg.js"></script>\n<script src="/js/jquery.cookie.js"></script>\n</head> \n<body>\n<div class="clickbar" id="oClick">\u70b9\u51fb\u663e\u793a</div>\n<div class="wrap">\n\t\n\t<div id="rtimeHeader" style="padding-top:5px;display:none;">\n\t\t<div class="top">\n\t\t\t<p class="navbar">\n\t\t\t\t<a href="/">\u9996\u9875</a>\n\t\t\t\t<a href="/list/day">\u6bcf\u5929</a>\n\t\t\t\t<a href="/list/hour">\u5c0f\u65f6</a>\n\t\t\t\t<a href="/list/host">\u5206\u7ec4</a>\n\t\t\t\t<a href="/list/realtime">\u76d1\u63a7</a>\n\t\t\t\t<a href="/devices">\u4e3b\u673a</a>\n\t\t\t\t<a href="/events">\u4e8b\u4ef6</a>\n\t\t\t\t<a href="/alert">\u62a5\u8b66</a>\n\t\t\t\t<a href="/contacts">\u8054\u7cfb\u4eba</a>\n\t\t\t\t<a href="#" onclick="javascript:void(0);">\u8fc7\u6ee4</a>\t\n\t\t\t</p>\n\t\t\t<span class="updatetime">\u66f4\u65b0: ')
        # SOURCE LINE 50
        __M_writer(escape(c.currentdatetime))
        __M_writer(u'</span><span class="updatetime">\u5171\u8ba1: ')
        __M_writer(escape(c.count))
        __M_writer(u'\u6761</span>\n\t\t\t<!-- \u5934\u90e8\u641c\u7d22\u6846 -->\n\t\t\t')
        # SOURCE LINE 52
        __M_writer(escape(search.bar("/list/realtime", c.view_mode)))
        __M_writer(u'\n\t\t</div>\n\t\t<div class="checkwrap">\n')
        # SOURCE LINE 55
        for typecode_k, typecode_v in c.r_typecode.iteritems():
            # SOURCE LINE 56
            if typecode_v in c.filter_list:
                # SOURCE LINE 57
                __M_writer(u'\t\t\t\t\t<input type="checkbox" name="filter" id="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'"  value="')
                __M_writer(escape(typecode_v))
                __M_writer(u'" checked="checked"/><label for="filter_')
                __M_writer(escape(typecode_v))
                __M_writer(u'">')
                __M_writer(escape(typecode_k))
                __M_writer(u'</label>\n')
                # SOURCE LINE 58
            else:
                # SOURCE LINE 59
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
        # SOURCE LINE 62
        __M_writer(u'\t\t</div>\n\t</div>\n\t<div class="chartwrap">\n\t\t<ul class="chartlist" id="chartlist">\n')
        # SOURCE LINE 66
        for x,t in enumerate(c.rows):
            # SOURCE LINE 67
            if t.alertlevel == 2 and t.r_weight > 5:
                # SOURCE LINE 68
                __M_writer(u'\t\t\t<li>\n\t\t\t\t<p class="chatname alert">\n\t\t\t\t\t\t<span class="sn">#')
                # SOURCE LINE 70
                __M_writer(escape(t.typeid))
                __M_writer(u'</span>\n')
                # SOURCE LINE 71
                if c.sw:
                    # SOURCE LINE 72
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.search_highlight(c.sw)))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 73
                else:
                    # SOURCE LINE 74
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.typename))
                    __M_writer(u'</span>\n')
                    pass
                # SOURCE LINE 76
                __M_writer(u'\t\t\t\t</p>\n\t\t\t\t<div class="imgbox">\n\t\t\t\t\t<a href="/view/data/')
                # SOURCE LINE 78
                __M_writer(escape(t.typeid))
                __M_writer(u'?s=')
                __M_writer(escape(c.sw))
                __M_writer(u'">\n\t\t\t\t\t\n\t\t\t\t\t<!-- <img alt="')
                # SOURCE LINE 80
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(h.url_for('/view/realtimegraph/'+str(t.typeid),host='')))
                __M_writer(u'/1.png"/>  -->\n\t\t\t\t\t\n\t\t\t\t\t<img class="alert" alt="')
                # SOURCE LINE 82
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/realtimegraph/')
                __M_writer(escape(t.typeid))
                __M_writer(u'/1.png"/>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t</li>\n')
                pass
            pass
        # SOURCE LINE 88
        for x,t in enumerate(c.rows):	
            # SOURCE LINE 89
            if t.alertlevel !=2 or t.r_weight <= 5:
                # SOURCE LINE 90
                __M_writer(u'\t\t\t<li>\n\t\t\t\t<p class="chatname">\n\t\t\t\t\t\t<span class="sn">#')
                # SOURCE LINE 92
                __M_writer(escape(t.typeid))
                __M_writer(u'</span>\n')
                # SOURCE LINE 93
                if c.sw:
                    # SOURCE LINE 94
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.search_highlight(c.sw)))
                    __M_writer(u'</span>\n')
                    # SOURCE LINE 95
                else:
                    # SOURCE LINE 96
                    __M_writer(u'\t\t\t\t\t\t\t<span class="sn2">')
                    __M_writer(escape(t.typename))
                    __M_writer(u'</span>\n')
                    pass
                # SOURCE LINE 98
                __M_writer(u'\t\t\t\t</p>\n\t\t\t\t<div class="imgbox">\n\t\t\t\t\t<a href="/view/data/')
                # SOURCE LINE 100
                __M_writer(escape(t.typeid))
                __M_writer(u'?s=')
                __M_writer(escape(c.sw))
                __M_writer(u'">\n\t\t\t\t\t\n\t\t\t\t\t<!-- <img alt="')
                # SOURCE LINE 102
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(h.url_for('/view/realtimegraph/'+str(t.typeid),host='')))
                __M_writer(u'/1.png"/>  -->\n\t\t\t\t\t\n\t\t\t\t\t<img alt="')
                # SOURCE LINE 104
                __M_writer(escape(t.typename))
                __M_writer(u'" _lazysrc="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/realtimegraph/')
                __M_writer(escape(t.typeid))
                __M_writer(u'/1.png"/>\n\t\t\t\t\t</a>\n\t\t\t\t</div>\n\t\t\t</li>\n')
                pass
            pass
        # SOURCE LINE 110
        __M_writer(u'\t\t</ul>\n\t</div>\n</div>\n<script>\nfunction lazy(){\nvar lazy = new ImagesLazyLoad({\n\t\tcontainer: window, mode: "vertical",\n\t\tholder: "/img/o_dot.gif"\n\t});\n}\nlazy();\n</script>\n<script type="text/javascript"> \n\tvar filter = "";\t\n\t$("document").ready(function(){\n\t\tslide();\n\t\tvar disrf = $.cookie("disrf");\n\t\tif(disrf == \'true\'){\n\t\t\tdocument.getElementById("disreflash").checked=true;\n\t\t}else{\n\t\t\tdocument.getElementById("disreflash").checked=false;\n\t\t\tdocument.getElementById("disreflash").defaultChecked=false;\n\t\t}\n\t\t/*hidden line*/\n\t\t  $("[name=\'filter\']").bind("click",function(){\n\t\t\t  filter="";\n\t\t\t\t  $("[name=\'filter\']").each(function(){\n\t\t\t\t\t\tif ($(this).attr("checked")==true){\n\t\t\t\t\t\t\t\tif (filter==""){\n\t\t\t\t\t\t\t\t\tfilter=$(this).val();\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\telse\n\t\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t\tfilter+=","+$(this).val();\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t}\n\t\t\t\t    })\n\t\t\t\t  if (filter == ""){filter=0}\n\t\t\t\t  \n\t\t\t\t  filterSelect(filter);\n\t\t\t  });\n\t\t\t/*$("#oClick").toggle(function(){\n\t\t\t\t$("#rtimeHeader").slideDown();\n\t\t\t\t$(this).html("\u70b9\u51fb\u9690\u85cf");\n\t\t\t},function(){\n\t\t\t\t$("#rtimeHeader").slideUp();\n\t\t\t\t$(this).html("\u70b9\u51fb\u663e\u793a");\n\t\t\t});*/\n\t\t\t\n\t\t\t\n\t\t\t$("#oClick").click(function(){\n\t\t\t\t\tif($("#rtimeHeader").css("display") == "none")\n\t\t\t\t\t{\n\t\t\t\t\t\t$("#rtimeHeader").slideDown();\n\t\t\t\t\t    $(this).html("\u70b9\u51fb\u9690\u85cf");\n\t\t\t\t\t    $.cookie(\'sk\',\'true\');\n\t\t\t\t\t}\n\t\t\t\t\telse\n\t\t\t\t\t{\n\t\t\t\t\t\t$("#rtimeHeader").slideUp();\n\t\t\t\t\t    $(this).html("\u70b9\u51fb\u663e\u793a");\n\t\t\t\t\t    $.cookie(\'sk\',\'false\');\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t$("#disreflash").click(function(){\n\t\t\t\t\tif (document.getElementById("disreflash").checked==true){\n\t\t\t\t\t\t$.cookie("disrf",true);\n\t\t\t\t\t\t}else{\n\t\t\t\t\t\t\t$.cookie("disrf",false);\n\t\t\t\t\t}\n\t\t\t\t\tlocation.reload();\n\t\t\t\t\t\n\t\t\t\t});\n\t});\n\tfunction filterSelect(fi) {\n\t\t  \t\n\t\t  \t\twindow.location = "?montoring=1&filter="+ fi; \n\t\t  \t\n\t}\n\tfunction slide(){\n\t\t\n\t\tif($.cookie(\'sk\') == \'true\'){\n\t\t\t\t$("#rtimeHeader").show();\n\t\t\t\t$("#oClick").html("\u70b9\u51fb\u9690\u85cf");\n\t\t}else{\n\t\t\t\t$("#rtimeHeader").hide();\n\t\t\t\t$("#oClick").html("\u70b9\u51fb\u663e\u793a");\n\t\t}\n\t}\n\t\n</script> \n</body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


