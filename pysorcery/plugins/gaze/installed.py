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
# Function gaze_installed
#
# view all installed packages and corresponding version numbers or check
# to see whether a particular package is installed and if it is
# installed display its version number
#
# shows all spells currently held
# (which means they are not to be updated)
#
# shows all spells currently exiled
# (which means they are not to be cast in any way)
#
# Input:  args
#         args.spell       - Spell to print compile log.
#                            Minimum 1
#         args.spellstatus - 
#         args.quiet       - decrease verbosity
# Output:
# Return: None
#
# Status: Works on Source Mage
#
#-------------------------------------------------------------------------------
def gaze_installed(args):
    logger.debug('Begin Function')

    if args.spell:
        for i in args.spell:
            spell = libspell.Spell(i)
            spell.print_version()

    else:
        spells = libspell.SpellList()
        if args.spellstatus:
            spell_list = spells.list_installed(args.spellstatus)
        else:
            spell_list = spells.list_installed()

        spells.print_list(spell_list)
        
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
    cmd = subparsers.add_parser('installed',
                                parents = [parent_parser],
                                help = 'View all installed packages and corresponding version numbers (Not Working)'
    )
    cmd.add_argument('spell',
                     nargs = '*',
                     help = 'Check to see whether a particular package is installed and if it is installed display its version number'
    )
    cmd.set_defaults(func = gaze_installed,
                     spellstatus=None
    )

    return cmd
