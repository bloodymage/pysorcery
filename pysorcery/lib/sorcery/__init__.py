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


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging

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
conf = config.SorceryConfig()

# Supported package commands
Commands = ('get_description',
            'get_version',
            'get_url',
            'get_short',
            'get_license',
            'get_pkg_maintainer',
            'get_section',
            'read_file',
            'is_package',
            'is_spell',
            'get_size',
            'get_queue',
            'get_installed',
            'get_log')

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract,
# ...)
# Programs starting with "py_" are Python modules.
Programs = {
    'smgl': {
        'spell': {
            #None: ('apt', 'apt-get', 'apt-cache'),
            'get_description': ('py_api_01', 'gaze'),
            'get_version': ('py_api_01',),
            'get_url': ('py_api_01',),
            'get_short': ('py_api_01',),
            'get_license': ('py_api_01',),
            'get_pkg_maintainer': ('py_api_01',),
            'get_section': ('py_api_01',),
            'is_package': ('py_api_01',),
            'is_spell': ('py_api_01',),
            'get_size': ('gaze',),
            'get_log': ('py_api_01',),
            'get_sources': ('gaze',),
            'get_source_uris': ('gaze',),
        },
        'spellversions': {
        },
        'spells': {
            'get_queue': ('py_api_01',),
            'get_installed': ('py_api_01',),
            'get_orphans': ('gaze',),
        },
        'section': {
            'get_section_maintainer': ('py_api_01',),
            'get_section_packages': ('py_api_01',),
            'get_section_spells': ('py_api_01',),
        },
        'sections': {
        },
        'grimoire': {
            'get_repository': ('py_api_01',),
        },
        'codex': {
            'get_codex': ('py_api_01',),
        }
    },
    'apt': {
        'package': {
            #None: ('apt', 'apt-get', 'apt-cache'),
            'get_description': ('py_apt',),
            'get_version': ('py_apt',),
            'get_url': ('py_apt',),
            'get_short': ('py_apt',),
            'get_license': ('py_apt',),
            'get_section': ('py_apt',),
            'get_size': ('py_apt',),
            'is_package': ('py_apt',),
            'read_file': ('apt',),
            'install' : ('apt', 'apt-get'),
        },
        'packageversions' : {
        },
        'packages': {
            'get_installed': ('apt',),
            'get_queue': ('py_apt',),
            'get_orphans': ('deborphan',),
        },
        'section': {
            'get_maintainer': ('py_apt',),
            'get_packages': ('py_apt',),
        },
        'sections': {
        },
        'repository': {
            'get_sections': ('py_apt',),
        },
        'repositories': {
            'get_repositories': ('apt-cache',),
        }
    }
}

