# -*- coding: utf-8 -*-

'''

    apptools-sample config: services

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

# stdlib
import hashlib


## Globals
_config = {}


## Project Services
_config['apptools.project.services'] = {

    'debug': False,    # Return extra debug info in responses
    'enabled': True,   # Disable API services system wide
    'logging': False,  # Logging for service request handling

    # Module-level (default) config
    'config': {
        'hmac_hash': hashlib.sha512,  # Hash algorithm to use for HMAC signatures
        'url_prefix': '/v1/rpc',  # Prefix for all service invocation URLs
        'secret_key': 'cvjoivnH)!@J!@)(07809709J!_(J@)*H(*Y&(*!@H)()!@J!_@)(JK0x87v0(*!_@)*(@',  # Secret for generating HMAC signings
    },

    # Installed API's
    'services': {
    }  # End services

}  # End services

# Global Services
_config['apptools.services'] = {

    'logging': False,

    'hooks': {
        'appstats': {'enabled': False},  # RPC profiling
        'apptrace': {'enabled': False},  # memory usage profiling
        'profiler': {'enabled': False}   # CPU usage profiling
    },

    'mappers': [
    ],

    'middleware': [],

    ## Configuration profiles that can be assigned to services
    'middleware_config': {},

    ### Default config values
    'defaults': {

        'module': {},
        'service': {

            'config': {
                'caching': 'none',
                'security': 'none',
                'recording': 'none'
            },

            'args': {

            }

        }

    },

}
