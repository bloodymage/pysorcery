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
# File: pysorcery/lib/util/__init__.py
#
# This file is part of Sorcery.
#
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License,
#    or (at your option) any later version.
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
#-----------------------------------------------------------------------
"""
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import glob
import importlib
import os
import pkg_resources

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import lib
from pysorcery.lib.util import text

# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
# Allow Color text on console
colortext = text.ConsoleText()

# Utilities
UTIL_ARCHIVE_PATH = pkg_resources.resource_filename('pysorcery',
                                                    'lib/util/files/archive/')
UTIL_COMPRESSED_PATH = pkg_resources.resource_filename('pysorcery',
                                                       'lib/util/files/compressed/')
UTIL_URL_PATH = pkg_resources.resource_filename('pysorcery', 'lib/util/url/')

# Cemmand Plugins
ARCHIVE_PATH = pkg_resources.resource_filename('pysorcery', 'plugins/archive/')
GAZE_PATH = pkg_resources.resource_filename('pysorcery', 'plugins/gaze/')

# Sorcecy
PACKAGES_PATH = pkg_resources.resource_filename('pysorcery','lib/sorcery/packages')
REPOSITORIES_PATH = pkg_resources.resource_filename('pysorcery',
                                                    'lib/sorcery/packages')

cmd_dir = {
    'util_archive': UTIL_ARCHIVE_PATH,
    'util_compressed': UTIL_COMPRESSED_PATH,
    'util_url': UTIL_URL_PATH,
    'gaze': GAZE_PATH,
    'archive': ARCHIVE_PATH,
    'packages': PACKAGES_PATH,
    'repositories': REPOSITORIES_PATH
}

import_path = {
    'util_archive': 'pysorcery.lib.util.files.archive.',
    'util_compressed': 'pysorcery.lib.util.files.compressed.',
    'util_url': 'pysorcery.lib.util.url.',
    'archive': 'pysorcery.plugins.archive.',
    'gaze': 'pysorcery.plugins.gaze.',
    'packages': 'pysorcery.lib.sorcery.packages.',
    'repositories': 'pysorcery.lib.sorcery.repositories.'
    }

# Used if module names can not be
# the same as the archive format
ArchiveModules = {
    }

CompressedModules = {
    }

UrlModules = {
}
#-----------------------------------------------------------------------
#
# Functions
#
# get_cmd_types
# get_cmd_func
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function get_cmd_types
#
# Inputs
# ------
#     cmd_class - I really need a new name for this...
#         
# Returns
# -------
#     supformats - 'Supported Formats'
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_cmd_types(cmd_class):
    logger.debug('Begin Function')

    # Use [a-z] to allow finding directories, but ignoring
    # '__pycache__', etc
    modules = glob.glob(os.path.dirname(cmd_dir[cmd_class]) + "/[a-z]*")
    logger.debug(modules)

    supformats = []
    for f in modules:
        # Verify f is a real file
        # skip f if f's name is __init__.py
        # skip f if f is an emacs backup
        if (os.path.isfile(f) and
            f.split('/')[-1] != '__init__.py' and
            f.split('.')[-1] != 'py~'):
            supformats.append(os.path.basename(f)[:-3])

    supformats.sort()
    logger.debug('Return: ' + str(supformats))
    logger.debug('End Function')
    return supformats

#-------------------------------------------------------------------
#
# Function get_module_func
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def get_module_func(cmd_class,
                    cmd_type,
                    command):
    logger.debug('Begun Function')

    basemodname = import_path[cmd_class]

    if cmd_class == 'util_archive':
        modulename = basemodname + ArchiveModules.get(cmd_type, cmd_type)
    elif cmd_class == 'util_compressed':
        modulename = basemodname + CompressedModules.get(cmd_type, cmd_type)
    else:
        modulename = basemodname + cmd_type


    # import the module
    module = importlib.import_module(modulename, __name__)
    #    try:
#        module = importlib.import_module(modulename, __name__)
#    except ImportError as msg:
#        logger.error(str(msg) + ' ' + str(modulename))

    # get the function
    try:
        logger.debug('Module: ' + str(modulename))
        logger.debug('Command: ' + str(command)) 
        logger.debug('End Function')
        return getattr(module, command)
    except AttributeError as msg:
        logger.error(msg)
        logger.debug('End Function')
        return
