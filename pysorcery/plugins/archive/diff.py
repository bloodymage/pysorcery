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
# Archive Diff
#
# This plugin provides the ability to compare archive and compressed
# files.
#
#-----------------------------------------------------------------------
"""
This plugin provides the ability to compare archive and compressed files.
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
# archive_diff
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions archive_diff
#
# Find and display all differences between two archive filesxs
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.archive1 - First archive to compare
#         args.archive2 - Second archive to compare
#         args.size - Compare content file sizes as well (conflicts with content)
#         args.content - Compare File Contents (conflicts with size)
# Return: None
#
#-----------------------------------------------------------------------
def archive_diff(args):
    logger.debug('Begin Function')

    lib.filediff(args.archive1, args.archive2, args.size, args.content)
    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function parser
#
# Create subcommand parsing options
#
# Input:  subparsers    - 
#         parent_parser - 
# Return: None
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):

    subparsers = args[0]

    parent_parsers = list(args[1:])
        
    cmd = subparsers.add_parser('diff',
                                parents = parent_parsers,
                                help = 'Compare Archive Files')
    cmpgroup = cmd.add_argument_group('Comparison Options')
    group = cmpgroup.add_mutually_exclusive_group()
    cmd.add_argument('archive1',
                     help = 'Archives to compare')
    cmd.add_argument('archive2',
                     help = 'Archives to compare')
    group.add_argument('-s',
                     '--size',
                     action='store_true',
                     help='Compare file names and sizes')
    group.add_argument('-c',
                     '--contents',
                     action='store_true',
                     help='Compare file contents')
    cmd.set_defaults(func = archive_diff)

    return cmd
