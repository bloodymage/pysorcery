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
from pysorcery.lib import distro
from pysorcery.lib import logging
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

#
pkg_mgr = distro.distro_group[distro.distro_id]

#-----------------------------------------------------------------------
#
# Classes
# 
# BasePackage
# BasePackages
# BasePackageVersions
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
    #    @return: description - The description of the package
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_description(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_description')
        self.description = func(self.name, repository=self.repository)
        return self.description

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
    #
    #-------------------------------------------------------------------
    def get_version(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_version')
        self.version = func(self.name, repository=self.repository)
        return self.version

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
    #
    #-------------------------------------------------------------------
    def get_url(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_url')
        self.url = func(self.name, repository=self.repository)
        return self.url

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
        self.short_description = func(self.name, repository=self.repository)
        return self.short_description

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # Get a package ...
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_section')
        self.section = func(self.name, repository=self.repository)
        return self.section

    #-------------------------------------------------------------------
    #
    # Function read_file
    #
    # Read a package's file.
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='read_file')
        conhents = func(self.name, repository=self.repository, filename=filename)
        return contents

    #-------------------------------------------------------------------
    #
    # Function is_package
    #
    # Verify package exists.
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='is_package')
        tf = func(self.name, repository=self.repository)
        return tf

    #-------------------------------------------------------------------
    #
    # Function get_license
    #
    # Get a package license.
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_license')
        self.license_ = func(self.name, repository=self.repository)
        return self.license_

    #-------------------------------------------------------------------
    #
    # Function get_maintainer
    #
    # Get a package maintainer
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_pkg_maintainer')
        self.maintainer = func(self.name, repository=self.repository)
        return self.maintainer

    #-------------------------------------------------------------------
    #
    # Function get_size
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
    #    @return: size - The amount of disk space of an installed
    #                    package.
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_size(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_size')
        self.size = func(self.name, repository=self.repository)
        return self.size

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
# Class BasePackages
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
class BasePackages():
    def __init__(self, packages=[]):
        self.packages = packages
        return

    #-------------------------------------------------------------------
    #
    # Function get_queue
    #
    # Get a list of packages in a queue
    #
    # Inputs
    # ------
    #    @param: self
    #    @param: which_queue
    #
    # Returns
    # -------
    #    @return: self.packages
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
    # Function get_installed
    #
    # Get a list of installed packages.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.packages
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
class BaseSection():
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_section_maintainer')
        self.maintainer = func(self.name, repository=self.repository)
        return self.maintainer

    #-------------------------------------------------------------------
    #
    # Function get_packages
    #
    # Get a list of packages within a section.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.name
    #            self.repository
    #
    # Returns
    # -------
    #    @return: self.packages
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_packages(self):
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_section_packages')
        self.packages = func(self.name, repository=self.repository)
        return self.packages

#-----------------------------------------------------------------------
#
# Class BaseSections
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
class BaseSections():
    def __init__(self, sections=[]):
        logger.debug("Begin Function")
        
        self.sections = sections

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class BaseRepository
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
class BaseRepository():
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
        func = util.get_module_func(scmd='sorcery',
                                    program=pkg_mgr,
                                    cmd='get_sections')
        self.sections = func(self.name, repository=self.repository)
        return self.sections

#-----------------------------------------------------------------------
#
# Class Repositories
#
# Provide support for a list of repositories.
# 
# Inputs
# ------
#    @param: repositories
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
class BaseRepositories():
    def __init__(self, repositories=[]):
        if repositories is None:
            self.repositories, self.directories = get_repositories()
        else:
            self.repositories = repositories

        return

#-----------------------------------------------------------------------
#
# Functions
#
# get_repository
# get_repositories
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
    func = util.get_module_func(scmd='sorcery',
                                program=pkg_mgr,
                                cmd='get_repository'
    )
    name, directory = func(name, repo_dir)
    return name, directory

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
#    @return: directories
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
    repositories, directories = func()
    return repositories, directories
