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
# File: pysorcery/lib/sorcery/packages/sorcery/smgl/__init__.py
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
from pysorcery.lib import logging
# Other Application Libraries

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
# SpellVersions
# Spells
# Section
# Sections
# Grimoire
# Codex
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Spell
# 
# ...
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
class Spell():
    pass
    
#-----------------------------------------------------------------------
#
# Class Spells
# 
# ...
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
class Spells():
    pass

#-----------------------------------------------------------------------
#
# Class Spells
# 
# ...
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
class SpellVersions():
    pass

#-----------------------------------------------------------------------
#
# Class Section
# 
# ...
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
class Section():
    pass

#-----------------------------------------------------------------------
#
# Class Sections
# 
# ...
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
class Sections():
    pass

#-----------------------------------------------------------------------
#
# Class Grimoire
# 
# Grimoire ...
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
class Grimoire():
    pass

#-------------------------------------------------------------------------------
#
# Class Codex
# 
#
#-------------------------------------------------------------------------------
class Codex():
    pass

#-------------------------------------------------------------------------------
#
# Functions
#
# get_repo_name
# get_repository_dirs
# get_repositories
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
def get_description(name, **kwargs):
    var = subprocess.check_output(['gaze','-q', 'what', name])

    description = ''
    for line in var.splitlines():
        line_list = str(line).split(',')
        item = line_list[0].split("'")[1]
        description += item

    return description

#-----------------------------------------------------------------------
#
# Function get_size
#
# Get the package size.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: size
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_size(name, **kwargs):
    var = subprocess.check_output(['gaze','-q', 'size', name])

    size = ''
    for line in var.splitlines():
        line_list = str(line).split(',')
        item = line_list[0].split("'")[1]
        size += item


    return size

#---------------------------------------------------------------
#
# Function get_orphans
#
# ...
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    @return:
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_orphans():
    logger.debug('Begin Function')
    
    var = subprocess.check_output(['gaze','orphans'])

    orphan_list = []
    for line in var.splitlines():
        line_list = str(line).split(',')
        item = line_list[0].split("'")[1]
        orphan_list.append(item)

    logger.debug2(orphan_list)
    logger.debug('End Function')
    return orphan_list

#---------------------------------------------------------------
#
# Function get_orphans
#
# ...
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    @return:
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_sources(spell, **kwargs):
    logger.debug('Begin Function')
    
    var = subprocess.check_output(['gaze','sources', spell])

    sources = []
    for line in var.splitlines():
        line_list = str(line).split(',')
        item = line_list[0].split("'")[1]
        sources.append(item)

    logger.debug2(sources)
    logger.debug('End Function')
    return sources
