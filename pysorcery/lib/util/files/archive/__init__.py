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
# This implements the archive classes
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
class Archive(files.BaseFile):        
    #-------------------------------------------------------------------
    #
    # Function extract
    #
    # Input:  ...
    # Return: None
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
    # Input:  ...
    # Return: None
    #
    #-------------------------------------------------------------------
    def create(self, root_dir=None, base_dir=None):
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
    # Input:  ...
    # Return: None
    #
    #-------------------------------------------------------------------
    def listfiles(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'listfiles')
        # We know what the format is, initialize that format's class
        archive_func(self.filename)
        
        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function testarchive
    #
    # Input:  ...
    # Return: None
    #
    #-------------------------------------------------------------------
    def testarchive(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_,
                                            'testarchive')
        # We know what the format is, initialize that format's class
        if archive_func(self.filename):
            logger.info(str(self.filename) + ' is a valid, readable archive')
        else:
            logger.error(str(self.filename) + ' is not a valid, readable archive')
            
        logger.debug('End Function')
        return

