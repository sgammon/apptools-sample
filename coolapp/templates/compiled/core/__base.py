from __future__ import division
from jinja2 import environment
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/core/__base.html'

    def root(context, environment=environment):
        if 0: yield None
        yield u'<!doctype html>'
        for event in context.blocks['_tpl_root'][0](context):
            yield event

    def block_prenorth(context, environment=environment):
        if 0: yield None

    def block_page_services(context, environment=environment):
        l_page = context.resolve('page')
        if 0: yield None
        if environment.getattr(l_page, 'services'):
            if 0: yield None
            yield u"\n        <!-- AppTools Config -->\n        <script id='js-config' type='application/json' data-role='pageconfig'>"
            for event in context.blocks['js_pageobject'][0](context):
                yield event
            yield u'\n        </script>'

    def block_head(context, environment=environment):
        l_page = context.resolve('page')
        l_asset = context.resolve('asset')
        if 0: yield None
        for event in context.blocks['meta'][0](context):
            yield event
        yield u'\n\n        <!-- Title -->\n        <title>'
        for event in context.blocks['title_prefix'][0](context):
            yield event
        for event in context.blocks['title_seperator'][0](context):
            yield event
        for event in context.blocks['title'][0](context):
            yield event
        yield u'</title>\n\n        <!-- Mobile/Extras -->\n        <meta name="MobileOptimized" content="640">\n        <meta name="HandheldFriendly" content="True">\n        <meta name="apple-mobile-web-app-capable" content="yes">\n        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">\n\n        <!-- Icons -->\n        <link rel="icon" href="/favicon.png" type="image/png" />\n        <link rel="icon" href="/favicon.ico" type="image/x-icon" />\n        '
        for event in context.blocks['prenorth'][0](context):
            yield event
        for event in context.blocks['stylesheets'][0](context):
            yield event
        for event in context.blocks['postnorth'][0](context):
            yield event
        if (not environment.getattr(l_page, 'mobile')):
            if 0: yield None
            yield u'\n        <!-- JS Pre-Init -->\n        <script id=\'js-preinit\' type=\'text/javascript\' data-role=\'appclock\'>\n             var __pn=window.performance.now?function(){return window.performance.now.call(window.performance)}:\n                window.performance.webkitNow?function(){return window.performance.webkitNow.call(window.performance)}:\n                function(){return +new Date()},deferred=[],__clock={pn:__pn,ts:[__pn()],clockpoint:function(c,v,s,l,o){\n                this.ts.push(this.track([window.__pn(),[c,v,s,l,o]]))},track:function(t){return t}};if(window.location.hash=="#_=_"){window.location.hash=""};\n        </script>'
        else:
            if 0: yield None
            yield u'\n        <!-- JS Pre-init (MOBILE) -->\n        <script id=\'js-preinit\' type=\'text/javascript\' data-role=\'appclock\'>\n            var __pn = function () { return +new Date(); }, deferred = _gaq = [], _gac = _gac = {},\n                __clock = {pn: __pn, ts: [__pn()], clockpoint: function (c,v,s,l,o) {this.ts.push(\n                this.track([window.__pn(), [c, v, s, l, o]]));}, track: function (t) {return t;}};\n                if(window.location.hash=="#_=_"){window.location.hash="";};\n        </script>\n        '
        yield u'\n        '
        for event in context.blocks['page_services'][0](context):
            yield event
        yield u'\n\n        <!-- Core JS -->\n        <script src="//code.jquery.com/jquery.js" type="text/javascript"></script>\n        <script src="%s" type="text/javascript"></script>\n        <script src="%s" type="text/javascript"></script>' % (
            context.call(environment.getattr(l_asset, 'script'), 'base', 'apptools'), 
            context.call(environment.getattr(l_asset, 'script'), 'main', 'bootstrap'), 
        )
        for event in context.blocks['pagestyles'][0](context):
            yield event

    def block_js_pageobject(context, environment=environment):
        l_security = context.resolve('security')
        l_page = context.resolve('page')
        l_transport = context.resolve('transport')
        if 0: yield None
        included_template = environment.get_template('macros/apptools.html', '/source/core/__base.html').module
        l_build_native_page_object = getattr(included_template, 'build_native_page_object', missing)
        if l_build_native_page_object is missing:
            l_build_native_page_object = environment.undefined("the template %r (imported on line 77 in '/source/core/__base.html') does not export the requested name 'build_native_page_object'" % included_template.__name__, name='build_native_page_object')
        yield u'\n            '
        yield to_string(context.call(l_build_native_page_object, l_page, l_transport, l_security))

    def block_title(context, environment=environment):
        if 0: yield None
        yield u'welcome'

    def block_title_seperator(context, environment=environment):
        if 0: yield None
        yield u' / '

    def block_body(context, environment=environment):
        if 0: yield None

    def block_presouth(context, environment=environment):
        if 0: yield None

    def block_postsouth(context, environment=environment):
        if 0: yield None

    def block_stylesheets(context, environment=environment):
        l_asset = context.resolve('asset')
        if 0: yield None
        yield u'\n        <!-- Stylesheets -->\n        <link rel=\'stylesheet\' href="%s" />\n        <link rel=\'stylesheet\' href="%s" />\n\n\n        ' % (
            context.call(environment.getattr(l_asset, 'style'), 'main', 'bootstrap'), 
            context.call(environment.getattr(l_asset, 'style'), 'app', 'static'), 
        )

    def block_meta(context, environment=environment):
        l__meta = context.resolve('_meta')
        if 0: yield None
        yield u'\n        <!-- Meta -->\n        <meta charset="utf-8" />\n        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />\n        '
        if context.call(environment.getattr(context.call(environment.getattr(l__meta, 'get'), 'google', {}), 'get'), 'site_verification', False):
            if 0: yield None
            yield u'<meta name="google-site-verification" content="%s" />' % (
                context.call(environment.getattr(context.call(environment.getattr(l__meta, 'get'), 'google'), 'get'), 'site_verification'), 
            )
        for event in context.blocks['meta_basic'][0](context):
            yield event

    def block_postnorth(context, environment=environment):
        if 0: yield None

    def block_jspagedata(context, environment=environment):
        if 0: yield None
        yield u'<!-- Page Data -->'

    def block_title_prefix(context, environment=environment):
        if 0: yield None
        yield u'apptools'

    def block__tpl_root(context, environment=environment):
        l_mobile = context.resolve('mobile')
        l_page = context.resolve('page')
        if 0: yield None
        if (not environment.getattr(l_page, 'manifest')):
            if 0: yield None
            yield u'\n<html class="no-js" lang="en" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb apptools-sample: http://ogp.me/ns/fb/apptools-sample#">\n'
        else:
            if 0: yield None
            yield u'\n<html class="no-js" lang="en" prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# apptools-sample: http://ogp.me/ns/fb/apptools-sample#" manifest="%s">' % (
                environment.getattr(environment.getattr(l_page, 'manifest'), 'location'), 
            )
        yield u'<head>'
        for event in context.blocks['head'][0](context):
            yield event
        yield u'\n\n</head>\n\n<body role="application" lang="en" translate="yes" dir="ltr"'
        if l_mobile:
            if 0: yield None
            yield u' data-mobile="true"'
        yield u'>\n'
        for event in context.blocks['body'][0](context):
            yield event
        for event in context.blocks['jspagedata'][0](context):
            yield event
        yield u'\n\n'
        for event in context.blocks['presouth'][0](context):
            yield event
        for event in context.blocks['south'][0](context):
            yield event
        for event in context.blocks['postsouth'][0](context):
            yield event
        yield u'</body>\n</html>'

    def block_south(context, environment=environment):
        if 0: yield None
        yield u'<!-- Page JS -->\n<script type="text/javascript">\n    $.apptools.rpc.state.config.jsonrpc = {\n        base_uri: \'/v1/rpc\',\n        enabled: true,\n        host: window.location.protocol + \'//\' + window.location.host\n    };\n\n    console.log(\'Apptools sample is ready. :)\');\n</script>\n\n<!-- Deferred JS -->\n<div id=\'js-deferred\' class=\'hidden resource\'></div><!-- end #js-deferred -->'

    def block_meta_basic(context, environment=environment):
        l__meta = context.resolve('_meta')
        l_len = context.resolve('len')
        t_1 = environment.filters['safe']
        if 0: yield None
        yield u'\n        <!-- Info -->\n        <meta name="author" content="%s" />\n        <meta name="publisher" content="%s" />\n        <meta name="keywords" content="%s" />\n        <meta name="copyright" content="%s" />\n        <meta name="description" content="%s" />\n        <meta name="application-name" content="%s" />\n        <meta name="robots" content="%s" />\n        <meta name="viewport" content="%s" />\n        <meta name="revisit-after" content="%s" />\n        ' % (
            context.call(environment.getattr(l__meta, 'get'), 'author', 'Keen IO <keen.io>'), 
            context.call(environment.getattr(l__meta, 'get'), 'publisher', 'Keen IO <keen.io>'), 
            context.call(environment.getattr(',', 'join'), context.call(environment.getattr(l__meta, 'get'), 'keywords', [])), 
            context.call(environment.getattr(l__meta, 'get'), 'copyright', 'Keen IO (c) 2013'), 
            t_1(context.call(environment.getattr(l__meta, 'get'), 'description', 'Welcome to apptools! :)')), 
            context.call(environment.getattr(l__meta, 'get'), 'application-name', 'apptools'), 
            context.call(environment.getattr(l__meta, 'get'), 'robots', 'index, follow'), 
            context.call(environment.getattr(l__meta, 'get'), 'viewport', ''), 
            context.call(environment.getattr(l__meta, 'get'), 'revisit-after', '7 days'), 
        )
        if context.call(l_len, context.call(environment.getattr(l__meta, 'get'), 'keywords')) > 2:
            if 0: yield None
            yield u'<!-- %s -->' % (
                context.call(environment.getattr(',', 'join'), context.call(environment.getattr(l__meta, 'get'), 'keywords')[0:3]), 
            )

    def block_pagestyles(context, environment=environment):
        if 0: yield None

    blocks = {'prenorth': block_prenorth, 'page_services': block_page_services, 'head': block_head, 'js_pageobject': block_js_pageobject, 'title': block_title, 'title_seperator': block_title_seperator, 'body': block_body, 'presouth': block_presouth, 'postsouth': block_postsouth, 'stylesheets': block_stylesheets, 'meta': block_meta, 'postnorth': block_postnorth, 'jspagedata': block_jspagedata, 'title_prefix': block_title_prefix, '_tpl_root': block__tpl_root, 'south': block_south, 'meta_basic': block_meta_basic, 'pagestyles': block_pagestyles}
    debug_info = '2=10&46=13&72=16&73=19&76=22&9=26&11=30&35=33&46=40&47=42&54=44&55=46&72=53&86=56&87=57&89=59&76=62&77=67&78=72&35=74&95=82&100=85&118=88&47=91&49=95&50=96&11=99&16=103&18=108&54=111&97=114&35=118&2=122&3=126&6=132&9=135&94=138&95=142&97=144&100=147&101=149&118=151&101=155&18=159&20=165&21=166&22=167&23=168&24=169&25=170&26=171&27=172&28=173&29=175&89=181'
    return locals()