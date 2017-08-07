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

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract,
# ...)
# Programs starting with "py_" are Python modules.
SMGLPrograms = {
    'spell': {
        #None: ('apt', 'apt-get', 'apt-cache'),
        'get_description': ('api_1', 'gaze'),
        'get_version': ('api_1',),
        'get_url': ('api_1',),
        'get_short': ('api_1',),
        'get_license': ('api_1',),
        'get_section': ('api_1',),
        'is_spell': ('api_1',),
        'get_size': ('gaze',),
    },
    'spells': {
        'get_queue': ('api_1',),
        'get_installed': ('api_1',),
    },
    'section': {
        'get_maintainer': ('api_1',),
        'get_spells': ('api_1',),
    },
    'sections': {
    },
    'grimoire': {
        'get_repository': ('api_1',),
    },
    'codex': {
        'get_codex': ('api_1',),
    }
}

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
class Spell():
    def __init__(self, name, repository=None):
        logger.debug("Begin Function")
        
        self.name = name
        self.repository = repository

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function get_description
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description - The description of the spell
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_description(self):
        program = find_spell_program('spell', 'get_description')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_description')
        self.description = func(self.name, repository=self.repository)
        return self.description

    #-------------------------------------------------------------------
    #
    # Function get_version
    #
    # Get a spell version.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: results
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_version(self):
        program = find_spell_program('spell', 'get_version')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_version')
        self.version = func(self.name, repository=self.repository)
        return self.version

    #-------------------------------------------------------------------
    #
    # Function get_url
    #
    # Get a spell url.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: url
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_url(self):
        program = find_spell_program('spell', 'get_url')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_url')
        self.url = func(self.name, repository=self.repository)
        return self.url

    #-------------------------------------------------------------------
    #
    # Function get_short
    #
    # Get a spell short description.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description - The description of the spell
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_short(self):
        program = find_spell_program('spell', 'get_short')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_short')
        self.short_description = func(self.name, repository=self.repository)
        return self.short_description

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a spell ...
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.section
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_section(self):
        program = find_spell_program('spell', 'get_section')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_section')
        self.section = func(self.name, repository=self.repository)
        return self.section

    #-------------------------------------------------------------------
    #
    # Function read_file
    #
    # Read a spell's file.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #    @param: filename
    #
    # Returns
    # -------
    #    @return: contents - File contents
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def read_file(self, filename):
        program = find_spell_program('spell', 'read_file')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='read_file')
        contents = func(self.name, repository=self.repository, filename=filename)
        return contents

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
        program = find_spell_program('spell', 'is_spell')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='is_spell')
        tf = func(self.name, repository=self.repository)
        return tf

    #-------------------------------------------------------------------
    #
    # Function is_package
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
    def is_package(self):
        return is_spell()

    #-------------------------------------------------------------------
    #
    # Function get_license
    #
    # Get a spell license.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.license_
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_license(self):
        program = find_spell_program('spell', 'get_license')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_license')
        self.license_ = func(self.name, repository=self.repository)
        return self.license_

    #-------------------------------------------------------------------
    #
    # Function get_maintainer
    #
    # Get a spell maintainer
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.maintainer
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_maintainer(self):
        program = find_spell_program('spell', 'get_pkg_maintainer')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_pkg_maintainer')
        self.maintainer = func(self.name, repository=self.repository)
        return self.maintainer

    #-------------------------------------------------------------------
    #
    # Function get_size
    #
    # Get a spell short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: size - The amount of disk space of an installed
    #                    spell.
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_size(self):
        program = find_spell_program('spell', 'get_size')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_size')
        self.size = func(self.name, repository=self.repository)
        return self.size

    #-------------------------------------------------------------------
    #
    # Function install
    #
    # Install a spell
    #
    # Inputs
    # ------
    #    @param: self
    #    @param: args
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def install(self,args):
        program = find_spell_program('spell', 'install')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='install')
        func(args)
        
        return

