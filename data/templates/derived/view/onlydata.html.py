# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318557074.136194
_template_filename=u'/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/view/onlydata.html'
_template_uri=u'/derived/view/onlydata.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace(u'pagination', context._clean_inheritance_tokens(), templateuri=u'/component/pagination.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, u'pagination')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, u'pagination')._populate(_import_ns, [u'*'])
        pagination = _mako_get_namespace(context, 'pagination')
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        enumerate = _import_ns.get('enumerate', context.get('enumerate', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(escape(pagination.pagin(c, True)))
        __M_writer(u'\n\n<div class="viewdata">\n\t<table>\n\t\t<tr>\n')
        # SOURCE LINE 8
        if c.pagename == "realtime" :
            # SOURCE LINE 9
            __M_writer(u'\t\t\t<th width="30">')
            __M_writer(escape(u"编号"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 10
            __M_writer(escape(u"日期"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 11
            __M_writer(escape(u"小时"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 12
            __M_writer(escape(u"分钟"))
            __M_writer(u'</th>\n\t\t\t<th>')
            # SOURCE LINE 13
            __M_writer(escape(u"键值"))
            __M_writer(u'</th>\t\t\n')
            # SOURCE LINE 14
        else:
            # SOURCE LINE 15
            __M_writer(u'\t\t\t<th>N</th>\n')
            # SOURCE LINE 16
            for y,item in enumerate(c.items):
                # SOURCE LINE 17
                __M_writer(u'\t\t\t\t<th>')
                __M_writer(escape(item))
                __M_writer(u'</th>\n')
                pass
            pass
        # SOURCE LINE 20
        __M_writer(u'\t\t</tr>\t\n')
        # SOURCE LINE 21
        for y,row in enumerate(c.rows):
            # SOURCE LINE 22
            if c.pagename == "realtime" :
                # SOURCE LINE 23
                __M_writer(u'\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 24
                __M_writer(escape(y+1))
                __M_writer(u'</td>\t\t\t\t\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 25
                __M_writer(escape(row.datei))
                __M_writer(u'</td>\t\t\t\t\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 26
                __M_writer(escape(row.houri))
                __M_writer(u'</td>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 27
                __M_writer(escape(row.minutei))
                __M_writer(u'</td>\n\t\t\t\t\t\t<td><a onclick="load_logstuff(\'/logstuffshow/index/')
                # SOURCE LINE 28
                __M_writer(escape(row.tid))
                __M_writer(u'/')
                __M_writer(escape(row.datei))
                __M_writer(u'/')
                __M_writer(escape(row.time()))
                __M_writer(u'\')">')
                __M_writer(escape(row.formatValue()))
                __M_writer(u'</a></td>\n\t\t\t\t\t</tr>\n')
                # SOURCE LINE 30
            else:
                # SOURCE LINE 31
                __M_writer(u'\t\t\t\t\t<tr>\n\t\t\t\t\t\t<td>')
                # SOURCE LINE 32
                __M_writer(escape(y+1))
                __M_writer(u'</td>\t\n')
                # SOURCE LINE 33
                for x,opt in enumerate(row.tostringlist()):				
                    # SOURCE LINE 34
                    __M_writer(u'\t\t\t\t\t\t\t<td>')
                    __M_writer(escape(opt))
                    __M_writer(u'</td>\t\t\t\t\n')
                    pass
                # SOURCE LINE 36
                __M_writer(u'\t\t\t\t\t</tr>\n')
                pass
            pass
        # SOURCE LINE 39
        __M_writer(u'\t</table>\n</div>\n')
        # SOURCE LINE 41
        __M_writer(escape(pagination.pagin(c, True)))
        __M_writer(u'\n<script type="text/javascript">\n$(function(){\n\tvar src = $("#img").attr("src");\n\t$("#ysizeok").click(function(){\n\t\t    var graphs = $("#img");\n\t\t    var img1 = $("#imglink");\n\t\t    var img2 = $(".scale");\n\t\t    var img3 = $(".zoomWrapperImage");\n\t\t\tvar ysize = parseInt($("#ysize").val());\n\t\t\tif(ysize){\n\t\t\t\tvar src2 = $("#imglink").attr("href");\n\t\t\t\t\tvar index = src.lastIndexOf("?");\n\t\t\t\t\tvar index2 = src.lastIndexOf("?ys=");\n\t\t\t\t\tvar index3 = src.lastIndexOf("&ys=");\n\t\t\t\t\tvar oindex1 = src2.lastIndexOf("?");\n\t\t\t\t\tvar oindex2 = src2.lastIndexOf("?ys=");\n\t\t\t\t\tvar oindex3 = src2.lastIndexOf("&ys=");\n\t\t\t\t\tif (index == -1 ){\n\t\t\t\t\t\tvar src2 = src2+"?ys="+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",src+"?ys="+ysize);\n\t\t\t\t\t\t$(img1).attr("href",src2);\n\t\t\t\t\t\t$(img2).css("background-img","url("+src2+")");\n\t\t\t\t\t\t$(img3).attr("src",src2);\n\t\t\t\t\t}\n\t\t\t\t\telse if(index2 != -1){\n\t\t\t\t\t\tstr1 = src.substring(0,index2)+src.substr(index2,4)+ysize;\n\t\t\t\t\t\tstr11 = src2.substring(0,index21)+src2.substr(index21,4)+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",str1);\n\t\t\t\t\t}else if(index3 != -1){\n\t\t\t\t\t\tstr2 = src.substring(0,index3)+src.substr(index3,4)+ysize;\n\t\t\t\t\t\tstr22 = src2.substring(0,index31)+src2.substr(index31,4)+ysize;\n\t\t\t\t\t\t$(graphs).attr("src",str2);\t\t\t\t\t\t\n\t\t\t\t\t}else{\n\t\t\t\t\t\t$(graphs).attr("src",src+"&ys="+ysize);\n\t\t\t\t\t}\n\t\t\t\t\t\n\t\t\t\t}\n\t\t\t\n\t\t\t\n\t\t});\n\t$("#ysizeclear").click(function(){\n\t\tvar graphs = $("#portfolio_0 a img");\n\t\tvar src = $(graphs).attr("src");\n\t\tvar index2 = src.lastIndexOf("?ys=");\n\t\tvar index3 = src.lastIndexOf("&ys=");\n\t\tvar str4;\n\t\tif(index2 != -1)\n\t\t\tstr4 = src.substring(0,index2)\n\t\telse if(index3 != -1)\n\t\t\tstr4 = src.substring(0,index3)\n\t\t$(graphs).attr("src",str4);\n\t\t\t$("#ysize").val("");\n\t\t});\n});\n</script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


