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
# File: pysorcery/plugins/archive/search.py
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
# Plugin: Search
#
#  This plugin gives the user the ability to search archives files for
#  files with the searched naame or string.
#
#-----------------------------------------------------------------------
"""
This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
archive files of multiple formats.  To test the capabilities of the
underlying code, this application was developed.

Plugin: Search

This plugin gives the user the ability to search archives files for
files with the searched naame or string.
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
# archive_search
# parser
#
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#
# Function archive_search
#
# Search archive for search term.
#
# Inputs
# ------
#    @param: args
#            args.quiet  - Decrease Output Verbosity
#            args.archive - Archive to search
#            args.search - What we are searching for
#
# Returns
# -------
#    None
#
# Raises
# ------
#    Error:
#
#-----------------------------------------------------------------------
def archive_search(args):
    logger.debug('Begin Function')

    archive = lib.File(args.archive)
    results = archive.search(args.searchterm)

    print(results)
    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function parser
#
# Create search parser options
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
#    cmd - the subcommand parsing options
#
# Raises
# ------
#    Error:
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):
    subparsers = args[0]
    parent_parsers = list(args[1:])

    cmd = subparsers.add_parser('search',
                                parents = parent_parsers,
                                help = 'Search archive')
    cmd.add_argument('archive',
                     help = 'Archive to search')
    cmd.add_argument('searchterm',
                     nargs = '+',
                     help = 'Term to search for')
    cmd.set_defaults(func = archive_search)

    return cmd
