# -*- coding: utf-8 -*-

'''

    apptools-sample handlers: landing

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


# apptools
from apptools.util import decorators

# handlers
from coolapp import handlers, routing


@routing.rule('/', name='landing')
@decorators.config(debug=True, path='coolapp.handlers.landing.Landing')
class Landing(handlers.WebHandler):

    ''' apptools-sample landing handler. '''

    def get(self):

        ''' HTTP GET '''

        return self.render('landing.html')
