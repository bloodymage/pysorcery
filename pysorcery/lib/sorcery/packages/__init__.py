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
# File: pysorcery/lib/sorcery/packages/__init__.py
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
import subprocess
import os

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib import util
# from pysorcery.lib.sorcery import repositories


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

#
pkg_mgr = distro.distro_group[distro.distro_id]
#-----------------------------------------------------------------------
#
# Classes
#
#
# BasePackage
# BasePackages
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class BasePackage
# 
#
#-----------------------------------------------------------------------
class BasePackage():
    def __init__(self,name):
        logger.debug("Begin Function")
        
        self.name = name

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function get_description
    #
    # Input:  ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def get_description(self):
        func = util.get_module_func('packages',
                                    pkg_mgr,
                                    'get_description')
        description = func(self.name)
        return description

    #-------------------------------------------------------------------
    #
    # Function get_description
    #
    # Input:  ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
    def get_version(self):
        func = util.get_module_func('packages',
                                    pkg_mgr,
                                    'get_version')
        version = func(self.name)
        return version

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def install(self,args):
        func = util.get_module_func('packages',
                                    pkg_mgr,
                                    'install')
        func(args)
        
        return

#-----------------------------------------------------------------------
#
# Class BaseSpells
# 
#
#-----------------------------------------------------------------------
class BasePackages():
    pass
