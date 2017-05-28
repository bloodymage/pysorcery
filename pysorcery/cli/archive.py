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
# real_main
# main
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Real_Main
#
# 1. Creates the argument parser
# 2. Eshablishes configuration
# 3. Runs the function specified by the arguments
#
# Input:  args
# 
# Return: None 
#
#-----------------------------------------------------------------------
def real_main(args):    
    logger.debug('Entered Function')

    epilog_text = """
See man pyarchive() for more information.\n
\n
Report bugs to ...
"""

    # Parse Command Line Arguments
    parser = argparse.ArgParser(
        description = 'Universal archive extractor. creator, etc...',
        epilog = epilog_text
    )

    parser.add_version_option()
    parent_parser = parser.add_logging_option()

    # Create subcommands
    subparsers = parser.create_subparsers()

    # Get list of subcommands
    subcommands = util.get_cmd_types('archive')

    # Create the subcommand arguments
    for i in subcommands:
        subcommand = util.get_module_func('archive',i,'parser')
        subcommand(subparsers, parent_parser)

    #
    args = parser.parse_args()

    # Set configuration
    config_ = config.main_configure(args)

    # Print status if debugging
    logger.debug('Configuration set')
    logger.debug2('Configuration Settings: ' + str(config_))
    logger.debug3('Arguments: ' + str(args))

    # 'application' code
    try:
        args.func(args)
    except:
        parser.print_help()
        logger.error('No command was given')

    #logging.verifydebuglevels()
    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Main
#
# The First function, initalizes everything else.
#
# Inputs come from command line argument
#
# This is ugly code
#
#
#
#
# Note: Any cli switches will override the settings in the config files
#
#-----------------------------------------------------------------------
def main(args=None):
    """Run the main command-line interface for pyarchive. Includes 
    top-level exception handlers that print friendly error messages.
    """
    logger.debug('Begin Application')

    try:         
        real_main(args)
    except:
        logger.critical('You Fucked Up')

    logger.debug('End Application')
    return

#-----------------------------------------------------------------------
#
#
#
#-----------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(main())
