#! /usr/bin/env python3
#-------------------------------------------------------------------------------
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
#    Dionysius is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Dionysius.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import argparse
import copy
import subprocess

# Other Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery import __version__
from pysorcery.lib import libconfig
from pysorcery.lib import libfiles
from pysorcery.lib import libtext

# Other Optional Libraries
if distro.distro_id in distro.distro_dict['deb']:
    import apt

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------



#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class Alien():
    def __init__(self):
        logger.debug("Begin Function")

        logger.debug("End Function")
        return

    def identify(self):
        logger.debug("Begin Function")
        
        logger.info("In a few minutes I will print files found on this disk")
        logger.info("that were not installed by sorcery.")
        logger.warning("This is not a security feature!")        
        logger.info("Files could still be lurking undetected on this box.")

        if distro.distro_id in distro.distro_dict['deb']:
            # Find a python solution
            subprocess.run(["cruft"])
            
        elif distro.distro_id in distro.distro_dict['smgl']:
            # 1. Find Install Log Files
            # 2. Gather list of installed files
            logger.info("Discovering installed files...")
            installed_files = libfiles.FileList.list_installed_files()
            
            # 3. Find all system files
            logger.info("Discovering ambient files...")
            system_files = libfiles.FileList.list_system_files()
            
            # 4. Print files from step 3 - files from 2            
            alien_files = list(set(system_files) - set(installed_files))

            alien_files.sort()
            
            for i in alien_files:
                logger.info1(i)

        else:
            logger.error("Alien Error")    
            
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class SourceFile
# 
#
#-------------------------------------------------------------------------------
class SourceFile(BaseFile):
    def __init__(self,name):
        logger.debug("Begin Function")
        self.name = name
        self.url = url
        logger.debug("End Function")
        return

    def download(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return

    def unpack(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return

    def verify(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return
