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
# File: pysorcery/plugins/gaze/dependencies.py
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
# pyGaze: dependencies
#
# ...
#
#-----------------------------------------------------------------------
"""
pyGaze: dependencies

...
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import os
import sys

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
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_dependencies
#
# shows the spells that spell explicitly or recursively depends on.
# Up to level $level if specified. The -c option skips trees that have already been
# shown, the --no-optionals flag skips optional dependencies.
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
def gaze_dependencies(args):
    logger.debug('Begin Function')

    spell = lib.Package(args.spell[0])
    dependencies = spell.get_dependencies()

    for dep in dependencies:
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

    cmd = subparsers.add_parser('dependencies',
                                parents = parent_parsers,
                                help = 'shows the spells that spell explicitly or recursively depends on.'
    )
    cmd.add_argument('spell',
                     nargs = 1,
                     help = 'Display System Info'
    )
    cmd.add_argument('level',
                     nargs = '?',
                     help = 'Up to level $level if specified.'
    )
    cmd.add_argument('-c',
                     action = 'store_true',
                     help = 'skips trees that have already been shown'
    )
    cmd.add_argument('--no-optionals',
                     action = 'store_true',
                     help = 'skips optional dependencies.'
    )
    cmd.set_defaults(func = gaze_dependencies,
                     sudo = False)

    return cmd
