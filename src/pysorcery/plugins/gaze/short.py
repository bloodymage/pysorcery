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
# File: pysorcery/plugins/gaze/short.py
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
# pyGaze: short
#
#    Provide a package short description.
#
#-----------------------------------------------------------------------
"""
pyGaze: short

Provide a package short description
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
# gaze_short
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function gaze_short
#
# view the short package description
#
# Inputs
# ------
#    #param: args
#            args.spell    - List of spells to get description.
#                            Minimum 1
#            args.grimoire - 
#            args.quiet    - 
# Returns
# -------
#    @return: None
#
#-----------------------------------------------------------------------
def gaze_short(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = lib.Package(i)
        short = spell.get_short()

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)
        message = colortext.colorize(short, 'none','white','black')
        logger.info1(message)

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

    cmd = subparsers.add_parser('short',
                                parents = parent_parsers,
                                help = 'Display spell short description.'
    )
    cmd.add_argument('spell',
                     nargs = '+',
                     help='Display System Info'
    )
    cmd.set_defaults(func = gaze_short,
                     sudo = False)
    return cmd
