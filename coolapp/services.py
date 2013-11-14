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

# stdlib
from datetime import datetime

# apptools
from apptools import rpc, model


## HelloMessage - Message for use in ``Hello.test``, containing a simple string.
class HelloMessage(model.Model):

  ''' Contains a simple string message (at :py:attr:`message`) that
      will be echoed back to the callee, unless it contains the
      phrase ``oops``, which will raise :py:class:`HelloException`.

      Default value for ``message`` is ``Hello, world!``. '''

  message = basestring, {'default': 'Hello, world!'}


## Signature - Request and response message that adds a new 'signature' the local ``guestbook``.
class Signature(model.Model):

  ''' Request (and response) to 'sign' the local 'guestbook'. Includes
      an email address, full name, and a short message. '''

  name = basestring
  email = basestring, {'required': True}
  message = basestring, {'default': 'Hello, apptools!'}
  timestamp = datetime


## GuestbookList - Response containing a list of existing guestbook signatures.
class GuestbookList(model.Model):

  ''' Response message that describes existing guestbook
      signatures. '''

  count = int, {'default': 0}
  signatures = Signature, {'repeated': True}


## HelloService - service class for the "Hello" service (for testing only).
@rpc.service('test', enabled=True, debug=False)
class HelloService(rpc.Service):

  ''' Simple 'Hello World!'-type test service.
      Contains only one method, :py:meth:`hello`,
      that takes and returns a :py:class:`HelloMessage`. '''

  # HelloException - `rpc.Error` subclass for testing service errors.
  class HelloException(rpc.Error):

    ''' Sample :py:class:`rpc.Error`-style exception
        class, for use with :py:class:`HelloService`.  '''

  exceptions = rpc.Exceptions(**{
      'generic': HelloException
  })

  @rpc.method(HelloMessage)
  def hello(self, request):

    ''' Accepts a message of type :py:class:`HelloMessage`,
        and returns a new :py:class:`HelloMessage` containing
        the original string passed to us at the attribute
        :py:attr:`HelloMessage.message`.

        If the message contains the phrase ``oops``, we raise
        the local exception :py:attr:`self.exceptions.generic`,
        which usually maps to :py:class:`HelloException`, a
        :py:mod:`protorpc`-style :py:class:`ApplicationError`.

        :param request: Request method submitted from a calling
        API client, of type :py:class:`HelloMessage`.

        :returns: New object of type :py:class:`HelloMessage`
        that contains the same string passed via ``request``
        at :py:attr:`request.message`. '''

    if 'oops' in request.message: raise self.exceptions.generic("can't say oops")
    return HelloMessage(message=request.message)


## GuestbookService - sample service class that mimicks a simple 'guestbook'-style app.
@rpc.service('guestbook', enabled=True, debug=False)
class GuestbookService(rpc.Service):

  ''' Service that presents an interface for a "Guestbook"-style
      app, where visiting users can choose to "sign" by leaving
      their name and email address, along with a short message
      that defaults to "Hello, apptools!". '''

  # InvalidEmail - raised when an invalid email address is encountered.
  class InvalidEmail(rpc.Error):

    ''' Raised when a user's 'email' is detected to be
        an invalid email address. '''

  # AlreadySigned - raised when the same user tries to sign more than once.
  class AlreadySigned(rpc.Error):

    ''' Since a user's email is used as their key name, we
        need to fail if they've already signed the guestbook. '''

  exceptions = rpc.Exceptions(**{
    'user_exists': AlreadySigned,
    'invalid_email': InvalidEmail
  })

  @rpc.method(Signature)
  def sign(self, request):

    ''' Remote method that processes a request to sign the
        guestbook. Accepts a :py:class:`Signature` message
        for storage, and returns it after storing it in
        the underlying adapted datastore.

        :param request: :py:class:`Signature` to add to the
        guestbook.

        :raises InvalidEmail: If a user provides an email
        address is detected to be invalid.

        :raises AlreadySigned: If a user has already signed
        the guestbook.

        :returns: Same :py:class:`Signature` message, with
        a filled-in key and timestamp. '''

    # barely validate the email address
    if '@' not in request.email or '.' not in request.email:
      raise self.exceptions.invalid_email("Woops! That's not a valid email address, you silly goose.")

    # check for an existing signature
    user = model.Key(Signature, request.email)  # `Signature` key with `request.email` as the keyname

    if user.get():
      raise self.exceptions.user_exists("Woops! You've already signed the guestbook. Stop! geez")
    else:

      signature = request

      # everything's cool, store the signature
      signature.timestamp = datetime.datetime.now()
      signature.put()

      return signature

  @rpc.method(rpc.messages.VoidMessage, GuestbookList)
  def list(self, request):

    ''' List existing Guestbook signatures. Basically, this
        just fetches and re-inflates each :py:class:`Signature`,
        then wraps them in a :py:class:`GuestbookList` response.

        :param request: :py:class:`VoidMessage` instance, since
        this method takes no parameters.

        :returns: :py:class:`GuestbookList` describing existing
        guestbook signatures. '''

    # grab up to 50 signatures
    guestbook = Signature.query().fetch()

    return GuestbookList(**{
      'count': len(guestbook),
      'signatures': guestbook
    })
