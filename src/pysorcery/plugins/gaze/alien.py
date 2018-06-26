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
# File: pysorcery/plugins/gaze/alien.py
#
# This file is part of Sorcery.
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
# pyGaze: alien
#
#    Find files not installed by sorcery
#
#-----------------------------------------------------------------------
"""
pyGaze: alien

Find files not installed by sorcery.
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
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery import lib
from pysorcery.lib.util import text

# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
# Allow Color text on console
colortext = text.ConsoleText()
pkg_mgr = distro.distro_group[distro.distro_id]

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
# gaze_alien
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_alien
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
# Status: Works on Ubuntu (Subprocess.run)
#         Works, but buggy on SourceMage (Prints significantly
#                        more than expected)
#
#-------------------------------------------------------------------------------
def gaze_alien(args):
    logger.debug('Begin Function')

    # create 'alien' object
    files = lib.Files()
    alien = files.get_alien()
    for f in alien:
        print(f)

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function parser
#
# Create subcommand parsing options
#
# Inputs
# ------
#    @param: *args    - tuple of all subparsers and parent parsers
#                       args[0]: the subparser
#                       args[1:] the parent parsers
#    @param: **kwargs - Not used (Future?)
#
# Returns
# -------
#    @return: cmd
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):
    subparsers = args[0]
    parent_parsers = list(args[1:])
    cmd_help = 'Find and Display all files not tracked by the Sorcery Package Management System.'
    cmd = subparsers.add_parser('alien',
                                parents = parent_parsers,
                                aliases = ['aliens'],
                                help = cmd_help)
    if pkg_mgr == 'apt':
        cmd.set_defaults(func = gaze_alien,
                         sudo = True)
    else:
        cmd.set_defaults(func = gaze_alien,
                         sudo = False)
    return cmd
