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
#    along with Dionysius.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file is a prototype.  There are several things I flat out do not
# know how to do.  This allows me to try out the parts I do know.
#
#-------------------------------------------------------------------------------

# added so distributors can consistently specify a private module location
#private_module_path = "/usr/share/weather-util"
#if private_module_path:
#    sys.path.insert(1, private_module_path)


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import argparse
import copy
import subprocess

# Other Libraries
import distro

# Application Libraries
from pysorcery import __version__
from pysorcery.lib import libtext
from pysorcery.lib import logging
from pysorcery.lib import libconfig
from pysorcery.lib import libspell
from pysorcery.lib import libgrimoire
from pysorcery.lib import libcodex

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
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
# Function cast
#
#
#
#-------------------------------------------------------------------------------
def cast(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)
        spell.install(args)
    
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

    parser = argparse.ArgumentParser(description='Process parameters')
    parser.add_argument('--cflags',
                        help='Custom CFLAGS',
                        nargs='*')
    parser.add_argument('--cxxflags',
                        help='Custom CXXFLAGS',
                        nargs='*')
    parser.add_argument('--cppflags',
                        help='Custom CPPFLAGS',
                        nargs='*')
    parser.add_argument('--ldflags',
                        help='Custom LDFLAGS',
                        nargs='*')
    parser.add_argument('--no-opts',
                        help='Turn off setting optimization flags, except for those found in --cflags, --cxxflags, --cppflags and --ldflags.',
                        action='store_true')
    parser.add_argument('-V',
                        help='Override \$VOYEUR setting',
                        nargs='?',
                        choices=['yes','no'])
    parser.add_argument('-d',
                        '--download',
                        help='Force download of sources (overwrite existing files).',
                        action='store_true')
    parser.add_argument('-s',
                        help='Download all given spells before compiling',
                        action='store_true')
    parser.add_argument('--deps',
                        help='Configure spells and determine dependencies, only cast dependencies, not spells themselves',
                        action='store_true')
    parser.add_argument('-c',
                        '--compile',
                        help="Recompile the spells (don't install from cache).",
                        action='store_true')
    parser.add_argument('-r',
                        '--reconfigure',
                        action='store_true',
                        help='Select new dependencies for spells (implies -c)')
    parser.add_argument('-g',
                        '--grimoire',
                        nargs='*',
                        help='Use only the specified grimoires for this cast.  NOTE: If there are any cross-grimoire dependencies on unspecified grimoires they will not work. The target spell will not be found. To avoid this, specify all relevant grimoires to the -g parameter in the order you wish them to be searched.')
    parser.add_argument('-R',
                        '--recast-down',
                        help='Recursively recast depended-upon spells, even if they are already installed. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.',
                        action='store_true')
    parser.add_argument('-B',
                        '--recast-up',
                        help='Recursively recast dependent spells. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.',
                        action='store_true')
    parser.add_argument('-O',
                        '--recast-optional',
                        help='If a spell being built has spells which could optionally depend on it, but those dependencies are disabled, ask to recast the dependee. Optional parameter can be one of: "always", "ask-yes", "ask-no", or "ignore"; it defaults to what is set via the sorcery menu. Implies -c.',
                        nargs='?',
                        choices=['always','ask-yes','ask-no','ignore'])
    parser.add_argument('-Z',
                        '--lazy-updates',
                        help='Perform updates on installed spells that need updates. Optional parameter same as above.',
                        nargs='?',
                        choices=['always','ask-yes','ask-no','ignore'])
    parser.add_argument('-b',
                        '--force-base-dep',
                        help='Force all spells to depend on basesystem',
                        action='store_true')
    parser.add_argument('--from',
                        help='Specify an alternate directory for $SOURCE_CACHE')
    parser.add_argument('--queue',
                        help='Cast all spells listed in $INSTALL_QUEUE',
                        action='store_true')
    parser.add_argument("spell",
                        nargs='+',
                        help='Spells to cast, separated by spaces')
    parser.add_argument("-q", "--quiet",
                        action="count",
                        default=0,
                    help="increase output verbosity")
    parser.add_argument("-v", "--verbosity",
                        action="count",
                        default=0,
                    help="increase output verbosity")
    parser.add_argument("--loglevel",
                        help="Set minimum logging level",
                        choices=["debug","info","warning",
                                 "error","critical","DEBUG",
                                 "INFO","WARNING","ERROR","CRITICAL"])
    parser.add_argument("--version",
                        help="Print version information and exit",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("--debug",
                        help="Enable Debugging",
                        action="store_true")

    args = parser.parse_args()

    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)

    # Get configuration settings
    config = libconfig.main_configure(args)

    logger.debug("Configuration set")
    logger.debug2("Configuration Settings: " + str(config))
    logger.debug3("Arguments: " + str(args))

    # "application" code
    cast(args)
    
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

