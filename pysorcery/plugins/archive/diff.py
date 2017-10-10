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
# This file is part of Sorcery.
#
# File: pysorcery/plugins/archive/diff.py
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
#
# pyArchive: Diff
#
#   This plugin provides the ability to compare archive and compressed
#   files.
#
#-----------------------------------------------------------------------
"""
pyArchive: Diff

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
from pysorcery.lib.files import archive

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
# Function archive_diff
#
# Find and display all differences between two archive filesxs
#
# Inputs
# ------
#    @param: args
#            args.quiet - Decrease Output Verbosity
#            args.archive1 - First archive to compare
#            args.archive2 - Second archive to compare
#            args.size - Compare content file sizes as well (conflicts with content)
#            args.content - Compare File Contents (conflicts with size)
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
def archive_diff(args):
    logger.debug('Begin Function')

    """Show differences between two archives."""
    try:
        archives = lib.Files(filelist=args.archive)
        result = archives.diff(verbosity=args.verbosity,
                               interactive=args.interactive)
    except Exception as msg:
        logger.error("error showing differences between %s and %s: %s" % (args.archive[0], args.archive[1], msg))

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
#    @param: **kwargs - Not used Future?
#
# Returns
# -------
#    @return: cmd - the subcommand parsing options
#
# Raises
# ------
#    @raises: ...
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
    cmd.add_argument('archive',
                     nargs=2,
                     help = 'Archives to compare')
    group.add_argument('-s',
                     '--size',
                     action='store_true',
                     help='Compare file names and sizes')
    group.add_argument('-c',
                     '--contents',
                     action='store_true',
                     help='Compare file contents')
    cmd.add_argument('-n',
                     '--non-interactive',
                     dest = 'interactive',
                     default = False,
                     action = 'store_false',
                     help="Don't query for user input (ie. passwords or when overwriting duplicate files); use with care since overwriting files or ignoring passwords could be unintended"
    )
    cmd.set_defaults(func = archive_diff)

    return cmd
