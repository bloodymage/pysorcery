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
import glob
import importlib
import os

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
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

ArchiveModules = {
    'tar': 'tar'
    }

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------


#-----------------------------------------------------------------------
#
# Functions
#
# get_archive_cmd_func
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function get_archive_cmd_func
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def get_archive_formats():
    modules = glob.glob(os.path.dirname(__file__)+"/*.py")
    supformats = []
    for f in modules:
        if (os.path.isfile(f) and
            f.split('/')[-1] != '__init__.py'):
            supformats.append(os.path.basename(f)[:-3])
            
    return supformats

#-------------------------------------------------------------------
#
# Function get_archive_cmd_func
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------
def get_archive_cmd_func(archive_format,command):
    modulename = "pysorcery.lib.util.files.archive." + ArchiveModules.get(archive_format, archive_format)
    # import the module
    try:
        module = importlib.import_module(modulename, __name__)
    except ImportError as msg:
        raise logger.error(msg)
    # get the function
    try:
        return getattr(module, command)
    except AttributeError as msg:
        raise logger.error(msg)
