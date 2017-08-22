import logging
import os

from pylons import config,request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect

from pyfisheyes.lib.base import BaseController, render

from pyfisheyes.lib.imageprocessing import ImageProcessing
from pyfisheyes.lib.helpers import md5_for_file, unchroot_path, remove_empty_dirs

from pyfisheyes.model.utils import EventHandle as _eh
from pyfisheyes import model
from webhelpers import paginate
import pyfisheyes.lib.helpers as h
import textile
from pyfisheyes.lib.archivefile import extractall

log = logging.getLogger(__name__)


class EventsController(BaseController):

    
    def index(self):
        c.pagename = "events"
        # Return a rendered template
        #return render('/events.mako')
        # or, return a string        
        return "404"
    
    def list(self,id="0000-00-00"):
        assert id and isinstance(id, basestring)
        c.pagename = "events"
        c.heading = "Events::List"
        eh = _eh.EventHandle(request)
        events = eh.searchEvent(id)

        c.events = paginate.Page(
            events,
            page=int(request.params.get('page', 1)),
            items_per_page = 20,
        ) 
        return render('/derived/events/list.html')
    
    #@h.auth.authorize(h.auth.is_valid_user)
    def new(self,id="0000-00-00 00:00:00"):
        assert id and isinstance(id, basestring)
        c.pagename = "events"
        c.event = model.Events()
        c.event.evdate = id
        c.heading = "Events::New"     
        log.debug("new::upload")
        self.__initValue__()
        if 'd1' in request.params:
            c.d1 = request.params['d1']
        if 'graphs' in request.params:
            c.imgid = request.params['graphs']
        return render('/derived/events/new.html')
    
    #@h.auth.authorize(h.auth.is_valid_user)
    def edit(self,id):
        c.pagename = "events"
        c.heading = "Events::Edit"
        assert id and isinstance(id, basestring)        
        c.event = model.meta.Session.query(model.Events).filter_by(id=id).first()
        
        c.id = id
        graphs = model.meta.Session.query(model.ImgEvent.imgid).filter_by(eid=id)
        self.__initValue__()
        glist = []
        for x, g in enumerate(graphs):
            glist.append(str(g.imgid))
        c.graphs = ','.join(glist)  
        return render('/derived/events/new.html')
    
    #@h.auth.authorize(h.auth.is_valid_user)
    def newsubmit(self):
        text = self.checkImgid()
        if text == "novalue":
            eh = _eh.EventHandle(request)
            result = eh.createEvent()
            redirect('/events/detail/' + str(result.lastrowid))
        else:
            eh = _eh.EventHandle(request)
            result = eh.createEvent()
            eh.createEImg(result.lastrowid)
            redirect('/events/detail/' + str(result.lastrowid))          
            return ''
    def checkImgid(self):
        text = ''
        imgids = request.params['graphs']
        import re
        #p = re.compile('^[0-9]+$')
        
        if imgids:
            try:
                text = "ErrorID"
                imgid = request.params['graphs'].split(',')
                
                for id in imgid:
                    checkid = model.meta.Session.query(model.Categories).filter_by(typeid=int(id)).first()
                    if not checkid:
                        text = text + ' ' + id
                    else:
                        pass
            except ValueError:
                text = "ValueError"
        else:
            text="novalue"
        return text
    
    #@h.auth.authorize(h.auth.is_valid_user)
    def editsubmit(self,id):
        assert id and isinstance(id, basestring)        
        eh = _eh.EventHandle(request)
        text = self.checkImgid()
        if text:
            pass
        else:
            eh.modifyEvent(id)        
            eh.modifyEImg(id)
        redirect('/events/detail/'+id)
        return '' 
        
    
    def detail(self,id):
        c.pagename = "events"
        c.heading = "Events::Detail"
        assert id and isinstance(id, basestring)
        eh = _eh.EventHandle(request)
        c.event = eh.viewEvent(id)
        c.graphs = eh.viewGraphs(id)
        c.messages = eh.viewMessages(id)
        c.imgpath = config["app_conf"]["img_path"]
        if not c.event:
            abort(404)
        
        return render('/derived/events/detail.html')
    def addmsgsubmit(self):
        
        eh = _eh.EventHandle(request)
        eh.addmsg()
        eid = request.params['eventid']
        redirect('/events/detail/'+eid)
        
    def preview(self):
        return h.literal(textile.textile(request.params['data']))
    
    def __initValue__(self):
        c.event_type = ['noset','Story','Failure']
        c.event_status = ['noset','New','Open','Closed']
        c.event_cause = ['noset','Physical Disaster','Component Failure','Capacity Planning','Operator Error or Malicious Users/Code','Planned Administration & Maintenance','Software Bug or Crash']
        c.event_domain = ['noset','yoursite.com','yoursite1.com','yoursite2.com','bbs','mobileapi','all','other']
        c.graphs = ''
    def upload(self):
        log.debug("events::upload")
        """POST /photos/upload: Upload archive of photo"""
        # url(controller='import', action='upload')

        # gp.fileupload stores uploaded filename in fieldstorage
        fieldstorage = request.params.get('file', u'')
        if fieldstorage == u'':
            log.debug("Nothing uploaded")
            abort(400)
        filepath = os.path.join(
            config['global_conf']['upload_dir'],
            fieldstorage.file.read().strip(" \n\r"))
        log.debug("File has been downloaded to %s" %(filepath))
        fieldstorage.file.close()
        res = {
            "status": False,
            "msg": '',
            "dest_uri": ''
        }
        try:
            # extract archive to "import" directory
            extractall(filepath, config['app_conf']['import_dir'])

            # walk in import directory to delete all files that are not photos
            for dirpath, dirs, files in os.walk(
                config['app_conf']['import_dir'], topdown=False):
                for filename in files:
                    abspath = os.path.join(dirpath, filename)
                    log.debug("walk on file: %s" %abspath)
                    
                    if os.path.splitext(abspath)[1].lower() not in ['.jpg', '.jpeg', '.png']:
                        log.debug("Remove non jpeg file: %s" %abspath)
                        os.remove(abspath)
                    else:
                        log.debug("json:" + os.path.split(abspath)[1])
                        log.debug("import_dir:"+config['app_conf']['import_dir'])
                        res = self._createImage('/import/'+os.path.split(abspath)[1])                       
                        
                for subdirname in dirs:
                    abspath = os.path.join(dirpath, subdirname)
                    log.debug("walk on dir: %s" %abspath)
                    try:
                        os.rmdir(abspath)
                    except OSError:
                        log.debug('directory is not empty')
            log.debug("Extraction to %s has succeeded" %(config['app_conf']['import_dir']))
        except Exception, e:
            # TODO: log error in session (flash message)
            log.error(e)
