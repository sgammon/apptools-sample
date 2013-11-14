from __future__ import division
from jinja2 import environment
from jinja2.runtime import LoopContext, TemplateReference, Macro, Markup, TemplateRuntimeError, missing, concat, escape, markup_join, unicode_join, to_string, identity, TemplateNotFound
def run(environment):
    name = '/source/landing.html'

    def root(context, environment=environment):
        parent_template = None
        if 0: yield None
        parent_template = environment.get_template('core/__base.html', '/source/landing.html')
        for name, parent_block in parent_template.blocks.iteritems():
            context.blocks.setdefault(name, []).append(parent_block)
        for event in parent_template.root_render_func(context):
            yield event

    def block_body(context, environment=environment):
        if 0: yield None
        yield u'\n\t<b>hi apptools :)</b>\n'

    blocks = {'body': block_body}
    debug_info = '1=10&3=16'
    return locals()