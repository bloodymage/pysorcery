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
from pysorcery.lib import sorcery
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
class Package(sorcery.BasePackage):
    def __init__(self, name, repository=None):
        self.scmd = 'sorcery_apt'
        self.program = 'package'
        self.pkg_mgr = 'apt'
        super(Package, self).__init__(name, repository)
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
class PackageVersions(sorcery.BasePackageVersions):
    def __init__(self, name, repositories=[]):
        self.scmd = 'sorcery_apt'
        self.program = 'packageversions'
        self.pkg_mgr = 'apt'
        super(PackageVersions, self).__init__(name, repositories)

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
class Packages(sorcery.BasePackages):
    def __init__(self, packages=[]):
        self.scmd = 'sorcery_apt'
        self.program = 'packages'
        self.pkg_mgr = 'apt'
        super(Packages, self).__init__(packages)
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
        self.scmd = 'sorcery_apt'
        self.program = 'section'
        self.pkg_mgr = 'apt'
        super(Section, self).__init__(name, repository)
        return

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
        self.scmd = 'sorcery_apt'
        self.program = 'sections'
        self.pkg_mgr = 'apt'
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
class Repository():
    def __init__(self, name=None, repo_dir=None):
        self.scmd = 'sorcery_apt'
        self.program = 'repository'
        self.pkg_mgr = 'apt'
        super(Repository, self).__init__(name, repo_dir)
        return

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
        self.scmd = 'sorcery_apt'
        self.program = 'repositories'
        self.pkg_mgr = 'apt'
        self.cmd = 'get_repositories'
        super(Repositories, self).__init__(repositories)
        return

#-----------------------------------------------------------------------
#
# Functions
#
#
#-----------------------------------------------------------------------
