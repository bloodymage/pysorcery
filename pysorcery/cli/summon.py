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


# Application Libraries
# System Library Overrides
from pysorcery.lib import argparse
from pysorcery.lib import distro
from pysorcery.lib import logging

# Other Application Libraries
from pysorcery import __version__, enable_debugging_mode
from pysorcery.lib import libtext
from pysorcery.lib import libconfig
from pysorcery.lib import libspell
from pysorcery.lib import libgrimoire
from pysorcery.lib import libcodex
from pysorcery.lib import libdownload
# Other Optional Libraries

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
# Function Error
#
#
#
#-------------------------------------------------------------------------------
def error(args):
    logger.debug("Begin Function")

    logger.error('We Fucked Up')
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def download_uri(args):
    logger.debug("Begin Function")

    uri = libdownload.URI(args.spell[0])
    uri.download()
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def summon(args):
    logger.debug("Begin Function")

    for spell in args.spell:
        logger.info1(spell)
    
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

    # Common Help Descriptions:
    quiet_help = 'Decrease output'
    verbose_help = 'Increase output'
    loglevel_help = 'Specify output level'
    debug_help = 'Maximize output level'

    parser = argparse.ArgumentParser(description="Query / View Sorcery package management information")

    parser.add_argument('spell',
                        nargs='+',
                        help = 'Spell(s) to download')
    parser.add_argument('-q','--quiet',
                        action = 'count',
                        default = 0,
                        help = quiet_help)
    parser.add_argument('-s','--section',
                        action = 'store_true',
                        default = 0,
                        help = "Flag the 'spell' argument as a section")
    if enable_debugging_mode is True:
        parser.add_argument("-v", "--verbosity",
                            action = "count",
                            default = 0,
                            help = verbose_help)
        parser.add_argument("--loglevel",
                            choices=["debug","info","warning",
                                     "error","critical","DEBUG",
                                     "INFO","WARNING","ERROR",
                                     "CRITICAL"],
                            help = loglevel_help)
        parser.add_argument("-V", "--version",
                            action="version",
                            help="Print version information and exit",
                            version="%(prog)s " + __version__)
        parser.add_argument("--debug",
                            action = "store_true",
                            help = debug_help)
    
    args = parser.parse_args()

    uri_types = [ 'http://', 'ftp://', 'rsync://', 'git://' ]

    if (len(args.spell) == 1 and
        any ( x in args.spell[0] for x in uri_types )):
        func = download_uri
                        
    elif os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)

        
    elif os.geteuid() == 0:
        func = summon
        
    else:
        func = error

    config = libconfig.main_configure(args)

    logger.debug("Configuration set")
    logger.debug2("Configuration Settings: " + str(config))
    logger.debug3("Arguments: " + str(args))

    # "application" code
    func(args)

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
