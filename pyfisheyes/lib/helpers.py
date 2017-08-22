"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password
import os
import hashlib

from webhelpers.html import escape, HTML, literal, url_escape, literal
from webhelpers.html.tags import *
from pylons import url
from pylons.controllers.util import redirect

from formbuild.helpers import field
from formbuild import start_with_layout as form_start, end_with_layout as form_end
from formbuild.helpers import checkbox_group

from routes import url_for

from pyfisheyes.lib import auth

from types import StringType, UnicodeType

def md5_for_file(f, block_size=2**20):
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return unicode(md5.hexdigest())

def unchroot_path(path, chroot):
    if type(path) != StringType and type(path) != UnicodeType:
        raise Exception('Bad path (type is not string)')
    while path.startswith(os.sep):
        path = path[len(os.sep):]
    if not path.startswith(os.path.basename(chroot)):
        raise Exception('Bad path (no chroot prefix)')

    uri = os.path.normpath(path[len(os.path.basename(chroot)):])
    while uri.startswith(os.sep):
        uri = uri[len(os.sep):]
    unchrooted = os.path.normpath(os.path.join(chroot, uri))

    if not unchrooted.startswith(chroot):
        raise Exception('Bad path (chroot protected)')
    if not os.path.exists(unchrooted):
        raise Exception('Bad path (does not exist): %s' %unchrooted)

    return (unchrooted, uri)

def remove_empty_dirs(root):
    # remove empty directories
    for dirpath, dirs, files in os.walk(root, topdown=False):
        for subdirname in dirs:
            try:
                os.rmdir(os.path.join(dirpath, subdirname))
            except OSError:
                pass
