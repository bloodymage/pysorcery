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
# File: pysorcery/lib/util/files/archive/cabextract.py
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
# Archive: CAB extract
#
#    Archive commands for the cabextract program.
#
#-----------------------------------------------------------------------
"""Archive commands for the cabextract program."""

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
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function extract_cab
#
# Extract a AR archive.
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
#    @return: 
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def extract_cab (archive, compression, cmd, verbosity, interactive, outdir):
    """Extract a CAB archive."""
    cmdlist = [cmd, '-d', outdir]
    if verbosity > 0:
        cmdlist.append('-v')
    cmdlist.append(archive)
    return cmdlist

#-------------------------------------------------------------------
#
# Function list_cab
#
# List a CAB archive.
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
#    @return: 
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def list_cab (archive, compression, cmd, verbosity, interactive):
    """List a CAB archive."""
    cmdlist = [cmd, '-l']
    if verbosity > 0:
        cmdlist.append('-v')
    cmdlist.append(archive)
    return cmdlist

#-------------------------------------------------------------------
#
# Function test_cab
#
# Test a CAB archive.
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
#    @return: 
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def test_cab (archive, compression, cmd, verbosity, interactive):
    """Test a CAB archive."""
    return [cmd, '-t', archive]
