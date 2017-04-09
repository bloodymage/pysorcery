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
# This file is a flat file prototype.  There are several things I flat out do not
# know how to do.  This allows me to try out the parts I do know.
#
#-------------------------------------------------------------------------------

# added so distributors can consistently specify a private module location
#private_module_path = "/usr/share/weather-util"
#if private_module_path:
#    sys.path.insert(1, private_module_path)


#-------------------------------------------------------------------------------
#
# Libraries
#
#
#-------------------------------------------------------------------------------

# System Libraries
import sys

# Other Libraries
import apt

# Application Libraries
from pysorcery.lib import logging
from pysorcery.lib import libtext
from pysorcery.lib import libspell

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Seethe Roadmap for version information


# Enable Logging
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(20)

# Define Handlers
consolehandler = logging.ColorizingStreamHandler()

# Define Formatters
consoleformatter = logging.ConsoleLvlFormatter("%(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")

# Set handler ...
consolehandler.setLevel(20)
consolehandler.setFormatter(consoleformatter)

# Add handlers to logger
logger.addHandler(consolehandler)


#-------------------------------------------------------------------------------
#
# Classes
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class DebianSpell
# 
#
#-------------------------------------------------------------------------------
class DebianSpell(libspell.Spell):
    def get_spell_info(self):
        cache    = apt.Cache()
        pkg      = cache[self.name]
        versions = pkg.versions
        self.description  = versions[0].description
        self.architecture = versions[0].architecture
        self.version=[]
        for i in versions:
            self.version.append(versions[i].version)
            
        self.url          = versions[0].homepage
        self.section      = versions[0].section
        self.dependencies = versions[0].dependencies
        self.optional_dependencies = versions[0].suggests

        return self

    def print_version(self,multi):
        print(multi)
        if multi:
            m = len(self.version)
        else:
            m = 1

        print("Repository       " +
              "Section          " +
              "Package          " +
              "Repo version     " +
              "Installed version")

        print("----------       " +
              "-------          " +
              "-------          " +
              "------------     " +
              "-----------------")

        for i in range(m):
            if self.version[i] == self.version[0]:
                p_version = self.version[0]
            else:
                p_version = '-'
                
            print("                 " +
                  self.section + "  " +
                  self.name +    "  " +
                  self.version[i] + "  " +
                  p_version)
