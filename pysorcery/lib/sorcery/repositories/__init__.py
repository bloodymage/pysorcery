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
#
#
#
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#
# Libraries
#
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os


# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib import util
from pysorcery.lib.util import text

# Other Optional Libraries
if distro.distro_group[distro.distro_id] == 'deb':
    import apt
    import aptsources
    import softwareproperties

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

pkg_mgr = distro.distro_group[distro.distro_id]
    
#-------------------------------------------------------------------------------
#
# Classes
#
# BaseRepository
# BaseRepositories
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Class BaseRepository
# 
#
#-------------------------------------------------------------------------------
class BaseRepository():
    def __init__(self,name=None,repo_dir=None):
        logger.debug('Begin Function')

        logger.debug2('Name: ' + str(name))

        self.name = get_repo_name(name, repo_dir)

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
    def add(self):
        logger.debug('Begin Function')


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
# Class Repositories
# 
#
#-------------------------------------------------------------------------------
class BaseRepositories():
    pass

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
# Function 
#
# Input:  ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_repo_name(name=None, repo_dir=None):
    func = util.get_module_func('repositories',
                                pkg_mgr,
                                'get_repo_name')
    name = func(name, repo_dir)
    return name

