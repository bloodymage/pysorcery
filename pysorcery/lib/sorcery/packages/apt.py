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
import apt
import sys
import subprocess
import os

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib.sorcery import repositories

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
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class DebianSpell
# 
#
#-------------------------------------------------------------------------------
class DebianSpell():
    def __init__(self,name):
        logger.debug("Begin Function")
        BaseSpell.__init__(self,name)

        self.cache    = apt.cache.Cache()
#        self.cache.update()
        self.cache.open()
        
        self.pkg      = self.cache[self.name]

        versions = self.pkg.versions

        self.version = versions[0].version

        self.architecture = versions[0].architecture
        self.description  = versions[0].description
        self.url = versions[0].homepage
        self.short = self.description

        pkg_section = versions[0].section

        if 'universe' in pkg_section or 'multiverse' in pkg_section:
            self.section = str(pkg_section).split('/')[1]
        else:
            self.section = str(pkg_section)            

        self.grimoire = 'Fix Me'            
        self.dependencies = versions[0].dependencies
        self.optional_dependencies = versions[0].suggests
        self.size = versions[0].installed_size
        
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ....x
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def install(self, args):
        logger.debug("Begin Function")

        if args.reconfigure:
            subprocess.run(['dpkg-reconfigure', self.name])

            
        if args.compile:
            subprocess.run(['apt-build', 'install', self.name])
        else:
            subprocess.run(['apt-get', 'install', self.name])
                    
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def remove(self, args):
        logger.debug("Begin Function")

        #subprocess.run(['apt-get', 'remove', self.name])

        cache = apt.cache.Cache()
        cache.open(None)
        pkg = cache[pkg_name]
        cache.update()
        pkg.mark_delete(True, purge=True)
        resolver = apt.cache.ProblemResolver(cache)
        
        if pkg.is_installed is False:
            logger.error(pkg_name + " not installed so not removed")
        else:
            for pkg in cache.get_changes():
                if pkg.mark_delete:
                    logger.info(pkg_name + " is installed and will be removed")
                    logger.info(" %d package(s) will be removed" % cache.delete_count)
                    resolver.remove(pkg)
                    
        try:
            cache.commit()
            cache.close()
        except Exception:
            logger.error("Sorry, package removal failed.")
                    
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Functions
#
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function get_description
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_description(name):
    cache    = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    versions = pkg.versions
    description  = versions[0].description

    cache.close()
    return description

#-------------------------------------------------------------------------------
#
# Function get_description
#
# Input:  ...
# Output: ...
# Return: ...
#
#-------------------------------------------------------------------------------
def get_version(name):
    cache = apt.cache.Cache()
    cache.open()
        
    pkg = cache[name]
    pkg_info = pkg.versions
    version = pkg_info[0].version

    cache.close()
    return version
