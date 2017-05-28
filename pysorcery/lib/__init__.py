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
# File: pysorcery/lib/__init__.py
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
# This file is the pysorcery API.  All files should reference this file.
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
# Other Application Libraries
from pysorcery.lib.sorcery import packages
#from pysorcery.lib.sorcery import repositories
#from pysorcery.lib.util import config
from pysorcery.lib.util import files
from pysorcery.lib.util.files import archive
from pysorcery.lib.util.files import compressed
#from pysorcery.lib.util import text
#from pysorcery.lib.util import url

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
# Files
# FileList
# Directories
# DirectoryList
# Package
# PackageList
# Repository
# RepositoryList
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Files
# 
# The File API.  This is the class that is used for ALL file activities
#
#-----------------------------------------------------------------------
class File(compressed.CompressedFile, archive.Archive, files.BaseFile):
    def read(self):
        if self.format_ != 'Unknown':
            content = compressed.CompressedFile.read(self)
        else:
            content = files.BaseFile.read(self)

        logger.debug('End Function')
        return content


#-----------------------------------------------------------------------
#
# Class FileList
# 
#
#-----------------------------------------------------------------------
class Files(files.BaseFiles):
    pass

#-----------------------------------------------------------------------
#
# Class Directories
# 
#
#-----------------------------------------------------------------------
#class Directories(files.DebianDirectories,files.BaseDirectories):
# pass

#-----------------------------------------------------------------------
#
# Functions
# 
# Repack
# Diff
#
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function repack
#
# Input:  @param: srcfile - the original file
#         @param: dstfile - the new file we are creating with the new
#                           compression method.
# Return: None
#
#-----------------------------------------------------------------------
def repack(srcfile, dstfile, componly=False):
    logger.debug('Begin Function')

    if (self.mimetype not in mimetypes.ArchiveMimetypes or
        componly is True):
        source_file = Files(srcfile)
        source_file.decompress(None)
    
        dest_file = Files(dstfile)
        dest_file.compress(source_file.basename)
    else:
        print('Fix Me')
        
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function diff
#
# Input:  @param: file1 - the original file
#         @param: file2 - the new file we are creating with the new
#                           compression method.
# Return: None
#
#-----------------------------------------------------------------------
def filediff(file1, file2, size=False, contents=False):
    logger.debug('Begin Function')

    logger.debug('End Function')
    return
