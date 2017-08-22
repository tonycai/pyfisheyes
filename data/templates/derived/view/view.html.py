# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1320386372.2915189
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/view/view.html'
_template_uri='/derived/view/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['script', 'toolbox', 'title', 'heading', 'head_tags']


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
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n')
        # SOURCE LINE 15
        __M_writer(u'\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        # SOURCE LINE 42
        __M_writer(u'\n')
        # SOURCE LINE 43
        if c.pagename == "realtime":	
            # SOURCE LINE 44
            __M_writer(u'\t<div class="container">\t\t\t\n\t\t    <ul class="tabs">\n\t\t        <li><a href="#tab1">\u56fe\u8868</a></li>\t\t        \n\t\t        <li><a href="#tab2">\u8bbe\u7f6e</a></li>\n\t\t        <li><a href="#tab3">\u884c\u52a8</a></li>\n\t\t    </ul>\t    \n\t    <div class="tab_container">\n\t        <div id="tab1" class="tab_content" style="text-align:center;">            \n\t            <p id="portfolio_0">\n')
            # SOURCE LINE 53
            if c.pweekday == '1':
                # SOURCE LINE 54
                __M_writer(u'\t\t            \t<a class="largeimg floatl" rel="gal1" href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'" id="imglink">\n\t\t            \t<img id="img" src="')
                # SOURCE LINE 55
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/0000-00-00/')
                __M_writer(escape(c.date2))
                __M_writer(u'/1.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'" />\n\t\t            \t</a>\n')
                # SOURCE LINE 57
            else:
                # SOURCE LINE 58
                __M_writer(u'\t\t            \t<a class="largeimg floatl" rel="gal1" href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png" id="imglink">\n\t\t            \t<img id="img" src="')
                # SOURCE LINE 59
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/0000-00-00/')
                __M_writer(escape(c.date2))
                __M_writer(u'/1.png" />\n\t\t            \t</a>\n')
                pass
            # SOURCE LINE 62
            __M_writer(u'\t\t                <p class="fguide">\n\t\t\t\t\t\t\t\t<a title="\u5bf9\u6bd4" href="/list/realtime?viewmdays&typeid=')
            # SOURCE LINE 63
            __M_writer(escape(c.template_id))
            __M_writer(u'&typename=')
            __M_writer(escape(c.topic))
            __M_writer(u'&odate=')
            __M_writer(escape(c.date2))
            __M_writer(u'" class="fl a1">\u5bf9\u6bd4</a>\n\t\t\t\t\t\t\t\t<a title="\u653e\u5927" href="')
            # SOURCE LINE 64
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph2/')
            __M_writer(escape(c.template_id))
            __M_writer(u'/')
            __M_writer(escape(c.opt))
            __M_writer(u'/')
            __M_writer(escape(c.date2))
            __M_writer(u'/7126x350/2.png" class="fl a2">\u653e\u5927</a>\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t</p> \n\t            </p>\n\t        </div>\n\t        <div id="tab2" class="tab_content">\n\t            <ul>\n\t            \t\n\t            \t<li><i>\u65e5\u62a5 </i>\n')
            # SOURCE LINE 73
            if c.t.d_report:
                # SOURCE LINE 74
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 75
            else:
                # SOURCE LINE 76
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 78
            __M_writer(u'\t            \t</li>\n\t            \t<li><i>\u63d0\u9192 </i>\n')
            # SOURCE LINE 80
            if c.t.r_alert:
                # SOURCE LINE 81
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 82
            else:
                # SOURCE LINE 83
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 85
            __M_writer(u'\t            \t</li>\n\t            \t<li><i>\u6743\u91cd </i>')
            # SOURCE LINE 86
            __M_writer(escape(c.t.r_weight))
            __M_writer(u'</li>\n\t            \t<li><i>\u53c2\u8003\u7ebf </i>\n')
            # SOURCE LINE 88
            if c.t.u_baseface:	            		       	
                # SOURCE LINE 89
                __M_writer(u'\t            \t\t\u5f00\u542f (')
                __M_writer(escape(c.t.baseface))
                __M_writer(u')\n')
                # SOURCE LINE 90
            else:
                # SOURCE LINE 91
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 93
            __M_writer(u'\t            \t</li>\n\t            \t\n\t            \t<li><i>\u77ed\u4fe1\u901a\u77e5 </i>\n')
            # SOURCE LINE 96
            if c.t.r_weight>5 and c.t.r_alert:
                # SOURCE LINE 97
                __M_writer(u'\t\t\t\t\t\t\u5f00\u542f\n')
                # SOURCE LINE 98
            else:
                # SOURCE LINE 99
                __M_writer(u'\t\t\t\t\t\t\u5173\u95ed\n')
                pass
            # SOURCE LINE 101
            __M_writer(u'\t\t\t\t\t</li>\n\t            \t<li><i>\u5206\u6790\u6a21\u578b </i>')
            # SOURCE LINE 102
            __M_writer(escape(c.t.r_mode))
            __M_writer(u'\u7c7b</li>\n\t            \t<li><i>\u62a5\u8b66\u9600\u503c </i>\n')
            # SOURCE LINE 104
            if c.t.r_mode == 'a':
                # SOURCE LINE 105
                __M_writer(u'\t\t\t\t\t\t\u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[2]))
                __M_writer(u' , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[3]))
                __M_writer(u'\n')
                # SOURCE LINE 106
            elif c.t.r_mode == 'b':            	
                # SOURCE LINE 107
                __M_writer(u'\t\t\t\t\t\t\u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[1]))
                __M_writer(u' , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[0]))
                __M_writer(u'\n')
                # SOURCE LINE 108
            elif c.t.r_mode in ['c','d']:
                # SOURCE LINE 109
                __M_writer(u'\t\t\t\t\t\t\u5d29\u6f70 -')
                __M_writer(escape(c.list_alarm_threshold[4]))
                __M_writer(u'% , \u8b66\u544a -')
                __M_writer(escape(c.list_alarm_threshold[5]))
                __M_writer(u'% , \u8b66\u544a ')
                __M_writer(escape(c.list_alarm_threshold[6]))
                __M_writer(u'% , \u5d29\u6f70 ')
                __M_writer(escape(c.list_alarm_threshold[7]))
                __M_writer(u'%\n')
                # SOURCE LINE 110
            else:
                # SOURCE LINE 111
                __M_writer(u'\t\t\t\t\t   noset\n')
                pass
            # SOURCE LINE 113
            __M_writer(u'\t            \t</li>\n\t            \t\n\t            </ul>       \n\t        </div>\n\t        <div id="tab3" class="tab_content">\t            \n\t            <p></p>\n\t        </div>\n\t    </div>\n\t</div>\n')
            # SOURCE LINE 122
        else:
            # SOURCE LINE 123
            __M_writer(u'\t<div class="graph">\n\t<p id="portfolio_0"><img src="')
            # SOURCE LINE 124
            __M_writer(escape(c.imgpath))
            __M_writer(u'/view/graph/')
            __M_writer(escape(c.template_id))
            __M_writer(u'/')
            __M_writer(escape(c.opt))
            __M_writer(u'/')
            __M_writer(escape(c.date))
            __M_writer(u'/')
            __M_writer(escape(c.date2))
            __M_writer(u'/1.png" /></p>\n\t</div>\n')
            pass
        # SOURCE LINE 127
        __M_writer(u'\n\n<div id="dialog" title="')
        # SOURCE LINE 129
        __M_writer(escape(c.topic))
        __M_writer(u'">\n\t<p id="dialog_content"></p>\n</div>\n\n')
        # SOURCE LINE 133
        if c.pagename == "realtime":	
            # SOURCE LINE 134
            __M_writer(u'<div class="clear">\t            \n\t<p><strong>\u5408\u8ba1</strong>\uff1a')
            # SOURCE LINE 135
            __M_writer(escape(c.sumvalue))
            __M_writer(u'\u3000\u9650\u5236\uff39\u8f74\u6700\u5927\u503c\uff1a<input type="text" id="ysize" style=\'width:80px;\' /> <input type="button" id="ysizeok" value="\u786e\u5b9a"/> <input type="button" id="ysizeclear" value="\u6e05\u9664"/>\n\t</p>\n</div>\n')
            pass
        # SOURCE LINE 139
        if c.pagename == "realtime":
            # SOURCE LINE 140
            if c.events:
                # SOURCE LINE 141
                __M_writer(u'<div ><h3 style="line-height:30px;font-weight:bold;border-bottom:1px solid orange;margin-top:5px;font-size:14px;color:#FF9933">\u4e8b\u4ef6</h3>\n')
                # SOURCE LINE 142
                for x,t in enumerate(c.events):
                    # SOURCE LINE 143
                    __M_writer(u'\t<dl style="line-height:24px;border-bottom:1px dashed orange;"><dt><a href="/events/detail/')
                    __M_writer(escape(t.id))
                    __M_writer(u'" style="color:#333;">')
                    __M_writer(escape(t.evtitle))
                    __M_writer(u'</a></dt><dd>')
                    __M_writer(escape(t.evcontent))
                    __M_writer(u'</dd><dl>\t\n')
                    pass
                # SOURCE LINE 145
                __M_writer(u'</div>\n')
                pass
            pass
        # SOURCE LINE 148
        __M_writer(u'<div id="page-area">')
        runtime._include_file(context, u'onlydata.html', _template_uri)
        __M_writer(u'</div>\n\n\n')
        # SOURCE LINE 245
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 16
        __M_writer(u'\n<script>\nvar opt = "')
        # SOURCE LINE 18
        __M_writer(escape(c.opt))
        __M_writer(u'";\nvar date = "')
        # SOURCE LINE 19
        __M_writer(escape(c.date))
        __M_writer(u'";\nvar date2 = "')
        # SOURCE LINE 20
        __M_writer(escape(c.date2))
        __M_writer(u'";\nvar tid = "')
        # SOURCE LINE 21
        __M_writer(escape(c.template_id))
        __M_writer(u'";\nvar pagename = "')
        # SOURCE LINE 22
        __M_writer(escape(c.pagename))
        __M_writer(u'";\nvar imgpath = "')
        # SOURCE LINE 23
        __M_writer(escape(c.imgpath))
        __M_writer(u'";\nvar ck = "')
        # SOURCE LINE 24
        __M_writer(escape(c.ck))
        __M_writer(u'"\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 151
        __M_writer(u'\n')
        # SOURCE LINE 152
        if c.pagename == "realtime":
            # SOURCE LINE 153
            __M_writer(u'<div class="box">\t\n\t\t<h3>')
            # SOURCE LINE 154
            __M_writer(escape("Search"))
            __M_writer(u'</h3>\t\n\t\t<form action="/list/realtime?montoring" method="get">\n\t\t\t<input type="hidden" name="montoring" value=1 />\n\t\t\t<input type="text" name="s" value="')
            # SOURCE LINE 157
            __M_writer(escape(c.sw))
            __M_writer(u'" />\t\n\t\t\t<input type="submit" value="Go" />\n\t\t\n\t\t</form>\n\t</div>\n')
            pass
        # SOURCE LINE 163
        __M_writer(u'\n<div class="box">\n\n')
        # SOURCE LINE 166
        if c.pagename == "day":
            # SOURCE LINE 167
            __M_writer(u'\t<h3>\u5f00\u59cb\u65e5\u671f:</h3>\n\t<div id="datepicker"></div>\n\t<h3></h3>\n\t<h3>\u7ed3\u675f\u65e5\u671f:</h3>\n\t<div id="datepicker2"></div>\n')
            # SOURCE LINE 172
        else:	
            # SOURCE LINE 173
            __M_writer(u'\t<h3>\u9009\u62e9\u65e5\u671f <input type="checkbox" name="onlyshowyester" id="osy"  value="')
            __M_writer(escape(c.yesterday))
            __M_writer(u'" ')
            __M_writer(escape(c.set_default_day))
            __M_writer(u' /><label style="font-size:10px" for="osy">\u8bb0\u4f4f</label></h3>\n\t\n\t<div id="datepicker2"></div>\n')
            pass
        # SOURCE LINE 177
        __M_writer(u'\n</div>\n\n\n')
        # SOURCE LINE 181
        if len(c.items)>2 and c.pagename == "day":
            # SOURCE LINE 182
            __M_writer(u'<div class="box">\n\t<h3>\u9690\u85cf</h3>\n\t<ul style="float:left;">\n')
            # SOURCE LINE 185
            for x,item in enumerate(c.items):
                # SOURCE LINE 186
                if x > 0:
                    # SOURCE LINE 187
                    __M_writer(u'\t\t\t<li style="float:left;"><input type="checkbox" name="item" id="item_')
                    __M_writer(escape(x))
                    __M_writer(u'"  value="')
                    __M_writer(escape(x))
                    __M_writer(u'" /><label for="item_')
                    __M_writer(escape(x))
                    __M_writer(u'">')
                    __M_writer(escape(item))
                    __M_writer(u'</label></li>\n')
                    pass
                pass
            # SOURCE LINE 190
            __M_writer(u'\t<br style="clear:both;"></br>\n\t</ul>\n</div>\n')
            pass
        # SOURCE LINE 194
        __M_writer(u'\n')
        # SOURCE LINE 195
        if len(c.items)>2 and c.pagename == "realtime":
            # SOURCE LINE 196
            __M_writer(u'<div class="box">\n\t<h3>\u9690\u85cf</h3>\n\t<ul>\n\t\t<li><input type="checkbox" name="pweekday" id="ritem_1"  value="1" checked/><label for="ritem_1">\u4e0a\u5468\u540c\u4e00\u5929</label></li>\t\t\n\t</ul>\n</div>\n')
            pass
        # SOURCE LINE 203
        __M_writer(u'\n<div class="box">\n\n<h3>\u5de5\u5177\u7bb1</h3>\n\n<ul>\n')
        # SOURCE LINE 209
        if c.pagename == "realtime":
            # SOURCE LINE 210
            __M_writer(u'\t<li><a href="/events/new?d1=')
            __M_writer(escape(c.date2))
            __M_writer(u'&graphs=')
            __M_writer(escape(c.template_id))
            __M_writer(u'" title="Report">New Event</a></li>\n\t<li>\n')
            # SOURCE LINE 212
            if c.pweekday == '1':
                # SOURCE LINE 213
                __M_writer(u'\t\t<a href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png?pweekday=')
                __M_writer(escape(c.pweekday))
                __M_writer(u'">\u67e5\u770b\u5927\u56fe</a>\n')
                # SOURCE LINE 214
            else:
                # SOURCE LINE 215
                __M_writer(u'\t\t<a href="')
                __M_writer(escape(c.imgpath))
                __M_writer(u'/view/graph2/')
                __M_writer(escape(c.template_id))
                __M_writer(u'/')
                __M_writer(escape(c.opt))
                __M_writer(u'/')
                __M_writer(escape(c.date2))
                __M_writer(u'/7126x350/2.png">\u67e5\u770b\u5927\u56fe</a>\n')
                pass
            # SOURCE LINE 217
            __M_writer(u'    </li>\n')
            pass
        # SOURCE LINE 219
        __M_writer(u'\t<li><a href="')
        __M_writer(escape(h.url(controller="view", action="exporttoexcel",id=c.template_id)))
        __M_writer(u'" id="ExporttoExcel">\u5bfc\u51faExcel</a></li>\n\t<li><a href="')
        # SOURCE LINE 220
        __M_writer(escape(h.url(controller="view", action="webapi",id=c.template_id)))
        __M_writer(u'">\u5199\u5165\u63a5\u53e3</a></li>\n')
        # SOURCE LINE 221
        if c.pagename == "realtime":
            # SOURCE LINE 222
            __M_writer(u'\t<li><a href="/list/realtime?montoring" title="\u6bcf\u5206\u949f\u5237\u65b0\u4e00\u6b21" >\u76d1\u63a7\u6a21\u5f0f</a></li>\n\t<li><a href="/list/realtime?fullscreen" title="\u4e0d\u5237\u65b0" >\u5168\u5c4f\u6a21\u5f0f</a></li>\n\t<li><a href="/daily_report/lookup_system" title="Report">Report</a></li>\n\t\n')
            pass
        # SOURCE LINE 227
        __M_writer(u'\t\n</ul>\n\n</div>\n\n<div class="box">\n\n<h3>\u4fe1\u606f</h3>\n\n<ul>\n')
        # SOURCE LINE 237
        if c.datasupport != "":
            # SOURCE LINE 238
            __M_writer(u'\t<li>\u6570\u636e\u652f\u6301\uff1a <a href="/contacts/list/1?qw=')
            __M_writer(escape(c.datasupport))
            __M_writer(u'">')
            __M_writer(escape(c.datasupport))
            __M_writer(u'</a></li>\n')
            pass
        # SOURCE LINE 240
        __M_writer(u'\t<li>\u8bbf\u95ee\u91cf\uff1a ')
        __M_writer(escape(c.accessed))
        __M_writer(u' \u6b21</li>\n</ul>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 15
        __M_writer(escape(c.topic))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 27
        __M_writer(u'\n<p class="pageguide floatl">\n')
        # SOURCE LINE 29
        if c.pre_topic:
            # SOURCE LINE 30
            __M_writer(u'<a class="pre" href="')
            __M_writer(escape(c.pre_topic.typeid))
            __M_writer(u'">&lt;&lt;&nbsp;')
            __M_writer(escape(c.pre_topic.typename))
            __M_writer(u'</a>\n')
            pass
        # SOURCE LINE 32
        if c.next_topic:
            # SOURCE LINE 33
            __M_writer(u'<a class="next" href="')
            __M_writer(escape(c.next_topic.typeid))
            __M_writer(u'">')
            __M_writer(escape(c.next_topic.typename))
            __M_writer(u'&nbsp;&gt;&gt;</a>\n')
            pass
        # SOURCE LINE 35
        __M_writer(u'</p>\n<h1 class="clear">\n')
        # SOURCE LINE 37
        __M_writer(escape(c.topic))
        __M_writer(u' #')
        __M_writer(escape(c.template_id))
        __M_writer(u'\n')
        # SOURCE LINE 38
        if request.environ.get('REMOTE_USER'):
            # SOURCE LINE 39
            __M_writer(u'\t <a href="/categories/edit/')
            __M_writer(escape(c.template_id))
            __M_writer(u'">\u7f16\u8f91</a>\n')
            pass
        # SOURCE LINE 41
        __M_writer(u'</h1>\n')
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
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-1.6.2.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-ui-1.8.8.custom.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/development-bundle/ui/i18n/jquery.ui.datepicker-zh-CN.js'))))
        __M_writer(u'  \n')
        # SOURCE LINE 7
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/development-bundle/external/jquery.cookie.js '))))
        __M_writer(u'  \n')
        # SOURCE LINE 8
        __M_writer(escape(h.stylesheet_link(h.url_for('/jquery/development-bundle/themes/pepper-grinder/jquery.ui.all.css'))))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/view.css'))))
        __M_writer(u'\n')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link(h.url_for('/lib/jqzoom/css/jquery.jqzoom.css'))))
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(escape(h.javascript_link(h.url_for('/js/view.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(escape(h.javascript_link(h.url_for('/lib/jqzoom/js/jquery.jqzoom-core.js'))))
        __M_writer(u' \n')
        return ''
    finally:
        context.caller_stack._pop_frame()


