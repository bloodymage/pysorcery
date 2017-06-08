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
# File: pysorcery/lib/util/files/archive/__init__.py
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
# This implements the archive classes
#
# ...
#
#-----------------------------------------------------------------------
"""
Impliments classes for working with archive files.
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
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
from pysorcery.lib.system import shutil
# Other Application Libraries
from pysorcery.lib import util
from pysorcery.lib.util import files

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
# Archive
# Archives
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
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
class Archive(files.BaseFile):        
    #-------------------------------------------------------------------
    #
    # Function extract
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def extract(self, extractdir=None):
        logger.debug('Begin Function')
        
        shutil.unpack_archive(self.filename, extractdir)

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function create
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def create(self, root_dir=None, base_dir=None, compression_lvl=9):
        logger.debug('Begin Function')
        
        shutil.make_archive(self.basename,
                            self.format_,
                            root_dir,
                            base_dir)

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function listfiles
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def listfiles(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'listfiles')
        # We know what the format is, initialize that format's class
        file_content = archive_func(self.filename)
        
        logger.debug('End Function')
        return file_content

    #-------------------------------------------------------------------
    #
    # Function testarchive
    #
    # Test to ensure the archive is a valid archive
    #
    # Inputs
    # ------
    #     self:
    #
    # Returns
    # -------
    #     None (change this to True or False?)
    #
    # Raises
    # ------
    #
    # 
    #-------------------------------------------------------------------
    def testarchive(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'testarchive')
        # We know what the format is, initialize that format's class
        if archive_func(self.filename):
            logger.info(str(self.filename) + ' is a valid, readable archive')
        else:
            logger.error(str(self.filename) + ' is not a valid, readable archive')
            
        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function search
    #
    # Searches archive files
    #
    # Inputs
    # ------
    #     self:
    #     searchstring:
    #
    # Returns
    # -------
    #     result
    #
    # Raises
    # ------
    #
    #
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'search')

        results = archive_func(self.filename, searchstring)
        
        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Classes
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
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
class Archives(files.BaseFiles):
    #-------------------------------------------------------------------
    #
    # Function search
    #
    # Searches archive files
    #
    # Inputs
    # ------
    #     self:
    #     searchstring:
    #
    # Returns
    # -------
    #     result
    #
    # Raises
    # ------
    #
    #-------------------------------------------------------------------
    def diff(self):
        logger.debug('Begin Function')

        results = "A + B"
        
        logger.debug('End Function')
        return results
