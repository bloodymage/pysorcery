#! /usr/bin/env python3
#-------------------------------------------------------------------------------
#
# Original BASH version
# Original version Copyright 2001 by Kyle Sallee
# Additions/corrections Copyright 2002 by the Source Mage Team
#
# Python rewrite
# Copyright 2017 Geoff S Derber
#
# This file is part of Sorcery.
#
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Sorcery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import urllib.request
import urllib.parse

# Other Libraries


# Application Libraries
# System Overrides
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery.lib import libtext

# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class BaseURI():
    def __init__(self,uri, download_dir=None):
        logger.debug('Begin Function')

        self.uri = uri
        self.download_dir = download_dir

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class HTTPUri
# 
#
#-------------------------------------------------------------------------------
class HTTPUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        u = urllib.request.urlopen(self.uri)
        scheme, netloc, path, query, fragment = urllib.parse.urlsplit(self.uri)
        filename = os.path.basename(path)
        if not filename:
            filename = 'downloaded.file'
        if self.download_dir:
            filename = os.path.join(self.download_dir, filename)

        with open(filename, 'wb') as f:
            meta = u.info()
            meta_func = meta.getheaders if hasattr(meta, 'getheaders') else meta.get_all
            meta_length = meta_func("Content-Length")
            file_size = None
            if meta_length:
                file_size = int(meta_length[0])
                print("Downloading: {0} Bytes: {1}".format(self.uri, file_size))

            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break

                file_size_dl += len(buffer)
                f.write(buffer)

                status = "{0:16}".format(file_size_dl)
                if file_size:
                    status += "   [{0:6.2f}%]".format(file_size_dl * 100 / file_size)
                    status += chr(13)
                    print(status, end="")
                print()

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class FTPUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class RsyncUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class GitUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class CVSUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class SVNUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class TorrentUri(BaseURI):
    def download(self):
        logger.debug('Begin Function')

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class Uri(HTTPUri,
          FTPUri,
          RsyncUri,
          GitUri,
          CVSUri,
          SVNUri,
          TorrentUri,
          BaseURI):
    def download(self):
        logger.debug('Begin Function')

        if self.uri.startswith('http'):
            HTTPUri.download(self)
        else:
            logger.error('We Fucked Up')
            
        logger.debug('End Function')
        return
