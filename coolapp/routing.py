# -*- coding: utf-8 -*-

'''

    apptools-sample: routing

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

# webapp2
from webapp2 import Route
from webapp2_extras import routes


## Globals
rules, _VERSION_PREFIX = [], 'v1'


def get_rules():

    ''' URL routes. '''

    return [

        routes.HandlerPrefixRoute('coolapp.handlers.', [
            # app-wide non-decorator routes go here
        ])

    ] + rules


def rule(*args, **kwargs):

    ''' Decorator for a handler that binds it to a newly-constructed
        route. Usable either as a callable decorator or a bound decorator. '''

    global rules

    # definitely a bound decorator (look for a `route` attribute)
    if len(args) == 1 and isinstance(args[0], (type, type(rule))):
        target = args.pop()
        if hasattr(target, 'route'):
          rules.append(Route(target.route, name=target.__name__, handler='.'.join((target.__module__, target.__name__))))
        else:
          raise AttributeError('Bound-rule handler had no route: "%s".' % target)
        return target

    # definitely a callable decorator
    if 'handler' in kwargs:
      new_route = Route(*args, **kwargs)
      rules.append(new_route)

    def _decorate(target):

        ''' Decorate that target! '''

        if 'handler' not in kwargs:
          kwargs['handler'] = '.'.join((target.__module__, target.__name__))
          new_route = Route(*args, **kwargs)
          rules.append(new_route)

        target.route = new_route
        return target

    return _decorate
