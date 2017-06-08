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
# File: pysorcery/plugins/archive/extract.py
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
# Plugin: Extract
#
#   This is a bonus application for pysorcery.  PySorcery for multiple
#   reasons to internally extract, create, list the contents, etc.
#   archive files of multiple formats.  To test the capabilities of the
#   underlying code, this application was developed.
#
# Plugin: extract
#
#   This plugin provides the extraction interface...
#
#-----------------------------------------------------------------------
"""
This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
archive files of multiple formats.  To test the capabilities of the
underlying code, this application was developed.

Plugin: Extract

This plugin provides the extraction interface...
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
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function archive_extract
#
# Extract files listed.
#
# Inputs
# ------
#    @param: args
#            args.quiet - Decrease Output Verbosity
#            args.files - List of files to extract
#            args.recursive - Extract all files in all subfolders
#            args.depth (Add me) - if recursive, limit to depth #
#            args.output_dir - Directory to extract to
#
# Returns
# -------
#    None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def archive_extract(args):
    logger.debug('Begin Function')

    for i in args.files:
        # Check for recursive extraction
        if args.recursive:
            # If True, extract all compressed files within a directory and
            # its sub directories
            #
            # Fix me! Add max depth option
            for root, dirs, files in os.walk(i):
                for sfile in files:
                    cfile = lib.File(sfile)
                    logger.debug3(cfile.mimetype)
                    if cfile.mimetype in mimetypes.ArchiveMimetypes:
                        cfile.extract(args.output_dir)
                    else:
                        cfile.decompress(args.output_dir)

        # Always extract what is explicitly listed
        #logger.info('Archive file: ' + i)
        cfile = lib.File(i)
        if cfile.mimetype in mimetypes.ArchiveMimetypes:
            cfile.extract(args.output_dir)
        else:
            cfile.decompress(args.output_dir)

    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function parser
#
# Create subcommand parsing options
#
# Inputs
#    @param: *args    - tuple of all subparsers and parent parsers
#                       args[0]: the subparser
#                       args[1:] the parent parsers
#    @param: **kwargs - Not used Future?
#
# Returns
# -------
#    cmd   - the subcommand parsing options
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):

    subparsers = args[0]
    parent_parsers = list(args[1:])

    cmd = subparsers.add_parser('extract',
                                parents = parent_parsers,
                                help = 'Extract files'
    )
    cmd.add_argument('files',
                     nargs = '+',
                     help = 'File(s) to extract'
    )
    cmd.add_argument('-o',
                     '--output-dir',
                     metavar = 'DIRECTORY',
                     help = 'Output Directory'
    )
    cmd.add_argument('-r',
                     '--recursive',
                     action = 'store_true',
                     help = 'Recursive'
    )
    cmd.add_argument('-d',
                     '--depth',
                     action = 'store_true',
                     help = 'limit recursion to specified depth'
    )
    cmd.set_defaults(func=archive_extract)

    return cmd
