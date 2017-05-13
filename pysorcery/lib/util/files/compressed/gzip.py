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
import gzip
import shutil

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
#from pysorcery.lib.system import mimetypes
#from pysorcery.lib.system import shutil
# Other Application Libraries
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

#-------------------------------------------------------------------
#
# Functions
#
# extract
#
#-------------------------------------------------------------------
def decompress(filename, root_dir=None, base_dir=None, verbose=0,
                 dry_run=0, owner=None, group=None, logger=None):
#    logger.debug('Begin Function')

    path, base_name, ext = files.pne(filename)
    with gzip.open(filename, 'rb') as f_in:
        with open(base_name, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    
#    logger.debug('End Function')
    return

def compress(filename, base_dir,verbose=0, dry_run=0, logger=None,
           owner=None,group=None):
#    logger.debug('Begin Function')

    with open(filename, 'rb') as f_in:
        with gzip.open(filename + '.gz', 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

#    logger.debug('End Function')
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
def read(filename):
    logger.debug("Begin Function")
    
    line_list = []    
    with gzip.open(filename, 'r') as f:
        for line in f:
            line_list.append(line.decode('utf-8')[:-1])

    logger.debug('End Function')
    return line_list


#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def testarchive(filename):
    logger.debug("Begin Function")    
    logger.debug('End Function')
    return True

#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def verify_extract():
    logger.debug('Begin Function')

    verified = True
    
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def verify_test():
    logger.debug('Begin Function')

    verified = True
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def verify_compress():
    logger.debug("Begin Function")

    verified = True

    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def verify_list():
    logger.debug("Begin Function")

    verified = True
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def archive_support():
    logger.debug("Begin Function")

    if verify_extract:
        logger.info('    extract : Works')
    else:
        logger.info('    extract : Not Supported')
    if verify_compress:
        logger.info('    create  : Works')
    else:
        logger.info('    create  : Not Supported')
    if verify_list:
        logger.info('    list    : Works')
    else:
        logger.info('    list    : Not Supported')
    if verify_test:
        logger.info('    test    : Works')
    else:
        logger.info('    test    : Not Supported')
    
    logger.debug('End Function')
    return
