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
from pysorcery.lib import sorcery
from pysorcery.lib.sorcery.smgl import bashspell
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
# Spell
# Spells
# Grimoire
# Codex
#
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#
# Class Spell
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
class Spell(sorcery.BasePackage):
    pass
    
#-----------------------------------------------------------------------
#
# Class Spells
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
class Spells(sorcery.BasePackages):
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
class Grimoire(sorcery.BaseRepository):
    def __init__(self, name=None, grim_dir=None):
        super(Grimoire, self).__init__(name, grim_dir)
        return

    #-------------------------------------------------------------------
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def add(self):
        logger.debug('Begin Function')


        logger.debug('End Function')
        return

    #-------------------------------------------------------------------------------
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
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
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------------------
    def get_grim_dir(self, grim_dir=None):
        if self.name and not grim_dir:
            grim_dir = '/var/lib/sorcery/codex/' + self.name

        file_ = files.BaseDirectory(grim_dir)

        if file_.isdir() is False:
            codex = Codex()
            grimoires = codex.list_grimoires()
            grim_dir = [s for s in grimoires if self.name in s][0]

        self.grim_dir = grim_dir
        return grim_dir

    #-------------------------------------------------------------------------------
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------------------
    def get_url(self):
        config_ = config.Sorcery()

        if self.name in config_.smgl_official_grimoires:
            self.url = config.urls['codex_tarball_url'] + self.name + '.tar.bz2'
        else:
            raise NotImplementedError

        return self.url

#-------------------------------------------------------------------------------
#
# Class Codex
# 
#
#-------------------------------------------------------------------------------
class Codex(sorcery.BaseRepositories):
    #-------------------------------------------------------------------------------
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------------------
    def grimoires(self):
        self.repositories = get_repositories()
        self.grimoires = self.repositories
        return self.repositories

    def grimoire_dirs(self):
        grimoire_dirs = get_repository_dirs()
        return grimoire_dirs

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

#-------------------------------------------------------------------------------
#
# Function get_repo_name
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
#-------------------------------------------------------------------------------
def get_repo_name(name=None, grim_dir=None):
    if grim_dir and not name:
        name = grim_dir.split('/')[-1]

    return name

#-------------------------------------------------------------------------------
#
# Function get_repository_dirs
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
#-------------------------------------------------------------------------------
def get_repository_dirs():
    grimoire_file = files.BaseFile('/etc/sorcery/local/grimoire')
    grimoires = grimoire_file.read()

    grimoire_dirs = []
    for grimoire in grimoires:
        grimoire_dirs.append(grimoire.split('=')[1])

    return grimoire_dirs

#-------------------------------------------------------------------------------
#
# Function get_repositories
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
#-------------------------------------------------------------------------------
def get_repositories(*args, **kwargs):
    if 'repositories' not in kwargs or kwargs['repositories'] is None:
        repositories = get_repository_dirs()
    else:
        repositories = kwargs['repositories']

    grimoires = []
    for grim_dir in repositories:
        grimoire = get_repo_name(grim_dir=grim_dir)
        grimoires.append(grimoire)

    return grimoires

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
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire =  Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
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
def get_version(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire =  Grimoire(repository)
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
def get_url(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire = Grimoire(repository)
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
def get_short(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire = Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    short = details['short']
    return short

#-----------------------------------------------------------------------
#
# Function get_section
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
def get_section(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire = Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    section = section_dir.split('/')[-1]
    return section

#-----------------------------------------------------------------------
#
# Function get_section
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
def read_file(name, **kwargs):

    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire =  Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)

    filename = kwargs['filename']
    classname = filename.capitalize()

    fileclass = getattr(bashspell, classname + 'File')
    file_ = fileclass(spell_directory)
    content = file_.read()
    
    return content

#-----------------------------------------------------------------------
#
# Function is_package
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
def is_package(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    if repository == False:
        return False
    else:
        return True

#-----------------------------------------------------------------------
#
# Function get_licens
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
def get_license(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

    grimoire =  Grimoire(repository)
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    short = details['license']
    return short

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
def get_maintainer(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository = get_first_repo(name)
    else:
        repository = kwargs['repository']

<<<<<<< HEAD:pysorcery/lib/sorcery/smgl/__init__.py
    grimoire =  Grimoire(repository)
=======
    grimoire =  sorcery.Grimoire(repository)
>>>>>>> 313c7ceeb96613e04a98a059a2306fc4c6639579:pysorcery/lib/sorcery/packages/sorcery/__init__.py
    grimoire_dir = grimoire.get_grim_dir()
    section_dir = get_section_dir(grimoire_dir, name)
    maintainer_file = files.BaseFile(section_dir + '/MAINTAINER')
    content = maintainer_file.read()
    return content[0]

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
    codex = Codex()
    grimoire_dirs = codex.grimoire_dirs()

    check = False
    for grimoire in grimoire_dirs:
        spell_list_file = files.BaseFile(grimoire + '/codex.index')
        spell_list = spell_list_file.read()
        
        for item in spell_list:
            spell, section_dir = item.split(' ')
            if name == spell:
                check = True
                break
            
        if name == spell:
            break

    if check:
        grimoire = grimoire.split('/')[-1]
        return grimoire
    else:
        return False

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
