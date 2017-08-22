# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321875308.3312659
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/devices/list.html'
_template_uri='/derived/devices/list.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['toolbox', 'script', 'heading', 'title']


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

    # SOURCE LINE 3
    ns = runtime.Namespace(u'search', context._clean_inheritance_tokens(), templateuri=u'/component/search.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'search')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        pagination = _mako_get_namespace(context, 'pagination')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 7
        __M_writer(escape(pagination.pagin(c, False)))
        __M_writer(u'\n<table class="atable" cellspacing="0" border="0" cellpadding="0" id="deviceList">\n<thead>\n<tr>\n\t\n\t<th>\u4e3b\u673a\u540d</th><th>CPU</th><th>\u5185\u5b58</th><th>\u78c1\u76d8</th><th>\u578b\u53f7</th><th>\u5185\u6838</th>\n\t\n\t\n</tr>\n</thead>\n<tbody>\n')
        # SOURCE LINE 18
        for x,d in enumerate(c.rows):
            # SOURCE LINE 19
            __M_writer(u'\t<tr>\n\t\t<td><a class=\'link\' href="/devices/deviceItems?dsn=')
            # SOURCE LINE 20
            __M_writer(escape(d.serial_no))
            __M_writer(u'&dn=')
            __M_writer(escape(d.hostname))
            __M_writer(u'">')
            __M_writer(escape(d.hostname))
            __M_writer(u'</a></td>\n\t\t<td>')
            # SOURCE LINE 21
            __M_writer(escape(d.cpuinfo))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 22
            __M_writer(escape(d.memsize))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 23
            __M_writer(escape(d.diskspace))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 24
            __M_writer(escape(d.hardware))
            __M_writer(u'</td>\n\t\t<td>')
            # SOURCE LINE 25
            __M_writer(escape(d.kernel_info))
            __M_writer(u'</td>\n\t\t\n\t</tr>\n')
            pass
        # SOURCE LINE 29
        __M_writer(u'</tbody>\n</table>\n')
        # SOURCE LINE 31
        __M_writer(escape(pagination.pagin(c, False)))
        __M_writer(u'\n\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        search = _mako_get_namespace(context, 'search')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n\n')
        # SOURCE LINE 36
        __M_writer(escape(search.device_finder("/devices", "get", c.ds)))
        __M_writer(u'\n\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 39
        __M_writer(u'\n<script type="text/javascript" src="/jquery/js/jquery-1.6.2.min.js"></script>\n<script type="text/javascript">\n$(function(){\n$("#deviceList tbody tr").hover(function(){\n\t$(this).children(\'td\').css({\'background-color\':\'#A6BAA6\',cursor:\'pointer\',color:\'#fff\'})\n\t\n},function(){\n\t$(this).children(\'td\').css({\'background-color\':\'#fff\',cursor:\'auto\',color:\'#000\'})\n\t\n});\n$("#deviceList tbody tr").click(function(){\n\th = $(this).find(\'.link\').attr(\'href\')\n\tlocation.href = h;\n\t\n});\n\t\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">')
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        _mako_get_namespace(context, u'search')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 5
        __M_writer(escape(c.pagename))
        return ''
    finally:
        context.caller_stack._pop_frame()


