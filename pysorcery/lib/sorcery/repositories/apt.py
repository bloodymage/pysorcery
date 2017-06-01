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
from pysorcery.lib.sorcery import repository
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


#-------------------------------------------------------------------------------
#
# Classes
#
# DebianRepository
# 
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class DebianRepository
# 
#
#-------------------------------------------------------------------------------
class DebianRepository(repository.BaseRepository):
    def __init__(self,name = None, grim_dir = None):
        logger.debug('Begin Function')
        BaseGrimoire.__init__(self,name, grim_dir)

        if self.name[0].startswith('ppa://'):
            self.url = self.name

            # force new ppa file to be 644 (LP: #399709)
            #os.umask(0o022)

            # get the line
            #line = args[0]
            #print(line)
            
            # add it
            #sp = SoftwareProperties(options=options)
            #distro = aptsources.distro.get_distro()
            #distro.get_sources(sp.sourceslist)

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
    def list_spells(self):
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

        section_list = [ 'Fuck' ]
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
    def add(self):
        logger.debug('Begin Function')

        print(self.url)

        logger.debug('End Function')
        return

