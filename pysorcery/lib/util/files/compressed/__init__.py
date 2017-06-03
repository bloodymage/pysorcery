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
import os

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
#-----------------------------------------------------------------------
class CompressedFile(files.BaseFile):
    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def decompress(self, extractdir=None):
        logger.debug('Begin Function')
        
        shutil.unpack_archive(self.filename, extractdir)

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def compress(self,
                 source_file=None,
                 root_dir=None,
                 base_dir=None,
                 compression_level=9):
        logger.debug('Begin Function')

        if source_file is None:
            source_file = self.basename
            
        shutil.make_archive(source_file,
                            self.format_,
                            root_dir,
                            base_dir)

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def read(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_compressed',
                                            self.format_,
                                            'read')
        # We know what the format is, initialize that format's class
        content = archive_func(self.filename)
        
        logger.debug('End Function')
        return content

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def testarchive(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_compressed',
                                            self.format_,
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
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_compressed',
                                            self.format_,
                                            'search')

        results = archive_func(self.filename, searchstring)
        
        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------
class CompressedFiles(files.BaseFiles):
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

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'diff')

        results = archive_func(self.filename)
        
        logger.debug('End Function')
        return results
