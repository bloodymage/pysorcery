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
from pysorcery.lib.util import files
from pysorcery.lib.util import config
from pysorcery.lib.util.files import compressed

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

spellfiles = [ 'BUILD',
               'CONFIGURE',
               'CONFLICTS',
               'DETAILS',
               'DEPENDS',
               'DOWNLOAD',
               'FINAL',
               'HISTORY',
               'INSTALL',
               'INSTALL_EXTRAS',
               'PATCH',
               'POST_BUILD',
               'POST_INSTALL',
               'POST_REMOVE',
               'POST_RESURRECT',
               'PRE_BUILD',
               'PRE_INSTALL',
               'PRE_REMOVE',
               'PRE_RESURRECT',
               'PRE_SUB_DEPENDS',
               'PREPARE',
               'PROVIDES',
               'SECURITY',
               'SUB_DEPENDS',
               'TRANSFER',
               'TRIGGER_CHECK',
               'TRIGGERS',
               'UP_TRIGGERS'
]

#-----------------------------------------------------------------------
#
# Classes
#
# BuildFile
# ConfigureFile
# ConflictsFile
# DetailsFile
# DependsFile
# DownloadFile
# FinalFile
# HistoryFile
# InstallFile
# InstallExtrasFile
# PatchFile
# PostBuildFile
# PostInstallFile
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
# Class BuildFile
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
class BuildFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(BuildFile, self).__init__(spell_directory + '/BUILD')
        return

#-----------------------------------------------------------------------
#
# Class ConfigureFile
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
class ConfigureFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(ConfigureFile, self).__init__(spell_directory + '/CONFIGURE')
        return


#-----------------------------------------------------------------------
#
# Class ConflictsFile
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
class ConflictsFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(ConflictFile, self).__init__(spell_directory + '/CONFLICTS')
        return


#-----------------------------------------------------------------------
#
# Class DetailsFile
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
class DetailsFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(DetailsFile, self).__init__(spell_directory + '/DETAILS')
        return

    #-------------------------------------------------------------------
    #
    # Function 
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
    def parse(self):
        logger.debug('Begin Function')
        
        details_dict = {}

        description_check = False
        case_check = False
        description = ''
        for i in open(self.filename):
            line = i[:-1]


            if (line.startswith('#')):
                logger.debug('Ignoring Line' + line)
            elif ('cat' in line and
                  'EOF' in line):
                description_check = True
            elif 'EOF' in line:
                description_check = False
            elif description_check is True:
                if len(description) == 0:
                    description = line
                else:
                    description += ' ' + line
            elif ('case' in line and
                  'in' in line):
                case_check = True
            elif 'esac' in line:
                case_check = False
            elif case_check is True:
                logger.debug('Ignore Case')
            elif '=' in line:

                key, value = line.split('=')
                if 'VERSION' in key:
                    logger.debug('Line: ' + line)
                    details_dict['version'] = value
                elif 'WEB_SITE' in key:
                    details_dict['website'] = value
                elif key.startswith('SOURCE'):
                    details_dict['source'] = value
                elif 'SHORT' in key:
                    details_dict['short'] = value
                elif 'LICENSE' in key:
                    details_dict['license'] = value
            else:
                logger.debug('Line: ' + line)

        details_dict['description'] = description

        logger.debug('End Function')
        return details_dict

#-----------------------------------------------------------------------
#
# Class DependsFile
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
class DependsFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(DependsFile, self).__init__(spell_directory + '/DEPENDS')
        return

#-----------------------------------------------------------------------
#
# Class DownloadFile
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
class DownloadFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(DownloadFile, self).__init__(spell_directory + '/DOWNLOAD')
        return

#-----------------------------------------------------------------------
#
# Class FinalFile
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
class FinalFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(FinalFile, self).__init__(spell_directory + '/FINAL')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
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
class HistoryFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(HistoryFile, self).__init__(spell_directory + '/HISTORY')
        return

#-----------------------------------------------------------------------
#
# Class InstallFile
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
class InstallFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(InstallFile, self).__init__(spell_directory + '/INSTALL')
        return

#-----------------------------------------------------------------------
#
# Class InstallExtrasFile
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
class InstallExtrasFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(InstallExtrasFile, self).__init__(spell_directory + '/INSTALLEXTRAS')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
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
class PatchFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PatchFile, self).__init__(spell_directory + '/PATCH')
        return

#-----------------------------------------------------------------------
#
# Class PostBuildFile
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
class PostBuildFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PostBuildFile, self).__init__(spell_directory + '/POST_BUILD')
        return

#-----------------------------------------------------------------------
#
# Class PostInstallFile
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
class PostInstallFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PostInstallFile, self).__init__(spell_directory + '/POST_INSTALL')
        return

#-----------------------------------------------------------------------
#
# Class PostRemoveFile
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
class PostRemoveFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PostRemoveFile, self).__init__(spell_directory + '/POST_REMOVE')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
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
class PostResurrectFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PostResurrectFile, self).__init__(spell_directory + '/POST_RESURRECT')
        return

#-----------------------------------------------------------------------
#
# Class PreBuildFile
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
class PreBuildFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(Pre_buildFile, self).__init__(spell_directory + '/PRE_BUILD')
        return

#-----------------------------------------------------------------------
#
# Class PreInstallFile
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
class PreInstallFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PreInstallFile, self).__init__(spell_directory + '/PRE_INSTALL')
        return

#-----------------------------------------------------------------------
#
# Class PreRemoveFile
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
class PreRemoveFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PreRemoveFile, self).__init__(spell_directory + '/PREREMOVE')
        return

#-----------------------------------------------------------------------
#
# Class PreResurrectFile
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
class PreResurrectFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PreResurrectFile, self).__init__(spell_directory + '/PRERESURRECT')
        return

#-----------------------------------------------------------------------
#
# Class PreSubDependsFile
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
class PreSubDependsFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PreSubDependsFile, self).__init__(spell_directory + '/PRESUBDEPENDS')
        return

#-----------------------------------------------------------------------
#
# Class PrepareFile
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
class PrepareFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(PrepareFile, self).__init__(spell_directory + '/PREPARE')
        return

#-----------------------------------------------------------------------
#
# Class ProvidesFile
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
class ProvidesFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(ProvidesFile, self).__init__(spell_directory + '/PROVIDES')
        return

#-----------------------------------------------------------------------
#
# Class SecurityFile
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
class SecurityFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(SecurityFile, self).__init__(spell_directory + '/SECURITY')
        return

#-----------------------------------------------------------------------
#
# Class SubDependsFile
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
class SubDependsFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(SubDependsFile, self).__init__(spell_directory + '/SUBDEPENDS')
        return

#-----------------------------------------------------------------------
#
# Class TransferFile
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
class TransferFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(TransferFile, self).__init__(spell_directory + '/TRANSFER')
        return

#-----------------------------------------------------------------------
#
# Class TriggerCheckFile
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
class TriggerCheckFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(TriggersCheckFile, self).__init__(spell_directory + '/TRIGGERS_CHECK')
        return

#-----------------------------------------------------------------------
#
# Class TriggersFile
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
class TriggersFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(TriggersFile, self).__init__(spell_directory + '/TRIGGERS')
        return

#-----------------------------------------------------------------------
#
# Class UpTriggersFile
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
class UpTriggersFile(files.BaseFile):
    def __init__(self, spell_directory):
        super(UpTriggersFile, self).__init__(spell_directory + '/UP_TRIGGERS')
        return

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
