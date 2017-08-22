# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321004887.3172851
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/component/navigation.html'
_template_uri=u'/component/navigation.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu', 'footer']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 62
        __M_writer(u'\n\n')
        # SOURCE LINE 69
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context,selected):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\t    <ul class="nav">\n')
        # SOURCE LINE 3
        if selected == "homepage":
            # SOURCE LINE 4
            __M_writer(u'\t\t\t<li><a class="active" href="/">\u9996\u9875</a></li>\n')
            # SOURCE LINE 5
        else:
            # SOURCE LINE 6
            __M_writer(u'\t\t    <li><a href="/">\u9996\u9875</a></li>\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'\t\t\n')
        # SOURCE LINE 9
        if selected == "day":
            # SOURCE LINE 10
            __M_writer(u'\t\t\t<li><a class="active" href="/list/day">\u6bcf\u5929</a></li>\n')
            # SOURCE LINE 11
        else:
            # SOURCE LINE 12
            __M_writer(u'\t\t\t<li><a href="/list/day">\u6bcf\u5929</a></li>\n')
            pass
        # SOURCE LINE 14
        __M_writer(u'\t\t\n')
        # SOURCE LINE 15
        if selected == "hour":
            # SOURCE LINE 16
            __M_writer(u'\t\t\t<li><a class="active" href="/list/hour">\u5c0f\u65f6</a></li>\n')
            # SOURCE LINE 17
        else:
            # SOURCE LINE 18
            __M_writer(u'\t\t\t<li><a href="/list/hour">\u5c0f\u65f6</a></li>\n')
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t\n')
        # SOURCE LINE 21
        if selected == "host":
            # SOURCE LINE 22
            __M_writer(u'\t\t\t<li><a class="active" href="/list/host">\u5206\u7ec4</a></li>\n')
            # SOURCE LINE 23
        else:
            # SOURCE LINE 24
            __M_writer(u'\t\t\t<li><a href="/list/host">\u5206\u7ec4</a></li>\n')
            pass
        # SOURCE LINE 26
        __M_writer(u'\t\t\n')
        # SOURCE LINE 27
        if selected == "realtime":
            # SOURCE LINE 28
            __M_writer(u'\t\t\t<li><a class="active" href="/list/realtime">\u76d1\u63a7</a></li>\n')
            # SOURCE LINE 29
        else:
            # SOURCE LINE 30
            __M_writer(u'\t\t\t<li><a href="/list/realtime">\u76d1\u63a7</a></li>\n')
            pass
        # SOURCE LINE 32
        if selected in ['devices','deviceitems','cmpitem'] :
            # SOURCE LINE 33
            __M_writer(u'\t\t\t<li><a class="active" href="/devices">\u4e3b\u673a</a></li>\n')
            # SOURCE LINE 34
        else:
            # SOURCE LINE 35
            __M_writer(u'\t\t\t<li><a href="/devices">\u4e3b\u673a</a></li>\n')
            pass
        # SOURCE LINE 37
        __M_writer(u'\t\t\n')
        # SOURCE LINE 38
        if selected == "speed":
            # SOURCE LINE 39
            __M_writer(u'\t\t\t<li><a class="active" href="/speed" style="display:none;">\u901f\u5ea6</a></li>\n')
            # SOURCE LINE 40
        else:
            # SOURCE LINE 41
            __M_writer(u'\t\t\t<li><a href="/speed" style="display:none;">\u901f\u5ea6</a></li>\n')
            pass
        # SOURCE LINE 43
        __M_writer(u'\t\t\n')
        # SOURCE LINE 44
        if selected == "events":
            # SOURCE LINE 45
            __M_writer(u'\t\t\t<li><a class="active" href="/events">\u4e8b\u4ef6</a></li>\n')
            # SOURCE LINE 46
        else:
            # SOURCE LINE 47
            __M_writer(u'\t\t\t<li><a href="/events">\u4e8b\u4ef6</a></li>\n')
            pass
        # SOURCE LINE 49
        __M_writer(u'\t\t\n')
        # SOURCE LINE 50
        if selected == "alert":
            # SOURCE LINE 51
            __M_writer(u'\t\t\t<li><a class="active" href="/alert">\u62a5\u8b66</a></li>\n')
            # SOURCE LINE 52
        else:
            # SOURCE LINE 53
            __M_writer(u'\t\t\t<li><a href="/alert">\u62a5\u8b66</a></li>\n')
            pass
        # SOURCE LINE 55
        __M_writer(u'\t\t\n')
        # SOURCE LINE 56
        if selected == "contacts":
            # SOURCE LINE 57
            __M_writer(u'\t\t\t<li><a class="active" href="/contacts">\u8054\u7cfb\u4eba</a></li>\n')
            # SOURCE LINE 58
        else:
            # SOURCE LINE 59
            __M_writer(u'\t\t\t<li><a href="/contacts">\u8054\u7cfb\u4eba</a></li>\n')
            pass
        # SOURCE LINE 61
        __M_writer(u'\t    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n<div class="footer">\n            <div class="footer_pypowered"><a href="http://www.python.org/" title="The Python Language Site"><img src="/img/python-logo.gif" width="88" height="30" alt="Python" class="pypowered" /></a></div>\n            <p class="copyright">Website content copyright &copy; by YourSiteInc-OPSTeam. All rights reserved. tonycai321(&amp;)gmail.com</p>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


