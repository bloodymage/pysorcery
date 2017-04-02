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
#    Dionysius is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Dionysius.  If not, see <http://www.gnu.org/licenses/>.
#
#
# Sorcery
#
# is part of the sorcery source-based package management suite. It is a
# general purpose command-line tool for displaying package logs, version 
# information, checking for installed packages, checksums, message digests,
# maintainer information, package URL information, removing obsolete packages,
# displaying new packages, untracked files, sections, searching for files that
# are installed, finding when spells were created and packages in the
# software catalogue. It can even take and retrieve snap shots of currently
# installed packages for easy duplication.
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
# System Library Overrides
from pysorcery.lib import argparse
from pysorcery.lib import logging

# Other Application Libraries
from pysorcery import __version__, enable_debugging_mode
from pysorcery.lib import libtext
from pysorcery.lib import libconfig
from pysorcery.lib import libsystem
from pysorcery.lib import libspell
from pysorcery.lib import libgrimoire
from pysorcery.lib import libcodex

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
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_update(args):
    logger.debug("Begin Function")

    codex = libcodex.Codex()
    codex.update
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_system_update(args):
    logger.debug("Begin Function")

    print("Fix Me")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_upgrade
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_upgrade(args):
    logger.debug("Begin Function")

    print("Fix Me")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_queue
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_queue_security(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_queue_newer(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_rebuild(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_hold(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_unhold(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_exile(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_unexile(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_add_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_remove_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_default(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function sorcery_update
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def sorcery_main(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Real_Main
#
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug("Entered Function")

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description="Menu-driven software package management utility.")
    parser.register('action', 'parsers', argparse.AliasedSubParsersAction)
    parser.add_argument("--config",
                        nargs=1,
                        help="Use specified config file")
    parser.add_argument("--debug",
                        action="store_true",
                        help="Enable Debugging")
    parser.add_argument("--loglevel",
                        choices=["debug","info","warning","error","critical",
                                 "DEBUG","INFO","WARNING","ERROR","CRITICAL"],
                        help="Set minimum logging level")
    parser.add_argument("-v", "--verbosity",
                        action="count",
                        default=0,
                        help="increase output verbosity")
    # help is required to go before version
    parser.add_argument("-V", "--version",
                        action="version",
                        help="Print version information and exit",
                        version="%(prog)s " + __version__)
    parser.set_defaults(func=False)
    
    subparsers = parser.add_subparsers(title='commands',
                                       metavar='Commands',
                                       help='Sub commands')

    # create the parser for the "alien" command
    parser_update = subparsers.add_parser('update',
                                         help='Updates the sorcery scripts (Not Working)')
    parser_update.add_argument('--debug',
                              action='store_true',
                              help='Enable Debugging')
    parser_update.add_argument("--loglevel",
                              choices=["debug","info","warning","error","critical",
                                       "DEBUG","INFO","WARNING","ERROR","CRITICAL"],
                              help="Set minimum logging level")
    parser_update.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_update.set_defaults(func=sorcery_update)

    # create the parser for the "orphans" command
    parser_system_update = subparsers.add_parser('system-update',
                                           help='Perform a system update (updates sorcery, grimoire, and spells).  [ sorcery update, scribe update, sorcery queue, cast --queue ] (Not Working)')
    parser_system_update.add_argument('--debug',
                                action='store_true',
                                help='Enable Debugging')
    parser_system_update.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical", "DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_system_update.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_system_update.set_defaults(func=sorcery_system_update)

    # create the parser for the "activity" command
    parser_upgrade = subparsers.add_parser('upgrade',
                                            help='Update spells without first updating the grimoire.  [ sorcery queue, cast --queue ]  (Not Working)')
    parser_upgrade.add_argument('--debug',
                                 action='store_true',
                                 help='Display System Info')
    parser_upgrade.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical", "DEBUG",
                                          "INFO","WARNING","ERROR","CRITICAL"],
                                 help="Set minimum logging level")
    parser_upgrade.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_upgrade.set_defaults(func=sorcery_upgrade)


    # create the parser for the "install-queue" command
    parser_queue = subparsers.add_parser('queue',
                                                 help='Compare installed grimoire to installed spells, generate queue of spells needing to be updated. (Not Working)')
    parser_queue.add_argument('--debug',
                                      action='store_true',
                                      help='Enable debugging information')
    parser_queue.add_argument("--loglevel",
                                      choices=["debug","info","warning",
                                               "error","critical","DEBUG",
                                               "INFO","WARNING","ERROR",
                                               "CRITICAL"],
                                      help="Set minimum logging level")
    parser_queue.add_argument("-v", "--verbosity",
                                      action="count",
                                      default=0,
                                      help="Increase output verbosity")
    parser_queue.set_defaults(func=sorcery_queue)

    # create the parser for the "show-held" command
    parser_queue_security = subparsers.add_parser('queue-security',
                                             help='Queue spells that had updates due to security fixes. (Not Working)')
    parser_queue_security.add_argument('--debug',
                                  action='store_true',
                                  help='Enable debugging information')
    parser_queue_security.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_queue_security.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_queue_security.set_defaults(func=sorcery_queue_security)

    # create the parser for the "remove-queue" command
    parser_queue_newer = subparsers.add_parser('queue-newer',
                                                help='Queue spells with newer versions only (i.e. no downgrades). (Not Working)')
    parser_queue_newer.add_argument('--debug',
                                     action='store_true',
                                     help='Enable debugging information')
    parser_queue_newer.add_argument("--loglevel",
                                     choices=["debug","info","warning",
                                              "error","critical","DEBUG",
                                              "INFO","WARNING","ERROR",
                                              "CRITICAL"],
                                     help="Set minimum logging level")
    parser_queue_newer.add_argument("-v", "--verbosity",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_queue_newer.set_defaults(func=sorcery_queue_newer)


    # create the parser for the "what" command
    parser_rebuild = subparsers.add_parser('rebuild',
                                               help='Automatically rebuilds all installed software packages. This option is non-interactive except for a bunch of config and depends questions the first time you run it. (Not Working)')
    parser_rebuild.add_argument('--reconfigure',
                                    action='store_true',
                                    help='Make cast reask all the questions unconditionally.')
    parser_rebuild.add_argument('--debug',
                                    action='store_true',
                                    help='Enable debugging information')
    parser_rebuild.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_rebuild.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_rebuild.set_defaults(func=sorcery_rebuild)

    # create the parser for the "what" command
    parser_rebuild_reconfigure = subparsers.add_parser('rebuild-reconfigure',
                                            help='Automatically rebuilds all installed software packages. Unlike -r, this option makes cast reask all the questions unconditionally. (Not Working)')
    parser_rebuild_reconfigure.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_rebuild_reconfigure.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_rebuild_reconfigure.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_rebuild_reconfigure.set_defaults(func=sorcery_rebuild,reconfigure=True)
    
    # create the parser for the "what" command
    parser_hold = subparsers.add_parser('hold',
                                        help="sets <spell|s> to held. This means that they stay installed, but that cast will refuse to cast them. This will prevent them from being updated or changed at all. This might be helpful if you change kernel versions and the package won't build right on the new system, but still install (wrong). (Not Working")
    parser_hold.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_hold.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_hold.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_hold.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_hold.set_defaults(func=sorcery_hold)

    # create the parser for the "what" command
    parser_unhold = subparsers.add_parser('unhold',
                                          help="unholds <spell|s>, changes their status from held back to installed. (Not Working)")
    parser_unhold.add_argument('spell',
                              nargs='+',
                              help='Display System Info')
    parser_unhold.add_argument('--debug',
                              action='store_true',
                              help='Enable debugging information')
    parser_unhold.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_unhold.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_unhold.set_defaults(func=sorcery_unhold)

    # create the parser for the "where" command
    parser_exile = subparsers.add_parser('exile',
                                         help="sets <spell|s> to exiled.  This means that they won't be installed in any way, sorcery just ignores them.")
    parser_exile.add_argument('spell',
                             nargs='+',
                             help='Spell(s) to display')
    parser_exile.add_argument('-p','-path', '--path',
                             action='store_true',
                             help='Display the full path to spell')
    parser_exile.add_argument('--debug',
                             action='store_true',
                             help='Enable Debugging')
    parser_exile.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_exile.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_exile.set_defaults(func=sorcery_exile)

    # create the parser for the "url" command
    parser_unexiled = subparsers.add_parser('unexiled',
                                       aliases=('website',),
                                       help='Removes exiled status from <spell|s>.  This means that they can be installed again. (Not Working)')
    parser_unexiled.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_unexiled.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_unexiled.add_argument("--loglevel",
                            choices=["debug","info","warning",
                                     "error","critical","DEBUG",
                                     "INFO","WARNING","ERROR",
                                     "CRITICAL"],
                            help="Set minimum logging level")
    parser_unexiled.add_argument("-v", "--verbosity",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_unexiled.set_defaults(func=sorcery_unexile)

    # create the parser for the "sources" command
    parser_add_queue = subparsers.add_parser('add-queue',
                                           help='Add spell(s) to install queue (Not Working)')
    parser_add_queue.add_argument('spell',
                                nargs='+',
                                help='Display System Info')
    parser_add_queue.add_argument('--debug',
                                action='store_true',
                                help='Enable debugging information')
    parser_add_queue.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_add_queue.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_add_queue.set_defaults(func=sorcery_add_queue)

    # create the parser for the "sources" command
    parser_remove_queue = subparsers.add_parser('remove-queue',
                                           help='Remove spell(s) from install queue (Not Working)')
    parser_remove_queue.add_argument('spell',
                                nargs='+',
                                help='Display System Info')
    parser_remove_queue.add_argument('--debug',
                                action='store_true',
                                help='Enable debugging information')
    parser_remove_queue.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_remove_queue.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_remove_queue.set_defaults(func=sorcery_remove_queue)

    # create the parser for the "source_urls" command
    parser_default = subparsers.add_parser('default',
                                              help='This is a sorcery feature to pre-answer some depends questions. They will still be asked, but they will default to what you set this to. (Not Working)')
    parser_default.add_argument('spell',
                                   nargs='+',
                                   help='Spell')
    parser_default.add_argument('--debug',
                                   action='store_true',
                                   help='Enable debugging information')
    parser_default.add_argument("--loglevel",
                                   choices=["debug","info","warning",
                                            "error","critical","DEBUG",
                                            "INFO","WARNING","ERROR",
                                            "CRITICAL"],
                                   help="Set minimum logging level")
    parser_default.add_argument("-v", "--verbosity",
                                   action="count",
                                   default=0,
                                   help="increase output verbosity")
    parser_default.set_defaults(func=sorcery_default)

    # Store all the arguments in a variable
    args = parser.parse_args()

    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)

    # Parse the config files
    config = libconfig.main_configure(args)

    logger.debug2("Configuration set")
    logger.debug3("Configuration Settings: " + str(config))
    logger.debug4("Arguments: " + str(args))

    # "application" code
    # Run the specified subcommand as per args
    if args.func:
        args.func(args)
    else:
        sorcery_main(args)

    print(distro_id)
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
# Input:  args
# Output:
# Return: None
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
        return

if __name__ == '__main__':
    main()
