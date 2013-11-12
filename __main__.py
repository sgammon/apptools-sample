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

## apptools!
from apptools import dispatch
from apptools.rpc import mappers
from apptools.rpc import dispatch as rpc

try:
  from gevent import pywsgi
  from gevent import monkey

except ImportError:

  ## stdlib wsgi server
  from wsgiref.simple_server import make_server

  def server(interface, port, *args, **kwargs):

    ''' Shim to run with a stdlib WSGI server. '''

    return make_server(interface, port, *args, **kwargs)

else:

  ## monkey patch stdlib
  monkey.patch_all()

  ## gevent will be our server today
  def server(interface, port, *args, **kwargs):

    ''' Shim to run with a gevent-based PyWSGI server. '''

    return pywsgi.WSGIServer((interface, port), *args, **kwargs)

# services! :)
from coolapp.services import *


def run(args):

    '''  '''

    try:
      if len(sys.argv) > 1 and sys.argv[1] == 'services':
        app, interface, port, label = rpc.initialize(), '127.0.0.1', 5001, 'services'
      else:
        app, interface, port, label = dispatch.gateway, '127.0.0.1', 5000, 'app'

      httpd = server(interface, port, app)  # @TODO: ssl support

      print "Serving apptools-sample %s on port %s..." % (label, port)
      httpd.serve_forever()
      return 0
    except Exception as e:
      print "Encountered exception: %s" % e
      return 1


if __name__ == '__main__': sys.exit(run(sys.argv))
