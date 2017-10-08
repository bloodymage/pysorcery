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
# File: pysorcery/lib/util/files/archive/archmage.py
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
# Compressed: Archmage
#
#    Archive commands for the archmage program.
#
#-----------------------------------------------------------------------
"""
Compressed: Archmage

Archive commands for the archmage program.
"""

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import os

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from .. import util
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


#-------------------------------------------------------------------
#
# Functions
#
# extract_chm
# test_chm
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function extract_chm
#
# Extract a CHM archive.
#
# Inputs
# ------
#    @param: archive
#    @param: compression
#    @param: cmd
#    @param: verbosity
#    @param: interactive
#    @param: outdir
#
# Returns
# -------
#    @return: ...
#
# Raises
# ------
#    @raises: ...
#
#-------------------------------------------------------------------
def extract_chm (archive, compression, cmd, verbosity, interactive, outdir):
    """Extract a CHM archive."""
    # archmage can only extract in non-existing directories
    # so a nice dirname is created
    name = util.get_single_outfile("", archive)
    outfile = os.path.join(outdir, name)
    return [cmd, '-x', os.path.abspath(archive), outfile]


#-------------------------------------------------------------------
#
# Function test_chm
#
# Test a CHM archive.
#
# Inputs
# ------
#    @param: archive     -
#    @param: compression -
#    @param: cmd         -
#    @param: verbosity   -
#    @param: interactive -
#
# Returns
# -------
#    @return: ...
#
# Raises
# ------
#    @raises: ...
#
#-------------------------------------------------------------------
def test_chm (archive, compression, cmd, verbosity, interactive):
    """Test a CHM archive."""
    return [cmd, '-d', os.path.abspath(archive)]
