# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1321876605.703449
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/component/pagination.html'
_template_uri=u'/component/pagination.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['pagin']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 9
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_pagin(context,cp,is_ajax):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<div class="pagination">\n')
        # SOURCE LINE 3
        if is_ajax:
            # SOURCE LINE 4
            __M_writer(u'\t')
            __M_writer(escape(cp.rows.pager('$link_previous ~4~ $link_next ',symbol_first=u'首页', symbol_last=u'末页', symbol_previous=u'上一页', symbol_next=u'下一页',onclick="$('#page-area').load('%s',function(){}); return false;")))
            __M_writer(u'\n')
            # SOURCE LINE 5
        else:
            # SOURCE LINE 6
            __M_writer(u'\t')
            __M_writer(escape(cp.rows.pager('total:$item_count page $page: $link_previous ~4~ $link_next', symbol_last=u'末页', symbol_previous=u'上一页', symbol_next=u'下一页')))
            __M_writer(u'\n')
            pass
        # SOURCE LINE 8
        __M_writer(u'</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


