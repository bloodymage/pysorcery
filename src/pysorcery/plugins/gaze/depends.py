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
# File: pysorcery/plugins/gaze/depends.py
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
# pyGaze: depends
#
#    ...
#
#-----------------------------------------------------------------------
"""
pyGaze: depends


...
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

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
# gaze_depends
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_depends
#
# shows the spells that explicitly or recursively depend on this
# installed spell.  Up to level $level if specified. Only enabled
# dependencies are shown.
#
# If --fast is specified more limited output is produced, but it run
#s much faster.
# If --required is specified only the required dependencies are shown and the
# runtime ones are skipped.
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_depends(args):
    logger.debug('Begin Function')

    spell = lib.Package(args.spell[0])
    depends = spell.get_depends()

    for dep in depends:
        print(dep)

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

    cmd_help = 'shows the spells that explicitly or recursively depend on this installed spell.  Only enabled dependencies are shown.'
    cmd = subparsers.add_parser('depends',
                                parents = parent_parsers,
                                help = cmd_help
    )
    cmd.add_argument('spell',
                     nargs = 1,
                     help = 'Display System Info')
    cmd.add_argument('level',
                     nargs = '?',
                     help='Up to level $level if specified')
    cmd.add_argument('--fast',
                     action = 'store_true',
                     help = 'Limit output, but runs much faster.')
    cmd.add_argument('--required',
                     action = 'store_true',
                     help = 'Show only the required dependencies and skip the runtime dependencies.')
    cmd.set_defaults(func = gaze_depends,
                     sudo = False)

    return cmd
