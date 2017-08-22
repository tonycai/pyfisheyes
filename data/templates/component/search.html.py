# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321876605.7170179
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/component/search.html'
_template_uri=u'/component/search.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['device_finder', 'bar']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n\n')
        # SOURCE LINE 40
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_device_finder(context,url,met,w):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 24
        __M_writer(u'\n<div class="slidebar">\n     <h3 class="sbartitle">\u5feb\u901f\u67e5\u627e</h3>\n     <form action="')
        # SOURCE LINE 27
        __M_writer(escape(url))
        __M_writer(u'" method="')
        __M_writer(escape(met))
        __M_writer(u'">\n       <input type="text" name="ds" value="')
        # SOURCE LINE 28
        __M_writer(escape(w))
        __M_writer(u'" />\n       <input type="submit" value="\u67e5\u627e" />\n     </form>\n</div>\n\n        <div class="slidebar">\n          <h3 class="sbartitle">\u5de5\u5177\u680f</h3>\n          <ul class="sbarlist">\n           <li><a href="/devices/devicerealtime?item=loadavg&hn=">\u96f7\u8fbeII</a></li>\n          </ul>\n        </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_bar(context,url,mode):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div class="searchwrap">\n\t\t<p style="float:left;line-height:20px;"><input type="checkbox" id="disreflash" style="vertical-align:middle;" name="disrf" />&nbsp;<lable for="disreflash" style="color:#990000;">\u7981\u6b62\u5237\u65b0</lable>&nbsp;</p>\n\t\t<form action="')
        # SOURCE LINE 4
        __M_writer(escape(url))
        __M_writer(u'" class="searchform floatl">\n\t\t\t<input type="hidden" name="')
        # SOURCE LINE 5
        __M_writer(escape(mode))
        __M_writer(u'" value=1 />\n\t\t\t<input type="text" name="s" value="')
        # SOURCE LINE 6
        __M_writer(escape(c.sw))
        __M_writer(u'" class="searchkey" id="searchkey" /> \n\t\t\t<input type="submit" value="\u641c\u7d22" />\n')
        # SOURCE LINE 8
        if c.sw:
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<input type="button" value="\u64a4\u9500" onclick="window.location.href=\'')
            __M_writer(escape(url))
            __M_writer(u'?')
            __M_writer(escape(mode))
            __M_writer(u'\'" /> \n')
            pass
        # SOURCE LINE 11
        __M_writer(u'\t\t</form>\t\t\t\t\n\t\t<p class="hotkey floatl">\n\t\t\t\u70ed\u70b9: \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 14
        __M_writer(escape(mode))
        __M_writer(u'=1&s=dfs">dfs</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 15
        __M_writer(escape(mode))
        __M_writer(u'=1&s=my">my</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 16
        __M_writer(escape(mode))
        __M_writer(u'=1&s=cache">cache</a> \n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 17
        __M_writer(escape(mode))
        __M_writer(u'=1&s=500">500</a>\n\t\t\t<a href="/list/realtime?')
        # SOURCE LINE 18
        __M_writer(escape(mode))
        __M_writer(u'=1&s=solr">solr</a> \n\t\t</p>\n\t\t<div class="clear"></div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


