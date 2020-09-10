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
from pysorcery.lib import files
from pysorcery.lib.files import archive
from pysorcery.lib.files import audio
from pysorcery.lib.files import compressed
from pysorcery.lib.files import package
from pysorcery.lib.files import video

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
#   Package
#   Audio
#   Video
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
#    @raises: ,,,
#
#-----------------------------------------------------------------------
class File():
    __file_classes = {
        'archive': archive.Archive,
        'audio': audio.AudioFile,
        'compressed': compressed.CompressedFile,
        'package': package.PackageFile,
        'video': video.VideoFile,
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
    #    @param: filename - ...
    #
    # Returns
    # -------
    #    @return: 'archive'
    #    @return: 'compressed'
    #    @return: 'package'
    #    @return: 'audio' - Not yet implemented
    #    @return: 'video' - Not yet implemented
    #    @return: 'default'
    #
    # Raises
    # ------
    #    @raises: ...
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
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: cls      - ...
    #    @param: filename - ...
    #
    # Returns
    # -------
    #    @param: share_class - ...
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Files():
    __file_classes = {
        'archive': archive.Archives,
        'compressed': compressed.CompressedFiles,
        'audio': audio.AudioFiles,
        'package': package.PackageFiles,
        'default': files.BaseFiles
    }

    #-------------------------------------------------------------------
    #
    # Function id_file_classes
    #
    # Do we have a text file, archive, compressed, or audio file?
    #
    # Inputs
    # ------
    #    @param: filename - ...
    #
    # Returns
    # -------
    #    @return: 'archive'
    #    @return: 'compressed'
    #    @return: 'package'
    #    @return: 'audio' - Not yet implemented
    #    @return: 'video' - Not yet implemented
    #    @return: 'default'
    #
    # Raises
    # ------
    #    @raises: ...
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
    # Function __new__
    #
    # Get the class for the filetype we are working with.
    #
    # Inputs
    # ------
    #    @param: cls - ...
    #
    # Returns
    # -------
    #    @param: share_class - ...
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, *args, **kwargs):

        if 'filelist' in kwargs:
            files = kwargs['filelist']
            name = Files.id_file_class(files[0])
        else:
            files = []
            name = 'default'

        share_class = Files.__file_classes.get(name.lower(), None)
        if share_class:
            return share_class(*args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")


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
#    @raises: ...
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
#    @raises: ...
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Package():
    __package_classes = {
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
    #    @param: cls  - ...
    #    @param: name - ...
    #
    # Returns
    # -------
    #    @param: share_class - list of packages that install filename
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    def __new__(cls, name, *args, **kwargs):
        share_class = Package.__package_classes.get(pkg_mgr.lower(), None)
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class PackageVersions():
    __package_classes = {
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
    #    @param: cls
    #    @param: name - ...
    #
    # Returns
    # -------
    #    @return: share_class - ...
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):

        share_class = PackageVersions.__package_classes.get(pkg_mgr.lower(), None)
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Packages():
    __package_classes = {
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
    #    @param: cls
    #
    # Returns
    # -------
    #    @param: share_class
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, *args, **kwargs):
        share_class = Packages.__package_classes.get(pkg_mgr.lower(), None)
        if share_class:
            return share_class(*args, **kwargs)
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Section():
    __package_classes = {
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
    #    @param: cls - ...
    #    @param: name - ...
    #
    # Returns
    # -------
    #    @return: share_class - ...
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, name, *args, **kwargs):
        share_class = Section.__package_classes.get(pkg_mgr.lower(), None)
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Sections():
    __package_classes = {
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
    #    @param: cls - ...
    #
    # Returns
    # -------
    #    @return: share_class - ...
    #
    # Raises
    # ------
    #    @raises
    #
    #-------------------------------------------------------------------
    def __new__(cls, *args, **kwargs):
        share_class = Sections.__package_classes.get(pkg_mgr.lower(), None)
        if share_class:
            return share_class(*args, **kwargs)
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
#    @raises: ...
#
#-----------------------------------------------------------------------
class Repository():
    __package_classes = {
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
    #    @param: cls
    #    @param: name
    #
    # Returns
    # -------
    #    @return: share_class - ...
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    def __new__(cls, name, *args, **kwargs):
        share_class = Repository.__package_classes.get(pkg_mgr.lower(), None)
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
#    @param: None
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class Repositories():
    __package_classes = {
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
    #    @param: cls
    #
    # Returns
    # -------
    #    @return: share_class - ...
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    @staticmethod
    def __new__(cls, *args, **kwargs):
        share_class = Repositories.__package_classes.get(pkg_mgr.lower(), None)
        if share_class:
            return share_class(*args, **kwargs)
        else:
            raise NotImplementedError("The requested File Class has not been implemented")

#-----------------------------------------------------------------------
#
# Functions
#
#
#
#-----------------------------------------------------------------------
