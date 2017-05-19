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
# pyArchive
#
#   This is a bonus application for pysorcery.  PySorcery for multiple
#   reasons to internally extract, create, list the contents, etc.
#   archive files of multiple formats.  To test the capabilities of the
#   underlying code, this application was developed.
#
#-----------------------------------------------------------------------
"""
This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
archive files of multiple formats.  To test the capabilities of the
underlying code, this application was developed.
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
# archive_extract
# archive_list
# archive_create
# archive_test
# archive_repack
# archive_recompress
# archive_diff
# archive_search
# archive_formats
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

    # For each spell in the spell list...
    if args._egg:
        terms = {
            'the_force': 'The Force is ...',
            '42': 'What is the answer to life, the universe, and everything?'
            }
        logger.info(terms[args.spell[0]])
        
    else:
        for i in args.spell:
            logger.debug2('Loop iteration: ' + i)
            
            spell = libspell.Spell(i)
            
            logger.debug3('Spell: ' + str(spell))
            
            message = colortext.colorize(spell.name, 'bold','white','black')
            logger.info(message)

            message = colortext.colorize(spell.description, 'none','white','black')
            logger.info1(message)

    
    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function archive_extract
#
# Extract files listed.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.files - List of files to extract
#         args.recursive - Extract all files in all subfolders
#         args.depth (Add me) - if recursive, limit to depth #
#         args.output_dir - Directory to extract to
# Return: None
#
#-----------------------------------------------------------------------
def parser(subparsers, parent_parser, repo_parent_parser=None):
    #-------------------------------------------
    #
    # create the parser for the 'what' command
    #
    #-------------------------------------------
    cmd = subparsers.add_parser('what',
                                        parents = [parent_parser,
                                                   repo_parent_parser
                                        ],
                                        help = 'Display spell description.'
    )
    subcmd = cmd.add_subparsers(title="",
                                description="")
    cmd.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    cmd.set_defaults(func = gaze_what)

    subcmd_is = subcmd.add_parser('is',
                                      parents = [parent_parser])
    subcmd_is.set_defaults(_egg = True)


    return cmd
