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
# File: pysorcery/lib/util/files/__init__.py
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
# Sorcery:
#
#
#-----------------------------------------------------------------------
"""
Files:

Library for sorcery that provides for interfacing with files and
directories.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries


# 3rd Party Libraries


# Application Libraries
# System Library Overrides

# Other Application Libraries

# Conditional Libraries

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

license_dir = { 'apt': '/usr/share/common-licenses',
                'sorcery': '/etc/sorcery/licenses'
                }
                
#-----------------------------------------------------------------------
#
# Classes
# 
#-----------------------------------------------------------------------
