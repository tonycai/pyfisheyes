import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

import os
import shutil
from pylons import config

log = logging.getLogger(__name__)

class FormController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/form.mako')
        # or, return a string
        #return 'Hello World'
        return render('/form.mako')

    def submit(self):
        return "hello, name: %s" % request.params['name']

    def upload(self):
        name   = request.POST['name']
        myfile = request.POST['file']
        local_name = os.path.join(config['app_conf']['upload_dir'], myfile.filename)
        local_file = open(local_name, "wb")
        shutil.copyfileobj(myfile.file, local_file)
        myfile.file.close()
        local_file.close()
        return "hello, name: %s, upload: %s" % (name, myfile.filename)
