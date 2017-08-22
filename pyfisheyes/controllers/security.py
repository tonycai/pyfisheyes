import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

log = logging.getLogger(__name__)

class SecurityController(BaseController):
    def index(self):
        """
        Show login form. Submits to login/submit
        """
        return render('/login.mako')

    def submit(self):
        """
        Verify username and password
        """
        auth_passed = False
        # Both fields filled?
        username = request.params.get('username')
        password = request.params.get('password')

        #for auth in cfg.auth:
        #    if auth(username=username, password=password, config=cfg):
        if username == "test":
            auth_passed = True
        #        break

        # Mark user as logged in
        if auth_passed:
            session['user'] = username
            log.info(u"User %s logged in" % session['user'])
            session.save()

            # Send user back to the page he originally wanted to get to
            if session.get('path_before_login'):
                redirect(url(session['path_before_login']))
            else: # if previous target is unknown just send the user to a welcome page
                redirect('/')
        else:
            log.error("User %s login failed from host [%s]" % ( username, request.remote_addr))
            session.clear()
            session.save()
            return render('/login.mako')

    def logout(self):
        """
        Logout the user and display a confirmation message
        """
        if 'user' in session:
            log.info("User %s logged out" % session['user'])
            del session['user']
            session.save()
        redirect(url("login"))

    def failed(self):
        return render('/auth_failed.mako')
