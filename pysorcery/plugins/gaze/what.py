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
# gaze whats
#
#   This is a bonus application for pysorcery.  PySorcery for multiple
#   reasons to internally extract, create, list the contents, etc.
#   archive files of multiple formats.  To test the capabilities of the
#   underlying code, this application was developed.
#
#-----------------------------------------------------------------------
"""
Gaze what

View the long package description
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
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes

# Other Application Libraries
from pysorcery import *
from pysorcery import lib
from pysorcery.lib import util
from pysorcery.lib.util import config
from pysorcery.lib.util import text
from pysorcery.lib.util.files import archive
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
# gaze_what
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
# view the long package description
#
# Input:  args
#         args.spell    - List of spells to get description.
#                         Minimum 1
#         args.grimoire - Grimoire(s) to check for spell
#         args.quiet    - Limit print output
# Output: Prints spell description
# Return: None
#
# Status: Working for Source Mage
#         Working for Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_what(args):
    logger.debug('Begin Function')

    terms = {
        'the_force': 'The Force is an energy field created by all living things. It surrounds us, penetrates us, and binds the galaxy together.',
        '42': '42 is the answer to life, the universe, and everything.',
        'the_matrix': '"The Matrix is everywhere. It is all around us, even now in this very room. You can see it when you look out your window or when you turn on your television. You can feel it when you go to work, when you go to church, when you pay your taxes; it is the world that has been pulled over your eyes to blind you from the truth."'
        
    }

    # Provide hidden easter egg:
    if (args.spell[0] == 'is' and
        args.spell[1] in terms):
        logger.info(terms[args.spell[1]])
        
    else:
        # For each spell in the spell list...
        for i in args.spell:
            logger.debug2('Loop iteration: ' + i)
            
            spell = lib.Package(i)
            try:
                description = spell.get_description()
            except:
                description = 'Fall back description, something went wrong'

            logger.debug3('Spell: ' + str(spell))
            
            message = colortext.colorize(spell.name, 'bold','white','black')
            logger.info(message)

            message = colortext.colorize(description, 'none','white','black')
            logger.info1(message)

    
    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function parser
#
# Generate command subparser
#
# Input:  subparser
#         parent_parser
#         repo_parent_parser
# Return: cmd
#
#-----------------------------------------------------------------------
def parser(subparsers, parent_parser, repo_parent_parser=None):
    cmd = subparsers.add_parser('what',
                                parents = [parent_parser,
                                           repo_parent_parser
                                ],
                                help = 'Display spell description.'
    )
    cmd.add_argument('spell',
                     nargs = '+',
                     help = 'Display System Info')
    cmd.set_defaults(func = gaze_what,
                     sudo = False)

    return cmd
