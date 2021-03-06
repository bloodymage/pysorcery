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
# File: pysorcery/lib/sorcery/packages/sorcery/smgl/py_api_01.py
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
from pysorcery.lib.sorcery import smgl
from pysorcery.lib.sorcery.smgl import bashspell
from pysorcery.lib import files
from pysorcery.lib.util import config
from pysorcery.lib.files import compressed

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
class Spell(smgl.Spell):
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
class Spells(smgl.Spells):
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
class SpellVersions(smgl.SpellVersions):
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
class Section(smgl.Section):
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
class Sections(smgl.Sections):
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
class Grimoire(smgl.Grimoire):
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
class Codex(smgl.Codex):
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

#-------------------------------------------------------------------------------
#
# Function get_repository
#
# Get ...
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
def get_repository(name=None, grim_dir=None):
    if grim_dir and not name:
        name = grim_dir.split('/')[-1]
    elif name and not grim_dir:
        grimoire = Grimoire(name)
        grim_dir = grimoire.get_grim_dir()
    elif not name and not grim_dir:
        raise Exception
    else:
        x = 1

    return name, grim_dir

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
def get_codex():
    return get_repository_dirs()

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
    content = grimoire_file.read()

    grimoires = []
    directories = []
    for grimoire in content:
        grimoire, directory = grimoire.split('=')
        grimoires.append(grimoire)
        directories.append(directory)

    return grimoires, directories

#-------------------------------------------------------------------------------
#
# Function get_repositories
#
# Get's a list of grimoires and a list of grimoire directories.
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#
# Returns
# -------
#    @return: grimoires
#    @return: directories
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def get_repositories(*args, **kwargs):
    if 'repositories' not in kwargs or kwargs['repositories'] is None:
        grimoires, directories = get_repository_dirs()
    else:
        grimoires = kwargs['repositories']
        directories = []
        
    return grimoires, directories

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
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

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
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

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
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

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
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

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
# Gets a spell's section
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: section
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    section_dir = get_section_dir(grimoire_dir, name)
    section = section_dir.split('/')[-1]
    return section

#-----------------------------------------------------------------------
#
# Function get_section
#
# Read a spells FILE.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: content
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def read_file(name, **kwargs):

    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    filename = kwargs['filename']
    
    # What I really need is camelcase.
    #classname = filename.capitalize()
    classname = filename
    fileclass = getattr(bashspell, classname + 'File')
    file_ = fileclass(spell_directory)
    content = file_.read()
    return content

#-----------------------------------------------------------------------
#
# Function get_section
#
# Read a spells FILE.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: content
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_log(spell, **kwargs):
    if kwargs['extension'] is None:
        extension = ''
    else:
        extension = kwargs['extension']
        
    filename = (config.log_dirs[config.pkg_mgr][kwargs['log']]
                + spell
                + '-'
                + kwargs['version']
                + extension)
    if extension == '':
        file_ = files.BaseFile(filename)
    else:
        file_ = compressed.CompressedFile(filename)
        
    content = file_.read()
    return content

