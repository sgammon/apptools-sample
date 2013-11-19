# -*- coding: utf-8 -*-

'''

    apptools-sample: config

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

import os

## Globals
debug = True
_config = {}
production = (not debug) and os.environ.get('SERVER_SOFTWARE', 'dev') != 'dev'


## App settings
_config['apptools'], _config['apptools.project'] = {}, {

    'name': 'apptools-sample',            # Change this to your app's name

    'version': {               # Change this according to your app's version
        'major': 0,
        'minor': 0,
        'micro': 1,
        'build': 20131111,
        'release': 'sample'
    }

}

## System settings
_config['apptools.system'] = {

    'debug': True,  # System-level debug messages

    'config': { 'debug': False }, # configuration debug

    'hooks': {  # System-level Developer's Hooks
        'callgraph': {'enabled': False},  # Use `pycallgraph` to generate an image callgraph of the WSGI app
        'profiler': {'enabled': False}   # Python profiler for CPU cycle/efficiency optimization + analysis
    },

    'include': [  # Extended configuration files to include

        ('model', 'config.model'),  # Model layer configuration
        ('assets', 'config.assets'),  # Asset manangement layer config
        ('output', 'config.output'),  # Output configuration
        ('services', 'config.services'),  # Global + site services (RPC/API) config
        ('integration', 'config.integration'),  # Library and 3rd-party config
        ('dev', 'config.dev')  # Development environment settings

    ]

}

## Platform Config
_config['apptools.system.platform'] = {

    'installed_platforms': [

        {'name': 'Generic WSGI', 'path': 'apptools.platform.generic.GenericWSGI'},
        {'name': 'Layer9 AppFactory', 'path': 'apptools.platform.appfactory.AppFactory'},
        {'name': 'Guestbook Platform', 'path': 'coolapp.platforms.Guestbook'}

    ]

}


## == load config includes == ##
_globals, _locals = globals(), {}
for name, submod in _config.get('apptools.system', {}).get('include', []):
    try:
        psplit = submod.split('.')
        mod = getattr(__import__('.'.join(psplit[:-1]), _globals, _locals, [psplit[-1]]), psplit[-1])
    except (ImportError, AttributeError) as e:
        print "!!! APPTOOLS: Failed to load config module `%s` at path `%s`. !!!" % (name, submod)
    else:
        if hasattr(mod, '_config'):
            _config.update(mod._config)
        else:
            print "APPTOOLS: Config include had no exported configuration. Continuing."
            continue


config = _config  # export
