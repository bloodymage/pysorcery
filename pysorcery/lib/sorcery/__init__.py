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

Library for sorcery that provides for interfacing with files and
directories.
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
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib import util
from pysorcery.lib.util import config

# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#
pkg_mgr = distro.distro_group[distro.distro_id]
                
config_ = config.SorceryConfig()
license_dir = config_.license_dir[pkg_mgr]

#-----------------------------------------------------------------------
#
# Classes
# 
# BasePackage
# BasePackages
# BaseSection
# BaseSections
# BaseRepository
# BaseRepositories
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class BasePackage
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
class BasePackage():
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
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def get_description(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_description')
        description = func(self.name, repository=self.repository)
        return description

    #-------------------------------------------------------------------
    #
    # Function get_version
    #
    # Get a package version.
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
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def get_version(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_version')
        version = func(self.name, repository=self.repository)
        return version

    #-------------------------------------------------------------------
    #
    # Function get_url
    #
    # Get a package url.
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
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def get_url(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_url')
        url = func(self.name, repository=self.repository)
        return url

    #-------------------------------------------------------------------
    #
    # Function get_short
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_short(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_short')
        short_description = func(self.name, repository=self.repository)
        return short_description

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_section(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_section')
        section = func(self.name, repository=self.repository)
        return section

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def read_file(self, filename):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='read_file')
        section = func(self.name, repository=self.repository, filename=filename)
        return section

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def is_package(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='is_package')
        tf = func(self.name, repository=self.repository)
        return tf

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_license(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_license')
        license_ = func(self.name, repository=self.repository)
        return license_

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_maintainer(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_maintainer')
        maintainer = func(self.name, repository=self.repository)
        return maintainer

    #-------------------------------------------------------------------
    #
    # Function install
    #
    # Install a package
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='install')
        func(args)
        
        return

#-----------------------------------------------------------------------
#
# Class BasePackageVersions
#
# This class is for working with mulhiple versions of the same package.
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
class BasePackageVersions(BasePackage):
    pass

#-----------------------------------------------------------------------
#
# Class BaseSpells
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
class BasePackages():
    def __init__(self, packages=[]):
        self.packages = packages
        return

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_queue(self, which_queue):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_queue')
        self.packages = func(which_queue)
        return self.packages


    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package short description.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_installed(self, status=None):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_installed')
        self.packages = func(status)
        return self.packages

#-----------------------------------------------------------------------
#
# Class BaseSection
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
class BaseSection():
    def __init__(self, name, repository=None):
        logger.debug("Begin Function")
        
        self.name = name
        self.repository = repository

        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class BaseSection
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
class BaseSections():
    pass

#-------------------------------------------------------------------------------
#
# Class BaseRepository
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
#-------------------------------------------------------------------------------
class BaseRepository():
    def __init__(self,name=None,repo_dir=None):
        logger.debug('Begin Function')

        logger.debug2('Name: ' + str(name))

        self.name = get_repo_name(name, repo_dir)

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
# Class Repositories
# 
#
#-------------------------------------------------------------------------------
class BaseRepositories():
    def __init__(self, repositories=None):
        if repositories is None:
            self.repositories = get_repositories()
        else:
            self.repositories = repositories

        return

#-------------------------------------------------------------------------------
#
# Functions
#
# Get_repo_name
# 
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function 
#
# Input:  ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_repo_name(name=None, repo_dir=None):
    func = util.get_module_func(scmd='sorcery',
                                program=pkg_mgr,
                                cmd='get_repo_name')
    name = func(name, repo_dir)
    return name

#-------------------------------------------------------------------------------
#
# Function get_repositories
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#
# Returns
# -------
#    @return: repositories
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def get_repositories(*args, **kwargs):
    func = util.get_module_func(scmd='sorcery',
                                program=pkg_mgr,
                                cmd='get_repositories')
    repositories = func()
    return repositories
