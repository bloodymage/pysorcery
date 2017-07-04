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
# File: pysorcery/lib/sorcery/repositories/sorcery/__init__.py
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
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#
#-----------------------------------------------------------------------

# System Libraries
import sys
import os


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery import lib
from pysorcery.lib.sorcery import repositories
from pysorcery.lib.util import config
from pysorcery.lib.util import files
from pysorcery.lib.util import text

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-----------------------------------------------------------------------
#
# Classes
#
# Grimoire
# Codex
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Grimoire
# 
#
#-----------------------------------------------------------------------
class Grimoire(repositories.BaseRepository):
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
class Codex(repositories.BaseRepositories):
    def __init__(self, name=None, grim_dir=None):
        super(Codex, self).__init__(name, grim_dir)
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
    def list_grimoires(self):

        grimoires = get_repositories()
        return grimoires

#-------------------------------------------------------------------------------
#
# Functions
#
# get_repo_name
# get_repository_dirs
# get_repositories
# 
#
#-------------------------------------------------------------------------------

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
def get_repository_dirs():
    grimoire_file = lib.File('/etc/sorcery/local/grimoire')
    grimoires = grimoire_file.read()

    repository_dirs = []
    for grimoire in unedited_grimoire_list:
        repository_dirs.append(grimoire.split('=')[1])

    return repository_dirs

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
def get_repositories(**kwargs):
    if 'repositories' not in kwargs or kwargs['repositories'] is None:
        repositories = get_repository_dirs()
    else:
        repositories = kwargs['repositories']

    grimoires = []
    for grim_dir in repositories:
        grimoire = get_repo_name(grim_dir=grim_dir)
        grimoires.append(grimoire)

    return grimoires
