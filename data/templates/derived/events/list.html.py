# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318562374.226258
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/events/list.html'
_template_uri='/derived/events/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'heading']


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
        # SOURCE LINE 3
        __M_writer(u'\n\n<div class="pagination">\n\t')
        # SOURCE LINE 6
        __M_writer(escape(c.events.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n\t')
        # SOURCE LINE 9
        __M_writer(u'\n</div>\n\n<table class="atable" cellspacing="0" border="0" cellpadding="0">\n<tr>\n\t<td>id</td>\n\t<td width="70%">name</td>\n\t<td>date</td>\n</tr>\n')
        # SOURCE LINE 18
        for x,e in enumerate(c.events):
            # SOURCE LINE 19
            __M_writer(u'\t<tr>\n\t\t<td><a href="/events/detail/')
            # SOURCE LINE 20
            __M_writer(escape(e.id))
            __M_writer(u'">#')
            __M_writer(escape(e.id))
            __M_writer(u'</a></td>\n\t\t<td>')
            # SOURCE LINE 21
            __M_writer(escape(e.evtitle))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 22
            __M_writer(escape(e.evdate))
            __M_writer(u'</td>\n\t\t\n\t</tr>\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'</table>\n\n<div class="pagination">\n\t')
        # SOURCE LINE 29
        __M_writer(escape(c.events.pager('total:$item_count Page $page/$page_count: $link_previous ~4~ $link_next ')))
        __M_writer(u'\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 32
        __M_writer(u'\n\t<div class="slidebar">\t\n\t\t<h3 class="sbartitle">')
        # SOURCE LINE 34
        __M_writer(escape("Assistant"))
        __M_writer(u'</h3>\t\n\t\t<ul class="sbarlist">\n\t\t\t<li><a href="/events/new">New Event</a></li>\n\t\t</ul>\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


