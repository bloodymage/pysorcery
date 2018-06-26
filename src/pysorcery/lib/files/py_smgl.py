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
from pysorcery.lib import files
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
# get_installed
# get_alien
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function get_installed
#
# Generate a list of all files installed by sorcery
#
# Inputs
# ------
#    @param: self
#
# Returns
# -------
#    @return: installed_files - List of files
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_installed():
    logger.debug("Begin Function")

    install_log_dir = '/var/log/sorcery/install'
    installed_files = []
    for root, dirs, files_  in os.walk(install_log_dir):
        for i in files_:
            install_log = install_log_dir + '/'+ i
            f = files.BaseFile(install_log)
            installed_files = installed_files + f.read()

    logger.debug("End Function")
    return installed_files

#-------------------------------------------------------------------
#
# Function get_alien
#
# Generate a list of all files installed by sorcery
#
# Inputs
# ------
#    @param: self
#
# Returns
# -------
#    @return: installed_files - List of files
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_alien():
    logger.debug("Begin Function")

    # 1. Gather list of installed files
    logger.info("Discovering installed files...")
    installed_files = get_installed()
    
    # 2. Find all system files
    logger.info("Discovering ambient files...")
    files_ = files.BaseFiles()
    system_files = files_.get_system()
            
    # 3. Print files from step 3 - files from 2            
    alien = list(set(system_files) - set(installed_files))
    alien.sort()
            
    return alien
