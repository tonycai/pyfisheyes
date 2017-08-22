# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321257510.4823411
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/list/list.html'
_template_uri='/derived/list/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading', 'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'/component/pagination.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        str = _import_ns.get('str', context.get('str', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n<table class="atable" cellspacing="0" border="0" cellpadding="0">\n')
        # SOURCE LINE 8
        for x,category in enumerate(c.rows):
            # SOURCE LINE 9
            __M_writer(u'\t<tr>\n\t\t<td class="first">')
            # SOURCE LINE 10
            __M_writer(escape(x+1))
            __M_writer(u'</td>\n\t\t<td> <a href="')
            # SOURCE LINE 11
            __M_writer(escape(h.url_for('/view/data/'+ str(category.typeid))))
            __M_writer(u'">')
            __M_writer(escape(category.typename))
            __M_writer(u'</a></a></td>\n\t\t<td class="last"><a href="/view/data/')
            # SOURCE LINE 12
            __M_writer(escape(category.typeid))
            __M_writer(u'">')
            __M_writer(escape("view"))
            __M_writer(u'</a></td>\n\t</tr>\n')
            pass
        # SOURCE LINE 15
        __M_writer(u'</table>\n\n')
        # SOURCE LINE 17
        __M_writer(escape(pagination.pagin(c, False)))
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 19
        __M_writer(u'\n')
        # SOURCE LINE 20
        if c.pagename == "realtime":
            # SOURCE LINE 21
            __M_writer(u'   <div class="slidebar">\t\n\t\t<h3 class="sbartitle">')
            # SOURCE LINE 22
            __M_writer(escape("Search"))
            __M_writer(u'</h3>\t\n\t\t<form action="/list/realtime?montoring" method="get">\n\t\t<input type="hidden" name="fullscreen" value=1 />\t\t\n\t\t\t<input type="text" name="s" value="" />\t\t\n\t\t\t<input type="submit" value="Go" />\n\t\n\t\t</form>\n\t</div>\n\t\n\t<div class="slidebar">\t\n\t\t\t<h3 class="sbartitle">')
            # SOURCE LINE 32
            __M_writer(escape("usefully"))
            __M_writer(u'</h3>\n\t\t\t<p>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=mysql">mysql</a> \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=vpn">vpn</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=ct">ct</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cnc">cnc</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cdn">cdn</a> \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=solr">solr</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=\u5b9e\u65f6\u8bf7\u6c42">\u5b9e\u65f6\u8bf7\u6c42</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=\u6162\u8bf7\u6c42">\u5b9e\u65f6\u6162\u8bf7\u6c42</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=connections">connections</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=cache">cache</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=release">release</a>\n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite">yoursite</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite1">yoursite1</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=yoursite2">yoursite2</a>  \n\t\t\t\t<a href="/list/realtime?fullscreen=1&s=500">500</a>  \n\t\t\t</p>\n\t</div>\n')
            pass
        # SOURCE LINE 52
        __M_writer(u'\n\t<div class="slidebar">\n\t\t<h3 class="sbartitle">\u5de5\u5177\u7bb1</h3>\n\t\t<ul class="sbarlist">\n')
        # SOURCE LINE 56
        if c.pagename == "realtime":
            # SOURCE LINE 57
            __M_writer(u'\t\t\t<li><a href="/list/realtime?montoring" title="\u6bcf\u5206\u949f\u5237\u65b0\u4e00\u6b21" >\u76d1\u63a7\u6a21\u5f0f</a></li>\n\t\t\t<li><a href="/list/realtime?fullscreen" title="\u4e0d\u5237\u65b0" >\u5168\u5c4f\u6a21\u5f0f</a></li>\n\t\t\t<li style="display:none;"><a href="/list/realtime?report" title="Report">Report</a></li>\n\t\t\t<li><a href="/daily_report/lookup_system" title="Report">Report</a></li>\n\t\t\t<li><a href="/html/vip_justin.html" title="">vip_Justin</a></li>\n\t\t\t<li><a href=\'/list/realtime?fullscreen=1&s=%E4%BD%8D%E7%BD%AE\' target="_blank">\u4f4d\u7f6e\u76d1\u63a7</a></li>\n')
            pass
        # SOURCE LINE 64
        __M_writer(u'\t\t</ul>\n\t</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.pagename))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(escape(c.pagename))
        return ''
    finally:
        context.caller_stack._pop_frame()


