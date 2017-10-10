# -*- coding: utf-8 -*-
# Copyright (C) 2012-2015 Bastian Kleineidam
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""Archive commands for the lcab program."""

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
# Function create_cab
#
# ...
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
def create_cab (archive, compression, cmd, verbosity, interactive, filenames):
    """Create a CAB archive."""
    cmdlist = [cmd, '-r']
    cmdlist.extend(filenames)
    cmdlist.append(archive)
    return cmdlist
