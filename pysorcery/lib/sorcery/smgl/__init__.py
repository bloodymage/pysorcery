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
# File: pysorcery/lib/sorcery/__init__.py
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
# Sorcery:
#
#
#-----------------------------------------------------------------------
"""
Sorcery:

Library for sorcery works with the package manager's packages.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import sys
import subprocess
import os

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib import sorcery
from pysorcery.lib import util

# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

# Supported packagex commands
Commands = ('get_description',
            'get_version',
            'get_url',
            'get_short',
            'get_license',
            'get_section',
            'read_file',
            'is_package',
            'get_codex')

#-----------------------------------------------------------------------
#
# Classes
# 
# Spell
# Spells
# SpellVersions
# Section
# Sections
# Repository
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
#    @return: None
 #
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Spell(sorcery.BasePackage):
    def __init__(self, name, repository=None, version=None):
        self.scmd = 'sorcery_smgl'
        self.program = 'spell'
        self.pkg_mgr = 'smgl'
        super(Spell, self).__init__(name, repository, version)
        return

    #-------------------------------------------------------------------
    #
    # Function is_spell
    #
    # Verify spell exists.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: tf - True or False
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def is_spell(self):
        return self.is_package('is_spell')

#-----------------------------------------------------------------------
#
# Class SpellVersions
#
# This class is for working with multiple versions of the same spell.
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
class SpellVersions(sorcery.BasePackageVersions):
    def __init__(self, name, repositories=[]):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'spellversions'
        super(SpellVersions, self).__init__(name, repositories)

#-----------------------------------------------------------------------
#
# Class Spells
#
# ...
# 
# Inputs
# ------
#    @param: ...
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
class Spells(sorcery.BasePackages):
    def __init__(self, packages=[]):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'spells'
        super(Spells, self).__init__(packages)
        self.spells = self.packages
        return

#-----------------------------------------------------------------------
#
# Class Section
#
# ...
#
# Inputs
# ------
#    @param: name
#    @param: repository
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
class Section(sorcery.BaseSection):
    def __init__(self, name, repository=None):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'section'
        super(Section, self).__init__(name, repository)
        return

    #-------------------------------------------------------------------
    #
    # Function get_spells
    #
    # Get a list of spells within a section.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.spells
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_section_spells(self):
        return self.get_section_packages()
    
#-----------------------------------------------------------------------
#
# Class Sections
#
# ...
#
# Inputs
# ------
#    @param: sections
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
class Sections(sorcery.BaseSections):
    def __init__(self, sections=[]):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'sections'
        super(Sections, self).__init__(sections)
        return

#-------------------------------------------------------------------------------
#
# Class Repository
#
# ...
#
# Inputs
# ------
#    @param: name
#    @param: reepo_dir
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
class Grimoire(sorcery.BaseRepository):
    def __init__(self, name=None, repo_dir=None):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'grimoire'
        super(Grimoire, self).__init__(name, repo_dir)
        return

#-----------------------------------------------------------------------
#
# Class Codex
#
# Provide support for a list of codex.
# 
# Inputs
# ------
#    @param: codex
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
class Codex(sorcery.BaseRepositories):
    def __init__(self, codex=[]):
        self.pkg_mgr = 'smgl'
        self.scmd = 'sorcery_smgl'
        self.program = 'codex'
        self.cmd = 'get_codex'
        super(Codex, self).__init__(codex)
        return

#-----------------------------------------------------------------------
#
# Functions
#
#
#-----------------------------------------------------------------------
