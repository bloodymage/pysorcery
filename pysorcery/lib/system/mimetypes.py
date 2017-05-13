#! /usr/bin/env python3
#-----------------------------------------------------------------------
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
#    Dionysius is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Dionysius.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
from mimetypes import *

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries

# Other Optional Libraries

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

# Map MIME types to file format

CompressedMimetypes = {
    'application/gzip': 'gzip',    
    'application/x-7z-compressed': '7z',
    'application/x-bzip2': 'bzip2',
    'application/x-compress': 'compress',
    'application/x-gzip': 'gzip',    
    'application/x-lzma': 'lzma',
    'application/x-xz': 'xz'
}

ArchiveMimetypes = {
    'application/java-archive': 'zip',
    'application/rar': 'rar',
    'application/x-ace': 'ace',
    'application/x-cpio': 'cpio',
    'application/x-debian-package': 'deb',
    'application/x-iso9660-image': 'iso',
    'application/x-rar': 'rar',
    'application/x-redhat-package-manager': 'rpm',
    'application/x-rpm': 'rpm',
    'application/x-tar': 'tar',
    'application/x-zip-compressed': 'zip',
    'application/zip': 'zip'
}

VerifyMimetypes = {
    'application/x-lzop': 'lzop',
    'application/x-lzip': 'lzip',
    'application/x-lha': 'lzh',
    'application/x-lrzip': 'lrzip',
    'application/x-lzh': 'lzh'
}

encoding_methods = {
    'gzip': 'gzip',
    'xz': 'lzma',
    'bzip2': 'bzip2'
}
