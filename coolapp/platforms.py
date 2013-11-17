# -*- coding: utf-8 -*-

'''

    apptools-sample: handlers

    :author: Sam Gammon <sam@keen.io>
    :author: Alex Rosner <alex@momentum.io>
    :copyright: (c) Keen IO, 2013
    :license: The inspection, use, distribution, modification or implementation
              of this source code is governed by a private license - all rights
              are reserved by the Authors (collectively, "Keen IO") and held
              under relevant California and US Federal Copyright laws. For full
              details, see ``LICENSE.md`` at the root of this project. Continued
              inspection of this source code demands agreement with the included
              license and explicitly means acceptance to these terms.

'''

from apptools import platform
from coolapp.models import Signature


class Guestbook(platform.Platform):

  '''  '''

  def shortcut_exports(self):

    '''  '''

    return [
      ("guestbook", self)
    ]

  def list(self):

    '''  '''

    signatures = Signature.query().fetch()
    return signatures if signatures else None

  def sign(self, **kwargs):

    '''  '''

    # barely validate the email address
    if not isinstance(kwargs['email'], basestring) or ('@' not in kwargs['email'] or '.' not in kwargs['email']):
      raise ValueError("no  @ or .")

    signature = Signature(**kwargs)

    # everything's cool, store the signature
    signature.put()

    return signature
    