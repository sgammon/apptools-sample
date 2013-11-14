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
import sys, os, inspect

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'coolapp'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'coolapp/lib'))

# coolapp!
from coolapp import handlers
from coolapp import services
from coolapp import templates

# import all the things
from coolapp.handlers import *
from coolapp.services import *
from coolapp.templates import *

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


def devserver(environ, start_response):

  '''  '''

  if not environ.get('PATH_INFO', '/').startswith('/assets'):

    # it's an app path, defer to apptools
    response = dispatch.gateway(environ, start_response)
    return response

  else:

    # it's a static asset path
    filepath = '/'.join(filter(lambda x: x != '', (environ['PATH_INFO'].split('?')[0] if '?' in environ['PATH_INFO'] else environ['PATH_INFO']).split('/')))

    try:
      with open(os.path.abspath(os.path.join(os.path.dirname(__file__), filepath)), 'r') as asset_handle:
        contents = asset_handle.read()

        mimetype = {

          # mapped content types
          'css': 'text/css',
          'js': 'application/javascript',
          'svg': 'image/svg+xml',
          'png': 'image/png',
          'gif': 'image/gif',
          'jpeg': 'image/jpeg',
          'jpg': 'image/jpg',
          'webp': 'image/webp',
          'manifest': 'text/cache-manifest',
          'txt': 'text/plain',
          'html': 'text/html',
          'xml': 'text/xml',
          'json': 'application/json'

        }.get(filepath.split('.')[-1], 'application/octet-stream')

        start_response('200 OK', [

          ('Content-Type', mimetype)

        ])

        return contents

    except IOError as e:
      
      import pprint;

      if 'no such file' in str(e).lower():
        ## 404 time nao
        status, message = '404', 'Not Found'

      elif 'permission denied' in str(e).lower():
        ## 403 time you scoundrel
        status, message = '403', 'Forbidden'

      start_response('%s %s' % (status, message), [('Content-Type', 'text/plain')])


      return '''

        <!doctype html>
        <html>
          <head>
            <title>%s</title>
          </head>
          <body>
            <h2>%s</h2>
            <br /><br />
            <b>Context:</b>
            <pre>
               %s
            </pre>
            <br />
            <br />
            <b>Exception:</b>
            <pre>
               %s
            </pre>
          </body>
        </html>

      ''' % (status, message, pprint.pprint(environ), pprint.pprint(e))



def run(args):

  '''  '''

  try:
    if len(sys.argv) > 1 and sys.argv[1] == 'services':
      app, interface, port, label = rpc.initialize(), '127.0.0.1', 8081, 'services'
    else:
      app, interface, port, label = dispatch.gateway, '127.0.0.1', 8080, 'app'

    httpd = server(interface, port, devserver)  # @TODO: ssl support

    print "Serving apptools-sample %s on port %s..." % (label, port)
    httpd.serve_forever()
    return 0
  except Exception as e:
    print "Encountered exception: %s" % e
    return 1


if __name__ == '__main__': sys.exit(run(sys.argv))
