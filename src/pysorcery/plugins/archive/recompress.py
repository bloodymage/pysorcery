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
# File: pysorcery/plugins/archive/recompress.py
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
# Plugin: Recompress
#
#   Recompresses an archive file
#
#-----------------------------------------------------------------------
"""
Plugin: Recompress

Recompress an archive file
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
# archive_recompress
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function archive_recompress
#
# Recompresses a file.
#
# Inputs
# ------
#    @param: args
#            args.quiet   - Decrease Output Verbosity
#            args.archive - Original File
#            args.compression_level - Compression level to recompress to.
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
def archive_recompress(args):
    logger.debug('Begin Function')

    """Recompress an archive to smaller size."""
    res = 0
    try:
        archive = lib.File(args.archive)
        archive.recompress_archive(verbosity=args.verbosity,
                                   interactive=args.interactive)
    except Exception as msg:
        logger.error("error recompressing %s: %s" % (args.archive, msg))
        res = 1
    return res

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

    cmd = subparsers.add_parser('recompress',
                                parents = parent_parsers,
                                help = 'Recompress files'
    )
    cmd.add_argument('archive',
                     help = 'Source file')
    cmd.add_argument('compression_level',
                     type = int,
                     choices = range(0, 9),
                     default = 9,
                     help = 'Set new compression level')
    cmd.add_argument('-n',
                     '--non-interactive',
                     dest = 'interactive',
                     default = False,
                     action = 'store_false',
                     help="Don't query for user input (ie. passwords or when overwriting duplicate files); use with care since overwriting files or ignoring passwords could be unintended"
    )
    cmd.set_defaults(func = archive_recompress)

    return cmd
