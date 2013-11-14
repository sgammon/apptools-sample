#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''

    apptools-sample: setup

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
import sys


## Globals
requirements = []
try:
    with open('./requirements.txt') as requirements_file:
        map(requirements.append, map(lambda x: x.replace('\n', ''), requirements_file))
except OSError as e:
    print "!!! Failed to load requirements.txt. Crashing super hard now. !!!"
    sys.exit(1)

info = {
    "name": "apptools_sample",
    "version": "0.1a",
    "description": "Sample of Apptools",
    "author": "Keen IO",
    "scripts": ["scripts/web"],
    "author_email": "sam@keen.io",
    "url": "https://github.com/keenlabs/apptools-sample",
    "packages": ["coolapp", "coolapp_tests"],
    "install_requires": requirements,
    "tests_require": ["nose"]
}


def run(cli=False):

    ''' Runs the setup routine, which delegates directly to
        :py:mod:`setuptools` via :py:func:`setuptools.setup`,
        along with some basic package metadata.

        :param cli: Flag indicating whether we're running
        from the command line. Triggers behavior like returning
        UNIX-style error/success codes instead of ``bool``.

        :returns: ``True``/``False`` or ``0``/``1``, depending
        on whether you're running from Python or the command line,
        respectively, according to the successfullness of the
        install routine kickoff. '''

    try:
        # == setuptools == #
        import setuptools

    except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()
    
    try:
        from setuptools import setup
    except ImportError:
        print "!!! Could not find setuptools or use ez_setup. !!!"
        if cli: return 1  # return failure exit code
        return False

    # == call module setup == #
    setup(**info)

    if cli: return 0  # return zero exit code if running via CLI
    return True


if __name__ == "__main__": sys.exit(run(True))
