# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1314759794.1874571
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/account/signin.html'
_template_uri='/derived/account/signin.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['heading', 'title']


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
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n<!-- ')
        # SOURCE LINE 19
        __M_writer(escape(h.form_start('%s', method="post")))
        __M_writer(u'-->\n<form class="signinform" action="/signin" method="post">\n\t<div><label for="username"> Username:</label><input id="username" name="username" type="text" /></div>\n\t<div><label for="password"> Password:</label><input id="password" name="password" type="password" /></div>\n\t<div><input id="submit" name="submit" type="submit" value="Sign in" /></div>\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1 class="heading">Sign In</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'Sign In')
        return ''
    finally:
        context.caller_stack._pop_frame()


