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
#  Cast
#
#    is part of the sorcery package management suite. It is a command-line
#    tool for automatically retrieving, unpacking, compiling, installing,
#    and tracking software installations.
#
#    In order to find a package (known as a 'spell') to cast, refer to
#    gaze (1) and scribe.
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import sys
import os
import copy

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import argparse
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery import __version__, DEBUG
from pysorcery.lib import util
from pysorcery.lib import config
from pysorcery.lib.util import text

# Conditional Libraries


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
# Allow color text on console
colortext = text.ConsoleText()

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------
            
#-------------------------------------------------------------------------------
#
# Functions
#
# cast
# real_main
# main
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function cast
#
# ... Description ...
#
# Input:  args
#    args.spell - list of packages to instalr
#    args.queue -
#    
#    args....
#
# Output: 
# Return: None
#
#-------------------------------------------------------------------------------
def cast(args):
    logger.debug("Begin Function")

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = lib.Package(i)
        spell.install()
        #try:
        #    description = spell.get_description()
        #except:
        #    description = 'Fall back description, something went wrong'

        logger.debug3('Spell: ' + str(spell))
            
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

    
    logger.debug("End Function")
    return


#-------------------------------------------------------------------------------
#
# Function Real_Main
#
# ... Description ...
#
# Input:  args
# Output: 
# Return: None
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug("Entered Function")

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description='Process parameters')

    #
    packages = parser.add_argument_group('Package List')
    packages.add_argument('--queue',
                        action='store_true',
                        help='Cast all spells listed in the install-queue')

    packages.add_argument("spell",
                        nargs='*',
                        help='Spells to cast, separated by spaces')

    # Configure Options
    config_opts = parser.add_argument_group('Compile Options')
    config_opts.add_argument('--cflags',
                             nargs='+',
                             help='Custom CFLAGS')
    config_opts.add_argument('--cxxflags',
                             nargs='+',
                             help='Custom CXXFLAGS')
    config_opts.add_argument('--cppflags',
                             nargs='+',
                             help='Custom CPPFLAGS')
    config_opts.add_argument('--ldflags',
                             nargs='+',
                        help='Custom LDFLAGS')
    config_opts.add_argument('--no-opts',
                             action='store_true',
                             help='Turn off setting optimization flags, except for those found in --cflags, --cxxflags, --cppflags and --ldflags.')

    parser.add_argument('-d',
                        '--download',
                        action='store_true',
                        help='Force download of sources (overwrite existing files).')
    parser.add_argument('-s',
                        '--summon',
                        action='store_true',
                        help='Download all given spells before compiling')
    parser.add_argument('--deps',
                        action='store_true',
                        help='Configure spells and determine dependencies, only cast dependencies, not spells themselves')
    parser.add_argument('-c',
                        '--compile',
                        action='store_true',
                        help="Recompile the spells (don't install from cache).")
    parser.add_argument('-r',
                        '--reconfigure',
                        action='store_true',
                        help='Reconfigure spell options')
    parser.add_argument('-g',
                        '--grimoire',
                        nargs='+',
                        help='Use only the specified grimoires for this cast.  NOTE: If there are any cross-grimoire dependencies on unspecified grimoires they will not work. The target spell will not be found. To avoid this, specify all relevant grimoires to the -g parameter in the order you wish them to be searched.')
    parser.add_argument('-R',
                        '--recast-down',
                        action='store_true',
                        help='Recursively recast depended-upon spells, even if they are already installed. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.')
    parser.add_argument('-B',
                        '--recast-up',
                        action='store_true',
                        help='Recursively recast dependent spells. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.')
    parser.add_argument('-O',
                        '--recast-optional',
                        nargs='?',
                        choices=['always','ask-yes','ask-no','ignore'],
                        help='If a spell being built has spells which could optionally depend on it, but those dependencies are disabled, ask to recast the dependee. Optional parameter can be one of: "always", "ask-yes", "ask-no", or "ignore"; it defaults to what is set via the sorcery menu. Implies -c.')
    parser.add_argument('-Z',
                        '--lazy-updates',
                        nargs='?',
                        choices=['always','ask-yes','ask-no','ignore'],
                        help='Perform updates on installed spells that need updates. Optional parameter same as above.')
    parser.add_argument('-b',
                        '--force-base-dep',
                        action='store_true',
                        help='Force all spells to depend on basesystem')
    parser.add_argument('--from',
                        nargs=1,
                        help='Specify an alternate directory for $SOURCE_CACHE')
    parser.add_argument('-V',
                        '--voyeur',
                        nargs='?',
                        choices=['yes','no'],
                        help='Override "Voyeur" setting')


    #
    log_opts = parser.add_argument_group('Logging Options')
    log_opts.add_argument("-q", "--quiet",
                          action="count",
                          default=0,
                          help="Decrease output verbosity")
    if enable_debugging_mode:
        log_opts.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="Increase output verbosity")
        log_opts.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR","CRITICAL"],
                              help="Set minimum logging level")
        log_opts.add_argument("--debug",
                              action="store_true",
                              help="Maximize logging information")
    
    #
    parser.add_argument("--version",
                        action="version",
                        help="Print version information and exit",
                        version="%(prog)s " + __version__)

    args = parser.parse_args()

    # Ensure we have root access
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
        # real_main(args)
        
        try:         
            real_main(args)
        except:
            logger.critical("You Fucked Up")

        logger.debug("End Application")
        return 0

if __name__ == '__main__':
    main()

