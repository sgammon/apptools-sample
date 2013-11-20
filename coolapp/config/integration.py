# -*- coding: utf-8 -*-

'''

    apptools-sample config: integration

    :author: Sam Gammon <sam@keen.io>
    :copyright: (c) Keen IO, 2013
    :license: The inspection, use, distribution, modification or implementation
              of this source code is governed by a private license - all rights
              are reserved by the Authors (collectively, "Keen IO") and held
              under relevant California and US Federal Copyright laws. For full
              details, see ``LICENSE.md`` at the root of this project. Continued
              inspection of this source code demands agreement with the included
              license and explicitly means acceptance to these terms.

'''


## Globals
_config = {}


## Webapp2: Core
_config['webapp2'] = {
    'apps_installed': [
        "coolapp"
    ]
}

## Webapp2: Jinja
_config['webapp2_extras.jinja2'] = {

    'template_path': 'coolapp/templates/source',  # Root directory for template storage
    'compiled_path': 'coolapp.templates.compiled',  # Compiled templates directory
    'force_compiled': True,  # Force Jinja to use compiled templates, even on the Dev server

    'environment_args': {  # Jinja constructor arguments
        'optimized': True,   # enable jinja2's builtin optimizer (recommended)
        'autoescape': True,  # Global Autoescape. BE CAREFUL WITH THIS.
        'trim_blocks': False,  # Trim trailing \n's from blocks.
        'auto_reload': True,  # Auto-reload templates every time.
        'extensions': ['jinja2.ext.autoescape', 'jinja2.ext.with_', 'jinja2.ext.loopcontrols'],
    }

}

## Webapp2: Sessions
_config['webapp2_extras.sessions'] = {

    'secret_key': 'ckvnocnboH(&@H!(&@GH!(@*0s709780982)(*@!&^*^!&TOUBJVNLFKVnxvhyvcouh*!@)&!@(*&(86cyxhnkfd',
    'default_backend': 'securecookie',
    'cookie_name': 'kio',
    'session_ttl': 172000000,
    'session_max_age': None,
    'cookie_args': {
        'name': 'kio',
        'max_age': 172000000,
        'domain':      'keen.io',
        'path': '/'
        #'secure':      False,
        #'httponly':    False
    },
    'require_valid': True

}

## Google APIs
_config['google.apis'] = {

    'client_id': '',
    'client_secret': '',
    'user_agent': 'Apptools/1.0',

    'scopes': [  # base scopes to request access to
    ]

}

## Layer9/AppFactory
_config['layer9.appfactory'] = {

    'enabled': True,
    'logging': False,

    'headers': {
        'full_prefix': 'X-AppFactory',
        'compact_prefix': 'XAF',
        'use_compact': True
    }

}

_config['layer9.appfactory.upstream'] = {

    'debug': False,
    'enabled': True,

    'preloading': {
        'gather_assets': True,
        'enable_spdy_push': False,
        'enable_link_fallback': False
    },

    'spdy': {

        'push': {

            'assets': {
                'force_priority': False,
                'default_priority': 7
            }

        }

    }

}

_config['layer9.appfactory.frontline'] = {'debug': False, 'enabled': True}
_config['layer9.appfactory.controller'] = {'debug': False, 'enabled': False}
