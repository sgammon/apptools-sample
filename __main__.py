#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    apptools-sample: dev entrypoint

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
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'coolapp'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'coolapp/lib'))

# coolapp!
from coolapp import config
from coolapp import handlers
from coolapp import services
from coolapp import templates

# import all the things
from coolapp.handlers import *
from coolapp.services import *
from coolapp.templates import *

# apptools!
from apptools import dispatch
from apptools.util import debug
from apptools.util import devserver


## start the devserver up
devserver.devserver()
