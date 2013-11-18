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
        l_signatures = context.resolve('signatures')
        if 0: yield None
        yield u'\n\t<!-- Form submit code -->\n\t<script type="text/javascript">\n\n\t\t\t// renders a single signature\n\t\t\tfunction renderSignature(sig) {\n\n\t\t\t\tsource = "<li><b><a href=\'mailto:" + sig.email + "\'>" + sig.name + "</a></b>";\n\t\t\t\tsource += "<br />" + sig.email + "<br />";\n\t\t\t\tsource += "<p>" + sig.message + "</p>";\n\t\t\t\treturn source;\n\n\t\t\t};\n\n\t\t\t// renders existing signatures\n\t\t\tfunction renderGuestbook(response) {\n\n\t\t\t\twrapper = "<div id=\'guestbook\'><ul id=\'siglist\'>";\n\n\t\t\t\tfor (var i = 0; i < response.signatures.length; i++) {\n\t\t\t\t\twrapper += renderSignature(response.signatures[i]);\n\t\t\t\t}\n\n\t\t\t\twrapper += "</ul></div>";\n\t\t\t\tdocument.getElementById(\'guestbook_wrap\').innerHTML = wrapper;\n\n\t\t\t};\n\n\t\t\t// shows a flashed message\n\t\t\tfunction flash(id) {\n\t\t\t\tdocument.getElementById(id).classList.remove(\'hidden\');\n\t\t\t\tsetTimeout(function () {\n\t\t\t\t\tdocument.getElementById(id).classList.add(\'hidden\');\n\t\t\t\t}, 2500);\n\t\t\t}\n\n\t\t\t// refreshes guestbook list\n\t\t\tfunction refreshGuestbook(event) {\n\n\t\t\t\tevent.preventDefault();\n\t\t\t\tevent.stopPropagation();\n\n\t\t\t\t$.apptools.api.guestbook.list().fulfill({\n\n\t\t\t\t\tsuccess: function (list) {\n\t\t\t\t\t\trenderGuestbook(list);\n\t\t\t\t\t\tflash(\'list_success\');\n\t\t\t\t\t},\n\n\t\t\t\t\tfailure: function (error) {\n\n\t\t\t\t\t\t// show error\n\t\t\t\t\t\tflash(\'list_failure\');\n\n\t\t\t\t\t\t// log a bunch\n\t\t\t\t\t\tconsole.error(\'Failed to list guestbook signatures.\');\n\t\t\t\t\t\tconsole.error(error);\n\n\t\t\t\t\t}\n\n\t\t\t\t});\n\n\t\t\t}\n\n\t\t\t// submits a new signature\n\t\t\tfunction submitSignature(event) {\n\n\t\t\t\tvar data = {  // collect form data\n\t\t\t\t\t\tname: document.getElementById(\'name_field\').value,\n\t\t\t\t\t\temail: document.getElementById(\'email_field\').value,\n\t\t\t\t\t\tmessage: document.getElementById(\'message_field\').value\n\t\t\t\t\t};\n\n\t\t\t\t\tevent.preventDefault();\n\t\t\t\t\tevent.stopPropagation();\n\n\t\t\t\t\t// show pending text, log\n\t\t\t\t\tconsole.log(\'Submitting form...\', data);\n\n\t\t\t\t\t// submit via `guestbook` service\n\t\t\t\t\t$.apptools.api.guestbook.sign(data).fulfill({\n\n\t\t\t\t\t\tsuccess: function (signature) {\n\n\t\t\t\t\t\t\t// add to local signatures and refresh\n\t\t\t\t\t\t\tvar newsig = document.createElement(\'li\');\n\t\t\t\t\t\t\t\tnewsig.innerHTML = renderSignature(signature),\n\t\t\t\t\t\t\t\tnosigs = document.getElementById(\'nosigs\');\n\n\t\t\t\t\t\t\t\tif (nosigs) {\n\t\t\t\t\t\t\t\t\tnosigs.parentElement.removeChild(nosigs);\n\t\t\t\t\t\t\t\t}\n\n\t\t\t\t\t\t\t\tdocument.getElementById(\'siglist\').appendChild(newsig);\n\n\t\t\t\t\t\t\t\t// close modal\n\t\t\t\t\t\t\t\t$(\'#signModal\').modal(\'hide\');\n\n\t\t\t\t\t\t\t\t// show success message\n\t\t\t\t\t\t\t\tflash(\'sign_success\');\n\n\t\t\t\t\t\t},\n\n\t\t\t\t\t\tfailure: function (error) {\n\n\t\t\t\t\t\t\t// show failure message\n\t\t\t\t\t\t\tflash(\'sign_failure\');\n\n\t\t\t\t\t\t\t// log a bunch\n\t\t\t\t\t\t\tconsole.error(\'Failed to sign guestbook.\');\n\t\t\t\t\t\t\tconsole.error(error);\n\n\t\t\t\t\t\t}\n\n\t\t\t\t\t});\n\n\t\t}\n\n\t</script>\n\n\t<!-- Alert messages -->\n\t<div id=\'sign_success\' class="alert alert-success hidden">You signed the guestbook :)</div>\n\t<div id=\'sign_failure\' class="alert alert-danger hidden">Oh noez! Couldn\'t sign the guestbook</div>\n\t<div id=\'list_success\' class="alert alert-success hidden">Yay! Refreshed the guestbook :)</div>\n\t<div id=\'list_failure\' class="alert alert-danger hidden">Oh noez! Couldn\'t refresh the guestbook</div>\n\n\t<!-- Button trigger modal -->\n\t<button class="btn btn-primary btn-lg" data-toggle="modal" data-target="#signModal">\n\t  Sign the guestbook\n\t</button>\n\t<button class="btn btn-info btn-lg" data-toggle="modal" onclick="refreshGuestbook(event);">\n\t  Refresh signatures\n\t</button>\n\n\t<!-- Sign modal -->\n\t<div class="modal fade" id="signModal" tabindex="-1" role="dialog" aria-labelledby="Sign Guestbook" aria-hidden="true">\n\n\t  <form onsubmit="submitSignature(event);">\n\t  \t<div class="modal-dialog">\n\t\t    <div class="modal-content">\n\t\t      <div class="modal-header">\n\t\t        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>\n\t\t        <h4 class="modal-title">Sign the guestbook</h4>\n\t\t      </div>\n\t\t      <div class="modal-body">\n\t\t        <div class="input-group">\n\t\t\t\t  <span class="input-group-addon">NAME:</span>\n\t\t\t\t  <input id=\'name_field\' type="text" class="form-control" placeholder="Full name">\n\t\t\t\t</div>\n\t\t\t\t<div class="input-group">\n\t\t\t\t  <span class="input-group-addon">EMAIL:</span>\n\t\t\t\t  <input id=\'email_field\' type="text" class="form-control" placeholder="Email address">\n\t\t\t\t</div>\n\t\t\t\t<div class="input-group">\n\t\t\t\t  <span class="input-group-addon">MESSAGE:</span>\n\t\t\t\t  <textarea id=\'message_field\' type="text" class="form-control" placeholder="Message"></textarea>\n\t\t\t\t</div>\n\t\t      </div>\n\t\t      <div class="modal-footer">\n\t\t        <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>\n\t\t        <button type="button" class="btn btn-primary" onclick="submitSignature(event);">Sign! :)</button>\n\t\t      </div>\n\t\t    </div><!-- /.modal-content -->\n\t\t  </div><!-- /.modal-dialog -->\n\t  </form> <!-- end form -->\n\t</div><!-- /.modal -->\n\n\t<!-- Guestbook list -->\n\t<br />\n\t<h2>Guestbook signatures</h2>\n\t<div id=\'guestbook_wrap\'>\n\t\t'
        if l_signatures:
            if 0: yield None
            yield u'\n\t\t<div id="guestbook">\n\t\t\t<ul id=\'siglist\'>\n\t\t\t'
            l_sig = missing
            for l_sig in l_signatures:
                if 0: yield None
                yield u'\n\t\t\t\t<li>\n\t\t\t\t\t<b><a href="mailto:%s">%s</a></b>\n\t\t\t\t\t<br />%s<br />\n\t\t\t\t\t<p>\n\t\t\t\t\t\t%s\n\t\t\t\t\t</p>\n\t\t\t\t</li>\n\t\t\t' % (
                    environment.getattr(l_sig, 'email'), 
                    environment.getattr(l_sig, 'name'), 
                    environment.getattr(l_sig, 'email'), 
                    environment.getattr(l_sig, 'message'), 
                )
            l_sig = missing
            yield u'\n\t\t\t</ul>\n\t\t</div>\n\t\t'
        else:
            if 0: yield None
            yield u"\n\t\t\t<b id='nosigs'>no signatures yet :(</b>\n\t\t\t<ul id='siglist'></ul>\n\t\t"
        yield u'\n\t</div>\n'

    blocks = {'body': block_body}
    debug_info = '1=10&3=16&174=20&177=24&179=27&180=29&182=30'
    return locals()