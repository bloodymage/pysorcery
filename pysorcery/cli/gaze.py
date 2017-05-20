#!/usr/bin/env python3
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
# Gaze
#
# is part of the Sorcery source-based package management suite. It is a
# general purpose command-line tool for displaying package logs, version 
# information, checking for installed packages, checksums, message
# digests, maintainer information, package URL information, removing
# obsolete packages, displaying new packages, untracked files, sections,
# searching for files that are installed, finding when spells were
# created and packages in the software catalogue. It can even take and
# retrieve snap shots of currently installed packages for easy
# duplication.
#
#
# Status:
#
#-----------------------------------------------------------------------
"""
Gaze is part of the Sorcery source-based package management suite. It 
is a general purpose command-line tool for displaying package logs, 
version information, checking for installed packages, checksums, message
digests, maintainer information, package URL information, removing
obsolete packages, displaying new packages, untracked files, sections,
searching for files that are installed, finding when spells were
created and packages in the software catalogue. It can even take and
retrieve snap shots of currently installed packages for easy
duplication.
"""

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
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging

# Other Application Libraries
#from pysorcery import *
#from pysorcery.lib.sorcery import repositories
#from pysorcery.lib.sorcery import packages
from pysorcery.lib import util
from pysorcery.lib.util import config
from pysorcery.lib.util import text


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

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Real_Main
#
# 
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug('Entered Function')

    subcommands = util.get_cmd_types('gaze')
    
    epilog_text = """
See man pygaze() for more information.\n
\n
Report bugs to ...
"""

    # Parse Command Line Arguments
    parser = argparse.CommonParser(
        description = 'Universal archive extractor. creator, etc...',
        epilog = epilog_text
    )

    parser.add_version_option()
    parent_parser = parser.add_logging_option()
    repo_parent_parser = argparse.ArgumentParser(add_help=False)

    # Create subcommands
    subparsers = parser.add_subparsers(title = 'commands',
                                       metavar = 'Command',
                                       help = 'Description'
    )

    repo_parent_parser.add_argument('-g','--grimoire',
                                    nargs = '*',
                                    help = 'Specify which grimoire(s) to look in.')

    for i in subcommands:
        subcommand = util.get_module_func('gaze',i,'parser')
        subcommand(subparsers, parent_parser, repo_parent_parser)
                                      
    
    # Parser Arguments
    #parser.add_argument('filename',
    #                    choices = [ 'BUILD',
    #                                'CONFIGURE',
    #                                'CONFLICTS',
    #                                'DETAILS',
    #                                'DEPENDS',
    #                                'DOWNLOAD',
    #                                'FINAL',
    #                                'HISTORY',
    #                                'INSTALL',
    #                                'INSTALL_EXTRAS',
    #                                'PATCH',
    #                                'POST_BUILD',
    #                                'POST_INSTALL',
    #                                'POST_REMOVE',
    #                                'POST_RESURRECT',
    #                                'PRE_BUILD',
    #                                'PRE_INSTALL',
    #                                'PRE_REMOVE',
    #                                'PRE_RESURRECT',
    #                                'PRE_SUB_DEPENDS',
    #                                'PREPARE',
    #                                'PROVIDES',
    #                                'SECURITY',
    #                                'SUB_DEPENDS',
    #                                'TRANSFER',
    #                                'TRIGGER_CHECK',
    #                                'TRIGGERS',
    #                                'UP_TRIGGERS'
    #                    ],
    #                    help = 'Show SCRIPT_NAME of the spell, where SCRIPT_NAME is any of the above spell scripts.')
    parser.set_defaults(func = False,
                        debug = False,
                        verbosity = 0,
                        loglevel = 'INFO')
    
    # Store all the arguments in a variable
    args = parser.parse_args()
    
    # Ensure we have root access if needed
    if (args.sudo is True and
        os.geteuid() != 0):
        # os.execvp() replaces the running process, rather than launching a
        # child process, so there's no need to exit afterwards. The extra
        # 'sudo' in the second parameter is required because Python
        # doesn't automatically set $0 in the new process.
        os.execvp('sudo', ['sudo'] + sys.argv)

    # Now we are definitely running as root

    # Parse the config files
    config_ = config.main_configure(args)

    logger.debug2('Configuration set')
    logger.debug3('Configuration Settings: ' + str(config_))
    logger.debug4('Arguments: ' + str(args))

    # 'application' code
    # Run the specified subcommand as per args
    args.func(args)
    
    logger.debug('End Function')
    return


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
#
# Note: Any cli switches will override the settings in the config files
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def main(args = None):
    """Run the main command-line interface for dionysius. Includes top-level
    exception handlers that print friendly error messages.
    """

    logger.debug('Begin Application')

    real_main(args)
    
#    try:         
#        real_main(args)
#    except:
#        logger.critical('You Fucked Up')

    logger.debug('End Application')
    return

if __name__ == '__main__':
    main()
