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
# File: pysorcery/lib/util/files/archive/arc.py
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
# Archive: Arc
#
#    Archive commands for the arc program.
#
#-----------------------------------------------------------------------
"""
Archive: Arc

Archive commands for the arc program.
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
# extract_arc
# list_arc
# test_arc
# create_arc
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function extract_arc
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
def extract_arc (archive, compression, cmd, verbosity, interactive, outdir):
    """Extract a ARC archive."""
    # Since extracted files will be placed in the current directory,
    # the cwd argument has to be the output directory.
    cmdlist = [cmd, 'x', os.path.abspath(archive)]
    return (cmdlist, {'cwd': outdir})

#-------------------------------------------------------------------
#
# Function list_arc
#
# List a ARC archive.
#
# Inputs
# ------
#    @param: archive
#    @param: compression
#    @param: cmd
#    @param: verbosity
#    @param: interactive
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
def list_arc (archive, compression, cmd, verbosity, interactive):
    """List a ARC archive."""
    cmdlist = [cmd]
    if verbosity > 1:
        cmdlist.append('v')
    else:
        cmdlist.append('l')
    cmdlist.append(archive)
    return cmdlist

#-------------------------------------------------------------------
#
# Function test_arc
#
# Test a ARC archive.
#
# Inputs
# ------
#    @param: archive
#    @param: compression
#    @param: cmd
#    @param: verbosity
#    @param: interactive
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
def test_arc (archive, compression, cmd, verbosity, interactive):
    """Test a ARC archive."""
    return [cmd, 't', archive]

#-------------------------------------------------------------------
#
# Function create_arc
#
# Create a ARC archive.
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
#    @return: ...
#
# Raises
# ------
#    @raises: ...
#
#-------------------------------------------------------------------
def create_arc (archive, compression, cmd, verbosity, interactive, filenames):
    """Create a ARC archive."""
    cmdlist = [cmd, 'a', archive]
    cmdlist.extend(filenames)
    return cmdlist
