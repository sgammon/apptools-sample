# -*- coding: utf-8 -*-

'''

    apptools-sample: services

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

from apptools import rpc
from apptools import model

from protorpc import remote


class HelloMessage(model.Model):

  '''  '''

  message = basestring, {'default': 'Hello, world!'}


class HelloException(remote.ApplicationError):

  '''  '''

  pass


@rpc.service
class HelloService(rpc.Service):

  ''' '''

  name = 'test'

  exceptions = rpc.Exceptions(**{
      'generic': HelloException
  })

  @rpc.method(HelloMessage)
  def hello(self, request):

    '''  '''

    if 'oops' in request.message:
      raise self.exceptions.generic("can't say oops")

    return HelloMessage(message=request.message)




