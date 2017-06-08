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
import tarfile

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
from pysorcery.lib.system import shutil
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

#-------------------------------------------------------------------
#
# Function decompress
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
def listfiles(filename):
    logger.debug("Begin Function")
    
    try:
        tar_file = tarfile.open(filename)
        file_content = []
        for name in tar_file.getnames():
            file_content.append(name)
    except tarfile.ExtractError:
        logger.error("Unk Extraction Error")
        pass
    except IOError:
        logger.error("IO Error")
        pass
    except:
        logger.error("Unknown Error")
        
    logger.debug('End Function')
    return file_content

#-------------------------------------------------------------------
#
# Function decompress
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
def testarchive(filename):
    logger.debug("Begin Function")    
    logger.debug('End Function')
    return tarfile.is_tarfile(filename)

#-------------------------------------------------------------------
#
# Function decompress
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
def diff(filename1, filename2):
    logger.debug("Begin Function")

    results = 'Tarfile diff'
    logger.debug('End Function')
    return results

#-------------------------------------------------------------------
#
# Function decompress
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
def search(filename, searchstring):
    logger.debug("Begin Function")    

    results = 'Tarfile search results'
    
    logger.debug('End Function')
    return results

#-------------------------------------------------------------------
#
# Function decompress
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
def verify_extract():
    logger.debug('Begin Function')

    verified = True
    
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function decompress
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
def verify_test():
    logger.debug('Begin Function')

    verified = True
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function decompress
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
def verify_compress():
    logger.debug("Begin Function")

    verified = True

    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function decompress
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
def verify_list():
    logger.debug("Begin Function")

    verified = True
    logger.debug('End Function')
    return verified

#-------------------------------------------------------------------
#
# Function decompress
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