#-----------------------------------------------------------------------
#
# Class SpellVersions
#
# This class is for working with mulhiple versions of the same spell.
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
class SpellVersions(Spell):
    pass

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
class Spells():
    def __init__(self, spells=[]):
        self.spells = spells
        return

    #-------------------------------------------------------------------
    #
    # Function get_queue
    #
    # Get a list of spells in a queue
    #
    # Inputs
    # ------
    #    @param: self
    #    @param: which_queue
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
    def get_queue(self, which_queue):
        program = find_spell_program('spells', 'get_queue')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_queue')
        self.spells = func(which_queue)
        return self.spells

    #-------------------------------------------------------------------
    #
    # Function get_installed
    #
    # Get a list of installed spells.
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
    def get_installed(self, status=None):
        program = find_spell_program('spells', 'get_installed')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_installed')
        self.spells = func(status)
        return self.spells

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
class Section():
    def __init__(self, name, repository=None):
        logger.debug("Begin Function")
        
        self.name = name
        self.repository = repository

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function get_maintainer
    #
    # Get a section maintainer
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: maintainer
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_maintainer(self):
        program = find_spell_program('section', 'get_maintainer')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_section_maintainer')
        self.maintainer = func(self.name, repository=self.repository)
        return self.maintainer

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
    def get_spells(self):
        program = find_spell_program('section', 'get_spells')
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_section_spells')
        self.spells = func(self.name, repository=self.repository)
        return self.spells

    #-------------------------------------------------------------------
    #
    # Function get_packages
    #
    # For compatability ...
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
    def get_packages(self):
        return get_spells()
    
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
class Sections():
    def __init__(self, sections=[]):
        logger.debug("Begin Function")
        
        self.sections = sections

        logger.debug('End Function')
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
class Grimoire():
    def __init__(self, name=None, repo_dir=None):
        logger.debug('Begin Function')

        logger.debug2('Name: ' + str(name))

        self.name, self.directory = get_repository(name, repo_dir)

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function get_repository
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: self.sections
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_sections(self):
        func = util.get_module_func(scmd='sorcery_smgl',
                                    program=program,
                                    cmd='get_sections')
        self.sections = func(self.name, repository=self.repository)
        return self.sections

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
class Codex():
    def __init__(self, codex=[]):
        if len(codex) == 0:
            self.codex, self.directories = get_codex()
        else:
            self.codex = codex

        return

#-----------------------------------------------------------------------
#
# Functions
#
# get_repository
# get_codex
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function get_repository 
#
# Inputs
# ------
#    @param: name
#    @param: repo_dir
#
# Returns
# -------
#    @return: name
#    @return: directory
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_repository(name=None, repo_dir=None):
    program = find_spell_program('repository', 'get_repository')    
    func = util.get_module_func(scmd='sorcery_smgl',
                                program=program,
                                cmd='get_repository'
    )
    name, directory = func(name, repo_dir)
    return name, directory

#-------------------------------------------------------------------------------
#
# Function get_codex
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#
# Returns
# -------
#    @return: codex
#    @return: directories
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def get_codex(*args, **kwargs):
    program = find_spell_program('codex', 'get_codex')
    func = util.get_module_func(scmd='sorcery_smgl',
                                program=program,
                                cmd='get_codex')
    codex, directories = func()
    return codex, directories

#-----------------------------------------------------------------------
#
# Function find_archive_program
#
# ...
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def find_spell_program (class_, command, program=None):
    """Find suitable archive program for given format and mode."""
    commands = SMGLPrograms[class_]
    programs = []
    if program is not None:
        # try a specific program first
        programs.append(program)
    # first try the universal programs with key None
    for key in (None, command):
        if key in commands:
            programs.extend(commands[key])
    if not programs:
        raise Exception("%s program class `%s' is not supported" % (command, class_))
    # return the first existing program
    for program in programs:
        if program.startswith('api_'):
            # it's a Python module and therefore always supported
            return program
        exe = util.find_program(program)
        if exe:
            return exe
    # no programs found
    raise Exception("could not find an executable program to %s format %s; candidates are (%s)," % (command, format, ",".join(programs)))
