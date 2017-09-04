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
# Additional code from 'patool'
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# File: pysorcery/lib/util/files/archive/genisoimage.py
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
# Archive: Genisoimage
#
#    Archive commands for the genisoimage program.
#
#-----------------------------------------------------------------------
"""Archive commands for the uncompress.real program."""

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
from pysorcery.lib import util
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

#-----------------------------------------------------------------------
#
# Classes
# 
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
# create_iso
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function create_compress
#
# Create ISO image.
#
# Inputs
# ------
#    @param: archive
#    @param: compression
#    @param: cmd
#    @param: verbosity
#    @param: interactive
#    @param: filenames
#
# Returns
# -------
#    @return: cmdlist
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def create_compress (archive, compression, cmd, verbosity, interactive, filenames):
    """Create a compressed archive."""
    cmdlist = [util.shell_quote(cmd)]
    if verbosity > 1:
        cmdlist.append('-v')
    cmdlist.append('-c')
    cmdlist.extend([util.shell_quote(x) for x in filenames])
    cmdlist.extend(['>', util.shell_quote(archive)])
    return (cmdlist, {'shell': True})
