# -*- coding: utf-8 -*-

'''

    apptools-sample config: assets

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


_std_config = {
    'min': False,
    'version_mode': 'getvar'
}


# Installed Assets
_config['apptools.project.assets'] = {

    'debug': False,    # Output log messages about what's going on.
    'verbose': False,  # Raise debug-level messages to 'info'.

    # JavaScript Libraries & Includes
    'js': {


        ### Core Dependencies ###
        ('core', 'core'): {

            'config': _std_config,

            'assets': {
            }

        },

        ### apptools ###
        ('apptools', 'apptools'): {

            'config': _std_config,

            'assets': {
            }

        },

        ### platform (compiled) ###
        ('platform', 'catnip'): {

            'config': _std_config,

            'assets': {
            }

        },

        ### compiled JS templates ###
        ('templates'): {

            'config': _std_config,

            'assets': {
            }
        }

    },


    # Cascading Style Sheets
    'style': {

        # Compiled (SASS) FCM Stylesheets
        ('compiled', 'compiled'): {

            'config': _std_config,

            'assets': {
            }

        },

        # Device-specific Frames
        ('frame', 'compiled/frame'): {

            'config': _std_config,

            'assets': {
            }

        }

    },


    # Other Assets
    'ext': {},

}
