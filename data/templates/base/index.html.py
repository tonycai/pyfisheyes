# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1322013558.4381249
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/base/index.html'
_template_uri=u'/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['profile', 'script', 'title', 'head_tags', 'toolbox', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace(u'navigation', context._clean_inheritance_tokens(), templateuri=u'/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        navigation = _mako_get_namespace(context, 'navigation')
        hasattr = _import_ns.get('hasattr', context.get('hasattr', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n<head>\n  \t<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n\t<link rel="shortcut icon" href="/favicon.ico" type="image/x-icon">\n  \t<title>pyfisheyes - ')
        # SOURCE LINE 9
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n\t<meta name="keywords" content="pyfisheyes" />\n\t<meta name="description" content="" />\n\t')
        # SOURCE LINE 12
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/report.css'))))
        __M_writer(u'\n\t<link type="text/css" href="/jquery/css/pepper-grinder/jquery-ui-1.8.8.custom.css" rel="stylesheet" />\n\t')
        # SOURCE LINE 14
        __M_writer(escape(self.head_tags()))
        __M_writer(u'\n\t')
        # SOURCE LINE 15
        __M_writer(escape(self.script()))
        __M_writer(u'\n\t\n</head>\n<body>\n\n<div class="wrap">\n\n\t<div class="header">\n\t    <div class="header_top">\n\t\t\t<a href="/" class="logo"><img src="/img/logo2.png" alt="logo" height="50px"/></a>\n\t\t\t')
        # SOURCE LINE 25
        __M_writer(escape(self.profile()))
        __M_writer(u'\n\t\t</div>\n\t\n\t   <!-- <div id="description">{toolkit}</div> --> \n')
        # SOURCE LINE 29
        if hasattr(c,'pagename') and c.pagename:
            # SOURCE LINE 30
            __M_writer(u'\t\t\t')
            __M_writer(escape(navigation.menu(c.pagename)))
            __M_writer(u'\n')
            # SOURCE LINE 31
        else:
            # SOURCE LINE 32
            __M_writer(u'\t\t\t')
            __M_writer(escape(navigation.menu("")))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 34
        __M_writer(u'\t    \n\t</div><!-- end header -->\n\t\n\t<div class="main">\n\t    <div class="main_left">\n\t\t    \t')
        # SOURCE LINE 39
        __M_writer(escape(self.heading()))
        __M_writer(u'\n\t\t\t\t')
        # SOURCE LINE 40
        __M_writer(escape(next.body()))
        __M_writer(u'\n\t    </div> <!-- end #content-inner, #content -->\n\t\t<div class="main_right">\t\n\t\t\t')
        # SOURCE LINE 43
        __M_writer(escape(self.toolbox()))
        __M_writer(u'\t\n\t\t</div> <!-- end #sidebar -->\n\t</div> <!-- end main -->\n\n\t<div class="footer">\n\t    <div class="footer_pypowered"><a href="http://www.python.org/" title="The Python Language Site"><img src="/img/python-logo.gif" width="88" height="30" alt="Python" class="pypowered" /></a></div>\n\t    <p class="copyright">Website content copyright &copy; by YourSiteInc-OPSTeam. All rights reserved. tonycai321(&amp;)gmail.com</p>\n\t</div>\n\n\n</div> <!-- end wrap --> \n</body>\n</html>\n\n')
        # SOURCE LINE 65
        __M_writer(u'\n\n')
        # SOURCE LINE 67
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n\n')
        # SOURCE LINE 80
        __M_writer(u'\n\n')
        # SOURCE LINE 82
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
        # SOURCE LINE 57
        __M_writer(u'\n    <div class="welcome">\n')
        # SOURCE LINE 59
        if not request.environ.get('REMOTE_USER'):
            # SOURCE LINE 60
            __M_writer(u'\t  \t\t<a href="/signin" class="login">\u767b\u5f55</a>\n')
            # SOURCE LINE 61
        else:
            # SOURCE LINE 62
            __M_writer(u'\t  \t\t\u4f60\u597d\uff0c')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u' <a href="/signout">\u9000\u51fa</a> | <a href="/template">\u914d\u7f6e</a> \n')
            pass
        # SOURCE LINE 64
        __M_writer(u'    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        # SOURCE LINE 73
        __M_writer(u'\n\t<div class="slidebar news">\t\n\t\t<h3 class="sbartitle">\u5de5\u5177\u7bb1</h3>\t\n\t\t<ul class="sbarlist">\n\t\t\t<li><a href="#">item</a></li>\n\t\t</ul>\t\n\t</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, u'navigation')._populate(_import_ns, [u'*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


