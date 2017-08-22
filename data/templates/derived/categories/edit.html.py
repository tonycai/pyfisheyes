# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1315195500.4765401
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/categories/edit.html'
_template_uri='/derived/categories/edit.html'
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
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n<form action="/categories/')
        # SOURCE LINE 20
        __M_writer(escape(c.action))
        __M_writer(u'" method="post">\n<table style="width:100%;border: 1px solid #ccc;">\n<tr>\n    <td colspan="2" style="text-align:center;background-color:#eee;"><strong>')
        # SOURCE LINE 23
        __M_writer(escape(u"基础信息"))
        __M_writer(u'</strong></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 26
        __M_writer(escape(u"名称"))
        __M_writer(u'</td><td><input type="text" name="typename" value=\'')
        __M_writer(escape(c.cate.typename))
        __M_writer(u'\' class="input_text" /></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 29
        __M_writer(escape(u"类名"))
        __M_writer(u'</td><td><input type="text" name="classname" value=\'')
        __M_writer(escape(c.cate.classname))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 33
        __M_writer(escape(u"数据项"))
        __M_writer(u'</td><td><input type="text" name="items" value=\'')
        __M_writer(escape(c.cate.items))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 36
        __M_writer(escape(u"图标题"))
        __M_writer(u'</td><td><input type="text" name="titles" value=\'')
        __M_writer(escape(c.cate.titles))
        __M_writer(u'\' class="input_text" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 39
        __M_writer(escape(u"显示天数"))
        __M_writer(u'</td><td>\n    <select  id="labels" name="labels">\n')
        # SOURCE LINE 41
        for labels in c.labels:
            # SOURCE LINE 42
            if labels == c.cate.labels:
                # SOURCE LINE 43
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(labels))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(labels))
                __M_writer(u'</option>\n')
                # SOURCE LINE 44
            else:
                # SOURCE LINE 45
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(labels))
                __M_writer(u'">')
                __M_writer(escape(labels))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 48
        __M_writer(u'</select>\n    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 52
        __M_writer(escape(u"隐藏"))
        __M_writer(u'</td><td>\n')
        # SOURCE LINE 53
        if c.cate.disable == 0:
            # SOURCE LINE 54
            __M_writer(u'\t    <input type="radio" name="disable" value="0" checked> No\n\t\t<input type="radio" name="disable" value="1"> Yes\t\n')
            # SOURCE LINE 56
        else:
            # SOURCE LINE 57
            __M_writer(u'    \t    <input type="radio" name="disable" value="0"> No\n\t\t\t<input type="radio" name="disable" value="1" checked> Yes\t\n')
            pass
        # SOURCE LINE 60
        __M_writer(u'    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 63
        __M_writer(escape(u"排序字段"))
        __M_writer(u'</td>\n    <td>\n\t    <select  id="orderby" name="orderby">\n')
        # SOURCE LINE 66
        for orderby in c.orderby:
            # SOURCE LINE 67
            if orderby == c.cate.orderby:
                # SOURCE LINE 68
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(orderby))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(orderby))
                __M_writer(u'</option>\n')
                # SOURCE LINE 69
            else:
                # SOURCE LINE 70
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(orderby))
                __M_writer(u'">')
                __M_writer(escape(orderby))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 73
        __M_writer(u'</select>\n\t    <input type="hidden" name="typeid" value=\'')
        # SOURCE LINE 74
        __M_writer(escape(c.cate.typeid))
        __M_writer(u'\' /> \n    </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 78
        __M_writer(escape(u"图形"))
        __M_writer(u'</td><td>\n    <select  id="graphtype" name="graphtype">\n')
        # SOURCE LINE 80
        for graphtype in c.graphtype:
            # SOURCE LINE 81
            if graphtype == c.cate.graphtype:
                # SOURCE LINE 82
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(graphtype))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(graphtype))
                __M_writer(u'</option>\n')
                # SOURCE LINE 83
            else:
                # SOURCE LINE 84
                __M_writer(u'  \t\t<option value="')
                __M_writer(escape(graphtype))
                __M_writer(u'">')
                __M_writer(escape(graphtype))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 87
        __M_writer(u'</select>\n    \n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 93
        __M_writer(escape(u"排序"))
        __M_writer(u'</td><td><input type="text" name="rankcode" value=\'')
        __M_writer(escape(c.cate.rankcode))
        __M_writer(u'\' class="input_text_short" /></td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
        # SOURCE LINE 97
        __M_writer(escape(u"数据支持"))
        __M_writer(u'</td><td><input type="text" name="datasupport" value=\'')
        __M_writer(escape(c.cate.datasupport))
        __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n\n')
        # SOURCE LINE 100
        if c.cate.graphtype == "realtime":
            # SOURCE LINE 101
            __M_writer(u'<tr>\n    <td colspan="2" style="text-align:center;background-color:#eee;"><strong>')
            # SOURCE LINE 102
            __M_writer(escape(u"实时监控"))
            __M_writer(u'</strong></td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 105
            __M_writer(escape(u"分类"))
            __M_writer(u'</td><td>\n<select  id="typecode" name="typecode">\n')
            # SOURCE LINE 107
            for typecode_k, typecode_v in c.r_typecode.iteritems():
                # SOURCE LINE 108
                if typecode_v == c.cate.typecode:
                    # SOURCE LINE 109
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(typecode_v))
                    __M_writer(u'" selected="selected">')
                    __M_writer(escape(typecode_k))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 110
                else:
                    # SOURCE LINE 111
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(typecode_v))
                    __M_writer(u'">')
                    __M_writer(escape(typecode_k))
                    __M_writer(u'</option>\n')
                    pass
                pass
            # SOURCE LINE 114
            __M_writer(u'</select>\n </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 118
            __M_writer(escape(u"警告"))
            __M_writer(u'</td><td><input type="text" name="warning" value=\'')
            __M_writer(escape(c.cate.warning))
            __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 121
            __M_writer(escape(u"崩潰"))
            __M_writer(u'</td><td><input type="text" name="critical" value=\'')
            __M_writer(escape(c.cate.critical))
            __M_writer(u'\' class="input_text_short" /> </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 125
            __M_writer(escape(u"日报"))
            __M_writer(u'</td><td>\n')
            # SOURCE LINE 126
            if c.cate.d_report == 0:
                # SOURCE LINE 127
                __M_writer(u'\t    <input type="radio" name="d_report" value="0" checked> No\n\t\t<input type="radio" name="d_report" value="1"> Yes\t\n')
                # SOURCE LINE 129
            else:
                # SOURCE LINE 130
                __M_writer(u'    \t    <input type="radio" name="d_report" value="0"> No\n\t\t\t<input type="radio" name="d_report" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 133
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 137
            __M_writer(escape(u"报警"))
            __M_writer(u'</td><td>   \n')
            # SOURCE LINE 138
            if c.cate.r_alert == 0:
                # SOURCE LINE 139
                __M_writer(u'\t    <input type="radio" name="r_alert" value="0" checked> No\n\t\t<input type="radio" name="r_alert" value="1"> Yes\t\n')
                # SOURCE LINE 141
            else:
                # SOURCE LINE 142
                __M_writer(u'    \t    <input type="radio" name="r_alert" value="0"> No\n\t\t\t<input type="radio" name="r_alert" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 145
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 149
            __M_writer(escape(u"权重"))
            __M_writer(u'</td><td>\n    <select  id="r_weight" name="r_weight">\n')
            # SOURCE LINE 151
            for r_weight in c.r_weight:
                # SOURCE LINE 152
                if r_weight == c.cate.r_weight:
                    # SOURCE LINE 153
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(r_weight))
                    __M_writer(u'" selected="selected">')
                    __M_writer(escape(r_weight))
                    __M_writer(u'</option>\n')
                    # SOURCE LINE 154
                else:
                    # SOURCE LINE 155
                    __M_writer(u'  \t\t<option value="')
                    __M_writer(escape(r_weight))
                    __M_writer(u'">')
                    __M_writer(escape(r_weight))
                    __M_writer(u'</option>\n')
                    pass
                pass
            # SOURCE LINE 158
            __M_writer(u'</select>\n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 163
            __M_writer(escape(u"分析模型"))
            __M_writer(u'</td><td>\n    \n')
            # SOURCE LINE 165
            for r_mode in c.r_mode:
                # SOURCE LINE 166
                if r_mode == c.cate.r_mode:
                    # SOURCE LINE 167
                    __M_writer(u'  \t\t<input type="radio" name="r_mode" value="')
                    __M_writer(escape(r_mode))
                    __M_writer(u'" checked> ')
                    __M_writer(escape(r_mode))
                    __M_writer(u'\n')
                    # SOURCE LINE 168
                else:
                    # SOURCE LINE 169
                    __M_writer(u'  \t\t<input type="radio" name="r_mode" value="')
                    __M_writer(escape(r_mode))
                    __M_writer(u'" > ')
                    __M_writer(escape(r_mode))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 172
            __M_writer(u'<span class="intro">\u8bf4\u660e\uff1aa:A, b:V, c:<> d:.<>.</span>\n    </td>\n</tr>\n')
            # SOURCE LINE 187
            __M_writer(u'\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 189
            __M_writer(escape(u"报警周期"))
            __M_writer(u'</td><td>\n')
            # SOURCE LINE 190
            for l_interval in c.l_interval:
                # SOURCE LINE 191
                if l_interval == c.cate.l_interval:
                    # SOURCE LINE 192
                    __M_writer(u'\t  \t\t<input type="radio" name="l_interval" value="')
                    __M_writer(escape(l_interval))
                    __M_writer(u'" checked> ')
                    __M_writer(escape(l_interval))
                    __M_writer(u'\n')
                    # SOURCE LINE 193
                else:
                    # SOURCE LINE 194
                    __M_writer(u'\t  \t\t<input type="radio" name="l_interval" value="')
                    __M_writer(escape(l_interval))
                    __M_writer(u'" > ')
                    __M_writer(escape(l_interval))
                    __M_writer(u'\n')
                    pass
                pass
            # SOURCE LINE 197
            __M_writer(u'    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 201
            __M_writer(escape(u"报警阀值"))
            __M_writer(u'</td><td class="tab_td2">\n    ')
            # SOURCE LINE 207
            __M_writer(u'\n    <lu>\n\t    <li><i>')
            # SOURCE LINE 209
            __M_writer(escape(u"最小值"))
            __M_writer(u'</i> <input type="text" name="x_thr_0" value=\'')
            __M_writer(escape(c.list_alarm_threshold[0]))
            __M_writer(u'\' class="input_text_short" /></li>\n\t   \t<li><i>')
            # SOURCE LINE 210
            __M_writer(escape(u"稍小值"))
            __M_writer(u'</i> <input type="text" name="x_thr_1" value=\'')
            __M_writer(escape(c.list_alarm_threshold[1]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 211
            __M_writer(escape(u"稍大值"))
            __M_writer(u'</i> <input type="text" name="x_thr_2" value=\'')
            __M_writer(escape(c.list_alarm_threshold[2]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 212
            __M_writer(escape(u"最大值"))
            __M_writer(u'</i> <input type="text" name="x_thr_3" value=\'')
            __M_writer(escape(c.list_alarm_threshold[3]))
            __M_writer(u'\' class="input_text_short" /> </li>\n\t   \t<li><i>')
            # SOURCE LINE 213
            __M_writer(escape(u"最小百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_4" value=\'')
            __M_writer(escape(c.list_alarm_threshold[4]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 214
            __M_writer(escape(u"稍小最分百"))
            __M_writer(u'</i> <input type="text" name="x_thr_5" value=\'')
            __M_writer(escape(c.list_alarm_threshold[5]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 215
            __M_writer(escape(u"稍大百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_6" value=\'')
            __M_writer(escape(c.list_alarm_threshold[6]))
            __M_writer(u'\' class="input_text_short" />% </li>\n\t   \t<li><i>')
            # SOURCE LINE 216
            __M_writer(escape(u"最大百分比"))
            __M_writer(u'</i> <input type="text" name="x_thr_7" value=\'')
            __M_writer(escape(c.list_alarm_threshold[7]))
            __M_writer(u'\' class="input_text_short" />% </li>\n   \t</lu>\n    </td>\n</tr>\n\n<tr>\n    <td class="tab_td1">')
            # SOURCE LINE 222
            __M_writer(escape(u"参考线"))
            __M_writer(u'</td><td>   \n\t    <input type="text" name="baseface" value="')
            # SOURCE LINE 223
            __M_writer(escape(c.cate.baseface))
            __M_writer(u'" />\n')
            # SOURCE LINE 224
            if c.cate.u_baseface == 0:
                # SOURCE LINE 225
                __M_writer(u'\t    <input type="radio" name="usebaseface" value="0" checked> No\n\t\t<input type="radio" name="usebaseface" value="1"> Yes\t\n')
                # SOURCE LINE 227
            else:
                # SOURCE LINE 228
                __M_writer(u'    \t    <input type="radio" name="usebaseface" value="0"> No\n\t\t\t<input type="radio" name="usebaseface" value="1" checked> Yes\t\n')
                pass
            # SOURCE LINE 231
            __M_writer(u'\t    \n    </td>\n</tr>\n\n')
            pass
        # SOURCE LINE 236
        __M_writer(u'\n<tr>\n    <td colspan="2" style="text-align:center;">    \n    <input type="submit" value="')
        # SOURCE LINE 239
        __M_writer(escape(u"保存"))
        __M_writer(u'" />\n')
        # SOURCE LINE 240
        if c.action == "submit":
            # SOURCE LINE 241
            __M_writer(u'    <input type="button" value="')
            __M_writer(escape(u'克隆'))
            __M_writer(u'" onclick="window.location.href=\'/categories/copy/')
            __M_writer(escape(c.cate.typeid))
            __M_writer(u'\'" /> \n')
            pass
        # SOURCE LINE 243
        __M_writer(u'    \n    </td>\n</tr>\n</table>\n</form>\n\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n<div class="box">\n\n<h3>toolbox</h3>\n\n<ul>\n\t<li><a href="/categories/add">new template</a></li>\n</ul>\n\n</div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n  <h1>')
        # SOURCE LINE 4
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


