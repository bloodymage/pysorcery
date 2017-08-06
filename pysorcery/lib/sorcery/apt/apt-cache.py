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
from pysorcery.lib import sorcery

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
# Function get_repositories
#
# Inputs
# ------
#    @param: 
#
# Returns
# -------
#    @return: repositories
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def get_repositories(*args, **kwargs):
    var = subprocess.check_output(['apt-cache', 'policy'])
    repositories = []
    
    for line in var.splitlines():
        if 'l=' in str(line):
            line_list=str(line).split(',')
            
            repo_main=''
            repo_sub=''
            for item in line_list:
                if 'l=' in item:
                    repo_main = item.split('=')[1]
                if 'c=' in item:
                    repo_sub = item.split('=')[1]
                if len(repo_main) > 0 and len(repo_sub) > 0:
                    repo = repo_main + ' : ' + repo_sub
                    if repo not in repositories:
                        repositories.append(repo)

    return repositories, None
