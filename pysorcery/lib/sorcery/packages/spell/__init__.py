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
import subprocess
import os

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib.sorcery import repositories

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#
# BaseSpell
# DebianSpell
# Spell
#
# BaseSpellQueue
# DebianSpellQueue
# SpellQueue
#
#-------------------------------------------------------------------------------

 
#-------------------------------------------------------------------------------
#
# Class BaseSpell
# 
#
#-------------------------------------------------------------------------------
class SMGLBashSpell(packages.BaseSpell):
    def __init__(self,name):
        logger.debug("Begin Function")
        BaseSpell.__init__(self,name)
        
        codex = libcodex.Codex()
        grimoire_list = codex.list_grimoires()

        for i in grimoire_list:
            spell_list_file = libfiles.Files(i + '/codex.index')
            spell_list = spell_list_file.read()

            for item in spell_list:
                spell, section_dir = item.split(' ')

                if self.name == spell:
                    self.section_dir = section_dir
                    break

            if self.name == spell:
                self.grimoire = i.split('/')[-1]
                break

        self.section = self.section_dir.split('/')[-1]
        self.spell_directory = self.section_dir + '/' + self.name

        details_file = libfiles.DetailsFile(self.spell_directory)
        details = details_file.read()
        
        self.description = details['description']
        self.version = details['version']
        self.url = details['website']
        self.short = details['short']
        
        self.source_files = {}

        #file_name = url.split('/')[-1]

        logger.debug("End Function")
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
    def install(self,args):
        logger.debug("Begin Function")
        print("Installing: " + self.name)
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Functions
#
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function get_description
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_description(name):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    description  = versions[0].description

    cache.close()
    return description