#-----------------------------------------------------------------------
#
# Classes
# 
# Warning: Do not call this classes directly.  The program will
# crash.
#
# BasePackage
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class BasePackage
#
# The base class for working with a single package.
#
# To Do: Build in error checking...
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
class BasePackage:
    def __init__(self, name, repository=None, version=None):
        self.name = name
        self.repository = repository
        self.version = version
        return

    #-------------------------------------------------------------------
    #
    # Function get_info
    #
    # Get the requested info about a packge.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.pkg_mgr
    #            self.program
    #            self.scmd
    #            self.name
    #            self.repository
    #    @param: info - identifies information to be obtained
    #
    # Returns
    # -------
    #    @return: info - The requested information
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def get_info(self, info):
        program = find_program(self.pkg_mgr, self.program, info)
        func = util.get_module_func(scmd=self.scmd,
                                    program=program,
                                    cmd=info)
        info = func(self.name, repository=self.repository)
        return info

    #-------------------------------------------------------------------
    #
    # Function get_description
    #
    # Get a package's description.
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
        self.description = self.get_info('get_description')
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
        self.version = self.get_info('get_version')
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
        self.url = self.get_info('get_url')
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
        self.short_description = self.get_info('get_short')
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
        self.section = self.get_info('get_section')
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
        contents = self.get_info('read_file')
        return contents


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
    def is_package(self, func='is_package'):      
        tf = self.get_info(func)
        return tf

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
        self.license_ = self.get_info('get_license')
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
        self.maintainer = self.get_info('get_pkg_maintainer')
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
        self.size = self.get_info('get_size')
        return self.size

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
    def get_log(self, log):
        if self.version is None:
            self.version = self.get_version()
        if log == 'compile':
            extension = conf.extension
        else:
            extension = None

        program = find_program(self.pkg_mgr, self.program, 'get_log')
        func = util.get_module_func(scmd=self.scmd,
                                    program=program,
                                    cmd='get_log')
        content = func(self.name,
                       log=log,
                       version=self.version,
                       extension=extension)
        return content

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
    def get_sources(self):
        self.sources = self.get_info('get_sources')
        return self.sources

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
    def get_source_uris(self):
        self.source_uris = self.get_info('get_source_uris')
        return self.source_uris

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
        program = find_package_program(self.pkg_mgr, self.program, 'install')
        func = util.get_module_func(scmd=self.scmd,
                                    program=self.program,
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
# The Class for working with Apt packages.
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
class BasePackages:
    def __init__(self, packages=[]):
        self.packages = packages
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
    def get_info(self, info, which_info=None):
        program = find_program(self.pkg_mgr, self.program, info)
        func = util.get_module_func(scmd=self.scmd,
                                    program=program,
                                    cmd=info)
        info = func(which_info)
        return info

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
        self.packages = self.get_info('get_queue', which_queue)
        return self.packages

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
        self.packages = self.get_info('get_installed', status)
        return self.packages

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
    def get_orphans(self):
        program = find_program(self.pkg_mgr, self.program, 'get_orphans')
        func = util.get_module_func(scmd=self.scmd,
                                    program=program,
                                    cmd='get_orphans')
        self.packages = func()
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
class BaseSection(BasePackages):
    def __init__(self, name, repository=None):
        self.name = name
        self.repository = repository
        super(BaseSection, self).__init__()
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
        self.maintainer = self.get_info('get_section_maintainer', self.name)
        return self.maintainer

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
        self.packages = self.get_info('get_section_packages',
                                      self.name)
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
        self.sections = sections
        return

#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------------
class BaseRepository():
    def __init__(self, name=None, repo_dir=None):
        self.name, self.directory = get_repository(name, repo_dir)
        return

    #-------------------------------------------------------------------
    #
    # Function get_info
    #
    # ...
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
    def get_info(self, info):
        program = find_program(self.program, info)
        func = util.get_module_func(scmd=self.scmd,
                                    program=program,
                                    cmd=info)
        info = func(self.name, self.repositories)
        return info

    #-------------------------------------------------------------------
    #
    # Function get_section
    #
    # ....
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
        self.sections = get_info('get_sections')
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
class BaseRepositories():
    def __init__(self, repositories=[]):
        if len(repositories) == 0:
            self.repositories, self.directories = get_repositories(self.pkg_mgr,
                                                                   self.scmd,
                                                                   self.program,
                                                                   self.cmd)
        else:
            self.repositories = repositories
        return

#-----------------------------------------------------------------------
#
# Functions
#
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
def get_repository(pkg_mgr, scmd, cmd, name=None, repo_dir=None):
    program = find_program(pkg_mgr, 'repository', cmd)    
    func = util.get_module_func(scmd=scmd,
                                program=program,
                                cmd=cmd
    )
    name, directory = func(name, repo_dir)
    return name, directory

#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------------
def get_repositories(pkg_mgr, scmd, program, cmd, *args, **kwargs):
    program = find_program(pkg_mgr, program, cmd)
    func = util.get_module_func(scmd=scmd,
                                program=program,
                                cmd=cmd)
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
def find_program(pkg_mgr, class_, command, program=None):
    """Find suitable archive program for given format and mode."""
    commands = Programs[pkg_mgr][class_]
    programs = []
    if program is not None:
        # try a specific program first
        programs.append(program)
    # first try the universal programs with key None
    for key in (None, command):
        if key in commands:
            programs.extend(commands[key])
    if not programs:
        raise Exception("%s program class `%s' is not supported"
                        % (command, class_))
    # return the first existing program
    for program in programs:
        if program.startswith('py_'):
            # it's a Python module and therefore always supported
            return program
        exe = util.find_program(program)
        return exe