#-----------------------------------------------------------------------
#
# Function is_package
#
# ...
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: check
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def is_package(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    spell_list_file = files.BaseFile(grimoire_dir + '/codex.index')
    spell_list = spell_list_file.read()
    check = False
    for item in spell_list:
        spell, section_dir = item.split(' ')
        section = section_dir.split('/')[-1]
        if name == spell:
            check = True
            break

    return check

#-----------------------------------------------------------------------
#
# Function is_package
#
# ...
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: check
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def is_spell(name, **kwargs):
    return is_package(name)

#-----------------------------------------------------------------------
#
# Function get_license
#
# ...
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: license
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_license(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository , grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    section_dir = get_section_dir(grimoire_dir, name)
    spell_directory = get_spell_dir(section_dir, name)
    details_file = bashspell.DetailsFile(spell_directory)
    details = details_file.parse()
    license_ = details['license']
    return license_

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
    raise NotImplementedError
    return size

#-----------------------------------------------------------------------
#
# Function get_pkg_maintainer
#
# Gets a spell's maintainer
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: maintainer
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_pkg_maintainer(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, directory = get_first_repo(name)
    else:
        repository = kwargs['repository']
        grimoire = Grimoire(repository)
        directory = grimoire.directory
 
    section_dir = get_section_dir(directory, name)
    maintainer_file = files.BaseFile(section_dir + '/MAINTAINER')
    content = maintainer_file.read()
    return content[0]

#-----------------------------------------------------------------------
#
# Function get_section_maintainer
#
# Gets a section's maintainer.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: maintainer
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section_maintainer(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    section_dir = grimoire_dir + '/' + name
    
    maintainer_file = files.BaseFile(section_dir + '/MAINTAINER')
    content = maintainer_file.read()
    maintainer = content[0]
    return maintainer

#-----------------------------------------------------------------------
#
# Function get_section_packages
#
# Gets a section's description.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: packages
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section_packages(name, **kwargs):
    if 'repository' not in kwargs or kwargs['repository'] is None:
        repository, grimoire_dir = get_first_repo(name)
    else:
        repository = kwargs['repository']

    section_dir = grimoire_dir + '/' + name

    try:
        packages = os.scandir(section_dir)
        return packages
    except FileNotFoundError:
        logger.error('Section %s does not exist' % name)
    finally:
        return

#-----------------------------------------------------------------------
#
# Function get_section_packages
#
# Gets a section's description.
#
# Inputs
# ------
#    @param: name
#
# Returns
# -------
#    @return: packages
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_section_spells(name, **kwargs):
    return get_section_packages(name)

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

    check = False
    for directory in codex.directories:
        spell_list_file = files.BaseFile(directory + '/codex.index')
        spell_list = spell_list_file.read()
        
        for item in spell_list:
            spell, section_dir = item.split(' ')
            section = section_dir.split('/')[-1]
            if name == spell or name == section:
                check = True
                break
            
        if name == spell or name == section:
            break

    if check:
        grimoire = directory.split('/')[-1]
        return grimoire, directory
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

#---------------------------------------------------------------
#
# Function get_queue
#
# Get a list of spells in a queue.
#
# Inputs
# ------
#    @param: which-queue
#
#
# Returns
# -------
#    @return: queue
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_queue(which_queue):
    logger.debug("Begin Function")
    queue_file = files.BaseFile('/var/log/sorcery/queue/' + which_queue)
    
    queue = queue_file.read()
    
    logger.debug("End Function")
    return queue
    
#---------------------------------------------------------------
#
# Function get_installed
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
def get_installed(status):
    logger.debug("Begin Function")
    
    spell_list = []
    
    for line in open('/var/state/sorcery/packages'):
        spell = line.split(':')
        
        name = spell[0]
        date = spell[1]
        spellstatus = spell[2]
        version = spell[3]

        if not status and spellstatus != 'exiled':
            spell_list.append(name)
            spell_list.append(date)
            spell_list.append(version)
        elif status == spellstatus:
            spell_list.append(name)
            spell_list.append(date)
            spell_list.append(version)
        else:
            pass
            
    logger.debug('End Function')
    return spell_list

#-----------------------------------------------------------------------
#
# Function get_sections
#
# Gets ...
#
# Inputs
# ------
#    @param: grimoire
#
# Returns
# -------
#    @return: section
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_sections(grimoire=None, grim_dir=None, **kwargs):
    logger.debug('Begin Function')
    
    dir_list = os.scandir(grim_dir)
    sections = []
    for item in dir_list:
        if item.is_dir():
            if 'git' not in item.name:
                section_list.append(item.name)

    logger.debug('End Function')
    return sections

#---------------------------------------------------------------
#
# Function get_providers
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
def get_providers(feature):
    logger.debug('Begin Function')
    
    grimoires = Codex()
    
    providers = []
    for grimoire in grimoires.get_repositories():
        for line in open(grimoire + '/provides.index'):
            if feature.upper() == line.split(' ')[0]:
                providers.append(line.split('/')[-1][:-1])
                
    logger.debug('End Function')
    return providers



#www.hnfs.com

#kim 
