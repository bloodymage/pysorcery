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
# File: pysorcery/plugins/archive/test.py
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
# Plugin: Test
#
#    This plugin checks to ensure an archive file is valid.
#
#-----------------------------------------------------------------------
"""
pyArchive: Test

This plugin checks to ensure an archive file is valid.
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
# archive_test
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function archive_test
#
# Verify the archive file is valid and can be opened
#
# Inputs
# ------
#    @param: args
#            args.quiet - Decrease Output Verbosity
#            args.files - List of files to extract
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
def archive_test(args):
    """Test files in archive(s)."""
    logger.debug('Begin Function')
    for i in args.archive:
        try:
            cfile = lib.File(i)
            cfile.test_archive(verbosity=args.verbosity,
                               interactive=args.interactive)
        except Exception as msg:
            logging.error("error testing %s: %s" % (archive, msg))

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
    cmd = subparsers.add_parser('test',
                                aliases = ['verify'],
                                parents = parent_parsers,
                                help = 'Test files')
    cmd.add_argument('archive',
                     nargs = '+',
                     help = 'Archive Files to test')
    cmd.add_argument('-n',
                     '--non-interactive',
                     dest = 'interactive',
                     default = False,
                     action = 'store_false',
                     help="Don't query for user input (ie. passwords or when overwriting duplicate files); use with care since overwriting files or ignoring passwords could be unintended"
    )
    cmd.set_defaults(func = archive_test)
    return cmd
