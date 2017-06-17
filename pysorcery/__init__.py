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
# Additional code from 'patool'
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# This file is part of Sorcery.
#
# File: pysorcery/__init__.py
#
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License,
#    or (at your option) any later version.
#
#    Sorcery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.
#
# Sorcery
#
#
#
#-----------------------------------------------------------------------
"""
BASH version
Original version Copyright 2001 by Kyle Sallee
Additions/corrections Copyright 2002 by the Source Mage Team

Python rewrite
Copyright 2017 Geoff S Derber

This file is part of Sorcery.

File: pysorcery/__init__.py

Additional code from 'patool'
Copyright (C) 2010-2015 Bastian Kleineidam

Sorcery is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published
by the Free Software Foundation, either version 3 of the License,
or (at your option) any later version.

Sorcery is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.

Sorcery

"""
#-----------------------------------------------------------------------
#
# Dunders
#
#-----------------------------------------------------------------------
__all__ = ['__author__',
           '__contact__',
           '__copyright__',
           '__license__',
           '__status__',
           '__version__',
           'DEBUG'
           ]
__author__ = 'Geoff S Derber'
__contact__ = 'gd.smlinux@gmail.com'
__copyright__ = 2017
__license__ = 'GPLv3+'
__status__ = 'Prototype'
__version__ = '0.0.1'

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries


# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
DEBUG=False

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
