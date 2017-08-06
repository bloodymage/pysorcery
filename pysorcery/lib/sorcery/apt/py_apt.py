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
import apt
import sys
import subprocess
import os

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries

# Other Optional Libraries


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
# Function get_description
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
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    description  = versions[0].description

    cache.close()
    return description

#-----------------------------------------------------------------------
#
# Function get_version
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
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    pkg_info = pkg.versions
    version = pkg_info[0].version

    cache.close()
    return version

#-----------------------------------------------------------------------
#
# Function get_url
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
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    pkg_info = pkg.versions
    url = pkg_info[0].homepage

    cache.close()
    return url

#-----------------------------------------------------------------------
#
# Function get_short
#
# Get's a package's short description.  In apt, the package's description is
# used as there isn't a short description.
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
def get_short(name, **kwargs):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    short_description  = versions[0].summary

    cache.close()
    return short_description

#-----------------------------------------------------------------------
#
# Function get_section
#
# ...
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
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions

    pkg_section = versions[0].section

    if 'universe' in pkg_section or 'multiverse' in pkg_section:
        section = pkg_section.split('/')[1]
    else:
        section = pkg_section            

    cache.close()
    return section

#-----------------------------------------------------------------------
#
# Function read_file
#
# Get's a package's short description.  In apt, the package's description is
# used as there isn't a short description.
#
# Inputs
# ------
#    @param: name
#    @param: **kwargs
#
# Returns
# -------
#    @return: description
#
# Raises
# ------
#    @error: NotImplementedError
#
#-----------------------------------------------------------------------
def read_file(name, **kwargs):
    raise NotImplementedError
    return

#-----------------------------------------------------------------------
#
# Function is_package
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
def is_package(name, **kwargs):
    try:
        cache = apt.cache.Cache()
        cache.open()
        pkg = cache[name]
        cache.close()
        pkg_exists = True
    except Exception:
        pkg_exists = False
        
    return pkg_exists

#-----------------------------------------------------------------------
#
# Function get_license
#
# Get the package license
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
def get_license(name, **kwargs):
    cache = apt.cache.Cache()
    cache.open()

    pkg = cache[name]
    versions = pkg.versions
    license_ = 'Not Implemented'

    raise NotImplementedError
    cache.close()
    
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
    cache = apt.cache.Cache()
    cache.open()

    pkg = cache[name]
    versions = pkg.versions
    size = versions[0].size
    
    cache.close()
    
    return size

#-------------------------------------------------------------------------------
#
# Function get_repository
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
def get_repository(name=None, directory=None):
    return name, None

#-----------------------------------------------------------------------
#
# Function get_pkg_maintainer
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
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    maintainer = 'Not Implemented'

    cache.close()

    raise NotImplementedError
    return maintainer

#-----------------------------------------------------------------------
#
# Function get_section_maintainer
#
# Inputs
# ------
#    @param: 
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
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    maintainer = 'Not Implemented'

    cache.close()

    raise NotImplementedError
    return maintainer

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
    if which_queue == 'install':
        cache = apt.cache.Cache()
        cache.open(None)
        cache.upgrade()
        queue = cache.get_changes()
    elif which_queue == 'remove':
        queue = []
        logger.error('Not Implimented')
        raise NotImplementedError
    else:
        queue = []
        logger.critical('We Fucked Up')
    return queue
