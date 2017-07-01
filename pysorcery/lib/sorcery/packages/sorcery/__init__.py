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
# File: pysorcery/lib/sorcery/packages/sorcery/__init__.py
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
from pysorcery.lib.sorcery.packages.sorcery import bashspell
from pysorcery.lib.sorcery import repositories
from pysorcery.lib.sorcery.repositories import sorcery

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

#-----------------------------------------------------------------------
#
# Classes
#
# Spell
#
#-----------------------------------------------------------------------

 
#-----------------------------------------------------------------------
#
# Class Spell
# 
#
#-----------------------------------------------------------------------
class Spell(packages.BasePackage):
    def __init__(self, *args, **kwargs):
        logger.debug("Begin Function")
        super(Spell, self).__init__(*args, **kwargs)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def set_details(self):
        logger.debug('Begin Function')
        
        codex = repositories.Repo_Lists()
        grimoire_list = codex.list_grimoires()

        for i in grimoire_list:
            spell_list_file = lib.File(i + '/codex.index')
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

        details_file = bashspell.DetailsFile(self.spell_directory)
        details = details_file.read()
        
        self.description = details['description']
        self.version = details['version']
        self.url = details['website']
        self.short = details['short']
        
        self.source_files = {}

        #file_name = url.split('/')[-1]

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Return: ...
    #
    #-------------------------------------------------------------------
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

#-----------------------------------------------------------------------
#
# Function get_description
#
# Input:  ...
# Return: ...
#
#-----------------------------------------------------------------------
def get_description(name):
    spell_codex = sorcery.Codex()
    grimoire_list = spell_codex.list_grimoires()

    for grimoire in grimoire_list:
        spell_list_file = lib.File(grimoire + '/codex.index')
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

#-----------------------------------------------------------------------
#
# Function get_description
#
# Input:  ...
# Output: ...
# Return: ...
#
#-----------------------------------------------------------------------
def get_version(name):
    spell_codex = sorcery.Codex()
    grimoire_list = spell_codex.list_grimoires()

    for grimoire in grimoire_list:
        spell_list_file = lib.File(grimoire + '/codex.index')
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
        
    version = details['version']

    return version

#-----------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Return: ...
#
#-----------------------------------------------------------------------
def print_version(self,multi=False):
    logger.debug("Begin Function")
    
    if multi:
        grimoires = libcodex.Codex()
        grimoire_list = grimoires.list_grimoires()
        
        m = len(grimoire_list)
    else:
        grimoire_list = [ self.grimoire ]
        m = 1
        
    print_list = [ "Grimoire         " ]    
    print_list.append("Section          ")
    print_list.append("Spell            ")
    print_list.append("Grimoire Version ")
    print_list.append("Installed version")
    print_list.append("----------       ")
    print_list.append("-------          ")
    print_list.append("-------          ")
    print_list.append("------------     ")
    print_list.append("-----------------")
    

    for i in grimoire_list:
        print_list.append(i.split('/')[-1])
        print_list.append(self.section)
        print_list.append(self.name)
        print_list.append(self.version)
        print_list.append('-')

    libmisc.column_print(print_list,cols=5,columnwise=False,gap=2)
                
    logger.debug("End Function")
    return
