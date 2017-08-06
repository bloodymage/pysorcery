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
# Other Application Libraries
from pysorcery.lib.sorcery import apt
from pysorcery.lib.sorcery import smgl
#from pysorcery.lib.util import config
from pysorcery.lib.util import files
from pysorcery.lib.util.files import archive
from pysorcery.lib.util.files import audio
from pysorcery.lib.util.files import compressed
from pysorcery.lib.util.files import package

# Conditional Libraries

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

# Get System Package Manoager
pkg_mgr = distro.distro_group[distro.distro_id]
#-----------------------------------------------------------------------
#
# Classes
#
# File
# Files
# Directory
# Directories
# Package
# PackageVersions
# Packages
# Section
# Sections
# Repository
# Repositories
#
#-----------------------------------------------------------------------
    
#-----------------------------------------------------------------------
#
# Class File
# 
# The File API.  This is a factory class that determines which class
# is used for each of the different file types.
#
# Supported File types
# --------------------
#   Text
#   Archive
#   Compressed
#   Audio
# 
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
        'audio': audio.AudioFile,
        'package': package.PackageFile,
        'default': files.BaseFile
    }

    #-------------------------------------------------------------------
    #
    # Function id_file_classes
    #
    # Do we have a text file, archive, compressed, or audio file?
    #
    # Inputs
    # ------
    #    @param: filename - 
    #
    # Returns
    # -------
    #    @return: 'archive'
    #    @return: 'compressed'
    #    @return: 'default'
    #    @return: 'audio' - Not yet implemented
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def id_file_class(filename):
        mimetype, encoding = mimetypes.guess_type(filename)

        try:
            id_ = mimetypes.fileclasstypes[mimetype]
        except:
            try:
                id_ = mimetypes.fileclasstypes[encoding]
            except:
                id_ = 'default'

        return id_
                
    #-------------------------------------------------------------------
    #
    # Function getcls
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, filename, *args, **kwargs):
        
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
class Package():
    __file_classes = {
        'smgl': smgl.Spell,
        'apt': apt.Package
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def __new__(cls, name, *args, **kwargs):
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class PackageVersions():
    __file_classes = {
        'smgl': smgl.SpellVersions,
        'apt': apt.PackageVersions
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class Packages():
    __file_classes = {
        'smgl': smgl.Spells,
        'apt': apt.Packages
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class Section():
    __file_classes = {
        'smgl': smgl.Section,
        'apt': apt.Section
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class Sections():
    __file_classes = {
        'smgl': smgl.Sections,
        'apt': apt.Sections
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class Repository():
    __file_classes = {
        'smgl': smgl.Grimoire,
        'apt': apt.Repository
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

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
class Repositories():
    __file_classes = {
        'smgl': smgl.Codex,
        'apt': apt.Repositories
    }
                
    #-------------------------------------------------------------------
    #
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: filename
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):
        
        share_class = Package.__file_classes.get(pkg_mgr.lower(), None)        
        if share_class:
            return share_class(name, *args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

#-----------------------------------------------------------------------
#
# Functions
# 
#
#
#-----------------------------------------------------------------------
