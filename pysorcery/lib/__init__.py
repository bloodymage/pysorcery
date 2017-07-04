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
# This file is the pysorcery API.  All applications should reference this file.
#
#-----------------------------------------------------------------------
"""
This file provides the top level Sorcery API.
"""
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
from pysorcery.lib.system import shutil
# Other Application Libraries
from pysorcery.lib.sorcery import packages
#from pysorcery.lib.sorcery import repositories
#from pysorcery.lib.util import config
from pysorcery.lib.util import files
from pysorcery.lib.util.files import archive
from pysorcery.lib.util.files import compressed

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
# File
# Files
# Directory
# Directories
# Package
# Repositories
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class File
# 
# The File API.  This is the class that is used for ALL file activities
# Parent classes: CompressedFile, Archive, BaseFile
#
# Inputs
# ------
#    @param: filename - The name of the file to operate on.
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class File(compressed.CompressedFile, archive.Archive, files.BaseFile):
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.format
    #
    # Returns
    # -------
    #    @return: content
    #
    # Raises
    # ------
    #    FileNotFoundError - Fix Me
    #    IsADirectoryError
    #    PermissionError
    #
    #-------------------------------------------------------------------
    def read(self):
        logger.debug('Begin Function')
        try:
            content = files.BaseFile.read(self)
        except Exception as msg:
            logger.error(msg)
        
        logger.debug('End Function')
        return content

    #-------------------------------------------------------------------
    #
    # Function search
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: results
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def search(self,
               pattern,
               verbosity=0,
               interactive=True):
        logger.debug('Begin Function')

        if self.mimetype in mimetypes.ArchiveMimetypes:
            results = archive.Archive.search(self,
                                             pattern,
                                             verbosity=0,
                                             interactive=True)
        else:
            raise NotImplementedError('BaseFile search Not implemented')            

        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Class Files
#
# The Files API.  This class provides toplevel functions for working
# with multiple files.
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
# 
#-----------------------------------------------------------------------
class Files(archive.Archives, files.BaseFiles):
    def __init__(self, *args, **kwargs):
        self.files = kwargs['filelist']

        return


#-----------------------------------------------------------------------
#
# Class Directory
# 
# Inputs
# ------
#    @param: filename
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Directory(files.BaseDirectory):
    pass

#-----------------------------------------------------------------------
#
# Class Directories
# 
# Inputs
# ------
#    @param: filelist
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Directories(files.BaseDirectories):
    pass

#-----------------------------------------------------------------------
#
# Class Package
# 
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Package(sorcery.BasePackage):
    pass

#-----------------------------------------------------------------------
#
# Class Repositories
# 
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Repositories(sorcery.BaseRepositories):
    pass

#-----------------------------------------------------------------------
#
# Functions
# 
#
#
#-----------------------------------------------------------------------