#            raise e
        # delete the uploaded archive if no exception is raised
        os.remove(filepath)
        
        if res['status']:            
            return '/' + config['app_conf']['photos_public_dir'] + '/orig/' + str(res['dest_uri'])
        else:
            return str(res['msg'])
        
    def _createImage(self,path=None):
        """POST /photos: Create a new item"""
        # url('photos')
        
        abspath, uri = unchroot_path(
            path,
            config['app_conf']['import_dir'])
        
        ip = ImageProcessing(
            config['app_conf']['import_dir'],
            os.path.join(
                config['pylons.paths']['static_files'],
                config['app_conf']['photos_public_dir']))

        error = False
        msg = None
        dest_uri = None
        try:
            # check same image has not already been imported
#            f = open(abspath)
#            try:
#                hash = md5_for_file(f)
#            finally:
#                f.close()
#            photo = Session.query(PyGallPhoto).filter_by(md5sum=hash)
#            if photo.count() > 0:
#                raise Exception("Same md5sum already exists in database")

            # process and import photos to public/data/photos dir
            date, dest_uri = ip.process_image(uri)
            # import image in db
#            photo = PyGallPhoto()
#            photo.uri = dest_uri
#            photo.md5sum = hash
#            photo.time = date
#            Session.add(photo)
#            Session.commit()

#            remove_empty_dirs(config['app_conf']['import_dir'])
        except Exception, e:
            error = True
            msg = "%s [%s]" %(str(e), path)
            log.error(msg)

        return {
            "status": not error,
            "msg": msg,
            "dest_uri": dest_uri
        }

    