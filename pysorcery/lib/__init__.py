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
This file provides the high level Sorcery API.
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
# from pysorcery.lib.sorcery import packages
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
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Files
# 
# The File API.  This is the class that is used for ALL file activities
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
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
    #    content
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def read(self):
        logger.debug('Begin Function')
        if self.format_ != 'Unknown':
            content = compressed.CompressedFile.read(self)
        else:
            content = files.BaseFile.read(self)

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
    #    results
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug('Begin Function')
        
        if self.format_class in shutil.archive_formats:
            results = archive.Archive.search(self, searchstring)
        elif self.format_ != 'Unknown':
            results = compressed.CompressedFile.search(self, searchstring)
        else:
            results = files.BaseFile.search(self, searchstring)

        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Class Files
#
# 
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#
# Returns
# -------
#    None
#
# Raises
# ------
#    ...
# 
#-----------------------------------------------------------------------
class Files(files.BaseFiles):
    def __init__(self, *args, **kwargs):
        files = kwargs['filelist']
        self.files = []
        for f in files:
            self.files.append(File(f))

        return
    #-------------------------------------------------------------------
    #
    # Function diff
    #
    # Diff ...
    # 
    # Inputs
    # ------
    #    @param: self
    #            self.files[0]
    #            self.files[1]
    #
    # Returns
    # -------
    #    Results
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def diff(self):
        logger.debug("Begin Function")

        file1 = self.files[0]
        file2 = self.files[1]

        if (file1.format_class in shutil.archive_formats and
            file2.format_class in shutil.archive_formats):

            list1 = file1.listfiles()
            list2 = file2.listfiles()

            results = list(set(list1) - set(list2))
            results = results + list(set(list2) - set(list1))
        else:
            results = "Diff results"

        logger.debug("Begin Function")
        return results


#-----------------------------------------------------------------------
#
# Class Directory
# 
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
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
#    ...
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Directories(files.BaseFiles):
    pass

#-----------------------------------------------------------------------
#
# Functions
# 
#
#
#-----------------------------------------------------------------------

