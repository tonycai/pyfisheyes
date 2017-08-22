# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1318562261.3755701
_template_filename='/home/tonycai/workspace/ops_repos/dev/pyfisheyes/pyfisheyes/templates/derived/events/new.html'
_template_uri='/derived/events/new.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['script', 'toolbox', 'title', 'heading', 'head_tags']


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
        str = context.get('str', UNDEFINED)
        hasattr = context.get('hasattr', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'\n\n')
        # SOURCE LINE 16
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 129
        __M_writer(u'\n\n\n<div>\n')
        # SOURCE LINE 133
        if hasattr(c,'id') and c.id:
            # SOURCE LINE 134
            __M_writer(u'\t<form action="/events/editsubmit/')
            __M_writer(escape(c.id))
            __M_writer(u'" method="post" enctype="multipart/form-data" onsubmit="return validate()">\n')
            # SOURCE LINE 135
        else:
            # SOURCE LINE 136
            __M_writer(u'\t<form action="/events/newsubmit" method="post" enctype="multipart/form-data" onsubmit="return validate()">\n')
            pass
        # SOURCE LINE 138
        __M_writer(u'\t\t<table class="newevent">\n\t\t\t<tr class="field"><td valign="top" colspan="2"><input name="submit" type="submit" value="Save" /></td></tr>\n\t\t\t<tr class="field"><td valign="top" colspan="2"><label for="event_name"><span style="color:red;">\uff0a</span> \u4e3b\u9898:</label> <input class="require" id="event_name" name="event_name" type="text" value="')
        # SOURCE LINE 140
        __M_writer(escape(c.event.evtitle))
        __M_writer(u'" size="80" style="width:400px;" /> #')
        __M_writer(escape(c.event.id))
        __M_writer(u'</td>\n\t\t</tr>\n\t\t    <tr class="field"><td valign="top" colspan="2"> <label for="event_date"><span style="color:red;">\uff0a</span> \u53d1\u751f\u65f6\u95f4:</label>\n')
        # SOURCE LINE 143
        if hasattr(c,'d1'):
            # SOURCE LINE 144
            __M_writer(u'\t\t    <input class="require date datetime" id="event_date" name="d1" type="text" value ="')
            __M_writer(escape(c.d1))
            __M_writer(u'" /> \n')
            # SOURCE LINE 145
        else:
            # SOURCE LINE 146
            __M_writer(u'\t\t    <input class="require date datetime" id="event_date" name="d1" type="text" value ="')
            __M_writer(escape(str(c.event.evdate)[0:10]))
            __M_writer(u'" />\n')
            pass
        # SOURCE LINE 148
        __M_writer(u'\t\t    <input class="require h datetime" value ="')
        __M_writer(escape(str(c.event.evdate)[11:13]))
        __M_writer(u'" name=\'h1\' type="text" style="width:40px;" maxlength="2" /> : <input class="require m datetime" name=\'m1\' type="text" style="width:40px;" maxlength="2" value="')
        __M_writer(escape(str(c.event.evdate)[14:16]))
        __M_writer(u'" /> </td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u53d1\u73b0\u65f6\u95f4: </label> <input class=" date datetime" name="d2" type="text" value ="')
        # SOURCE LINE 150
        __M_writer(escape(str(c.event.dt2)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h2\' style="width:40px;" class="h datetime" maxlength="2"  value="')
        __M_writer(escape(str(c.event.dt2)[11:13]))
        __M_writer(u'"/> : <input value="')
        __M_writer(escape(str(c.event.dt2)[14:16]))
        __M_writer(u'" name=\'m2\' type="text" style="width:40px;" maxlength="2" class="m datetime" /></td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u67e5\u660e\u539f\u56e0\u65f6\u95f4: </label> <input class="date datetime" name="d3" type="text" value ="')
        # SOURCE LINE 152
        __M_writer(escape(str(c.event.dt3)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h3\' style="width:40px;" class="h datetime"  maxlength="2" value="')
        __M_writer(escape(str(c.event.dt3)[11:13]))
        __M_writer(u'" /> : <input value="')
        __M_writer(escape(str(c.event.dt3)[14:16]))
        __M_writer(u'" type="text" name=\'m3\' class="m datetime" style="width:40px;" maxlength="2" /></td>\n\t\t</tr>\n\t\t<tr class="field"><td valign="top" colspan="2"><label for="">\u89e3\u51b3\u95ee\u9898\u65f6\u95f4: </label> <input class="date datetime" name="d4" type="text" value ="')
        # SOURCE LINE 154
        __M_writer(escape(str(c.event.dt4)[0:10]))
        __M_writer(u'" /> <input type="text" name=\'h4\' style="width:40px;" class="h datetime"  maxlength="2" value="')
        __M_writer(escape(str(c.event.dt4)[11:13]))
        __M_writer(u'" /> : <input value="')
        __M_writer(escape(str(c.event.dt4)[14:16]))
        __M_writer(u'" type="text" name=\'m4\' class="m datetime" style="width:40px;" maxlength="2" /></td>\n\t\t</tr>\n\t\t\t<tr><td><label>\u4e8b\u4ef6\u56fe\u7247:</label>\n')
        # SOURCE LINE 157
        if hasattr(c,'imgid'):
            # SOURCE LINE 158
            __M_writer(u'\t\t\t<input type="text" value="')
            __M_writer(escape(c.imgid))
            __M_writer(u'" name="graphs"/>\n')
            # SOURCE LINE 159
        else:
            # SOURCE LINE 160
            __M_writer(u'\t\t\t<input type="text" value="')
            __M_writer(escape(c.graphs))
            __M_writer(u'" name="graphs"/> \n')
            pass
        # SOURCE LINE 162
        __M_writer(u'\t\t\t<span>\u591a\u5f20\u56fe\u7247\u8bf7\u4ee5\u9017\u53f7","\u76f8\u9694</span></td></tr>\n\t\t\t<tr class="field"><td valign="top" colspan="2"><textarea id="ftextile" cols="80" name="event_content" rows="20">')
        # SOURCE LINE 163
        __M_writer(escape(c.event.evcontent))
        __M_writer(u'</textarea>\n\t\t</td></tr>\n\t\t\t<tr><td valign="top" colspan="2">\n\t\t\t\t\t\ttags:<input id="event_tags" name="event_tags" type="text" value ="')
        # SOURCE LINE 166
        __M_writer(escape(c.event.evtags))
        __M_writer(u'" size=15 />\n\t\t\t\t\t\tmin:<input id="event_minutes" name="event_minutes" type="text" value ="')
        # SOURCE LINE 167
        __M_writer(escape(c.event.evminutes))
        __M_writer(u'" size=3 />\n\t\t\t\t\t\tlosspv:<input id="event_losspv" name="event_losspv" type="text" value ="')
        # SOURCE LINE 168
        __M_writer(escape(c.event.evlosspv))
        __M_writer(u'" size=3 />\n\t\t\t\t\t\tcause:<select id="event_cause" name="event_cause">\n')
        # SOURCE LINE 170
        for cause in c.event_cause:  
            # SOURCE LINE 171
            if cause == c.event.evcause:
                # SOURCE LINE 172
                __M_writer(u'\t\t\t\t\t\t\t\t\t  \t\t<option value="')
                __M_writer(escape(cause))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(cause))
                __M_writer(u'</option>\n')
                # SOURCE LINE 173
            else:
                # SOURCE LINE 174
                __M_writer(u'\t\t\t\t\t\t\t\t\t  \t\t<option value="')
                __M_writer(escape(cause))
                __M_writer(u'">')
                __M_writer(escape(cause))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 177
        __M_writer(u'\t\t\t\t\t\t\t</select>\n\t\t\t\t\t</td>\n\t\t\t</tr>\n\t\t\t<tr><td>\n\t\t\t\ttype:<select  id="event_type" name="event_type">\n')
        # SOURCE LINE 182
        for evtype in c.event_type:
            # SOURCE LINE 183
            if evtype == c.event.evtype:
                # SOURCE LINE 184
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(evtype))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(evtype))
                __M_writer(u'</option>\n')
                # SOURCE LINE 185
            else:
                # SOURCE LINE 186
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(evtype))
                __M_writer(u'">')
                __M_writer(escape(evtype))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 189
        __M_writer(u'\t\t\t\t</select>\n\t\t\t\t\n\t\t\t\tstatus:<select id="event_status" name="event_status">\n')
        # SOURCE LINE 192
        for status in c.event_status:
            # SOURCE LINE 193
            if status == c.event.evstatus:
                # SOURCE LINE 194
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(status))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(status))
                __M_writer(u'</option>\n')
                # SOURCE LINE 195
            else:
                # SOURCE LINE 196
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(status))
                __M_writer(u'">')
                __M_writer(escape(status))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 199
        __M_writer(u'\t\t\t\t</select>\n\t\t\t\tdomain:<select  id="event_domain" name="event_domain">\n')
        # SOURCE LINE 201
        for domain in c.event_domain:
            # SOURCE LINE 202
            __M_writer(u'\t\t\t\t  \n')
            # SOURCE LINE 203
            if domain == c.event.evdomain:
                # SOURCE LINE 204
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(domain))
                __M_writer(u'" selected="selected">')
                __M_writer(escape(domain))
                __M_writer(u'</option>\n')
                # SOURCE LINE 205
            else:
                # SOURCE LINE 206
                __M_writer(u'\t\t\t\t  \t\t<option value="')
                __M_writer(escape(domain))
                __M_writer(u'">')
                __M_writer(escape(domain))
                __M_writer(u'</option>\n')
                pass
            pass
        # SOURCE LINE 209
        __M_writer(u'\t\t</select>\n\t\t\n\t\t\t</td>\n\t\t\t</tr>\n\t\t\n\t\t\t<tr class="field">\n\t\t\t<td valign="top" colspan="2"><input id="submit" name="submit" type="submit" value="Save" /></td>\n\t\t\t</tr>\n\t\t</table>\n\t</form>\n</div>\n<div id="flash"></div>\n<!-- <div id="upload"></div> -->\n\n\n')
        # SOURCE LINE 232
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_script(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n  \t<script type="text/javascript">\t\t\n\t\t$("document").ready(function(){\n\t\t\t\n\t\t\t$(function() {\n\t\t\t\t$( ".date" ).datepicker({ dateFormat: \'yy-mm-dd\' });\t\t\t\t\n\t\t\t});\n\n\t\t\t$(\'#ftextile\').markItUp(myTextileSettings);\n\n\t\t\t/* jQuery(\'#forms\').fileUpload({action:\'/\', field_name:\'file_field\',submit_label:\'upload\',use_iframes:true}) */\n\t\t\t\n\t\t\t/* \u9a8c\u8bc1\u56fe\u7247ID\u662f\u5426\u5b58\u5728 */\n\t\t\t\n\t\t\t$("input[name=\'graphs\']").blur(function(){\n\t\t\t\t  \n\t\t\t\t  if($(this).val() != \'\'){\n\t\t\t\t\t\t$.ajax({\n\t\t\t\t\t\t\t\turl:"/events/checkImgid",\n\t\t\t\t\t\t\t\tdata:"graphs="+$(this).val(),\n\t\t\t\t\t\t\t\tsuccess:function(html){\n\t\t\t\t\t\t\t\t\t$("input[name=\'graphs\']").siblings(".error").remove();\n\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\tif(html)\n\t\t\t\t\t\t\t\t\t{\n\t\t\t\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t\t\t$("input[name=\'graphs\']").after("<span class=\'error\'> \u56fe\u7247ID"+html+"\u4e0d\u5b58\u5728! </span>");\t\n\t\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\n\t\t\t\t\t\t\t   });\n\t\t\t\t\t}\n\n\t\t\t\t});\n\n\n\t\t\t/* \u9a8c\u8bc1\u65e5\u671f\u4e0e\u65f6\u95f4\u7684\u683c\u5f0f */\n\n\t\t\t$(".datetime").blur(function(){\n\t\t\t\t\n\t\t\t\t\tvar patt1=/\\d{4}\\-\\d{2}\\-\\d{2}/\n\t\t\t\t\tvar patt2=/\\d{2}/\n\t\t\t\t\n\t\t\t\t\tif($(this).hasClass("date")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt1.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte ){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65e5\u671f\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}else if($(this).hasClass("h")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt2.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte || parseInt($(this).val())>24){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65f6\u95f4\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}else if($(this).hasClass("m")&&$(this).val()){\n\t\t\t\t\t\t\n\t\t\t\t\t\tvar resulte = patt2.test($(this).val())\n\t\t\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\tif(!resulte || parseInt($(this).val())>60){\n\t\t\t\t\t\t\t\n\t\t\t\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u65f6\u95f4\u683c\u5f0f\u9519\u8bef</span>");\n\t\t\t\t\t\t\t}\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\t\t\t\t});\n\t\t\t$(".require").blur(function(){\n\t\t\t\t$(this).siblings(".error").remove();\n\t\t\t\tif($(this).val()==""){\n\t\t\t\t\t$(this).parent("td").append("<span class=\'error\'> \u5fc5\u586b\u9879\u4e0d\u80fd\u4e3a\u7a7a</span>");\n\t\t\t\t}\n\t\t\t\t\t\n\t\t  \t    });\n\t\t\t\t\t\t\t\t\t\n\t\t  });\n\t\t  \n\t\t  $("document").ready(App.Upload.init);\t\n\t\t  \n\t\t  function validate(){\n\t\t\t  \t  \n\t\t\t      // \u9a8c\u8bc1\u5fc5\u586b\u9879\u662f\u5426\u5b58\u5728\n\t\t\t\t  $(".require").each(function(){\n\t\t\t\t\t  \t\t$(this).siblings(".error").remove();\n\t\t\t\t\t\t\tif($(this).val() == \'\'){\n\t\t\t\t\t\t   \t\t\t$(this).parent("td").append("<span class=\'error\'> \u5fc5\u586b\u9879\u4e0d\u80fd\u4e3a\u7a7a</span>");\n\t\t\t\t\t\t   \t\t}\n\t\t\t\t\t\t\t\t\n\t\t\t\t\t});\n\t\t\t\t\tif($(".error").length > 0){\n\t\t\t\t\t\t\n\t\t\t\t\t\treturn false;\n\t\t\t\t\t\t\n\t\t\t\t\t}else{\n\t\t\t\t\t\t\n\t\t\t\t\t\treturn true;\n\t\t\t\t\t\t\n\t\t\t\t\t}\n\n\t\t\t  } \n\t\t  \n\t</script>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_toolbox(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 224
        __M_writer(u'\n\t<div class="box">\t\n\t\t<h3>')
        # SOURCE LINE 226
        __M_writer(escape("Assistant"))
        __M_writer(u'</h3>\t\n\t\t<ul>\n\t\t\t<li><a href="/events/new">New Event</a></li>\n\t\t\t<li><a href="http://redcloth.org/hobix.com/textile/" target="_blank">Textile Reference</a></li>\n\t\t</ul>\t\n\t</div>\t\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 18
        __M_writer(escape(c.heading))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<h1>')
        # SOURCE LINE 4
        __M_writer(escape(c.heading))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head_tags(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 7
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-1.4.4.min.js'))))
        __M_writer(u'\n')
        # SOURCE LINE 9
        __M_writer(escape(h.javascript_link(h.url_for('/jquery/js/jquery-ui-1.8.8.custom.min.js'))))
        __M_writer(u'    \n')
        # SOURCE LINE 10
        __M_writer(escape(h.stylesheet_link(h.url_for('/jquery/development-bundle/themes/pepper-grinder/jquery.ui.all.css'))))
        __M_writer(u'\n<script type="text/javascript" src="/markitup/jquery.markitup.js"></script>\n<script type="text/javascript" src="/markitup/sets/textile/set.js"></script>\n<!-- <script src="')
        # SOURCE LINE 13
        __M_writer(escape(url('/js/App.Upload.js')))
        __M_writer(u'" type="text/javascript"></script> -->\n<link rel="stylesheet" type="text/css" href="/markitup/skins/markitup/style.css" />\n<link rel="stylesheet" type="text/css" href="/markitup/sets/textile/style.css" />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


