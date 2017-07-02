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
# Sorcery Spell
#
#    This provides the functions for working with sorcery spells.
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

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib.sorcery import packages
from pysorcery.lib.sorcery.packages.sorcery import bashspell
from pysorcery.lib.sorcery import repositories
from pysorcery.lib.sorcery.repositories import sorcery
from pysorcery.lib.util import files

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
#-----------------------------------------------------------------------
 
#-----------------------------------------------------------------------
#
# Functions
#
# get_description
# get_version
# get_url
# get_short
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function get_description
#
# Gets a spell's description.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_description(name, repository=None):
    if repository is None:
        repository = get_first_repo(name)

    grimoire =  sorcery.Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details = details_file.parse()
    description = details['description']
    return description

#-----------------------------------------------------------------------
#
# Function get_version
#
# Get's a spell's version.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: version
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_version(name, repository=None):
    if repository is None:
        repository = get_first_repo(name)

    grimoire =  sorcery.Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    version = details['version']
    return version

#-----------------------------------------------------------------------
#
# Function get_url
#
# Gets a spell's url.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: url
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_url(name, repository=None):
    if repository is None:
        repository = get_first_repo(name)

    grimoire =  sorcery.Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    url = details['website']
    return url

#-----------------------------------------------------------------------
#
# Function get_short
#
# Gets a spell's short description.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: short
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_short(name, repository=None):
    
    if repository is None:
        repository = get_first_repo(name)

    grimoire =  sorcery.Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    short = details['short']
    return short


#-----------------------------------------------------------------------
#
# Function get_first_repo
#
# Get the first repository containing a spell by spell name.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: grimoire
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_first_repo(name):
    spell_codex = sorcery.Codex()
    grimoire_list = spell_codex.list_grimoires()

    for grimoire in grimoire_list:
        spell_list_file = files.BaseFile(grimoire + '/codex.index')
        spell_list = spell_list_file.read()
        
        for item in spell_list:
            spell, section_dir = item.split(' ')
            if name == spell:
                break
            
        if name == spell:
            grimoire = grimoire.split('/')[-1]
            break
        
    return grimoire

#-----------------------------------------------------------------------
#
# Function get_section_dir
#
# Inputs
# ------
#    @param: grimoire
#    @param: name
#
# Returns
# -------
#    @return: section_dir
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section_dir(grimoire, name):
    spell_codex = sorcery.Codex()
    spell_list_file = files.BaseFile(grimoire + '/codex.index')
    spell_list = spell_list_file.read()
    
    for item in spell_list:
        spell, section_dir = item.split(' ')
        if name == spell:
            break

    return section_dir

#-----------------------------------------------------------------------
#
# Function get_spell_dir
#
# Inputs
# ------
#    @param: section_dir
#    @param: name
#
# Returns
# -------
#    @return: spell_directory
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_spell_dir(section_dir, name):
    section = section_dir.split('/')[-1]
    spell_directory = section_dir + '/' + name
    return spell_directory

#-----------------------------------------------------------------------
#
# Function 
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
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
