# -*- coding: utf-8 -*-
import os
import datetime
import shutil
import logging
import string
from random import choice
log = logging.getLogger(__name__)

# CONSTANTS
ORIG = "orig"
SCALED = "scaled"

class ImageProcessing:

    def __init__(self,
                 src_dir,
                 dest_dir,
                 crop_dimension=700,
                 crop_quality=80):
        self.src_dir = src_dir
        self.dest_dir = dest_dir
        self.abs_orig_dest_dir = os.path.join(self.dest_dir, ORIG)
        self.abs_scaled_dest_dir = os.path.join(self.dest_dir, SCALED)
        self.dimension = crop_dimension
        self.quality = crop_quality


    def copy_orig(self, uri, dest_uri=None):
        """
        Copy the original image to orig dest directory
        """
        src = os.path.join(self.src_dir, uri)
        dest_uri = uri if dest_uri is None else dest_uri
        dest = os.path.join(self.abs_orig_dest_dir, dest_uri)

        self._check_paths(src, dest)

        # copy original photo
        dirpath = os.path.dirname(dest)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath, 0755)
        shutil.copy2(src, dest)
        log.info("Copied: %s" % dest)


    def unlink(self, uri):
        """
        Remove the original image from disk
        """
        src = os.path.join(self.src_dir, uri)

        self._check_paths(src)

        # unlink original photo
        os.unlink(src)
        log.info("Removed: %s" % src)


    def process_image(self, uri):
        """
        Standard processing for the given image:
        Built the destination relative path based on image timestamp
        Copy the original image to orig dest directory
        Copy the scaled and rotated image to scaled dest directory
        Remove the original image from disk
        """
        date = self._get_datetime(uri)
        ext = os.path.splitext(uri)[1].lower()
        genstr = self._filenamegenerator()
        filename = genstr + ext
        dest_uri = os.path.join(
            date.strftime("%Y"),
            date.strftime("%m"),
            date.strftime("%d"),
            os.path.basename(os.path.join(self.src_dir, filename))
        )
        log.debug("process_image::uri:"+ uri)
        self.copy_orig(uri, dest_uri)
        
        self.unlink(uri)
        return (date, dest_uri)


    def _get_datetime(self, uri):
        """
        Built the destination relative path based on image timestamp
        """
        date = datetime.datetime.today()
        return date


    def _check_paths(self, src, dest=None):
        """
        Checks validity of src and/or dest paths
        """
        # abort if src photo does not exist
        if not os.path.exists(src):
            raise Exception("Source image does not exists")        

        # abort if dest photo already exists
        if dest is not None and os.path.exists(dest):
            raise Exception("Destination image already exists")
        
    def _filenamegenerator(self,size=24):
        s = ''.join([choice(string.letters + string.digits) for i in range(size)])
        ss = s.lower()
        return ss

