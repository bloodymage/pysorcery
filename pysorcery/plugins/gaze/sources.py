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
# File: pysorcery/plugins/gaze/sources.py
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
# pyGaze: sources
#
#    List all source files contained in a spell.
#
#-----------------------------------------------------------------------
"""
pyGaze: sources

List all source files contained in a spell.
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
# gaze_sources
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function gaze_sources
#
# list all source files contained in a spell
#
# Inputs
# ------
#    @param: args
#            args.spell - List of spells to get section.
#                         Minimum 1
#            args.quiet - decrease verbosity
#
# Returns
# -------
#    @return: None
#
# Raises
# ______
#    ...
#
#-----------------------------------------------------------------------
def gaze_sources(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = lib.Package(i)
        sources = spell.get_sources()
        
        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)
        for source in sources:
            logger.info1(source)

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

    cmd = subparsers.add_parser('sources',
                                parents = parent_parsers,
                                help = 'List all source files contained in a spell.'
    )
    cmd.add_argument('spell',
                     nargs = '+',
                     help = 'Display System Info'
    )        
    cmd.set_defaults(func = gaze_sources,
                     sudo = False)

    return cmd
