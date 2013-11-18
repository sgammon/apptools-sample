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


_config = {}


_config['devserver'] = {
  
  'debug': True,

  'bind': {
    'address': '127.0.0.1',
    'port': 8080
  },

  'static': {
    
    'caching': {
      'enabled': True,
      'serve304': True,
      'timeout': 500,  # defaults to 5 minutes
      'mode': 'public'  # defaults to `public`
    },

    'source': [
      'assets/js/source/*',
      'assets/style/source/*'
    ],

    'compiled': [
      'assets/js/static/*',
      'assets/style/static/*'
    ]
  
  }

}
