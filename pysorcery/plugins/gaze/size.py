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
# File: pysorcery/cli/archive.py
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
# pyGaze: size
#
#    View ...
#
#-----------------------------------------------------------------------
"""
pyGaze: size

View...
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
from pysorcery.lib.system import argparse
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import lib
from pysorcery.lib import util
from pysorcery.lib.util import config
from pysorcery.lib.util import text
# Conditional Libraries

pkg_mgr = distro.distro_group[distro.distro_id]
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
# gaze_size
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_size
#
# print the sizes and file counts of the passed installed spell(s) or if -all is
# specified, of all the spells. In addition, this will print the largest spell.
#
# Inputs
# ------
#    @param: args
#            args.spell - Spell to print compile log.
#                         Maximum 1
#            args.all   -
#            args.quiet - decrease verbosity
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def gaze_size(args):
    logger.debug('Begin Function')

    for i in args.spell:
        spell = lib.Package(i)

        size = spell.get_size()
        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(str(spell.size) + 'kb', 'none','white','black')
        logger.info1(message)

    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
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

    help_ = { 'apt': 'Print the sizes and file counts of the passed installed Package(s).',
              'smgl': 'Print the sizes and file counts of the passed installed spell(s).'
    }
    cmd = subparsers.add_parser('size',
                                parents = parent_parsers,
                                help = help_[pkg_mgr]
    )

    arg = { 'apt': 'package',
            'smgl': 'spell'
    }
    help_ = { 'apt': 'Package to view size',
              'smgl': 'Spell to view size'
              }
    cmd.add_argument('spell',
                     nargs = '+',
                     metavar = arg[pkg_mgr],
                     help = help_[pkg_mgr])
    cmd.add_argument('-a','-all','--all',
                     action = 'store_true',
                     help = 'Display sizes of all the spells. In addition, this will print the largest spell.')
    cmd.set_defaults(func = gaze_size,
                     sudo = False)

    return cmd
