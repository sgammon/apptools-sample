#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

"""

    gaefy.jinja2.compiler
    ~~~~~~~~~~~~~~~~~~~~~

    Helper functions to parse Jinja2 templates and store them as Python code.
    The compiled templates can be loaded using gaefy.jinja2.code_loaders,
    avoiding all the parsing process.

    To compile a whole dir:

        from jinja2 import Environment
        from gaefy.jinja2.compiler import compile_dir

        env = Environment()
        src_path = '/path/to/templates'
        dst_path = '/path/to/templates_compiled'

        compile_dir(env, src_path, dst_path)

    :copyright: 2009 by tipfy.org.
    :license: BSD, see LICENSE.txt for more details.

"""

import sys, os

_extra_paths = [
	'coolapp/',
	'coolapp/lib'
]

for path in filter(lambda x: x not in sys.path, _extra_paths):
    sys.path.insert(0, path)

#import bootstrap
import re, json
from os import path, listdir, mkdir

from jinja2 import Environment
from jinja2.ext import with_, autoescape, do, loopcontrols

#from apptools.api.output import content


def compile_file(env, src_path, dst_path, encoding='utf-8', base_dir='',
    as_module=False):
    """Compiles a Jinja2 template to python code.
    Params:
        `env`: a Jinja2 Environment instance.
        `src_path`: path to the source file.
        `dst_path`: path to the destination file.
        `encoding`: template encoding.
        `base_dir`: the base path to be removed from the compiled template
            filename.
        `as_module`: if True, saves the compiled code with a .py extension.
    """
    # Read the template file.
    src_file = file(src_path, 'r')
    source = src_file.read().decode(encoding)
    src_file.close()

    # Compile the template to raw Python code..
    name = src_path.replace(base_dir, '')
    raw = env.compile(source, name=name, filename=name, raw=True)

    if as_module:
        # Save as .py
        name, ext = path.splitext(dst_path)
        dst_path = name + '.py'
        if path.isdir(name):
            raise Exception("Template name conflict: %s is a module directory, "
               "so %s%s can't exist as a template." % (name, name, ext))

    # Save to the destination.
    dst_file = open(dst_path, 'w')
    dst_file.write(raw)
    dst_file.close()


def compile_dir(env, src_path, dst_path, pattern=r'^.*\.(html|js)$',
    encoding='utf-8', base_dir=None, as_module=False):
    """Compiles a directory of Jinja2 templates to python code.
    Params:
        `env`: a Jinja2 Environment instance.
        `src_path`: path to the source directory.
        `dst_path`: path to the destination directory.
        `encoding`: template encoding.
        `pattern`: a regular expression to match template file names.
        `base_dir`: the base path to be removed from the compiled template
            filename.
        `as_module`: if True, creates __init__.py for each directory and saves
            the compiled code with a .py extension.
     """
    if base_dir is None:
        # In the first call, store the base dir.
        base_dir = src_path

    if as_module and path.isdir(dst_path):
        # Create a __init__.py if not already there.
        init = path.join(dst_path, '__init__.py')
        if not path.exists(init):
            open(init, 'w').close()

    for filename in listdir(src_path):
        src_name = path.join(src_path, filename)
        dst_name = path.join(dst_path, filename)

        if path.isdir(src_name):
            mkdir(dst_name)
            compile_dir(env, src_name, dst_name, encoding=encoding,
                base_dir=base_dir, as_module=as_module)
        elif path.isfile(src_name) and re.match(pattern, filename):
            compile_file(env, src_name, dst_name, encoding=encoding,
                base_dir=base_dir, as_module=as_module)


def run(module=None, sources=None, target=None):

    import os

    if not module or not sources or not target:
        join = os.path.join
        base = os.path.dirname(os.path.abspath(os.path.realpath(__file__))) ## tools/bin
        base = os.path.dirname(base) ## tools/
        #base = os.path.dirname(base) ## /

        module = base+'/coolapp/templates'
        sources = base+'/coolapp/templates/source'
        target = base+'/coolapp/templates/compiled'

    env = Environment(extensions=[with_, autoescape, do, loopcontrols], optimized=True)  #, content])
    env.filters['json'] = json.dumps
    compile_dir(env, sources, target, base_dir=module, as_module=True)
    
    return 0

if __name__ == "__main__":
    exit(run())
