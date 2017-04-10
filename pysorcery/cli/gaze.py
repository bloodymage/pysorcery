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
import pysorcery
from pysorcery import __version__, enable_debugging_mode
from pysorcery.lib import libcodex
from pysorcery.lib import libconfig
from pysorcery.lib import libfiles
from pysorcery.lib import libgrimoire
from pysorcery.lib import libspell
from pysorcery.lib import libsystem
from pysorcery.lib import libtext

# Other Optional Libraries
#if distro.distro_id in distro.distro_dict['deb']:
#    import apt

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
colortext = libtext.ConsoleText()

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------
            
#-------------------------------------------------------------------------------
#
# Functions
#
# gaze_alien
# gaze_orphans
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
# Output: Prints list of alien files
# Return: None
#
# Status: Works on Ubuntu
#         Works, but buggy on SourceMage
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
# Status: Works on ubuntu
#
#-------------------------------------------------------------------------------
def gaze_orphans(args):
    logger.debug("Begin Function")

    orphans = libspell.SpellList()

    orphan_list = orphans.list_orphans()

    orphans.print_list(orphan_list)
    
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
# Status: Works on Ubuntu
#         Works on Source Mage
#
#         Printing could display better
#
#-------------------------------------------------------------------------------
def gaze_activity(args):
    logger.debug("Begin Function")

    activity = libfiles.ActivityLog()
    activity.print_activity()
    
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

    queue = libspell.SpellList()
    queue.list_install_queue()

    queue.print_list()
    
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

    spell = libfiles.Files(args.filename[0])

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

    if args.spell:
        for i in args.spell:
            spell = libspell.Spell(i)
            spell.print_version()

    else:
        installed_spells = libspell.InstalledSpells()
        installed_spells.print_installed()
        
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
    logger.debug('Entered Function')

    # Common Help Descriptions:
    quiet_help = 'Decrease output'
    verbose_help = 'Increase output'
    loglevel_help = 'Specify output level'
    debug_help = 'Maximize output level'

    # Parse Command Line Arguments
    parser = argparse.ArgumentParser(description = 'Query / View Sorcery package management information')


    # Create subcommands
    subparsers = parser.add_subparsers(title = 'commands',
                                       metavar = 'Command',
                                       help = 'Description')
    # Enable aliases for subcommands
    parser.register('action',
                    'parsers',
                    argparse.AliasedSubParsersAction)

    #------------------------------------------
    #
    # Create the parser for the "alien" command
    #
    #-------------------------------------------
    alien_help = "Find and Display all files not tracked by the Sorcery Package Management System " + colortext.colorize('(Functionally Working, buggy)', 'bold', 'yellow', 'black') + "."
    parser_alien = subparsers.add_parser('alien',
                                         aliases = ('aliens',),
                                         help = alien_help)

    # Parser Groups
    alien_logging_opts = parser_alien.add_argument_group('Logging Options')

    # Parser Arguments
    alien_logging_opts.add_argument("-q", "--quiet",
                                    action = "count",
                                    default = 0,
                                    help= quiet_help)

    if enable_debugging_mode is True:
        alien_logging_opts.add_argument("-v", "--verbosity",
                                        action = "count",
                                        default = 0,
                                        help = verbose_help)
        alien_logging_opts.add_argument("--loglevel",
                                        choices = ["debug","info","warning",
                                                 "error","critical",
                                                 "DEBUG","INFO","WARNING",
                                                 "ERROR","CRITICAL"],
                                        help = loglevel_help)
        alien_logging_opts.add_argument('--debug',
                                        action = 'store_true',
                                        help = debug_help)

    parser_alien.set_defaults(func = gaze_alien)

    #-------------------------------------------
    #
    # create the parser for the "orphans" command
    #
    #-------------------------------------------
    orphans_help = "Display installed spells that do not have any explicit dependencies on them " + colortext.colorize('(Not Working)', 'bold', 'red', 'black') + "."
    parser_orphans = subparsers.add_parser('orphans',
                                           help = orphans_help)
    orphans_logging_opts = parser_orphans.add_argument_group('Logging Option')
    orphans_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = quiet_help)

    if enable_debugging_mode is True:
        orphans_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        orphans_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical", "DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        orphans_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_orphans.set_defaults(func = gaze_orphans)

    
    # create the parser for the "activity" command
    activity_help = "Show the activity log.  (Note: this is actually a log of all that happened involving sorcery, such as casts, summons etc.) " + colortext.colorize('(Not Working)', 'bold', 'red', 'black') + "."
    parser_activity = subparsers.add_parser('activity',
                                            help = activity_help)
    activity_logging_opts = parser_activity.add_argument_group('Logging Options')
    activity_logging_opts.add_argument("-q", "--quiet",
                                       action = "count",
                                       default = 0,
                                       help = quiet_help)

    if enable_debugging_mode is True:
        activity_logging_opts.add_argument("-v", "--verbosity",
                                           action = "count",
                                           default = 0,
                                           help = verbose_help)
        activity_logging_opts.add_argument("--loglevel",
                                           choices = ["debug","info","warning",
                                                    "error","critical", "DEBUG",
                                                    "INFO","WARNING",
                                                    "ERROR","CRITICAL"],
                                           help = loglevel_help)
        activity_logging_opts.add_argument('--debug',
                                           action = 'store_true',
                                           help = debug_help)
        
    activity_logging_opts.set_defaults(func = gaze_activity)

    #-------------------------------------------
    #
    # create the parser for the "install-queue" command
    #
    #-------------------------------------------
    install_help = "Show spells waiting to be installed " + colortext.colorize('(Not Working)', 'bold', 'red', 'black') + "."
    parser_install_queue = subparsers.add_parser('install-queue',
                                                 help = install_help)
    inst_queue_logging_opts = parser_install_queue.add_argument_group('Logging Options')
    inst_queue_logging_opts.add_argument("-q", "--quiet",
                                         action = "count",
                                         default = 0,
                                         help = quiet_help)

    if enable_debugging_mode is True:
        inst_queue_logging_opts.add_argument("-v", "--verbosity",
                                             action = "count",
                                             default = 0,
                                             help = verbose_help)
        inst_queue_logging_opts.add_argument("--loglevel",
                                             choices = ["debug","info","warning",
                                                      "error","critical","DEBUG",
                                                      "INFO","WARNING","ERROR",
                                                      "CRITICAL"],
                                             help = loglevel_help)
        inst_queue_logging_opts.add_argument('--debug',
                                             action = 'store_true',
                                             help = debug_help)

    parser_install_queue.set_defaults(func = gaze_install_queue)

    #-------------------------------------------
    #
    # create the parser for the "remove-queue" command
    #
    #-------------------------------------------
    remove_help = "Show spells to be removed  " + colortext.colorize('(Not Working)', 'bold', 'red', 'black') + "."
    parser_remove_queue = subparsers.add_parser('remove-queue',
                                                help = remove_help)

    remove_queue_logging_opts = parser_remove_queue.add_argument_group('Logging Options')
    remove_queue_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                     help = quiet_help)

    if enable_debugging_mode is True:
        remove_queue_logging_opts.add_argument("-v", "--verbosity",
                                               action = "count",
                                               default = 0,
                                               help = verbose_help)
        remove_queue_logging_opts.add_argument("--loglevel",
                                               choices = ["debug","info","warning",
                                                        "error","critical","DEBUG",
                                                        "INFO","WARNING","ERROR",
                                                        "CRITICAL"],
                                               help = loglevel_help)
        remove_queue_logging_opts.add_argument('--debug',
                                               action = 'store_true',
                                               help = debug_help)

    parser_remove_queue.set_defaults(func = gaze_remove_queue)

    #-------------------------------------------
    #
    # create the parser for the "show-held" command
    #
    #-------------------------------------------
    show_held_help = 'Shows all spells currently held (which means they are not to be updated). (Not Working)'
    parser_show_held = subparsers.add_parser('show-held',
                                             help = show_held_help)


    show_held_logging_opts = parser_show_held.add_argument_group('Logging Options')


    show_held_logging_opts.add_argument("-q", "--quiet",
                                        action = "count",
                                        default = 0,
                                        help = quiet_help)

    if enable_debugging_mode is True:
        show_held_logging_opts.add_argument("-v", "--verbosity",
                                            action = "count",
                                            default = 0,
                                            help = verbose_help)
        show_held_logging_opts.add_argument("--loglevel",
                                            choices = ["debug","info","warning",
                                                     "error","critical","DEBUG",
                                                     "INFO","WARNING","ERROR",
                                                     "CRITICAL"],
                                            help = loglevel_help)
        show_held_logging_opts.add_argument('--debug',
                                            action = 'store_true',
                                            help = debug_help)
        
    parser_show_held.set_defaults(func = gaze_show_held)


    #-------------------------------------------
    #
    # create the parser for the "show-exiled" command
    #
    #-------------------------------------------
    show_exiled_help = 'Shows all spells currently exiled (which means they are not to be cast in any way). (Not Working)'
    parser_show_exiled = subparsers.add_parser('show-exiled',
                                               help = show_exiled_help)
    show_exiled_logging_opts = parser_show_exiled.add_argument_group('Logging Options')
    show_exiled_logging_opts.add_argument("-q", "--quiet",
                                  action = "count",
                                  default = 0,
                                  help = quiet_help)

    if enable_debugging_mode is True:
        show_exiled_logging_opts.add_argument("-v", "--verbosity",
                                              action = "count",
                                              default = 0,
                                              help = verbose_help)
        show_exiled_logging_opts.add_argument("--loglevel",
                                              choices = ["debug","info","warning",
                                                       "error","critical","DEBUG",
                                                       "INFO","WARNING","ERROR",
                                                       "CRITICAL"],
                                              help = loglevel_help)
        show_exiled_logging_opts.add_argument('--debug',
                                              action = 'store_true',
                                              help = debug_help)

    parser_show_exiled.set_defaults(func = gaze_show_exiled)


    #-------------------------------------------
    #
    # create the parser for the "provides" command
    #
    #-------------------------------------------
    parser_provides = subparsers.add_parser('provides',
                                            help = 'Displays spells that provide the feature. (Not Working)')
    provides_logging_opts = parser_provides.add_argument_group('Logging Options')
    parser_provides.add_argument('feature',
                             nargs = 1,
                             help = 'Feature')
    provides_logging_opts.add_argument("-q", "--quiet",
                                 action = "count",
                                 default = 0,
                                 help = quiet_help)
    
    if enable_debugging_mode is True:
        provides_logging_opts.add_argument("-v", "--verbosity",
                                           action = "count",
                                           default = 0,
                                           help = verbose_help)
        provides_logging_opts.add_argument("--loglevel",
                                           choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                           help = loglevel_help)
        provides_logging_opts.add_argument('--debug',
                                           action = 'store_true',
                                           help = debug_help)

    parser_provides.set_defaults(func = gaze_provides)
    

    #-------------------------------------------
    #
    # create the parser for the "what" command
    #
    #-------------------------------------------
    parser_what = subparsers.add_parser('what',
                                        help = 'Display spell description')
    what_logging_opts = parser_what.add_argument_group('Logging Options')
    parser_what.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_what.add_argument('-g','--grimoire',
                             nargs = '+',
                             help = 'specify which grimoire(s) to look in.')
    what_logging_opts.add_argument("-q", "--quiet",
                                   action = "count",
                                   default = 0,
                                   help = quiet_help)

    if enable_debugging_mode is True:
        what_logging_opts.add_argument("-v", "--verbosity",
                                       action = "count",
                                       default = 0,
                                       help = verbose_help)
        what_logging_opts.add_argument("--loglevel",
                                       choices = ["debug","info","warning",
                                                "error","critical","DEBUG",
                                                "INFO","WARNING","ERROR",
                                                "CRITICAL"],
                                       help = loglevel_help)
        what_logging_opts.add_argument('--debug',
                                       action = 'store_true',
                                       help = debug_help)

    parser_what.set_defaults(func = gaze_what)


    #-------------------------------------------
    #
    # create the parser for the "short" command
    #
    #-------------------------------------------
    parser_short = subparsers.add_parser('short',
                                         help = 'Display spell short description (Not Working)')
    parser_short.add_argument('spell',
                              nargs = '+',
                              help='Display System Info')
    parser_short.add_argument('-g','--grimoire',
                              nargs = '+',
                              help = 'Specify which grimoire(s) to look in.')
    parser_short.add_argument("-q", "--quiet",
                              action = "count",
                              default = 0,
                              help = quiet_help)
    
    if enable_debugging_mode is True:
        parser_short.add_argument("-v", "--verbosity",
                                  action = "count",
                                  default = 0,
                                  help = verbose_help)
        parser_short.add_argument("--loglevel",
                                  choices = ["debug","info","warning",
                                           "error","critical","DEBUG",
                                           "INFO","WARNING","ERROR",
                                           "CRITICAL"],
                                  help = loglevel_help)
        parser_short.add_argument('--debug',
                                  action = 'store_true',
                                  help = debug_help)

    parser_short.set_defaults(func = gaze_short)


    #-------------------------------------------
    #
    # create the parser for the "where" command
    #
    #-------------------------------------------
    parser_where = subparsers.add_parser('where',
                                         help = 'Display the section a spell belongs to.')


    where_logging_opts = parser_where.add_argument_group('Logging Options')


    parser_where.add_argument('spell',
                             nargs = '+',
                             help = 'Spell(s) to display')
    parser_where.add_argument('-p','-path', '--path',
                             action = 'store_true',
                             help = 'Display the full path to spell')
    parser_where.add_argument('-g','--grimoire',
                              nargs = '+',
                              help = 'specify which grimoire(s) to look in.')
    where_logging_opts.add_argument("-q", "--quiety",
                              action = "count",
                              default = 0,
                              help = quiet_help)

    if enable_debugging_mode is True:
        where_logging_opts.add_argument("-v", "--verbosity",
                                        action = "count",
                                        default = 0,
                                        help = verbose_help)
        where_logging_opts.add_argument("--loglevel",
                                        choices = ["debug","info","warning",
                                                 "error","critical","DEBUG",
                                                 "INFO","WARNING","ERROR",
                                                 "CRITICAL"],
                                        help = loglevel_help)
        where_logging_opts.add_argument('--debug',
                                        action = 'store_true',
                                        help = debug_help)
        
    parser_where.set_defaults(func = gaze_where)


    #-------------------------------------------
    #
    # create the parser for the "url" command
    #
    #-------------------------------------------
    parser_url = subparsers.add_parser('url',
                                       aliases = ('website',),
                                       help = 'Display spell homepage')

    
    url_logging_opts = parser_url.add_argument_group('Logging Options')


    parser_url.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_url.add_argument('-g','--grimoire',
                            nargs = '+',
                            help = 'Specify which grimoire(s) to look in.')
    url_logging_opts.add_argument("-q", "--quiet",
                                  action = "count",
                                  default = 0,
                                  help = quiet_help)

    if enable_debugging_mode is True:
        url_logging_opts.add_argument("-v", "--verbosity",
                                      action = "count",
                                      default = 0,
                                      help = verbose_help)
        url_logging_opts.add_argument("--loglevel",
                                      choices = ["debug","info","warning",
                                               "error","critical","DEBUG",
                                               "INFO","WARNING","ERROR",
                                               "CRITICAL"],
                                      help = loglevel_help)
        url_logging_opts.add_argument('--debug',
                                      action = 'store_true',
                                      help = debug_help)

    parser_url.set_defaults(func = gaze_url)

    
    #-------------------------------------------
    #
    # create the parser for the "sources" command
    #
    #-------------------------------------------
    parser_sources = subparsers.add_parser('sources',
                                           help = 'List all source files contained in a spell. (Not Working)')


    sources_logging_opts = parser_sources.add_argument_group('Logging Options')


    parser_sources.add_argument('spell',
                                nargs = '+',
                                help = 'Display System Info')
    parser_sources.add_argument('-g','--grimoire',
                                nargs = '+',
                                help = 'specify which grimoire(s) to look in.')
    sources_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = quiet_help)
    
    if enable_debugging_mode is True:
        sources_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        sources_logging_opts.add_argument("--loglevel",
                                          choices=["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        sources_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_sources.set_defaults(func = gaze_sources)


        #-------------------------------------------
        #
        # create the parser for the "source_urls" command
        #
        #-------------------------------------------
    parser_source_url = subparsers.add_parser('source_urls',
                                              help = 'Lists the urls to all files contained in a spell. (Not Working)')


    source_url_logging_opts = parser_source_url.add_argument_group('Logging Options')


    parser_source_url.add_argument('spell',
                                   nargs = '+',
                                   help = 'Spell')
    parser_source_url.add_argument('-g','--grimoire',
                                   nargs = '+',
                                   help = 'specify which grimoire(s) to look in.')
    source_url_logging_opts.add_argument("-q", "--quiet",
                                         action = "count",
                                         default = 0,
                                         help = quiet_help)

    if enable_debugging_mode is True:
        source_url_logging_opts.add_argument("-v", "--verbosity",
                                             action = "count",
                                             default = 0,
                                             help = verbose_help)
        source_url_logging_opts.add_argument("--loglevel",
                                             choices = ["debug","info","warning",
                                                      "error","critical","DEBUG",
                                                      "INFO","WARNING","ERROR",
                                                      "CRITICAL"],
                                             help = loglevel_help)
        source_url_logging_opts.add_argument('--debug',
                                             action = 'store_true',
                                             help = debug_help)
        
    parser_source_url.set_defaults(func = gaze_source_urls)


    #-------------------------------------------
    #
    # create the parser for the "maintainer" command
    #
    #-------------------------------------------
    parser_maintainer = subparsers.add_parser('maintainer',
                                              help = 'Display the email address of the person responsible for maintaining a specified spell. (Not Working)')


    maintainer_logging_opts = parser_maintainer.add_argument_group('Logging Options')


    parser_maintainer.add_argument('spell',
                                   nargs = '+',
                                   help = 'Spell')
    parser_maintainer.add_argument('-g','--grimoire',
                                   nargs = '+',
                                   help = 'specify which grimoire(s) to look in.')
    maintainer_logging_opts.add_argument("-q", "--quiet",
                                         action = "count",
                                         default = 0,
                                         help = quiet_help)

    if enable_debugging_mode is True:
        maintainer_logging_opts.add_argument("-v", "--verbosity",
                                             action = "count",
                                             default = 0,
                                             help = verbose_help)
        maintainer_logging_opts.add_argument("--loglevel",
                                             choices = ["debug","info","warning",
                                                      "error","critical","DEBUG",
                                                      "INFO","WARNING","ERROR",
                                                      "CRITICAL"],
                                             help = loglevel_help)
        maintainer_logging_opts.add_argument('--debug',
                                             action = 'store_true',
                                             help = debug_help)
        
    parser_maintainer.set_defaults(func = gaze_maintainer)


    #-------------------------------------------
    #
    # create the parser for the "compile" command
    #
    #-------------------------------------------
    parser_compile = subparsers.add_parser('compile',
                                           help = 'Show the compiler output generated when the spell was built.  If no optional version was given, try the installed version.  If the spell is not installed use the version in the grimoire. (Not Working)')

    #
    compile_logging_opts = parser_compile.add_argument_group('Logging Options')

    #
    parser_compile.add_argument('spell',
                                nargs = 1,
                                help = 'Spell')
    parser_compile.add_argument('version',
                                nargs = '?',
                                help = 'Specifies which Version of spell to view.')
    compile_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = quiet_help)


    if enable_debugging_mode is True:
        compile_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        compile_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        compile_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_compile.set_defaults(func = gaze_compile)


    #-------------------------------------------
    #
    # create the parser for the "install" command
    #
    #-------------------------------------------
    parser_install = subparsers.add_parser('install',
                                           help = 'Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files. If no optional version was given, try the installed version. (Not Working)')


    install_logging_opts = parser_install.add_argument_group('Logging Options')


    parser_install.add_argument('spell',
                                nargs = 1,
                                help = 'Spell')
    parser_install.add_argument('version',
                                nargs = 1,
                                help = 'Specifies which version of spell to view')
    install_logging_opts.add_argument("-q", "--quiet",
                                action = "count",
                                default = 0,
                                help = quiet_help)

    if enable_debugging_mode is True:
        install_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)        
        install_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        install_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_install.set_defaults(func = gaze_install,
                                install_display = False)


    #-------------------------------------------
    #
    # create the parser for the "install-full" command
    #
    #-------------------------------------------
    parser_install_full = subparsers.add_parser('install-full',
                                                help = 'Used to determine what files were installed by a spell and where those files are located.  If no optional version was given, try the installed version.  (Not Working)')

    #
    install_full_logging_opts = parser_install_full.add_argument_group('Logging Options')

    #
    parser_install_full.add_argument('spell',
                                     nargs = 1,
                                     help = 'Spell')
    parser_install_full.add_argument('version',
                                     nargs = 1,
                                     help = 'Specifies which version of the spell to view.')
    install_full_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                           help = quiet_help)

    if enable_debugging_mode is True:
        install_full_logging_opts.add_argument("-v", "--verbosity",
                                               action = "count",
                                               default = 0,
                                               help = verbose_help)
        install_full_logging_opts.add_argument("--loglevel",
                                               choices = ["debug","info","warning",
                                                        "error","critical","DEBUG",
                                                        "INFO","WARNING","ERROR",
                                                        "CRITICAL"],
                                               help = loglevel_help)
        install_full_logging_opts.add_argument('--debug',
                                               action = 'store_true',
                                               help = debug_help)
        
    parser_install_full.set_defaults(func = gaze_install,
                                     install_display = 'Full')


    #-------------------------------------------
    #
    # create the parser for the "install-spell" command
    #
    #-------------------------------------------
    parser_install_spell = subparsers.add_parser('install-spell',
                                                 help = 'Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files and sorcery log files.  If no optional version was given, try the installed version. (Not Working)')


    install_spell_logging_opts = parser_install_spell.add_argument_group('Logging Options')


    parser_install_spell.add_argument('spell',
                                      nargs = 1,
                                      help = 'Spell')
    parser_install_spell.add_argument('version',
                                      nargs = 1,
                                      help = 'Specifies which version of the spell to view')
    install_spell_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                            help = quiet_help)

    if enable_debugging_mode is True:
        install_spell_logging_opts.add_argument("-v", "--verbosity",
                                                action = "count",
                                                default = 0,
                                                help = verbose_help)
        install_spell_logging_opts.add_argument("--loglevel",
                                                choices = ["debug","info","warning",
                                                         "error","critical","DEBUG",
                                                         "INFO","WARNING","ERROR",
                                                         "CRITICAL"],
                                                help = loglevel_help)
        install_spell_logging_opts.add_argument('--debug',
                                                action = 'store_true',
                                                help = debug_help)
        
    parser_install_spell.set_defaults(func = gaze_install,
                                      install_display = 'Spell')


    #-------------------------------------------
    #
    # create the parser for the "version" command
    #
    #-------------------------------------------
    parser_version = subparsers.add_parser('version',
                                           help = 'Shows the installed version of the spell and the main grimoires version.')


    version_logging_opts = parser_version.add_argument_group('Logging Options')


    parser_version.add_argument('spell',
                                nargs = 1,
                                help = 'Display System Info')
    parser_version.add_argument('-g','--grimoire',
                                nargs = '+',
                                help = 'specify which grimoire(s) to look in.')
    version_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = quiet_help)

    if enable_debugging_mode is True:
        version_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        version_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        version_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_version.set_defaults(func = gaze_version,
                                multi = False)


    #-------------------------------------------
    #
    # create the parser for the "versions" command
    #
    #-------------------------------------------
    parser_versions = subparsers.add_parser('versions',
                                            help = 'Shows the installed version of the spell and lists all available versions in all grimoires. If used without a spell name, then lists order of available grimoires.')

    #
    versions_logging_opts = parser_versions.add_argument_group('Logging Options')

    #
    parser_versions.add_argument('spell',
                                 nargs = 1,
                                 help = 'Display System Info')
    versions_logging_opts.add_argument("-q", "--quiet",
                                 action = "count",
                                 default = 0,
                                       help = quiet_help)

    if enable_debugging_mode is True:
        versions_logging_opts.add_argument("-v", "--verbosity",
                                           action = "count",
                                           default = 0,
                                           help = verbose_help)
        versions_logging_opts.add_argument("--loglevel",
                                           choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                           help = loglevel_help)
        versions_logging_opts.add_argument('--debug',
                                           action = 'store_true',
                                           help = debug_help)
        
    parser_versions.set_defaults(func = gaze_version,
                                 multi = True)


    #-------------------------------------------
    #
    # create the parser for the "license" command
    #
    #-------------------------------------------
    parser_license = subparsers.add_parser('license',
                                           help = 'View the license(s) of the given spell(s), or spells in given section(s), or view the information about given license(s) (Not Working)')

    #
    license_logging_opts = parser_license.add_argument_group('Logging Options')

    #
    parser_license.add_argument('ssl',
                                nargs = '+',
                                help = 'Specify Spell, Section, or License to view')
    parser_license.add_argument('-g','--grimoire',
                                nargs = '+',
                                help = 'specify which grimoire(s) to look in.')
    license_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = debug_help)

    if enable_debugging_mode is True:
        license_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        license_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        license_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_license.set_defaults(func = gaze_license)


    #-------------------------------------------
    #
    # create the parser for the "versions" command
    #
    #-------------------------------------------
    parser_sum = subparsers.add_parser('sum',
                                       help = 'Print CRC checksums for spells(s). If no spell is given it default to all. (Not Working)')


    sum_logging_opts = parser_sum.add_argument_group('Logging Options')


    parser_sum.add_argument('spell',
                            nargs = '?',
                            help = 'Display System Info')
    sum_logging_opts.add_argument("-q", "--quiet",
                            action = "count",
                            default = 0,
                                  help = quiet_help)

    if enable_debugging_mode is True:
        sum_logging_opts.add_argument("-v", "--verbosity",
                                      action = "count",
                                      default = 0,
                                      help = verbose_help)
        sum_logging_opts.add_argument("--loglevel",
                                      choices = ["debug","info","warning",
                                               "error","critical","DEBUG",
                                               "INFO","WARNING","ERROR",
                                               "CRITICAL"],
                                      help = loglevel_help)
        sum_logging_opts.add_argument('--debug',
                                      action = 'store_true',
                                      help = debug_help)
        
    parser_sum.set_defaults(func = gaze_checksum,
                            check_type = 'CRC')


    #-------------------------------------------
    #
    # create the parser for the "md5sum" command
    #
    #-------------------------------------------
    parser_md5sum = subparsers.add_parser('md5sum',
                                          help = 'Print spell MD5 message digests (fingerprints). If no spell is given it default to all (Not Working)')


    md5sum_logging_opts = parser_md5sum.add_argument_group('Logging Options')


    parser_md5sum.add_argument('spell',
                               nargs = '?',
                               help = 'Display System Info')
    md5sum_logging_opts.add_argument("-q", "--quiet",
                               action = "count",
                               default = 0,
                                     help = quiet_help)

    if enable_debugging_mode is True:
        md5sum_logging_opts.add_argument("-v", "--verbosity",
                                         action = "count",
                                         default = 0,
                                         help = verbose_help)
        md5sum_logging_opts.add_argument("--loglevel",
                                         choices = ["debug","info","warning",
                                                  "error","critical","DEBUG",
                                                  "INFO","WARNING","ERROR",
                                                  "CRITICAL"],
                                         help = loglevel_help)
        md5sum_logging_opts.add_argument('--debug',
                                         action = 'store_true',
                                         help = debug_help)
        
    parser_md5sum.set_defaults(func = gaze_checksum,
                               check_type = 'MD5')


    #-------------------------------------------
    #
    # create the parser for the "size" command
    #
    #-------------------------------------------
    parser_size = subparsers.add_parser('size',
                                        help = 'print the sizes and file counts of the passed installed spell(s). (Not Working)')


    size_logging_opts = parser_size.add_argument_group('Logging Options')


    parser_size.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_size.add_argument('-a','-all','--all',
                             action = 'store_true',
                             help = 'Display sizes of all the spells. In addition, this will print the largest spell.')
    size_logging_opts.add_argument("-q", "--quiet",
                             action = "count",
                             default = 0,
                                   help = quiet_help)

    if enable_debugging_mode is True:
        size_logging_opts.add_argument("-v", "--verbosity",
                                       action = "count",
                                       default = 0,
                                       help = verbose_help)
        size_logging_opts.add_argument("--loglevel",
                                       choices = ["debug","info","warning",
                                                  "error","critical","DEBUG",
                                                  "INFO","WARNING","ERROR",
                                                  "CRITICAL"],
                                       help = loglevel_help)
        size_logging_opts.add_argument('--debug',
                                       action = 'store_true',
                                       help = debug_help)
        
    parser_size.set_defaults(func = gaze_size)


    #-------------------------------------------
    #
    # create the parser for the "export" command
    #
    #-------------------------------------------
    parser_export = subparsers.add_parser('export',
                                          help = 'Take a snapshot of all currently installed spells and their configuration. (Not Working)')


    export_logging_opts = parser_export.add_argument_group('Logging Options')


    export_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                     help = quiet_help)

    if enable_debugging_mode is True:
        export_logging_opts.add_argument("-v", "--verbosity",
                                         action = "count",
                                         default = 0,
                                         help = verbose_help)
        export_logging_opts.add_argument("--loglevel",
                                         choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                         help = loglevel_help)
        export_logging_opts.add_argument('--debug',
                                         action = 'store_true',
                                         help = debug_help)
        
    parser_export.set_defaults(func = gaze_export)


    #-------------------------------------------
    #
    # create the parser for the "import" command
    #
    #-------------------------------------------
    parser_import = subparsers.add_parser('import',
                                          help = 'restore the snapshot from a previous "gaze export" command (see above). (Not Working)')


    import_logging_opts = parser_import.add_argument_group('Logging Options')


    parser_import.add_argument('snapshot',
                               nargs = 1,
                               help = 'Display System Info')
    parser_import.add_argument('--depreciated',
                               action = 'store_true',
                               help = 'Use the old behaviour.  An old cache is expected. There is no significant problem if an old cache is restored with the new importer. A few files will be ignored - only the files that the new exporter saves are considered - and the queuing logic wille be slighty more agressive.')
    import_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                     help = quiet_help)
    
    if enable_debugging_mode is True:
        import_logging_opts.add_argument("-v", "--verbosity",
                                         action = "count",
                                         default = 0,
                                         help = verbose_help)
        import_logging_opts.add_argument("--loglevel",
                                         choices = ["debug","info","warning",
                                                  "error","critical","DEBUG",
                                                  "INFO","WARNING","ERROR",
                                                  "CRITICAL"],
                                         help = loglevel_help)
        import_logging_opts.add_argument('--debug',
                                         action = 'store_true',
                                         help = debug_help)
        
    parser_import.set_defaults(func = gaze_import)


    #-------------------------------------------
    #
    # create the parser for the "grimoire" command
    #
    #-------------------------------------------
    parser_grimoire = subparsers.add_parser('grimoire',
                                            help = "Prints specified grimoire's spells or all grimoires if grimoire-name is omitted (Not Working)")

    
    grimoire_logging_opts = parser_grimoire.add_argument_group('Logging Options')


    parser_grimoire.add_argument('grimoire',
                                 nargs = '*',
                                 help = 'Specify grimoire to view')
    grimoire_logging_opts.add_argument("-q", "--quiet",
                                 action = "count",
                                 default = 0,
                                       help = quiet_help)
    
    if enable_debugging_mode is True:
        grimoire_logging_opts.add_argument("-v", "--verbosity",
                                           action = "count",
                                           default = 0,
                                           help = verbose_help)
        grimoire_logging_opts.add_argument("--loglevel",
                                           choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                           help = loglevel_help)
        grimoire_logging_opts.add_argument('--debug',
                                           action = 'store_true',
                                           help = debug_help)
        
    parser_grimoire.set_defaults(func = gaze_grimoire,
                                 multi = False,
                                 display_format = 'console')


    # create the parser for the "grimoires" command
    parser_grimoires = subparsers.add_parser('grimoires',
                                             help = 'Display installed grimoires by name only. (Not Working)')


    grimoires_logging_opts = parser_grimoires.add_argument_group('Logging Options')


    grimoires_logging_opts.add_argument("-q", "--quiet",
                                        action = "count",
                                        default = 0,
                                        help = quiet_help)
    
    if enable_debugging_mode is True:
        grimoires_logging_opts.add_argument("-v", "--verbosity",
                                            action = "count",
                                            default = 0,
                                            help = verbose_help)
        grimoires_logging_opts.add_argument("--loglevel",
                                            choices = ["debug","info","warning",
                                                     "error","critical","DEBUG",
                                                     "INFO","WARNING","ERROR",
                                                     "CRITICAL"],
                                            help = loglevel_help)
        grimoires_logging_opts.add_argument('--debug',
                                            action = 'store_true',
                                            help = debug_help)
        
    parser_grimoires.set_defaults(func = gaze_grimoire,
                                  multi = True,
                                  display_format = 'console')


    #-------------------------------------------
    #
    # create the parser for the "html" command
    #
    #-------------------------------------------
    parser_html = subparsers.add_parser('html',
                                        help = 'Prints the specified grimoire or all grimoires if grimoire-name is omitted in a nice html format. (Not Working)')

    
    html_logging_opts = parser_html.add_argument_group('Logging Options')

    
    parser_html.add_argument('grimoire',
                             nargs = '*',
                             help = 'Specified grimoire(s)')
    parser_html.add_argument('-s','--source',
                             action = 'store_true',
                             help = 'Displays links to the source files.')
    html_logging_opts.add_argument("-q", "--quiet",
                             action = "count",
                             default = 0,
                                   help = quiet_help)
    
    if enable_debugging_mode is True:
        html_logging_opts.add_argument("-v", "--verbosity",
                                       action = "count",
                                       default = 0,
                                       help = verbose_help)
        html_logging_opts.add_argument("--loglevel",
                                       choices = ["debug","info","warning",
                                                "error","critical","DEBUG",
                                                "INFO","WARNING","ERROR",
                                                "CRITICAL"],
                                       help = loglevel_help)
        html_logging_opts.add_argument('--debug',
                                       action = 'store_true',
                                       help = debug_help)
        
    parser_html.set_defaults(func = gaze_grimoire,
                             multi = False,
                             display_format = 'html')

    
    #-------------------------------------------
    #
    # create the parser for the "search" command
    #
    #-------------------------------------------
    parser_search = subparsers.add_parser('search',
                                          help = 'Searches spells name, short description and long description for phrase (Not Working)')

    #
    search_logging_opts = parser_search.add_argument_group('Logging Options')

    #
    # Need to make the following mutually exclusive
    parser_search.add_argument('-n','-name','--name',
                             action = 'store_true',
                             help = 'Only search spells name')
    parser_search.add_argument('-s','-short','--short',
                             action = 'store_true',
                             help = 'Only search spells short description')

    #
    parser_search.add_argument('phrase',
                               nargs = 1,
                               help = "Any valid extended regular expression. For optimal results, don't forget to escape any special characters and use quotes to protect the expression.")
    parser_search.add_argument('-g','--grimoire',
                               nargs = '+',
                               help = 'specify which grimoire(s) to look in.')
    search_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                     help = quiet_help)

    if enable_debugging_mode is True:
        search_logging_opts.add_argument("-v", "--verbosity",
                                         action = "count",
                                         default = 0,
                                         help = verbose_help)
        search_logging_opts.add_argument("--loglevel",
                                         choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                         help = loglevel_help)
        search_logging_opts.add_argument('--debug',
                                         action = 'store_true',
                                         help = debug_help)
        
    parser_search.set_defaults(func = gaze_search)


    #-------------------------------------------
    #
    # create the parser for the "newer" command
    #
    #-------------------------------------------
    parser_newer = subparsers.add_parser('newer',
                                         help = "Print packages first submitted after a specified date. (Not Working)")

    
    newer_logging_opts = parser_newer.add_argument_group('Logging Options')


    parser_newer.add_argument('date',
                              nargs = '?',
                              default = 'last_sorcery_update',
                              help = "Specify Date.  The date must be in the 'yyyymmdd' format, where y = year, m = month, and d = day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_newer.add_argument('-g','--grimoire',
                              nargs = '+',
                              help = 'specify which grimoire(s) to look in.')
    newer_logging_opts.add_argument("-q", "--quiet",
                                    action = "count",
                                    default = 0,
                                    help = quiet_help)

    if enable_debugging_mode is True:
        newer_logging_opts.add_argument("-v", "--verbosity",
                                        action = "count",
                                        default = 0,
                                        help = verbose_help)
        newer_logging_opts.add_argument("--loglevel",
                                        choices = ["debug","info","warning",
                                                 "error","critical","DEBUG",
                                                 "INFO","WARNING","ERROR",
                                                 "CRITICAL"],
                                        help = loglevel_help)
        newer_logging_opts.add_argument('--debug',
                                        action = 'store_true',
                                        help = debug_help)
        
    parser_newer.set_defaults(func = gaze_newer)


    #-------------------------------------------
    #
    # create the parser for the "older" command
    #
    #-------------------------------------------
    parser_older = subparsers.add_parser('older',
                                         help = 'print packages that were first submitted before a specified date. (Not Working)')

    #
    older_logging_opts = parser_older.add_argument_group('Logging Options')

    #
    parser_older.add_argument('date',
                              nargs = '?',
                              help = "Specify Date.  The date must be in the 'yyyymmdd' format, where y = year, m = month, and d = day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_older.add_argument('-g','--grimoire',
                               nargs = '+',
                               help = 'specify which grimoire(s) to look in.')
    older_logging_opts.add_argument("-q", "--quiet",
                                    action = "count",
                                    default = 0,
                                    help = quiet_help)

    if enable_debugging_mode is True:
        older_logging_opts.add_argument("-v", "--verbosity",
                                        action = "count",
                                        default = 0,
                                        help = verbose_help)
        older_logging_opts.add_argument("--loglevel",
                                        choices = ["debug","info","warning",
                                                 "error","critical","DEBUG",
                                                 "INFO","WARNING","ERROR",
                                                 "CRITICAL"],
                                        help = loglevel_help)
        older_logging_opts.add_argument('--debug',
                                        action = 'store_true',
                                        help = debug_help)
        
    parser_older.set_defaults(func = gaze_older)


    #-------------------------------------------
    #
    # create the parser for the "from" command
    #
    #-------------------------------------------
    parser_from = subparsers.add_parser('from',
                                        help = "find out which spell has installed 'path/file.'  Matching is done literally against the end of the path names in the lists of installed files. (Not Working)")

    
    from_logging_opts = parser_from.add_argument_group('Logging Options')

    
    parser_from.add_argument('filename',
                             nargs = 1,
                             help = 'Display System Info')
    parser_from.add_argument('-r','-regex','--regex',
                             action = 'store_true',
                             help = 'Matching using basic regular expressions against the whole paths in the lists of installed files.')
    from_logging_opts.add_argument("-q", "--quiet",
                             action = "count",
                             default = 0,
                             help = quiet_help)
    if enable_debugging_mode is True:
        from_logging_opts.add_argument("-v", "--verbosity",
                                       action = "count",
                                       default = 0,
                                       help = verbose_help)
        from_logging_opts.add_argument("--loglevel",
                                       choices = ["debug","info","warning",
                                                "error","critical","DEBUG",
                                                "INFO","WARNING","ERROR",
                                                "CRITICAL"],
                                       help = loglevel_help)
        from_logging_opts.add_argument('--debug',
                                       action = 'store_true',
                                       help = debug_help)
        
    parser_from.set_defaults(func = gaze_from)



    #-------------------------------------------
    #
    # create the parser for the "installed" command
    #
    #-------------------------------------------
    parser_installed = subparsers.add_parser('installed',
                                             help = 'View all installed packages and corresponding version numbers (Not Working)')

    
    installed_logging_opts = parser_installed.add_argument_group('Logging Options')


    parser_installed.add_argument('spell',
                                  nargs = '*',
                                  help = 'Check to see whether a particular package is installed and if it is installed display its version number')
    installed_logging_opts.add_argument("-q", "--quiet",
                                  action = "count",
                                  default = 0,
                                  help = quiet_help)

    if enable_debugging_mode is True:
        installed_logging_opts.add_argument("-v", "--verbosity",
                                            action = "count",
                                            default = 0,
                                            help = verbose_help)
        installed_logging_opts.add_argument("--loglevel",
                                            choices = ["debug","info","warning",
                                                     "error","critical","DEBUG",
                                                     "INFO","WARNING","ERROR",
                                                     "CRITICAL"],
                                            help = loglevel_help)
        installed_logging_opts.add_argument('--debug',
                                            action = 'store_true',
                                            help = debug_help)
        
    parser_installed.set_defaults(func = gaze_installed)


    #-------------------------------------------
    #
    # create the parser for the "section" command
    #
    #-------------------------------------------
    parser_section = subparsers.add_parser('section',
                                           help = 'View a list of all sections in the software catalogue or display a list of packages from a specific section. (Not Working)')

    
    section_logging_opts = parser_section.add_argument_group('Logging Options')


    parser_section.add_argument('section',
                                nargs = '?',
                                help = 'Display System Info')
    parser_section.add_argument('-g','--grimoire',
                                nargs = '+',
                                help = 'specify which grimoire(s) to look in.')
    section_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help=quiet_help)

    if enable_debugging_mode is True:
        section_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        section_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        section_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_section.set_defaults(func = gaze_section)


    #-------------------------------------------
    #
    # create the parser for the "voyeur" command
    #
    #-------------------------------------------
    parser_voyeur = subparsers.add_parser('voyeur',
                                          help = 'start looking at what cast is compiling at the moment and outputs its compiler messages. A spell can be optionally specified, or a delay after which to abort when no casts could be found. (Not Working)')

    
    voyeur_logging_opts = parser_voyeur.add_argument_group('Logging Options')


    parser_voyeur.add_argument('spell',
                               nargs = '?',
                               help = 'Display System Info')
    voyeur_logging_opts.add_argument("-q", "--quiet",
                               action = "count",
                               default = 0,
                                     help = quiet_help)

    if enable_debugging_mode is True:
        voyeur_logging_opts.add_argument("-v", "--verbosity",
                                         action = "count",
                                         default = 0,
                                         help = verbose_help)
        voyeur_logging_opts.add_argument("--loglevel",
                                         choices = ["debug","info","warning",
                                                  "error","critical","DEBUG",
                                                  "INFO","WARNING","ERROR",
                                                  "CRITICAL"],
                                         help = loglevel_help)
        voyeur_logging_opts.add_argument('--debug',
                                         action = 'store_true',
                                         help = debug_help)
        
    parser_voyeur.set_defaults(func = gaze_voyeur)


    #-------------------------------------------
    #
    # create the parser for the "history" command
    #
    #-------------------------------------------
    parser_history = subparsers.add_parser('history',
                                           help = 'Show history for a spell (alias for gaze HISTORY). (Not Working)')

    
    history_logging_opts = parser_history.add_argument_group('Logging Options')


    parser_history.add_argument('spell',
                                nargs = 1,
                                help = 'Display System Info')
    parser_history.add_argument('-g','--grimoire',
                                nargs = '+',
                                help = 'specify which grimoire(s) to look in.')
    history_logging_opts.add_argument("-q", "--quiet",
                                      action = "count",
                                      default = 0,
                                      help = quiet_help)

    if enable_debugging_mode is True:
        history_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        history_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                     "error","critical","DEBUG",
                                                     "INFO","WARNING","ERROR",
                                                     "CRITICAL"],
                                          help = loglevel_help)
        history_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = debug_help)
        
    parser_history.set_defaults(func = gaze_file,
                                filename = 'HISTORY')


    #-------------------------------------------
    #
    # create the parser for the "checkmd5s" command
    #
    #-------------------------------------------
    parser_checkmd5s = subparsers.add_parser('checkmd5s',
                                             help = 'Computes the md5sum on spell sources based on passed spell(s), section(s) or entire grimoire(s) if left blank. (Not Working)')

    
    checkmd5_logging_opts = parser_checkmd5s.add_argument_group('Logging Parser')


    parser_checkmd5s.add_argument('spell',
                                  nargs = '*',
                                  help = 'Display System Info')
    parser_checkmd5s.add_argument('-g','--grimoire',
                                  nargs = '+',
                                  help = 'specify which grimoire(s) to look in.')
    checkmd5_logging_opts.add_argument("-q", "--quiet",
                                       action = "count",
                                       default = 0,
                                       help = quiet_help)

    if enable_debugging_mode is True:
        checkmd5_logging_opts.add_argument("-v", "--verbosity",
                                           action = "count",
                                           default = 0,
                                           help = verbose_help)
        checkmd5_logging_opts.add_argument("--loglevel",
                                           choices = ["debug","info","warning",
                                                    "error","critical","DEBUG",
                                                    "INFO","WARNING","ERROR",
                                                    "CRITICAL"],
                                           help = loglevel_help)
        checkmd5_logging_opts.add_argument('--debug',
                                           action = 'store_true',
                                           help = debug_help)

    parser_checkmd5s.set_defaults(func = gaze_checksum,
                                  filename = 'checksum')


    #-------------------------------------------
    #
    # create the parser for the "depends" command
    #
    #-------------------------------------------
    parser_depends = subparsers.add_parser('depends',
                                           help = 'shows the spells that explicitly or recursively depend on this installed spell.  Only enabled dependencies are shown. (Not Working)')

    
    depends_logging_opts = parser_depends.add_argument_group('Logging Options')


    parser_depends.add_argument('spell',
                                nargs = 1,
                                help = 'Display System Info')
    parser_depends.add_argument('level',
                                nargs = '?',
                                help='Up to level $level if specified')
    parser_depends.add_argument('--fast',
                                action = 'store_true',
                                help = 'Limit output, but runs much faster.')
    parser_depends.add_argument('--required',
                                action = 'store_true',
                                help = 'Show only the required dependencies and skip the runtime dependencies.')
    depends_logging_opts.add_argument("-q", "--quiet",
                                action = "count",
                                default = 0,
                                      help = quiet_help)

    if enable_debugging_mode is True:
        depends_logging_opts.add_argument("-v", "--verbosity",
                                          action = "count",
                                          default = 0,
                                          help = verbose_help)
        depends_logging_opts.add_argument("--loglevel",
                                          choices = ["debug","info","warning",
                                                   "error","critical","DEBUG",
                                                   "INFO","WARNING","ERROR",
                                                   "CRITICAL"],
                                          help = loglevel_help)
        depends_logging_opts.add_argument('--debug',
                                          action = 'store_true',
                                          help = quiet_help)
        
    parser_depends.set_defaults(func = gaze_depends)


    #-------------------------------------------
    #
    # create the parser for the "dependencies" command
    #
    #-------------------------------------------
    parser_dependencies = subparsers.add_parser('dependencies',
                                                help = 'shows the spells that spell explicitly or recursively depends on. (Not Working)')


    dependencies_logging_opts = parser_dependencies.add_argument_group('Logging Options')


    parser_dependencies.add_argument('spell',
                                     nargs = 1,
                                     help = 'Display System Info')
    parser_dependencies.add_argument('level',
                                     nargs = '?',
                                     help = 'Up to level $level if specified.')
    parser_dependencies.add_argument('-c',
                                     action = 'store_true',
                                     help = 'skips trees that have already been shown')
    parser_dependencies.add_argument('--no-optionals',
                                     action = 'store_true',
                                     help = 'skips optional dependencies.')
    dependencies_logging_opts.add_argument("-q", "--quiet",
                                     action = "count",
                                     default = 0,
                                           help = quiet_help)
    
    if enable_debugging_mode is True:
        dependencies_logging_opts.add_argument("-v", "--verbosity",
                                               action = "count",
                                               default = 0,
                                               help = verbose_help)
        dependencies_logging_opts.add_argument("--loglevel",
                                               choices = ["debug","info","warning",
                                                        "error","critical","DEBUG",
                                                        "INFO","WARNING","ERROR",
                                                        "CRITICAL"],
                                               help = loglevel_help)
        dependencies_logging_opts.add_argument('--debug',
                                               action = 'store_true',
                                               help = debug_help)

    parser_dependencies.set_defaults(func = gaze_dependencies)

    
    #-------------------------------------------
    #
    # create the parser for the "time" command
    #
    #-------------------------------------------
    parser_time = subparsers.add_parser('time',
                                        help = 'Shows the time the spell(s) needed to get cast. By default the last casting time is shown, alternatively the median, mean or weighted mean can be shown.  If more then one spell is specified, also a total time is shown. (Not Working)')
    time_logging_opts = parser_time.add_argument_group('Logging Options')
    parser_time.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_time.add_argument('-g','--grimoire',
                             nargs = '+',
                             help = 'specify which grimoire(s) to look in.')
    parser_time.add_argument('--last',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time.add_argument('--medium',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time.add_argument('--mean',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time.add_argument('--weight-last',
                             action = 'store_true',
                             help = 'Give more weight to the last casting time.')
    parser_time.add_argument('--full',
                             action = 'store_true',
                             help = 'Display System Info')
    time_logging_opts.add_argument("-q", "--quiet",
                             action = "count",
                             default = 0,
                             help = quiet_help)
    if enable_debugging_mode is True:
        time_logging_opts.add_argument("-v", "--verbosity",
                                       action = "count",
                                       default = 0,
                                       help = verbose_help)
        time_logging_opts.add_argument("--loglevel",
                                       choices = ["debug","info","warning",
                                                "error","critical","DEBUG",
                                                "INFO","WARNING","ERROR",
                                                "CRITICAL"],
                                       help = loglevel_help)
        time_logging_opts.add_argument('--debug',
                                       action = 'store_true',
                                       help = debug_help)
        
    parser_time.set_defaults(func = gaze_time,
                             system = False)

    #-------------------------------------------
    #
    # create the parser for the "time-system" command
    #
    #-------------------------------------------
    parser_time_system = subparsers.add_parser('time-system',
                                               help = 'Shows the time the whole system needed to get cast. (Not Working)')


    time_system_logging_opts = parser_time_system.add_argument_group('Logging Options')


    parser_time_system.add_argument('--no-orphans',
                             action = 'store_true',
                             help = 'Skip orphaned spells.')
    parser_time_system.add_argument('--last',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time_system.add_argument('--medium',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time_system.add_argument('--mean',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time_system.add_argument('--weight-last',
                             action = 'store_true',
                             help = 'Display System Info')
    parser_time_system.add_argument('--full',
                             action = 'store_true',
                             help = 'Display System Info')
    time_system_logging_opts.add_argument("-q", "--quiet",
                                    action = "count",
                                    default = 0,
                                    help = quiet_help)
    if enable_debugging_mode is True:
        time_system_logging_opts.add_argument("-v", "--verbosity",
                                              action = "count",
                                              default = 0,
                                              help = verbose_help)
        time_system_logging_opts.add_argument("--loglevel",
                                              choices = ["debug","info","warning",
                                                       "error","critical","DEBUG",
                                                       "INFO","WARNING","ERROR",
                                                       "CRITICAL"],
                                              help = loglevel_help)
        time_system_logging_opts.add_argument('--debug',
                                              action = 'store_true',
                                              help = debug_help)
        
    parser_time_system.set_defaults(func = gaze_time,
                                    system = True)

     # Parser Groups
    logging_opts = parser.add_argument_group('Logging Options')

    # Parser Arguments
    #parser.add_argument("filename",
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
    #                    help = "Show SCRIPT_NAME of the spell, where SCRIPT_NAME is any of the above spell scripts.")
    parser.add_argument('-g','--grimoire',
                        nargs = '*',
                        help = 'Specify which grimoire(s) to look in.')
    logging_opts.add_argument("-q", "--quiet",
                              action = "count",
                              default = 0,
                              help = quiet_help)

    if enable_debugging_mode is True:
        logging_opts.add_argument("-v", "--verbosity",
                                  action = "count",
                                  default = 0,
                                  help = verbose_help)
        logging_opts.add_argument("--loglevel",
                                  choices = ["debug","info","warning",
                                           "error","critical",
                                           "DEBUG","INFO","WARNING",
                                           "ERROR","CRITICAL"],
                                  help = loglevel_help)
        logging_opts.add_argument('--debug',
                                  action = 'store_true',
                                  help = debug_help)

    # With version, help description must be before version declaration
    parser.add_argument("-V", "--version",
                        action = "version",
                        help = "Print version information and exit",
                        version = "%(prog)s " + __version__)
    parser.set_defaults(func = False,
                        debug = False,
                        verbosity = 0,
                        loglevel = 'INFO')

    
    # Store all the arguments in a variable
    args = parser.parse_args()


    
    # Ensure we have root access
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
    args.func(args)
    

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
def main(args = None):
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
