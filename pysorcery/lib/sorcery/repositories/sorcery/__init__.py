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
# File: pysorcery/lib/sorcery/repositories/sorcery/__init__.py
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
#
#
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#
#-----------------------------------------------------------------------

# System Libraries
import sys
import os


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery import lib
from pysorcery.lib.sorcery import repositories
from pysorcery.lib.util import text

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
# Grimoire
# Codex
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Grimoire
# 
#
#-----------------------------------------------------------------------
class Grimoire(repositories.BaseRepository):
    def __init__(self, name=None, grim_dir=None):
        logger.debug('Begin Function')
        super(Grimoire, self).__init__(name, grim_dir)

        logger.debug2('Name: ' + str(name))
        
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
    def add(self):
        logger.debug('Begin Function')

        self.url = 'http://codex.sourcemage.org/' + self.name + '.tar.bz2'


        logger.debug('End Function')
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
    def list_sections(self):
        logger.debug('Begin Function')

        dir_list = os.scandir(self.grim_dir)
        section_list = []
        for item in dir_list:
            if item.is_dir():
                if 'git' not in item.name:
                    section_list.append(item.name)

        logger.debug('End Function')
        return section_list

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def get_grim_dir(self, grim_dir=None):
        if self.name and not grim_dir:
            grim_dir = '/var/lib/sorcery/codex' + name

        self.grim_dir = grim_dir

        return grim_dir

#-------------------------------------------------------------------------------
#
# Class Grimoire
# 
#
#-------------------------------------------------------------------------------
class Codex(Grimoire):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # 
    #
    #-------------------------------------------------------------------------------
    def list_grimoires(self):
        logger.debug('Begin Function')

        grimoire_file = lib.File('/etc/sorcery/local/grimoire')
        unedited_grimoire_list = grimoire_file.read()

        grimoire_list = []
        for grimoire in unedited_grimoire_list:
            grimoire_list.append(grimoire.split('=')[1])
        
        logger.debug('End Function')
        return grimoire_list

#-------------------------------------------------------------------------------
#
# Functions
#
# Get Repo Name
# 
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function get_repo_name
#
# Input:  ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_repo_name(name=None, grim_dir=None):
    if grim_dir and not name:
        name = grim_dir.split('/')[-1]

    return name
