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
# Archive: Ar
#
#    Archive commands for the AR program.
#
#-----------------------------------------------------------------------
"""
Archive: Ar

Archive commands for the ar program.
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
# extract_ar
# list_ar
# test_ar
# create_ar
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function extract_ar
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
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-------------------------------------------------------------------
def extract_ar (archive, compression, cmd, verbosity, interactive, outdir):
    """Extract a AR archive."""
    opts = 'x'
    if verbosity > 1:
        opts += 'v'
    cmdlist = [cmd, opts, os.path.abspath(archive)]
    return (cmdlist, {'cwd': outdir})

#-------------------------------------------------------------------
#
# Function list_ar
#
# LIST a AR archive.
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
def list_ar (archive, compression, cmd, verbosity, interactive):
    """List a AR archive."""
    opts = 't'
    if verbosity > 1:
        opts += 'v'
    return [cmd, opts, archive]

#-------------------------------------------------------------------
#
# Function test_ar
#
# Test a AR archive.
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
test_ar = list_ar

#-------------------------------------------------------------------
#
# Function create_ar
#
# Create a AR archive.
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
#    @raises: ...
#
#-------------------------------------------------------------------
def create_ar (archive, compression, cmd, verbosity, interactive, filenames):
    """Create a AR archive."""
    opts = 'rc'
    if verbosity > 1:
        opts += 'v'
    cmdlist = [cmd, opts, archive]
    cmdlist.extend(filenames)
    return cmdlist
