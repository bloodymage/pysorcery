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
# File: pysorcery/plugins/archive/formats.py
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
# Plugin: formats
#
#    This plugin prints a list of all Sorcery supported archive and
#    compression options along with status on underlying system
#    support.
#
#-----------------------------------------------------------------------
"""
pyArchive

This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
archive files of multiple formats.  To test the capabilities of the
underlying code, this application was developed.

Plugin: formats

This plugin prints a list of all Sorcery supported archive and 
compression options along with status on underlying system support.
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
# archive_formats
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function archive_formats
#
# List all archive and compression formats supported.
#
# Inputs
# ------
#    @param: args
#
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
def archive_formats(args):
    logger.debug('Begin Function')

    format_groups = ['util_archive', 'util_compressed']

    cmd = 'archive_support'

    for group in format_groups:
        # Obtain list of all supported formats of type 'x'
        formats = util.get_cmd_types(group)

        # 
        for format_ in formats:
            logger.info(format_ + ' files:')

            # Identify function that displays formats support
            archive_func = util.get_module_func(group,
                                                format_,
                                                cmd)
            
            # Execute the identified function
            archive_func()

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
#    cmd - the subcommand parsing options
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):

    subparsers = args[0]
    parent_parsers = list(args[1:])

    cmd = subparsers.add_parser('formats',
                                parents = parent_parsers,
                                help = 'Formats files')
    cmd.set_defaults(func = archive_formats)

    return cmd
