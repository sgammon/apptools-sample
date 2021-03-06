# -*- coding: utf-8 -*-

'''

    apptools-sample: models

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
import datetime

# model API
from apptools import model


## Signature - Request and response message that adds a new 'signature' the local ``guestbook``.
class Signature(model.Model):

  ''' Request (and response) to 'sign' the local 'guestbook'. Includes
      an email address, full name, and a short message. '''

  __adapter__ = "RedisAdapter"  # store signatures in redis plz

  name = basestring
  email = basestring, {'required': True}
  message = basestring, {'default': 'Hello, apptools!'}
