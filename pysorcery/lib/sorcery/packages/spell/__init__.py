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
from pysorcery import lib
from pysorcery.lib.sorcery import packages
from pysorcery.lib.sorcery.packages.spell import bashspell
from pysorcery.lib.sorcery import repositories
from pysorcery.lib.sorcery.repositories import codex

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
#
#-------------------------------------------------------------------------------

 
#-------------------------------------------------------------------------------
#
# Class BaseSpell
# 
#
#-------------------------------------------------------------------------------
class Spell(packages.BasePackage):
    def __init__(self,name):
        logger.debug("Begin Function")
        super(Spell, self).__init__(*args, **kwargs)

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
    spell_codex = codex.Codex()
    grimoire_list = spell_codex.list_grimoires()


    for grimoire in grimoire_list:
        spell_list_file = lib.Files(grimoire + '/codex.index')
        spell_list = spell_list_file.read()
        
        for item in spell_list:
            spell, section_dir = item.split(' ')

            if name == spell:
                break
            
        if name == spell:
            grimoire = grimoire.split('/')[-1]
            break

    section = section_dir.split('/')[-1]
    spell_directory = section_dir + '/' + name

    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
        
    description = details['description']

    return description
