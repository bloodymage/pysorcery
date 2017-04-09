#! /usr/bin/env python3
#-------------------------------------------------------------------------------
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
#    Sorcery is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
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
#
#
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import copy
import subprocess

# Other Libraries
import distro

# Application Libraries
# Application Overrides
from pysorcery.lib import argparse
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery import __version__
from pysorcery.lib import libtext
from pysorcery.lib import libconfig
from pysorcery.lib import libspell
from pysorcery.lib import libgrimoire
from pysorcery.lib import libcodex

# Other Optional Libraries
if pysorcery.distro_id in pysorcery.distro_dict['deb']:
    import apt


#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)


#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

            
#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_depends(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def gaze_dependencies(args):
    logger.debug("Begin Function")

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def gaze_time(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Real_Main
#
# 
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug("Entered Function")

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description="Query / View Sorcery package management information")
    parser.add_argument("--config",
                        nargs=1,
                    help="Use specified config file")
    parser.add_argument("-v", "--verbosity",
                        action="count",
                        default=0,
                    help="increase output verbosity")
    parser.add_argument("--loglevel",
                        help="Set minimum logging level",
                        choices=["debug","info","warning","error","critical","DEBUG","INFO","WARNING","ERROR","CRITICAL"])
    parser.add_argument("-V", "--version",
                        help="Print version information and exit",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("--debug",
                        help="Enable Debugging",
                        action="store_true")
    
    subparsers = parser.add_subparsers(help='Sub commands')

    # create the parser for the "alien" command
    parser_what = subparsers.add_parser('alien', help='Find and Display all files not tracked by the Sorcery Package Management System (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_what.set_defaults(func=gaze_alien)


    args = parser.parse_args()

    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)

    config = libconfig.main_configure(args)

    logger.debug("Configuration set")
    logger.debug2("Configuration Settings: " + str(config))
    logger.debug3("Arguments: " + str(args))

    # "application" code
    args.func(args)
    
#    logging.verifydebuglevels()
    logger.debug("End Function")
    return 0


#-------------------------------------------------------------------------------
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
# Reads configuration files in the following order:
# 1. ~/.config/dionysius/dionysis.conf
# 2. /etc/dionysius/dionysius.conf
# 3. {python-dir}/dist-___/pydionysius/dionysius.conf
#
# Conf files are in yaml format
#
# Note: Any cli switches will override the settings in the config files
#
#-------------------------------------------------------------------------------
def main(args=None):
        """Run the main command-line interface for dionysius. Includes top-level
    exception handlers that print friendly error messages.
        """

        logger.debug("Begin Application")
#        try:         
#            real_main(args)
        real_main(args)        
#        except:
#            logger.critical("You Fucked Up")

        logger.debug("End Application")
        return 0

if __name__ == '__main__':
    main()
