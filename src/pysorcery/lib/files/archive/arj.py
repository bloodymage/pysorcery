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
# File: pysorcery/lib/util/files/archive/arj.py
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
# Archive: Arj
#
#    Archive commands for the Arj program.
#
#-----------------------------------------------------------------------
"""
Archive: Arj

Archive commands for the arj program.
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
# Function extract_arj
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
def extract_arj (archive, compression, cmd, verbosity, interactive, outdir):
    """Extract an ARJ archive."""
    cmdlist = [cmd, 'x', '-r']
    if not interactive:
        cmdlist.append('-y')
    cmdlist.extend([archive, outdir])
    return cmdlist

#-------------------------------------------------------------------
#
# Function list_arj
#
# Extract a ARJ archive.
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
def list_arj (archive, compression, cmd, verbosity, interactive):
    """List an ARJ archive."""
    cmdlist = [cmd]
    if verbosity > 1:
        cmdlist.append('v')
    else:
        cmdlist.append('l')
    if not interactive:
        cmdlist.append('-y')
    cmdlist.extend(['-r', archive])
    return cmdlist

#-------------------------------------------------------------------
#
# Function test_arj
#
# Extract a ARJ archive.
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
def test_arj (archive, compression, cmd, verbosity, interactive):
    """Test an ARJ archive."""
    cmdlist = [cmd, 't', '-r']
    if not interactive:
        cmdlist.append('-y')
    cmdlist.append(archive)
    return cmdlist

#-------------------------------------------------------------------
#
# Function create_arj
#
# Extract a ARJ archive.
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
def create_arj (archive, compression, cmd, verbosity, interactive, filenames):
    """Create an ARJ archive."""
    cmdlist = [cmd, 'a', '-r']
    if not interactive:
        cmdlist.append('-y')
    cmdlist.append(archive)
    cmdlist.extend(filenames)
    return cmdlist
