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
# Gaze
#
# is part of the Sorcery source-based package management suite. It is a
# general purpose command-line tool for displaying package logs, version 
# information, checking for installed packages, checksums, message digests,
# maintainer information, package URL information, removing obsolete packages,
# displaying new packages, untracked files, sections, searching for files that
# are installed, finding when spells were created and packages in the
# software catalogue. It can even take and retrieve snap shots of currently
# installed packages for easy duplication.
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
import copy
import subprocess

# Other Libraries
import distro

# Application Libraries
# System Library Overrides
from pysorcery.lib import argparse
from pysorcery.lib import logging

# Other Application Libraries
import pysorcery
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
# Function gaze_alien
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_alien(args):
    logger.debug("Begin Function")

    # create 'alien' object
    alien = libsystem.Alien()

    alien.identify()
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_orphans
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_orphans(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_activity
#
# show the activity log.
# (note: this is actually a log of all that happened involving sorcery,
# such as casts, summons etc.)
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_activity(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_install_queue
#
# Shows the queue of spells waiting to be installed
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_install_queue(args):
    logger.debug("Begin Function")

    queue = libspell.SpellQueue()
    queue.inst_queue()

#    print("shit")

    queue.print_queue()

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_remove_queue
#
# Shows the queue of spells waiting to be removed
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_remove_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_show_held
#
# shows all spells currently held
# (which means they are not to be updated)
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_show_held(args):
    logger.debug("Begin Function")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_exiled
#
# shows all spells currently exiled
# (which means they are not to be cast in any way)
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_show_exiled(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_provides
#
# displays spells that provide the feature
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_provides(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
# view the long package description
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_what(args):
    logger.debug("Begin Function")

    for i in args.spell:
        logger.debug2("Loop iteration: " + i)
        
        spell = libspell.Spell(i)

        logger.debug3("Spell: " + str(spell))
        
        colortext = libtext.ConsoleText()
        message = colortext.colorize(spell.name, "bold","white","black")
        logger.info(message)

        message = colortext.colorize(spell.description, "none","white","black")
        logger.info1(message)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_short
#
# view the short package description
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_short(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function where
#
# display the section a spell belongs to.
# If -path is given, display the full path to spell
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_where(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        colortext = libtext.ConsoleText()
        name = colortext.colorize(str(spell.name), "bold","white","black")
        section = colortext.colorize(str(spell.section), "none","white","black")
        logger.info(name + ": ")
        logger.info1(section)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_url
#
# display the URL for the specified spell
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_url(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        colortext = libtext.ConsoleText()
        name = colortext.colorize(spell.name, "bold","white","black")
        url = colortext.colorize(spell.url, "none","white","black")
        logger.info(name + ": ")
        logger.info1(url)

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_sources
#
# list all source files contained in a spell
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_sources(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_source_urls
#
# lists the urls to all files contained in a spell
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_source_urls(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_maintainer
#
# display the email address of the person currently responsible for
# maintaining a specified section
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_maintainer(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_compile
#
# Show the compiler output generated when the spell was built. 
# If no optional version was given, try the installed version. 
# If the spell is not installed use the version in the grimoire.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_compile(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_install
#
# Used to determine what files were installed by a spell and where
# those files are located, excludes sorcery state files.
# If no optional version was given, try the installed version.
#
# If install-full
#   Like gaze install spell, but shows sorcery state files.
#
# If install-spell
#   Like gaze install spell, but excludes sorcery log files.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_install(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_version
#
# Shows the installed version of the spell and the main grimoires version.
#
# If versions
#   Shows the installed version of the spell and lists all available versions 
#   in all grimoires. If used without a spell name, then lists order of available
#   grimoires.
# 
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_version(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)

        spell.print_version(args.multi)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_license
#
# View the license(s) of the given spell(s), or spells in given section(s),
# or view the information about given license(s)
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_license(args):
    logger.debug("Begin Function")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_checksum
#
# print CRC checksums for spells(s). If no spell is given it default to all.
#
# If md5sum
#   print spell MD5 message digests (fingerprints). If no spell is given it default 
#   to all
#
# If checkmd5s
#   computes the md5sum on spell sources based on passed spell(s),
#   section(s) or entire grimoire(s) if left blank.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_checksum(args):
    logger.debug("Begin Function")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_size
#
# print the sizes and file counts of the passed installed spell(s) or if -all is
# specified, of all the spells. In addition, this will print the largest spell.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_size(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_export
#
# take a snapshot of all currently installed spells and their configuration.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_export(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_import
#
# restore the snapshot from a previous 'gaze export' command (see above)
#
# If --deprecated is specified, the old behaviour is activated and an old cache
# is expected. There is no significant problem if an old cache is restored with
# the new importer. A few files will be ignored - only the files that the new
# exporter saves are considered - and the queuing logic wille be slighty more
# agressive.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_import(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_grimoire
#
# Prints specified grimoire's spells or all grimoires if grimoire-name is omitted
#
# If grimoires:
#   Displays installed grimoires by name only
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_grimoire(args):
    logger.debug("Begin Function")

    if args.multi:
        grimoires = libcodex.Codex()
        grimoires.print_grimoires()

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_html
#
# Prints the specified grimoire or all grimoires if grimoire-name is omitted
# in a nice html format.  Additionally displays links to the source files
# when -s is given.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_html(args):
    logger.debug("Begin Function")

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_search
#
# search [-name|-short] "phrase"
#
# When omitting -name and -short searches spells name, short description and
# long description for.
#
# With -name searches spells name and with -short searches spells short
# description for phrase
#
# Phrase can be any valid extended regular expression. For optimal results,
# don't forget to escape any special characters and use quotes to protect
# the expression.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_search(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_newer
#
# print packages first submitted after a specified date. the date must be
# specified in the 'yyyymmdd' format, where y=year, m=month, and d=day.
# There are two special dates, last_sorcery_update and last_cast.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_newer(args):
    logger.debug("Begin Function")

    

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_older
#
# print packages that were first submitted before a specified date.
# the date must be specified in 'yyyymmdd' format
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_older(args):
    logger.debug("Begin Function")

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_from
#
# find out which spell has installed path/file
#
# Matching is done literally against the end of the path names in the lists
# of installed files. If -regex is passed, the matching is done using basic
# regular expressions against the whole paths in the lists of installed files.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_from(args):
    logger.debug("Begin Function")

    spell = libsystem.Files(args.filename[0])

    spell.print_from()
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_installed
#
# view all installed packages and corresponding version numbers or check
# to see whether a particular package is installed and if it is
# installed display its version number
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_installed(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_section
#
# view a list of all sections in the software catalogue or display a list
# of packages from a specific section
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_section(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_voyeur
#
# start looking at what cast is compiling at the moment and outputs its
# compiler messages. A spell can be optionally specified, or a delay
# after which to abort when no casts could be found.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_voyeur(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_file
#
# show SCRIPT_NAME of the spell, where SCRIPT_NAME is any of the
# following spell scripts:
# 
# BUILD | CONFIGURE | CONFLICTS | DETAILS | DEPENDS | DOWNLOAD | FINAL |
# HISTORY | INSTALL | INSTALL_EXTRAS | PATCH | POST_BUILD | POST_INSTALL |
# POST_REMOVE | POST_RESURRECT | PRE_BUILD | PRE_INSTALL | PRE_REMOVE |
# PRE_RESURRECT | PRE_SUB_DEPENDS | PREPARE | PROVIDES | SECURITY |
# SUB_DEPENDS | TRANSFER | TRIGGER_CHECK | TRIGGERS | UP_TRIGGERS
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_file(args):
    logger.debug("Begin Function")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_history
#
# Show history for a spell (alias for gaze HISTORY <spell>)
#
# Input:  args
# Output: 
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_history(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_depends
#
# shows the spells that explicitly or recursively depend on this
# installed spell.  Up to level $level if specified. Only enabled
# dependencies are shown.
#
# If --fast is specified more limited output is produced, but it runs much faster.
# If --required is specified only the required dependencies are shown and the
# runtime ones are skipped.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_depends(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_dependencies
#
# shows the spells that spell explicitly or recursively depends on.
# Up to level $level if specified. The -c option skips trees that have already been
# shown, the --no-optionals flag skips optional dependencies.
#
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def gaze_dependencies(args):
    logger.debug("Begin Function")

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_time
#
# shows the time the spell(s) needed to get cast. By default the last casting
# time is shown, alternatively the median, mean or weighted mean can be shown.
# The weighted mean mode gives more weight to the last casting time. If more
# then one spell is specified, also a total time is shown.
#
# If --full is specified, then all the calculations will be shown for each spell.
#
# If time-system:
#   shows the time the whole system needed to get cast. If --no-orphans is
#   specified orphaned spells are skipped.
#
# Input:  args
# Output:
# Return: None
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
# Input:  args
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug("Entered Function")

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description="Query / View Sorcery package management information")
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
    parser_alien = subparsers.add_parser('alien',
                                         aliases=('aliens',),
                                         help='Find and Display all files not tracked by the Sorcery Package Management System (Not Working)')
    parser_alien.add_argument('--debug',
                              action='store_true',
                              help='Enable Debugging')
    parser_alien.add_argument("--loglevel",
                              choices=["debug","info","warning","error","critical",
                                       "DEBUG","INFO","WARNING","ERROR","CRITICAL"],
                              help="Set minimum logging level")
    parser_alien.add_argument("-q", "--quiet",
                              action="count",
                              default=0,
                              help="Decrease output verbosity")
    parser_alien.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="Increase output verbosity")
    parser_alien.set_defaults(func=gaze_alien)

    # create the parser for the "orphans" command
    parser_orphans = subparsers.add_parser('orphans',
                                           help='Display installed spells that do not have any explicit dependencies on them (Not Working)')
    parser_orphans.add_argument('--debug',
                                action='store_true',
                                help='Enable Debugging')
    parser_orphans.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical", "DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_orphans.add_argument("-q", "--quiet",
                             action="count",
                             default=0,
                             help="Decrease output verbosity")
    parser_orphans.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="Increase output verbosity")
    parser_orphans.set_defaults(func=gaze_orphans)

    # create the parser for the "activity" command
    parser_activity = subparsers.add_parser('activity',
                                            help='Show the activity log.  (Note: this is actually a log of all that happened involving sorcery, such as casts, summons etc.)  (Not Working)')
    parser_activity.add_argument('--debug',
                                 action='store_true',
                                 help='Display System Info')
    parser_activity.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical", "DEBUG",
                                          "INFO","WARNING","ERROR","CRITICAL"],
                                 help="Set minimum logging level")
    parser_activity.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="Increase output verbosity")
    parser_activity.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="Increase output verbosity")
    parser_activity.set_defaults(func=gaze_activity)


    # create the parser for the "install-queue" command
    parser_install_queue = subparsers.add_parser('install-queue',
                                                 help='Show spells waiting to be installed (Not Working)')
    parser_install_queue.add_argument('--debug',
                                      action='store_true',
                                      help='Enable debugging information')
    parser_install_queue.add_argument("--loglevel",
                                      choices=["debug","info","warning",
                                               "error","critical","DEBUG",
                                               "INFO","WARNING","ERROR",
                                               "CRITICAL"],
                                      help="Set minimum logging level")
    parser_install_queue.add_argument("-q", "--quiet",
                                      action="count",
                                      default=0,
                                      help="Increase output verbosity")
    parser_install_queue.add_argument("-v", "--verbosity",
                                      action="count",
                                      default=0,
                                      help="Increase output verbosity")
    parser_install_queue.set_defaults(func=gaze_install_queue)

    # create the parser for the "remove-queue" command
    parser_remove_queue = subparsers.add_parser('remove-queue',
                                                help='Show spells to be removed (Not Working)')
    parser_remove_queue.add_argument('--debug',
                                     action='store_true',
                                     help='Enable debugging information')
    parser_remove_queue.add_argument("--loglevel",
                                     choices=["debug","info","warning",
                                              "error","critical","DEBUG",
                                              "INFO","WARNING","ERROR",
                                              "CRITICAL"],
                                     help="Set minimum logging level")
    parser_remove_queue.add_argument("-q", "--quiet",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_remove_queue.add_argument("-v", "--verbosity",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_remove_queue.set_defaults(func=gaze_remove_queue)

    # create the parser for the "show-held" command
    parser_show_held = subparsers.add_parser('show-held',
                                             help='Shows all spells currently held (which means they are not to be updated). (Not Working)')
    parser_show_held.add_argument('--debug',
                                  action='store_true',
                                  help='Enable debugging information')
    parser_show_held.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_show_held.add_argument("-q", "--quiet",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_show_held.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_show_held.set_defaults(func=gaze_show_held)

    # create the parser for the "what" command
    parser_show_exiled = subparsers.add_parser('show-exiled',
                                               help='Shows all spells currently exiled (which means they are not to be cast in any way). (Not Working)')
    parser_show_exiled.add_argument('--debug',
                                    action='store_true',
                                    help='Enable debugging information')
    parser_show_exiled.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_show_exiled.add_argument("-q", "--quiet",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_show_exiled.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_show_exiled.set_defaults(func=gaze_show_exiled)

    # create the parser for the "what" command
    parser_provides = subparsers.add_parser('provides',
                                            help='Displays spells that provide the feature. (Not Working)')
    parser_provides.add_argument('feature',
                             nargs=1,
                             help='Feature')
    parser_provides.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_provides.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_provides.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_provides.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_provides.set_defaults(func=gaze_provides)
    
    # create the parser for the "what" command
    parser_what = subparsers.add_parser('what',
                                        help='Display spell description')
    parser_what.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_what.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="Decrease output verbosity")
    parser_what.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="Increase output verbosity")
    parser_what.set_defaults(func=gaze_what)

    # create the parser for the "short" command
    parser_short = subparsers.add_parser('short',
                                         help='Display spell short description (Not Working)')
    parser_short.add_argument('spell',
                              nargs='+',
                              help='Display System Info')
    parser_short.add_argument('--debug',
                              action='store_true',
                              help='Enable debugging information')
    parser_short.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_short.add_argument("-q", "--quiet",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_short.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_short.set_defaults(func=gaze_short)

    # create the parser for the "where" command
    parser_where = subparsers.add_parser('where',
                                         help='Display the section a spell belongs to.')
    parser_where.add_argument('spell',
                             nargs='+',
                             help='Spell(s) to display')
    parser_where.add_argument('-p','-path', '--path',
                             action='store_true',
                             help='Display the full path to spell')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Enable Debugging')
    parser_where.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_where.add_argument("-q", "--quiety",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_where.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_where.set_defaults(func=gaze_where)

    # create the parser for the "url" command
    parser_url = subparsers.add_parser('url',
                                       aliases=('website',),
                                       help='Display spell homepage')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_url.add_argument("--loglevel",
                            choices=["debug","info","warning",
                                     "error","critical","DEBUG",
                                     "INFO","WARNING","ERROR",
                                     "CRITICAL"],
                            help="Set minimum logging level")
    parser_url.add_argument("-q", "--quiet",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_url.add_argument("-v", "--verbosity",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_url.set_defaults(func=gaze_url)

    # create the parser for the "sources" command
    parser_sources = subparsers.add_parser('sources',
                                           help='List all source files contained in a spell. (Not Working)')
    parser_sources.add_argument('spell',
                                nargs='+',
                                help='Display System Info')
    parser_sources.add_argument('--debug',
                                action='store_true',
                                help='Enable debugging information')
    parser_sources.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_sources.add_argument("-q", "--quiet",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_sources.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_sources.set_defaults(func=gaze_sources)

    # create the parser for the "source_urls" command
    parser_source_url = subparsers.add_parser('source_urls',
                                              help='Lists the urls to all files contained in a spell. (Not Working)')
    parser_source_url.add_argument('spell',
                                   nargs='+',
                                   help='Spell')
    parser_source_url.add_argument('--debug',
                                   action='store_true',
                                   help='Enable debugging information')
    parser_source_url.add_argument("--loglevel",
                                   choices=["debug","info","warning",
                                            "error","critical","DEBUG",
                                            "INFO","WARNING","ERROR",
                                            "CRITICAL"],
                                   help="Set minimum logging level")
    parser_source_url.add_argument("-q", "--quiet",
                                   action="count",
                                   default=0,
                                   help="increase output verbosity")
    parser_source_url.add_argument("-v", "--verbosity",
                                   action="count",
                                   default=0,
                                   help="increase output verbosity")
    parser_source_url.set_defaults(func=gaze_source_urls)

    # create the parser for the "maintainer" command
    parser_maintainer = subparsers.add_parser('maintainer',
                                              help='Display the email address of the person responsible for maintaining a specified spell. (Not Working)')
    parser_maintainer.add_argument('spell',
                                   nargs='+',
                                   help='Spell')
    parser_maintainer.add_argument('--debug',
                                   action='store_true',
                                   help='Display System Info')
    parser_maintainer.add_argument("--loglevel",
                                   choices=["debug","info","warning",
                                            "error","critical","DEBUG",
                                            "INFO","WARNING","ERROR",
                                            "CRITICAL"],
                                   help="Set minimum logging level")
    parser_maintainer.add_argument("-q", "--quiet",
                                   action="count",
                                   default=0,
                                   help="increase output verbosity")
    parser_maintainer.add_argument("-v", "--verbosity",
                                   action="count",
                                   default=0,
                                   help="increase output verbosity")
    parser_maintainer.set_defaults(func=gaze_maintainer)

    # create the parser for the "compile" command
    parser_compile = subparsers.add_parser('compile',
                                           help='Show the compiler output generated when the spell was built.  If no optional version was given, try the installed version.  If the spell is not installed use the version in the grimoire. (Not Working)')
    parser_compile.add_argument('spell',
                                nargs=1,
                                help='Spell')
    parser_compile.add_argument('version',
                                nargs='?',
                                help='Specifies which Version of spell to view.')
    parser_compile.add_argument('--debug',
                                action='store_true',
                                help='Display Debugging Information')
    parser_compile.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_compile.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_compile.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_compile.set_defaults(func=gaze_compile)

    # create the parser for the "install" command
    parser_install = subparsers.add_parser('install',
                                           help='Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files. If no optional version was given, try the installed version. (Not Working)')
    parser_install.add_argument('spell',
                                nargs=1,
                                help='Spell')
    parser_install.add_argument('version',
                                nargs=1,
                                help='Specifies which version of spell to view')
    parser_install.add_argument('--debug',
                                action='store_true',
                                help='Display Debugging Information')
    parser_install.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_install.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_install.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_install.set_defaults(func=gaze_install,
                                install_display=False)

    # create the parser for the "install-full" command
    parser_install_full = subparsers.add_parser('install-full',
                                                help='Used to determine what files were installed by a spell and where those files are located.  If no optional version was given, try the installed version.  (Not Working)')
    parser_install_full.add_argument('spell',
                                     nargs=1,
                                     help='Spell')
    parser_install_full.add_argument('version',
                                     nargs=1,
                                     help='Specifies which version of the spell to view.')
    parser_install_full.add_argument('--debug',
                                     action='store_true',
                                     help='Display Debugging Information')
    parser_install_full.add_argument("--loglevel",
                                     choices=["debug","info","warning",
                                              "error","critical","DEBUG",
                                              "INFO","WARNING","ERROR",
                                              "CRITICAL"],
                                     help="Set minimum logging level")
    parser_install_full.add_argument("-q", "--quiet",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_install_full.add_argument("-v", "--verbosity",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_install_full.set_defaults(func=gaze_install,
                                     install_display='Full')

    # create the parser for the "install-spell" command
    parser_install_spell = subparsers.add_parser('install-spell',
                                                 help='Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files and sorcery log files.  If no optional version was given, try the installed version. (Not Working)')
    parser_install_spell.add_argument('spell',
                                      nargs=1,
                                      help='Spell')
    parser_install_spell.add_argument('version',
                                      nargs=1,
                                      help='Specifies which version of the spell to view')
    parser_install_spell.add_argument('--debug',
                                      action='store_true',
                                      help='Display System Info')
    parser_install_spell.add_argument("--loglevel",
                                      choices=["debug","info","warning",
                                               "error","critical","DEBUG",
                                               "INFO","WARNING","ERROR",
                                               "CRITICAL"],
                                      help="Set minimum logging level")
    parser_install_spell.add_argument("-q", "--quiet",
                                      action="count",
                                      default=0,
                                      help="increase output verbosity")
    parser_install_spell.add_argument("-v", "--verbosity",
                                      action="count",
                                      default=0,
                                      help="increase output verbosity")
    parser_install_spell.set_defaults(func=gaze_install,
                                      install_display='Spell')

    # create the parser for the "what" command
    parser_version = subparsers.add_parser('version',
                                           help='Shows the installed version of the spell and the main grimoires version.')
    parser_version.add_argument('spell',
                                nargs=1,
                                help='Display System Info')
    parser_version.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_version.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_version.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_version.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_version.set_defaults(func=gaze_version,
                                multi=False)

    # create the parser for the "versions" command
    parser_versions = subparsers.add_parser('versions',
                                            help='Shows the installed version of the spell and lists all available versions in all grimoires. If used without a spell name, then lists order of available grimoires.')
    parser_versions.add_argument('spell',
                                 nargs=1,
                                 help='Display System Info')
    parser_versions.add_argument('--debug',
                                 action='store_true',
                                 help='Display System Info')
    parser_versions.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_versions.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_versions.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_versions.set_defaults(func=gaze_version,
                                 multi=True)

    # create the parser for the "license" command
    parser_license = subparsers.add_parser('license',
                                           help='View the license(s) of the given spell(s), or spells in given section(s), or view the information about given license(s) (Not Working)')
    parser_license.add_argument('ssl',
                                nargs='+',
                                help='Specify Spell, Section, or License to view')
    parser_license.add_argument('--debug',
                                action='store_true',
                                help='Enable debugging information')
    parser_license.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_license.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_license.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_license.set_defaults(func=gaze_license)

    # create the parser for the "versions" command
    parser_sum = subparsers.add_parser('sum',
                                       help='Print CRC checksums for spells(s). If no spell is given it default to all. (Not Working)')
    parser_sum.add_argument('spell',
                            nargs='?',
                            help='Display System Info')
    parser_sum.add_argument('--debug',
                            action='store_true',
                            help='Display System Info')
    parser_sum.add_argument("--loglevel",
                            choices=["debug","info","warning",
                                     "error","critical","DEBUG",
                                     "INFO","WARNING","ERROR",
                                     "CRITICAL"],
                            help="Set minimum logging level")
    parser_sum.add_argument("-q", "--quiet",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_sum.add_argument("-v", "--verbosity",
                            action="count",
                            default=0,
                            help="increase output verbosity")
    parser_sum.set_defaults(func=gaze_checksum,
                            check_type='CRC')

    # create the parser for the "versions" command
    parser_md5sum = subparsers.add_parser('md5sum',
                                          help='Print spell MD5 message digests (fingerprints). If no spell is given it default to all (Not Working)')
    parser_md5sum.add_argument('spell',
                               nargs='?',
                               help='Display System Info')
    parser_md5sum.add_argument('--debug',
                               action='store_true',
                               help='Display System Info')
    parser_md5sum.add_argument("--loglevel",
                               choices=["debug","info","warning",
                                        "error","critical","DEBUG",
                                        "INFO","WARNING","ERROR",
                                        "CRITICAL"],
                               help="Set minimum logging level")
    parser_md5sum.add_argument("-q", "--quiet",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_md5sum.add_argument("-v", "--verbosity",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_md5sum.set_defaults(func=gaze_checksum,
                               check_type='MD5')

    # create the parser for the "versions" command
    parser_size = subparsers.add_parser('size',
                                        help='print the sizes and file counts of the passed installed spell(s). (Not Working)')
    parser_size.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_size.add_argument('-a','-all','--all',
                             action='store_true',
                             help='Display sizes of all the spells. In addition, this will print the largest spell.')
    parser_size.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_size.add_argument("--loglevel",
                             choices=["debug","info","warning",
                                      "error","critical","DEBUG",
                                      "INFO","WARNING","ERROR",
                                      "CRITICAL"],
                             help="Set minimum logging level")
    parser_size.add_argument("-q", "--quiet",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_size.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_size.set_defaults(func=gaze_size)

    # create the parser for the "versions" command
    parser_export = subparsers.add_parser('export',
                                          help='Take a snapshot of all currently installed spells and their configuration. (Not Working)')
    parser_export.add_argument('--debug',
                               action='store_true',
                               help='Display System Info')
    parser_export.add_argument("--loglevel",
                               choices=["debug","info","warning",
                                        "error","critical","DEBUG",
                                        "INFO","WARNING","ERROR",
                                        "CRITICAL"],
                               help="Set minimum logging level")
    parser_export.add_argument("-q", "--quiet",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_export.add_argument("-v", "--verbosity",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_export.set_defaults(func=gaze_export)

    # create the parser for the "import" command
    parser_import = subparsers.add_parser('import',
                                          help='restore the snapshot from a previous "gaze export" command (see above). (Not Working)')
    parser_import.add_argument('snapshot',
                               nargs=1,
                               help='Display System Info')
    parser_import.add_argument('--depreciated',
                               action='store_true',
                               help='Use the old behaviour.  An old cache is expected. There is no significant problem if an old cache is restored with the new importer. A few files will be ignored - only the files that the new exporter saves are considered - and the queuing logic wille be slighty more agressive.')
    parser_import.add_argument('--debug',
                               action='store_true',
                               help='Display Debugging Information')
    parser_import.add_argument("--loglevel",
                               choices=["debug","info","warning",
                                        "error","critical","DEBUG",
                                        "INFO","WARNING","ERROR",
                                        "CRITICAL"],
                               help="Set minimum logging level")
    parser_import.add_argument("-q", "--quiet",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_import.add_argument("-v", "--verbosity",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_import.set_defaults(func=gaze_import)

    # create the parser for the "grimoire" command
    parser_grimoire = subparsers.add_parser('grimoire',
                                            help="Prints specified grimoire's spells or all grimoires if grimoire-name is omitted (Not Working)")
    parser_grimoire.add_argument('grimoire',
                                 nargs='*',
                                 help='Specify grimoire to view')
    parser_grimoire.add_argument('--debug',
                                 action='store_true',
                                 help='Display System Info')
    parser_grimoire.add_argument("--loglevel",
                                 choices=["debug","info","warning",
                                          "error","critical","DEBUG",
                                          "INFO","WARNING","ERROR",
                                          "CRITICAL"],
                                 help="Set minimum logging level")
    parser_grimoire.add_argument("-q", "--quiet",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_grimoire.add_argument("-v", "--verbosity",
                                 action="count",
                                 default=0,
                                 help="increase output verbosity")
    parser_grimoire.set_defaults(func=gaze_grimoire,
                                 multi=False,
                                 display_format='console')

    # create the parser for the "what" command
    parser_grimoires = subparsers.add_parser('grimoires',
                                             help='Display installed grimoires by name only. (Not Working)')
    parser_grimoires.add_argument('--debug',
                                  action='store_true',
                                  help='Display System Info')
    parser_grimoires.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_grimoires.add_argument("-q", "--quiet",
                                  action="count",
                                  default=0,
                                  help="Decrease output verbosity")
    parser_grimoires.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_grimoires.set_defaults(func=gaze_grimoire,
                                  multi=True,
                                  display_format='console')

    # create the parser for the "html" command
    parser_html = subparsers.add_parser('html',
                                        help='Prints the specified grimoire or all grimoires if grimoire-name is omitted in a nice html format. (Not Working)')
    parser_html.add_argument('grimoire',
                             nargs='*',
                             help='Specified grimoire(s)')
    parser_html.add_argument('-s','--source',
                             action='store_true',
                             help='Displays links to the source files.')
    parser_html.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_html.add_argument("--loglevel",
                             choices=["debug","info","warning",
                                      "error","critical","DEBUG",
                                      "INFO","WARNING","ERROR",
                                      "CRITICAL"],
                             help="Set minimum logging level")
    parser_html.add_argument("-q", "--quiet",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_html.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_html.set_defaults(func=gaze_grimoire,
                             multi=False,
                             display_format='html')


    # create the parser for the "versions" command
    parser_search = subparsers.add_parser('search',
                                          help='Searches spells name, short description and long description for phrase (Not Working)')
    # Need to make the following mutually exclusive
    parser_search.add_argument('-n','-name','--name',
                             action='store_true',
                             help='Only search spells name')
    parser_search.add_argument('-s','-short','--short',
                             action='store_true',
                             help='Only search spells short description')
    parser_search.add_argument('phrase',
                               nargs=1,
                               help="Any valid extended regular expression. For optimal results, don't forget to escape any special characters and use quotes to protect the expression.")
    parser_search.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_search.add_argument("--loglevel",
                               choices=["debug","info","warning",
                                        "error","critical","DEBUG",
                                        "INFO","WARNING","ERROR",
                                        "CRITICAL"],
                               help="Set minimum logging level")
    parser_search.add_argument("-q", "--quiet",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_search.add_argument("-v", "--verbosity",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_search.set_defaults(func=gaze_search)

    # create the parser for the "what" command
    parser_newer = subparsers.add_parser('newer',
                                         help="Print packages first submitted after a specified date. (Not Working)")
    parser_newer.add_argument('date',
                              nargs='?',
                              default='last_sorcery_update',
                              help="Specify Date.  The date must be in the 'yyyymmdd' format, where y=year, m=month, and d=day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_newer.add_argument('--debug',
                              action='store_true',
                              help='Display System Info')
    parser_newer.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_newer.add_argument("-q", "--quiet",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_newer.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_newer.set_defaults(func=gaze_newer)

    # create the parser for the "what" command
    parser_older = subparsers.add_parser('older',
                                         help='print packages that were first submitted before a specified date. (Not Working)')
    parser_older.add_argument('date',
                              nargs='?',
                              help="Specify Date.  The date must be in the 'yyyymmdd' format, where y=year, m=month, and d=day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_older.add_argument('--debug',
                              action='store_true',
                              help='Display System Info')
    parser_older.add_argument("--loglevel",
                              choices=["debug","info","warning",
                                       "error","critical","DEBUG",
                                       "INFO","WARNING","ERROR",
                                       "CRITICAL"],
                              help="Set minimum logging level")
    parser_older.add_argument("-q", "--quiet",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_older.add_argument("-v", "--verbosity",
                              action="count",
                              default=0,
                              help="increase output verbosity")
    parser_older.set_defaults(func=gaze_older)

    # create the parser for the "from" command
    parser_from = subparsers.add_parser('from',
                                        help="find out which spell has installed 'path/file.'  Matching is done literally against the end of the path names in the lists of installed files. (Not Working)")
    parser_from.add_argument('filename',
                             nargs=1,
                             help='Display System Info')
    parser_from.add_argument('-r','-regex','--regex',
                             action='store_true',
                             help='Matching using basic regular expressions against the whole paths in the lists of installed files.')
    parser_from.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_from.add_argument("--loglevel",
                             choices=["debug","info","warning",
                                      "error","critical","DEBUG",
                                      "INFO","WARNING","ERROR",
                                      "CRITICAL"],
                             help="Set minimum logging level")
    parser_from.add_argument("-q", "--quiet",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_from.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_from.set_defaults(func=gaze_from)

    # create the parser for the "what" command
    parser_installed = subparsers.add_parser('installed',
                                             help='View all installed packages and corresponding version numbers (Not Working)')
    parser_installed.add_argument('spell',
                                  nargs='*',
                                  help='Check to see whether a particular package is installed and if it is installed display its version number')
    parser_installed.add_argument('--debug',
                                  action='store_true',
                                  help='Display System Info')
    parser_installed.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_installed.add_argument("-q", "--quiet",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_installed.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_installed.set_defaults(func=gaze_installed)

    # create the parser for the "what" command
    parser_section = subparsers.add_parser('section',
                                           help='View a list of all sections in the software catalogue or display a list of packages from a specific section. (Not Working)')
    parser_section.add_argument('section',
                                nargs='?',
                                help='Display System Info')
    parser_section.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_section.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_section.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_section.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_section.set_defaults(func=gaze_section)

    # create the parser for the "what" command
    parser_voyeur = subparsers.add_parser('voyeur',
                                          help='start looking at what cast is compiling at the moment and outputs its compiler messages. A spell can be optionally specified, or a delay after which to abort when no casts could be found. (Not Working)')
    parser_voyeur.add_argument('spell',
                               nargs='?',
                               help='Display System Info')
    parser_voyeur.add_argument('--debug',
                               action='store_true',
                               help='Display System Info')
    parser_voyeur.add_argument("--loglevel",
                               choices=["debug","info","warning",
                                        "error","critical","DEBUG",
                                        "INFO","WARNING","ERROR",
                                        "CRITICAL"],
                               help="Set minimum logging level")
    parser_voyeur.add_argument("-q", "--quiet",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_voyeur.add_argument("-v", "--verbosity",
                               action="count",
                               default=0,
                               help="increase output verbosity")
    parser_voyeur.set_defaults(func=gaze_voyeur)

    # create the parser for the "what" command
    parser_DEPENDS = subparsers.add_parser('DEPENDS',
                                           help='Show DEPENDS of the spell (Not Working)')
    parser_DEPENDS.add_argument('spell',
                                nargs=1,
                                help='Display System Info')
    parser_DEPENDS.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_DEPENDS.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_DEPENDS.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_DEPENDS.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_DEPENDS.set_defaults(func=gaze_file,
                                filename='DEPENDS')

    # create the parser for the "what" command
    parser_HISTORY = subparsers.add_parser('HISTORY',
                                           help='Shom HISTORY of the spell (Not Working)')
    parser_HISTORY.add_argument('spell',
                                nargs=1,
                                help='Spell')
    parser_HISTORY.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_HISTORY.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_HISTORY.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_HISTORY.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_HISTORY.set_defaults(func=gaze_file,
                                filename='HISTORY')

    # create the parser for the "what" command
    parser_history = subparsers.add_parser('history',
                                           help='Show history for a spell (alias for gaze HISTORY). (Not Working)')
    parser_history.add_argument('spell',
                                nargs=1,
                                help='Display System Info')
    parser_history.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_history.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_history.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_history.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_history.set_defaults(func=gaze_file,
                                filename='HISTORY')

    # create the parser for the "what" command
    parser_checkmd5s = subparsers.add_parser('checkmd5s',
                                             help='Computes the md5sum on spell sources based on passed spell(s), section(s) or entire grimoire(s) if left blank. (Not Working)')
    parser_checkmd5s.add_argument('spell',
                                  nargs='*',
                                  help='Display System Info')
    parser_checkmd5s.add_argument('--debug',
                                  action='store_true',
                                  help='Display System Info')
    parser_checkmd5s.add_argument("--loglevel",
                                  choices=["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help="Set minimum logging level")
    parser_checkmd5s.add_argument("-q", "--quiet",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_checkmd5s.add_argument("-v", "--verbosity",
                                  action="count",
                                  default=0,
                                  help="increase output verbosity")
    parser_checkmd5s.set_defaults(func=gaze_checksum,
                                  filename='checksum')

    # create the parser for the "what" command
    parser_depends = subparsers.add_parser('depends',
                                           help='shows the spells that explicitly or recursively depend on this installed spell.  Only enabled dependencies are shown. (Not Working)')
    parser_depends.add_argument('spell',
                                nargs=1,
                                help='Display System Info')
    parser_depends.add_argument('level',
                                nargs='?',
                                help='Up to level $level if specified')
    parser_depends.add_argument('--fast',
                                action='store_true',
                                help='Limit output, but runs much faster.')
    parser_depends.add_argument('--required',
                                action='store_true',
                                help='Show only the required dependencies and skip the runtime dependencies.')
    parser_depends.add_argument('--debug',
                                action='store_true',
                                help='Display System Info')
    parser_depends.add_argument("--loglevel",
                                choices=["debug","info","warning",
                                         "error","critical","DEBUG",
                                         "INFO","WARNING","ERROR",
                                         "CRITICAL"],
                                help="Set minimum logging level")
    parser_depends.add_argument("-q", "--quiet",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_depends.add_argument("-v", "--verbosity",
                                action="count",
                                default=0,
                                help="increase output verbosity")
    parser_depends.set_defaults(func=gaze_depends)

    # create the parser for the "what" command
    parser_dependencies = subparsers.add_parser('dependencies',
                                                help='shows the spells that spell explicitly or recursively depends on. (Not Working)')
    parser_dependencies.add_argument('spell',
                                     nargs=1,
                                     help='Display System Info')
    parser_dependencies.add_argument('level',
                                     nargs='?',
                                     help='Up to level $level if specified.')
    parser_dependencies.add_argument('-c',
                                     action='store_true',
                                     help='skips trees that have already been shown')
    parser_dependencies.add_argument('--no-optionals',
                                     action='store_true',
                                     help='skips optional dependencies.')
    parser_dependencies.add_argument('--debug',
                                     action='store_true',
                                     help='Display System Info')
    parser_dependencies.add_argument("--loglevel",
                                     choices=["debug","info","warning",
                                              "error","critical","DEBUG",
                                              "INFO","WARNING","ERROR",
                                              "CRITICAL"],
                                     help="Set minimum logging level")
    parser_dependencies.add_argument("-q", "--quiet",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_dependencies.add_argument("-v", "--verbosity",
                                     action="count",
                                     default=0,
                                     help="increase output verbosity")
    parser_dependencies.set_defaults(func=gaze_dependencies)

    # create the parser for the "what" command
    parser_time = subparsers.add_parser('time',
                                        help='Shows the time the spell(s) needed to get cast. By default the last casting time is shown, alternatively the median, mean or weighted mean can be shown.  If more then one spell is specified, also a total time is shown. (Not Working)')
    parser_time.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_time.add_argument('--last',
                             action='store_true',
                             help='Display System Info')
    parser_time.add_argument('--medium',
                             action='store_true',
                             help='Display System Info')
    parser_time.add_argument('--mean',
                             action='store_true',
                             help='Display System Info')
    parser_time.add_argument('--weight-last',
                             action='store_true',
                             help='Give more weight to the last casting time.')
    parser_time.add_argument('--full',
                             action='store_true',
                             help='Display System Info')
    parser_time.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_time.add_argument("--loglevel",
                             choices=["debug","info","warning",
                                      "error","critical","DEBUG",
                                      "INFO","WARNING","ERROR",
                                      "CRITICAL"],
                             help="Set minimum logging level")
    parser_time.add_argument("-q", "--quiet",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_time.add_argument("-v", "--verbosity",
                             action="count",
                             default=0,
                             help="increase output verbosity")
    parser_time.set_defaults(func=gaze_time,
                             system=False)

    # create the parser for the "what" command
    parser_time_system = subparsers.add_parser('time-system', help='Shows the time the whole system needed to get cast. (Not Working)')
    parser_time_system.add_argument('--no-orphans',
                             action='store_true',
                             help='Skip orphaned spells.')
    parser_time_system.add_argument('--last',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument('--medium',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument('--mean',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument('--weight-last',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument('--full',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_time_system.add_argument("--loglevel",
                                    choices=["debug","info","warning",
                                             "error","critical","DEBUG",
                                             "INFO","WARNING","ERROR",
                                             "CRITICAL"],
                                    help="Set minimum logging level")
    parser_time_system.add_argument("-q", "--quiet",
                                    action="count",
                                    default=0,
                                    help="increase output verbosity")
    parser_time_system.add_argument("-v", "--verbosity",
                                    action="count",
                                    default=0,
                                    help="increase output verbosity")
    parser_time_system.set_defaults(func=gaze_time,
                                    system=True)

    # Store all the arguments in a variable
    args = parser.parse_args()

    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra "sudo" in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
        os.execvp("sudo", ["sudo"] + sys.argv)

    # Now we are definitely running as root

    # Parse the config files
    config = libconfig.main_configure(args)

    logger.debug2("Configuration set")
    logger.debug3("Configuration Settings: " + str(config))
    logger.debug4("Arguments: " + str(args))

    # "application" code
    # Run the specified subcommand as per args
    if args.func:
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
