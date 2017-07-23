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
from pysorcery.lib import sorcery
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
class File():
    __file_classes = {
        'archive': archive.Archive,
        'compressed': compressed.CompressedFile,
        'default': files.BaseFile
    }

    @staticmethod
    def id_file_class(filename):
        mimetype, encoding = mimetypes.guess_type(filename)
        if mimetype in mimetypes.ArchiveMimetypes:
            return 'archive'
        elif encoding in mimetypes.CompressedMimetypes:
            return 'compressed'
        else:
            return 'default'
        
    @staticmethod
    def getcls(name, filename, *args, **kwargs):
        name = File.id_file_class(filename)

        share_class = File.__file_classes.get(name.lower(), None)        
        if share_class:
            return share_class(filename, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class PackageVersions(sorcery.BasePackageVersions):
    pass

#-----------------------------------------------------------------------
#
# Class Packages
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
class Packages(sorcery.BasePackages):
    pass

#-----------------------------------------------------------------------
#
# Class Section
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
class Section(sorcery.BaseSection):
    pass

#-----------------------------------------------------------------------
#
# Class Sections
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
class Sections(sorcery.BaseSections):
    pass

#-----------------------------------------------------------------------
#
# Class Repository
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
class Repository(sorcery.BaseRepository):
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
