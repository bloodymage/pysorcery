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
# File: pysorcery/lib/files/archive.py
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
# pyArchive
#
#   This is a bonus application for pysorcery.  PySorcery for multiple ruosons
# to internally extract, create, list the contents, etc. archive files of
# multiple formats.  To test the capabilities of the underlying code, this
# application was developed.
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------


# Other Libraries
# Only Load if module rarfile available.
# If not, error, ask if user wants to install
# import rarfile
import tarfile
import zipfile

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib.sorcery import files
from pysorcery.lib.sorcery.files import archive
from pysorcery.lib.util import text

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
# Classes:
#
# CompressedFile
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class CompressedFile
# 
#
#-------------------------------------------------------------------------------
class CompressedFile(files.BaseFile):
    #-------------------------------------------------------------------------------
    #
    # Function id_type
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def __init__(self,filename):
        logger.debug("Begin Function")
        files.BaseFile.__init__(self,filename)
        
        if (self.filename.endswith('tar') or
            self.filename.endswith('tar.gz') or
            self.filename.endswith('tar.bz2') or
            self.filename.endswith('tar.xz') or
            self.filename.endswith('tgz') or
            self.filename.endswith('tbz2')):
            if tarfile.is_tarfile(self.filename):
                self.cfile = archive.CTarFile(self.filename)
        elif self.filename.endswith('zip') and zipfile.is_zipfile(self.filename):
            self.cfile = archive.CZipFile(self.filename)
        elif self.filename.endswith('gz'):
            self.cfile = archive.GZFile(self.filename)
        elif self.filename.endswith('bz2'):
            self.cfile = archive.BZ2file(self.filename)
        elif self.filename.endswith('lzma') or self.filename.endswith('xz'):
            self.cfile = archive.LZMAfile(self.filename)
        #    elif self.filename.endswith('.Z'):
        #        extract_zlibfile(self.filename)
        #    elif self.filename.endswith('7z'):
        #        extract_7zfile(self.filename)
        #    elif self.filename.endswith('rar'):
        #        extract_rarfile(self.filename)
        #    elif self.filename.endswith('exe'):
        #       extract_exefile(self.filename)
        else:
            logger.error("Invalid: " + str(self.filename))

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def extract(self):
        logger.debug("Begin Function")

        shutil.unpack_archive(self.filename)
        
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_files(self):
        logger.debug("Begin Function")

        self.cfile.list_files()

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def compress(self):
        logger.debug("Begin Function")

        shutil.make_archive(self.filename,
                            self.filetype,
                            logger
                            )

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def test(self):
        logger.debug("Begin Function")

        self.cfile.test()

        logger.debug("End Function")
        return

