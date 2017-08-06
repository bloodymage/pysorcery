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
# Apt:
#
#    These functions work with apt packages.
#
#-----------------------------------------------------------------------
"""
Apt:


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
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib import util

# Conditional Libraries
try:
    # use Python 3 lzma module if available
    import apt
    py_apt = ('py_apt',)
except ImportError:
    py_apt = ()


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

# Supported packagex commands
PackageCommands = ('get_description',
                   'get_version',
                   'get_url',
                   'get_short',
                   'get_license',
                   'get_section',
                   'read_file',
                   'is_package')

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract,
# ...)
# Programs starting with "py_" are Python modules.
AptPrograms = {
    'package': {
        #None: ('apt', 'apt-get', 'apt-cache'),
        'get_description': ('py_apt', 'apt'),
        'get_version': ('py_apt',),
        'get_url': ('py_apt',),
        'get_short': ('py_apt',),
        'get_license': ('py_apt',),
        'get_section': ('py_apt',),
        'is_package': ('py_apt',),
        'read_file': ('apt',),
        'install' : ('apt','apt-get'),
    },
    'packages': {
        'get_installed': ('apt',),
        'get_queue': ('py_apt',),
    },
    'section': {
        'get_maintainer': ('py_apt',),
        'get_packages': ('py_apt',),
    },
    'repository': {
        'get_sections': ('py_apt',),
    },
    'repositories': {
        'get_repositories': ('apt-cache',),
    }
}

#-----------------------------------------------------------------------
#
# Classes
#
# AptPackage
# AptPackageVersions
# AptPackages
# AptSection
# AptSections
# AptRepository
# AptRepositories
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Package
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
class Package():
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
        program = find_package_program('package', 'get_description')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_version')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_url')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_short')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_section')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'read_file')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
                                    cmd='read_file')
        contents = func(self.name, repository=self.repository, filename=filename)
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
        program = find_package_program('package', 'is_package')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_license')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_maintainer')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'get_size')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('package', 'install')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
                                    cmd='install')
        func(args)
        
        return

#-----------------------------------------------------------------------
#
# Class PackageVersions
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
class PackageVersions(Package):
    pass

#-----------------------------------------------------------------------
#
# Class Packages
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
class Packages():
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
        program = find_package_program('packages', 'get_queue')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('packages', 'get_installed')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
                                    cmd='get_installed')
        self.packages = func(status)
        return self.packages

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
        program = find_package_program('section', 'get_maintainer')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
        program = find_package_program('section', 'get_packages')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
                                    cmd='get_section_packages')
        self.packages = func(self.name, repository=self.repository)
        return self.packages

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
class Repository():
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
        program = find_package_program('repository', 'get_sections')
        func = util.get_module_func(scmd='sorcery_apt',
                                    program=program,
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
class Repositories():
    def __init__(self, repositories=[]):
        if len(repositories) == 0:
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
    program = find_package_program('package', 'get_description')
    func = util.get_module_func(scmd='sorcery_apt',
                                program=program,
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
    program = find_package_program('repositories', 'get_repositories')
    func = util.get_module_func(scmd='sorcery_apt',
                                program=program,
                                cmd='get_repositories')
    repositories, directories = func()
    return repositories, directories

#-----------------------------------------------------------------------
#
# Functions
#
# get_description
# get_version
# get_url
# get_short
# get_section
# read_file
# is_package
# get_license
# get_size
#
#-----------------------------------------------------------------------

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
def find_package_program (class_, command, program=None):
    """Find suitable archive program for given format and mode."""
    commands = AptPrograms[class_]
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
        if program.startswith('py_'):
            # it's a Python module and therefore always supported
            return program
        exe = util.find_program(program)
        return exe
