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
# File: pysorcery/plugins/archive/create.py
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
# plugin: create
#
#   This plugin adds archive/compressed file creation and the
#   applicable command line arguments.
#
#-----------------------------------------------------------------------
"""
This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
archive files of multiple formats.  To test the capabilities of the
underlying code, this application was developed.

This plugin adds archive/compressed file creation and the applicable 
command line arguments.
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
# archive_create
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function archive_create
#
# Create archive file.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.files - List of files to extract
#         args.output_dir - Directory to create archive of
#                           If this is a single file, compress the file
# Return: None
#
#-----------------------------------------------------------------------
def archive_create(args):
    logger.debug('Begin Function')

    cfile = lib.File(args.archive)
    if cfile.mimetype in mimetypes.ArchiveMimetypes:
        cfile.create(os.getcwd(), args.filename)
    else:
        cfile.compress(args.filename)

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function parser
#
# Creates the parser subcommand and
#
# Input:  *args - tuple of all parent parsers
# Return: cmd
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):
    subparsers = args[0]
    parent_parsers = list(args[1:])

    cmd = subparsers.add_parser('create',
                                parents = parent_parsers,
                                help = 'Create files')
    cmd.add_argument('archive',
                     help = 'Archive file to create')
    cmd.add_argument('filename',
                     help = 'Files / Directories to add to the archive')
    cmd.set_defaults(func = archive_create)

    return cmd
