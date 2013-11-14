from __future__ import division
from jinja2 import environment
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/macros/apptools.html'

    def root(context, environment=environment):
        t_1 = environment.filters['json']
        t_2 = environment.filters['safe']
        if 0: yield None
        def macro(l_page, l_transport, l_security):
            t_3 = []
            l_sys = context.resolve('sys')
            l_handler = context.resolve('handler')
            l_util = context.resolve('util')
            l_api = context.resolve('api')
            l_authorized = context.resolve('authorized')
            l_oauth = context.resolve('oauth')
            l_null = context.resolve('null')
            l_channel = context.resolve('channel')
            pass
            t_3.append(
                to_string(t_2(t_1({'platform': {'name': environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'project'), 'name'), 'version': environment.getattr(l_sys, 'version'), 'origindc': environment.getattr(l_util, 'datacenter'), 'instance': environment.getattr(l_util, 'instance'), 'debug': (True if environment.getattr(environment.getattr(l_util, 'config'), 'debug') else False)}, 'debug': {'logging': (environment.getattr(environment.getattr(l_util, 'config'), 'debug') or context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin'))), 'eventlog': environment.getattr(environment.getattr(l_util, 'config'), 'debug'), 'verbose': environment.getattr(environment.getattr(l_util, 'config'), 'debug'), 'strict': False}, 'push': ({'enabled': (True if environment.getattr(l_channel, 'token') else False), 'token': (environment.getattr(l_channel, 'token') if environment.getattr(l_channel, 'token') else l_null), 'timeout': ((environment.getattr(environment.getattr(l_channel, '_TTL'), 'seconds') / 60) if l_channel else l_null)} if l_channel else {}), 'user': ({'email': l_null, 'is_user_admin': l_null, 'nickname': l_null} if environment.getattr(l_security, 'current_user') != None else False), 'session': ({'blob': context.call(environment.getattr(environment.getattr(l_handler, 'session'), '_encode_session'))} if environment.getattr(l_handler, 'session') else {}), 'media': ({'key': environment.getattr(environment.getattr(l_page, 'media'), 'key'), 'ref': environment.getattr(environment.getattr(l_page, 'media'), 'ref'), 'name': environment.getattr(environment.getattr(l_page, 'media'), 'name')} if environment.getattr(l_page, 'media') else {'ref': None}), 'oauth': (({'id': environment.getattr(l_oauth, 'fbid')} if l_authorized else {'redirect': environment.getattr(l_oauth, 'redirect'), 'mode': environment.getattr(l_oauth, 'mode')}) if l_oauth else {}), 'services': {'endpoint': context.call(environment.getattr('://', 'join'), [(('https' if environment.getattr(l_handler, 'force_https') else False) or environment.getattr(environment.getattr(l_handler, 'request'), 'scheme')), environment.getattr(environment.getattr(l_transport, 'services'), 'endpoint')]), 'consumer': environment.getattr(environment.getattr(l_transport, 'services'), 'consumer'), 'scope': environment.getattr(environment.getattr(l_transport, 'services'), 'scope'), 'apis': context.call(environment.getattr(environment.getattr(l_transport, 'services'), 'make_object'), environment.getattr(l_page, 'services'))}}))), 
            )
            return concat(t_3)
        context.exported_vars.add('build_native_page_object')
        context.vars['build_native_page_object'] = l_build_native_page_object = Macro(environment, macro, 'build_native_page_object', ('page', 'transport', 'security'), (), False, False, False)
        def macro(l_services, l_config, l_page):
            t_4 = []
            l_null = context.resolve('null')
            pass
            t_4.append(
                u'$(document).ready(function (){\n\n\t', 
            )
            for event in context.blocks['platform_statement'][0](context):
                t_4.append(event)
            t_4.append(
                u'\n\n\t', 
            )
            if l_services != l_null:
                pass
                t_4.append(
                    u'\n\t$.apptools.api.rpc.factory([', 
                )
                l_action = l_cfg = l_opts = l_service = missing
                l_util = context.resolve('util')
                l_enumerate = context.resolve('enumerate')
                for (l_service, l_action, l_cfg, l_opts), l_loop in LoopContext(l_services):
                    pass
                    t_4.extend((
                        u"{\n\t\t\t\tname: '", 
                        to_string(l_service), 
                        u"',\n\t\t\t\tbase_uri: '", 
                        to_string(l_action), 
                        u"',\n\t\t\t\tmethods: [", 
                    ))
                    t_5 = l_loop
                    l_i = l_method = missing
                    l_len = context.resolve('len')
                    for (l_i, l_method) in context.call(l_enumerate, environment.getattr(l_cfg, 'methods')):
                        pass
                        t_4.extend((
                            u"'", 
                            to_string(l_method), 
                            u"'", 
                        ))
                        if l_i != (context.call(l_len, environment.getattr(l_cfg, 'methods')) - 1):
                            pass
                            t_4.append(
                                u',', 
                            )
                    l_loop = t_5
                    l_i = l_method = missing
                    t_4.extend((
                        u'],\n\t\t\t\tconfig: ', 
                        to_string(t_2(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), l_opts))), 
                        u'\n\t\t\t}', 
                    ))
                    if (not environment.getattr(l_loop, 'last')):
                        pass
                        t_4.append(
                            u',', 
                        )
                l_action = l_cfg = l_opts = l_service = missing
                t_4.append(
                    u']);\n\t', 
                )
            t_4.append(
                u'\n\n\t', 
            )
            if environment.getattr(l_page, 'open_channel'):
                pass
                t_4.append(
                    u'\n\t', 
                )
                if environment.getattr(l_page, 'channel_token'):
                    pass
                    t_4.extend((
                        u'\n\t\t$.apptools.push.channel.establish("', 
                        to_string(environment.getattr(l_page, 'channel_token')), 
                        u'").listen();\n\t', 
                    ))
                t_4.append(
                    u'\n\t', 
                )
            t_4.append(
                u'\n\n\t', 
            )
            for event in context.blocks['userobj'][0](context):
                t_4.append(event)
            t_4.append(
                u"\n\n\t$.apptools.events.trigger('API_READY');\n\n});", 
            )
            return concat(t_4)
        context.exported_vars.add('build_page_object')
        context.vars['build_page_object'] = l_build_page_object = Macro(environment, macro, 'build_page_object', ('services', 'config', 'page'), (), False, False, False)

    def block_platform_statement(context, environment=environment):
        l_util = context.resolve('util')
        l_sys = context.resolve('sys')
        l_api = context.resolve('api')
        if 0: yield None
        yield u"\n\t\t$.apptools.sys.platform = {\n\t\t\tname: '%s', version: '%s', origindc: '%s', instance: '%s'," % (
            environment.getattr(environment.getattr(environment.getattr(l_util, 'config'), 'project'), 'name'), 
            environment.getattr(l_sys, 'version'), 
            environment.getattr(environment.getattr(l_util, 'appengine'), 'datacenter'), 
            environment.getattr(environment.getattr(l_util, 'appengine'), 'instance'), 
        )
        if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin')):
            if 0: yield None
            yield u'debug: '
            l_off = context.resolve('off')
            if 0: yield None
            t_6 = context.eval_ctx.save()
            context.eval_ctx.autoescape = l_off
            yield (context.eval_ctx.autoescape and escape or to_string)(context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), environment.getattr(environment.getattr(l_util, 'config'), 'debug')))
            context.eval_ctx.revert(t_6)
        yield u'};'
        if (environment.getattr(environment.getattr(l_util, 'config'), 'debug') or context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin'))):
            if 0: yield None
            yield u'$.apptools.dev.setDebug({logging: true, eventlog: true, verbose: true});'
        else:
            if 0: yield None
            yield u'$.apptools.dev.setDebug({logging: false, eventlog: false, verbose: false});'

    def block_userobj(context, environment=environment):
        l_util = context.resolve('util')
        l_api = context.resolve('api')
        l_userapi = context.resolve('userapi')
        l_userobj = context.resolve('userobj')
        if 0: yield None
        if l_userapi != None:
            if 0: yield None
            yield u'$.apptools.user.setUserInfo({'
            if context.call(environment.getattr(environment.getattr(l_api, 'users'), 'get_current_user')) != None:
                if 0: yield None
                l_userobj = context.call(environment.getattr(environment.getattr(l_api, 'users'), 'get_current_user'))
                yield u'current_user: {\n\t\t\t\t\t\tnickname: "%s",\n\t\t\t\t\t\temail: "%s"\n\t\t\t\t\t},\n\t\t\t\t\tis_user_admin: %s' % (
                    context.call(environment.getattr(l_userobj, 'nickname')), 
                    context.call(environment.getattr(l_userobj, 'email')), 
                    context.call(environment.getattr(environment.getattr(environment.getattr(l_util, 'converters'), 'json'), 'dumps'), context.call(environment.getattr(environment.getattr(l_api, 'users'), 'is_current_user_admin'))), 
                )
            else:
                if 0: yield None
                yield u'current_user: null,\n\t\t\t\t\tis_user_admin: false'
            yield u'});'

    blocks = {'platform_statement': block_platform_statement, 'userobj': block_userobj}
    debug_info = '1=11&55=23&58=28&62=35&76=40&78=48&80=52&81=54&82=60&83=76&84=79&89=91&90=96&91=100&95=109&62=118&64=124&65=129&66=136&69=139&95=146&96=152&100=155&101=157&103=159&104=160&106=161'
    return locals()