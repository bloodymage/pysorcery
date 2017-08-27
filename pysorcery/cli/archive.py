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
# Additional code from 'patool'
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# This file is part of Sorcery.
#
# File: pysorcery/cli/archive.py
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
pyArchive

This is a bonus application for pysorcery.  PySorcery for multiple
reasons needs to internally extract, create, list the contents, etc.
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
from pysorcery.lib.files import archive

# Conditional Libraries
try:
    # to all bash completion, doesn't seem to work
    import argcomplete 
    BASHCOMPLETE = True
except ImportError as msg:
    BASHCOMPLETE = False

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
# Function Real_Main
#
# 1. Creates the argument parser
# 2. Eshablishes configuration
# 3. Runs the function specified by the arguments
#
# Inputs
# ------
#    @param: args
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
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
    subparsers = parser.create_subparsers()

    # Get list of subcommands
    subcommands = util.get_cmd_types('archive')

    # Create the subcommand arguments
    for i in subcommands:
        subcommand = util.get_module_func(scmd='archive',
                                          program=i,
                                          cmd='parser')
        subcommand(subparsers, parent_parser)

    # This doesn't work...
    if BASHCOMPLETE is True:
        argcomplete.autocomplete(parser)
    #
    args = parser.parse_args()

    # Set configuration
    config_ = config.main_configure(args)

    # Print status if debugging
    logger.debug('Configuration set')
    logger.debug2('Configuration Settings: ' + str(config_))
    logger.debug3('Arguments: ' + str(args))

    # 'application' code
    if DEBUG is False:
        try:
            args.func(args)
        except:
            parser.print_help()
            logger.error('No command was given')
    else:
        args.func(args)    

    #logging.verifydebuglevels()
    logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Main
#
# The First function, initalizes everything else.  Attempts to execute
# everything through exception handlers with easy to read messages.
#
# Inputs
# ------
#    @param: args
#
# Returns
# -------
#    @param: None (Change this for error exits)
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def main(args=None):
    """Run the main command-line interface for pyarchive. Includes 
    top-level exception handlers that print friendly error messages.


    Inputs
    ------
         @param: args

    Returns
    -------
         @return: None

    Raises
    ------
         ...

    """
    
    if DEBUG is False:
        try:         
            real_main(args)
        except KeyboardInterrupt:
            log_error("aborted")
        except Exception as msg:
            logger.critical('You Fucked Up')
            logger.critical(msg)
    else:
        real_main(args)

    logger.debug('End Application')
    return

#-----------------------------------------------------------------------
#
#
#
#-----------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(main())
