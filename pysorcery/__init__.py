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
#-------------------------------------------------------------------------------

# System Libraries
import sys

# Other Libraries
import distro

# Application Libraries
from pysorcery.lib import libtext
from pysorcery.lib import logging

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
__version__ = '0.1.1'

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

# Other Optional Libraries
deb_distro_list=['Ubuntu']
distro_id=distro.linux_distribution()[0]
