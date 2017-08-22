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


