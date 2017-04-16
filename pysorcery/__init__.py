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
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib import libtext

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
__version__ = '0.0.1'
enable_debugging_mode=True

# Enable Logging
# create logger
logger = logging.getLogger(__name__)
logger.setLevel(20)

# Define Handlers
consolehandler = logging.ColorizingStreamHandler()

# Define Formatters
consoleformatter = logging.ConsoleLvlFormatter("%(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s")

# Set handler ...
consolehandler.setLevel(0)
consolehandler.setFormatter(consoleformatter)

# Add handlers to logger
logger.addHandler(consolehandler)
