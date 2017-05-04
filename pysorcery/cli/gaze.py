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


#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import argparse
import sys
import os
import copy

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import argparse
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import *
#from pysorcery.lib.sorcery import repositories
#from pysorcery.lib.sorcery import packages
from pysorcery.lib.util import config
#from pysorcery.lib.util import files
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
# gaze_alien        - Works
# gaze_orphans      - Works (Ubuntu)
# gaze_activity     - Works
# gaze_queue        - Works (Source Mage / Partial Ubntu)
# gaze_provides     - Works (Source Mage)
# gaze_what         - Works
# gaze_short        - Works
# gaze_where        - Works
# gaze_url          - Works
# gaze_sources      - Not Implemented
# gaze_source_urls  - Not Implemented
# gaze_maintainer   - Not Implemented
# gaze_logs         - Not Implemented
# gaze_version      - Works
# gaze_checksum     - Not Implemented
# gaze_license      - Not Implemented
# gaze_checksum     - Not Implemented
# gaze_size         - Not Implemented
# gaze_expert       - Not Implemented
# gaze_import       - Not Implemented
# gaze_grimoire     - Works (Source Mage)
# gaze_search       - Not Iwplemented
# gaze_newer        - Not Implemented
# gaze_older        - Not Implemented
# gaze_from         - Works (Ubuntu)
# gaze_installed    - Works (Source Mage)
# gaze_section      - Not Implemented
# gaze_voyeur       - Not Implemented
# gaze_file         - Not Implemented
# gaze_depends      - Not Implementod
# gaze_dependencies - Not Implemented
# gaze_time         - Not Implemented
# real_main         - Works
# main              - Works
#
# 22/72
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
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
# Status: Works on Ubuntu (Subprocess.run)
#         Works, but buggy on SourceMage (Prints significantly
#                        more than expected)
#
#-------------------------------------------------------------------------------
def gaze_alien(args):
    logger.debug('Begin Function')

    # create 'alien' object
    alien = libsystem.Alien()
    alien.identify()

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_orphans
#
# Display installed spells that have no explicit dependencies on them
#
# Input:  args
#         args.quiet
# Output: Prints a list of orphaned files
# Return: None
#
# Status: Works on Ubuntu (subprocess)
#         Works on Source Mage (subprocess)
#
#-------------------------------------------------------------------------------
def gaze_orphans(args):
    logger.debug('Begin Function')

    # Create Orphan object
    orphans = libspell.SpellList()
    # Gather List of orphans
    orphan_list = orphans.list_orphans()
    # Print Orphan List
    orphans.print_list(orphan_list)

    logger.debug('End Function')
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
#         args.quiet - Decrease Output Verbosity
# Output: Prints the activity log to the console
# Return: None
#
# Status: Works on Ubuntu (subprocess)
#         Works on Source Mage
#
#-------------------------------------------------------------------------------
def gaze_activity(args):
    logger.debug('Begin Function')

    activity_files = {
        'deb'  : '/var/log/apt/history.log',
        'smgl' : '/var/log/sorcery/activity'
    }
    
    activity = lib.Files()
    activity.print_activity()

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_queue
#
# Shows the queue of spells waiting to be Installed
# Shows the queue of spells waiting to be Removed
#
# Input:  args
#         args.queue - sets which queue to print (install or remove)
#         args.quiet - decrease verbosity
# Output: Prints the queue
# Return: None
#
# Status: Works on Source Mage
#         'Install' queue works on Ubuntu
#         'Remove' queue does not work on Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_queue(args):
    logger.debug('Begin Function')

    # 
    queue = libspell.SpellList()
    spell_queue = queue.list_queue(args.queue)

    queue.print_list(spell_queue)
    
    logger.debug('End Function')
    return


#-------------------------------------------------------------------------------
#
# Function gaze_provides
#
# displays spells that provide the feature
#
# Input:  args
#         args.feature - feature to search for
#         args.quiet   - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_provides(args):
    logger.debug('Begin Function')

    queue = libspell.SpellList()

    for feature in args.feature:
        provides_list = queue.list_provides(feature)
        message = colortext.colorize(feature + ':', 'bold','white','black')
        logger.info(message)
        queue.print_list(provides_list)
        logger.info('')

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
# view the long package description
#
# Input:  args
#         args.spell    - List of spells to get description.
#                         Minimum 1
#         args.grimoire - Grimoire(s) to check for spell
#         args.quiet    - Limit print output
# Output: Prints spell description
# Return: None
#
# Status: Working for Source Mage
#         Working for Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_what(args):
    logger.debug('Begin Function')

    # For each spell in the spell list...
    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(spell.description, 'none','white','black')
        logger.info1(message)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_short
#
# view the short package description
#
# Input:  args
#         args.spell    - List of spells to get description.
#                         Minimum 1
#         args.grimoire - 
#         args.quiet    - 
# Output:
# Return: None
#
# Status: Working for Source Mage
#         Working for Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_short(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(spell.short, 'none','white','black')
        logger.info1(message)

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_where
#
# display the section a spell belongs to.
# If -path is given, display the full path to spell
#
# Input:  args
#         args.spell     - List of spells to get section.
#                          Minimum 1
#         args.grimoires - 
#         args.path      - Print spell path information instead
#                          of section name.
#         args.quiet     - decrease verbosity
# Output:
# Return: None
#
# Status: Working for Source Mage
#         Working for Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_where(args):
    logger.debug('Begin Function')

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug2(spell)
        
        name = colortext.colorize(str(spell.name), 'bold','white','black')
        section = colortext.colorize(str(spell.section), 'none','white','black')
        logger.info(name + ': ')
        logger.info1(section)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_url
#
# display the URL for the specified spell
#
# Input:  args
#         args.spell    - List of spells to get section.
#                         Minimum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
# Output:
# Return: None
#
# Status: Working for Source Mage
#         Working for Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_url(args):
    logger.debug('Begin Function')

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        name = colortext.colorize(spell.name, 'bold','white','black')
        url = colortext.colorize(spell.url, 'none','white','black')
        logger.info(name + ': ')
        logger.info1(url)

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_sources
#
# list all source files contained in a spell
#
# Input:  args
#         args.spell - List of spells to get section.
#                      Minimum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_sources(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(spell.description, 'none','white','black')
        logger.info1(message)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_source_urls
#
# lists the urls to all files contained in a spell
#
# Input:  args
#         args.spell    - List of spells to get section.
#                         Minimum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_source_urls(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(spell.description, 'none','white','black')
        logger.info1(message)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_maintainer
#
# display the email address of the person currently responsible for
# maintaining a specified section
#
# Input:  args
#         args.spell    - List of spells to get section.
#                         Minimum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_maintainer(args):
    logger.debug('Begin Function')

    for i in args.spell:
        logger.debug2('Loop iteration: ' + i)
        
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(spell.description, 'none','white','black')
        logger.info1(message)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_logs
#
# Show the compiler output generated when the spell was built. 
# If no optional version was given, try the installed version. 
# If the spell is not installed use the version in the grimoire.
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_log(args):
    logger.debug('Begin Function')
        
    spell = libspell.Spell(i)
    
    logger.debug3('Spell: ' + str(spell))
        
    message = colortext.colorize(spell.name, 'bold','white','black')
    logger.info(message)

    message = colortext.colorize(spell.description, 'none','white','black')
    logger.info1(message)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_version
#
# Shows the installed version of the spell and the main grimoires version.
# 
# Input:  args
#         args.spell    - Spell to print compile log.
#                         Maximum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
#         args.multi    - Shows the installed version of the spell
#                         and lists all available versions in all
#                         grimoires. If used without a spell name,
#                         then lists order of available grimoires.
# Output:
# Return: None
#
# Status: Works on Source Mage
#         Works on Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_version(args):
    logger.debug('Begin Function')

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)

        spell.print_version(args.multi)
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_license
#
# View the license(s) of the given spell(s), or spells in given section(s),
# or view the information about given license(s)
#
# Input:  args
#         args.spell    - Spell to print compile log.
#                         Maximum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_license(args):
    logger.debug('Begin Function')
        
    spell = libspell.Spell(i)

    logger.debug3('Spell: ' + str(spell))
    
    message = colortext.colorize(spell.name, 'bold','white','black')
    logger.info(message)

    message = colortext.colorize(spell.description, 'none','white','black')
    logger.info1(message)

    logger.debug('End Function')
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
#         args.spell    - Spell to print compile log.
#                         Maximum 1
#         args.grimoire -
#         args.quiet    - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_checksum(args):
    logger.debug('Begin Function')
            
    spell = libspell.Spell(i)

    logger.debug3('Spell: ' + str(spell))
        
    message = colortext.colorize(spell.name, 'bold','white','black')
    logger.info(message)

    message = colortext.colorize(spell.description, 'none','white','black')
    logger.info1(message)

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_size
#
# print the sizes and file counts of the passed installed spell(s) or if -all is
# specified, of all the spells. In addition, this will print the largest spell.
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.all   -
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_size(args):
    logger.debug('Begin Function')

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug3('Spell: ' + str(spell))
        
        message = colortext.colorize(spell.name, 'bold','white','black')
        logger.info(message)

        message = colortext.colorize(str(spell.size) + 'kb', 'none','white','black')
        logger.info1(message)

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_export
#
# take a snapshot of all currently installed spells and their configuration.
#
# Input:  args
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_export(args):
    logger.debug('Begin Function')

    spell = libspell.Spell(i)

    logger.debug3('Spell: ' + str(spell))
        
    message = colortext.colorize(spell.name, 'bold','white','black')
    logger.info(message)

    message = colortext.colorize(spell.description, 'none','white','black')
    logger.info1(message)

    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_import(args):
    logger.debug('Begin Function')

    spell = libspell.Spell(i)

    logger.debug3('Spell: ' + str(spell))
        
    message = colortext.colorize(spell.name, 'bold','white','black')
    logger.info(message)

    message = colortext.colorize(spell.description, 'none','white','black')
    logger.info1(message)

    logger.debug('End Function')
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
#         args.grimoire      - Spell to print compile log.
#                              Minimum 1
#         args.quiet         - decrease verbosity
#         args.multi         -
#         args.displayformat - console or html
#         args.columns       - have the grimoires be columns
# Output:
# Return: None
#
# Status: Works on Source Mage
#
#-------------------------------------------------------------------------------
def gaze_grimoire(args):
    logger.debug('Begin Function')

    if args.multi:
        grimoires = libcodex.Codex()
        grimoires.print_grimoires()

    elif args.grimoire:
        logger.info('Fix Me')

    else:
        libgaze.print_codex()          
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_search
#
# search [-name|-short] 'phrase'
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.name  -
#         args.short -
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_search(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_newer(args):
    logger.debug('Begin Function')

    

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_older
#
# print packages that were first submitted before a specified date.
# the date must be specified in 'yyyymmdd' format
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_older(args):
    logger.debug('Begin Function')

    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Working on Ubuntu
#
#-------------------------------------------------------------------------------
def gaze_from(args):
    logger.debug('Begin Function')

    spell = libfiles.Files(args.filename[0])
    spell.print_from()
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_installed
#
# view all installed packages and corresponding version numbers or check
# to see whether a particular package is installed and if it is
# installed display its version number
#
# shows all spells currently held
# (which means they are not to be updated)
#
# shows all spells currently exiled
# (which means they are not to be cast in any way)
#
# Input:  args
#         args.spell       - Spell to print compile log.
#                            Minimum 1
#         args.spellstatus - 
#         args.quiet       - decrease verbosity
# Output:
# Return: None
#
# Status: Works on Source Mage
#
#-------------------------------------------------------------------------------
def gaze_installed(args):
    logger.debug('Begin Function')

    if args.spell:
        for i in args.spell:
            spell = libspell.Spell(i)
            spell.print_version()

    else:
        spells = libspell.SpellList()
        if args.spellstatus:
            spell_list = spells.list_installed(args.spellstatus)
        else:
            spell_list = spells.list_installed()

        spells.print_list(spell_list)
        
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_section
#
# view a list of all sections in the software catalogue or display a list
# of packages from a specific section
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_section(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_voyeur(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_file(args):
    logger.debug('Begin Function')
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function gaze_depends
#
# shows the spells that explicitly or recursively depend on this
# installed spell.  Up to level $level if specified. Only enabled
# dependencies are shown.
#
# If --fast is specified more limited output is produced, but it run
#s much faster.
# If --required is specified only the required dependencies are shown and the
# runtime ones are skipped.
#
# Input:  args
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_depends(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_dependencies(args):
    logger.debug('Begin Function')

    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_time(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
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
#         args.spell - Spell to print compile log.
#                      Maximum 1
#         args.quiet - decrease verbosity
# Output:
# Return: None
#
# Status: Not implimented
#
#-------------------------------------------------------------------------------
def gaze_42(args):
    logger.debug('Begin Function')

    logger.info1('What is the meaning of life?')
    
    logger.debug('End Function')
    return

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

    # Common Help Descriptions:
    quiet_help = 'Decrease output'
    verbose_help = 'Increase output'
    loglevel_help = 'Specify output level'
    debug_help = 'Maximize output level'
    loglevel_choices = [ 'debug',
                         'info',
                         'warning',
                         'error',
                         'critical',
                         'DEBUG',
                         'INFO',
                         'WARNING',
                         'ERROR',
                         'CRITICAL'
    ]

    # Parse Command Line Arguments
    parser = argparse.ArgumentParser(description = 'Query / View Sorcery package management information')
    parent_parser = argparse.ArgumentParser(add_help=False)
    repo_parent_parser = argparse.ArgumentParser(add_help=False)

    repo_parent_parser.add_argument('-g','--grimoire',
                        nargs = '*',
                        help = 'Specify which grimoire(s) to look in.')
     # Parser Groups
    logging_opts = parent_parser.add_argument_group('Logging Options')
    logging_opts.add_argument('-q', '--quiet',
                              action = 'count',
                              default = 0,
                              help = quiet_help
    )
    if enable_debugging_mode is True:
        logging_opts.add_argument('-v', '--verbosity',
                                  action = 'count',
                                  default = 0,
                                  help = verbose_help
        )
        logging_opts.add_argument('--loglevel',
                                  choices = loglevel_choices,
                                  default = 'INFO',
                                  help = loglevel_help
        )
        logging_opts.add_argument('--debug',
                                  action = 'store_true',
                                  help = debug_help
        )

    # With version, help description must be before version declaration
    parent_parser.add_argument('-V', '--version',
                               action = 'version',
                               help = 'Print version information and exit',
                               version = '%(prog)s ' + __version__)

    
    # Create subcommands
    subparsers = parser.add_subparsers(title = 'commands',
                                       metavar = 'Description')

    #------------------------------------------
    #
    # Create the parser for the 'alien' command
    #
    #-------------------------------------------
    alien_help = 'Find and Display all files not tracked by the Sorcery Package Management System.'
    parser_alien = subparsers.add_parser('alien',
                                         parents = [parent_parser],
                                         aliases = ['aliens'],
                                         help = alien_help)
    parser_alien.set_defaults(func = gaze_alien)

    #-------------------------------------------
    #
    # create the parser for the 'orphans' command
    #
    #-------------------------------------------
    orphans_help = 'Display installed spells that do not have any explicit dependencies on them.'
    parser_orphans = subparsers.add_parser('orphans',
                                           parents = [parent_parser],
                                           help = orphans_help
    )    
    parser_orphans.set_defaults(func = gaze_orphans)

    #-------------------------------------------
    #
    # create the parser for the 'activity' command
    #
    #-------------------------------------------
    activity_help = 'Show the activity log.  (Note: this is actually a log of all that happened involving sorcery, such as casts, summons etc.).'
    parser_activity = subparsers.add_parser('activity',
                                            parents = [parent_parser],
                                            help = activity_help
    )        
    parser_activity.set_defaults(func = gaze_activity)

    #-------------------------------------------
    #
    # create the parser for the 'install-queue' command
    #
    #-------------------------------------------
    install_help = 'Show spells waiting to be installed.'
    parser_install_queue = subparsers.add_parser('install-queue',
                                                 parents = [parent_parser],
                                                 help = install_help)
    parser_install_queue.set_defaults(func = gaze_queue,
                                      queue = 'install'
    )

    #-------------------------------------------
    #
    # create the parser for the 'remove-queue' command
    #
    #-------------------------------------------
    remove_help = 'Show spells to be removed.'
    parser_remove_queue = subparsers.add_parser('remove-queue',
                                                parents = [parent_parser],
                                                help = remove_help)
    parser_remove_queue.set_defaults(func = gaze_queue,
                                     queue = 'remove'
    )

    #-------------------------------------------
    #
    # create the parser for the 'show-held' command
    #
    #-------------------------------------------
    show_held_help = 'Shows all spells currently held (which means they are not to be updated).'
    parser_show_held = subparsers.add_parser('show-held',
                                             parents = [parent_parser],
                                             help = show_held_help
    )   
    parser_show_held.set_defaults(func = gaze_installed,
                                  spellstatus = 'held',
                                  spell = False
    )

    #-------------------------------------------
    #
    # create the parser for the 'show-exiled' command
    #
    #-------------------------------------------
    show_exiled_help = 'Shows all spells currently exiled (which means they are not to be cast in any way).'
    parser_show_exiled = subparsers.add_parser('show-exiled',
                                               parents = [parent_parser],
                                               help = show_exiled_help
    )
    parser_show_exiled.set_defaults(func = gaze_installed,
                                    spellstatus = 'exiled',
                                    spell = False
    )

    #-------------------------------------------
    #
    # create the parser for the 'provides' command
    #
    #-------------------------------------------
    parser_provides = subparsers.add_parser('provides',
                                            parents = [parent_parser,
                                                       repo_parent_parser
                                            ],
                                            help = 'Displays spells that provide the feature.'
    )
    parser_provides.add_argument('feature',
                                 nargs = '+',
                                 help = 'Feature'
    )
    parser_provides.set_defaults(func = gaze_provides)

    #-------------------------------------------
    #
    # create the parser for the 'what' command
    #
    #-------------------------------------------
    parser_what = subparsers.add_parser('what',
                                        parents = [parent_parser,
                                                   repo_parent_parser
                                        ],
                                        help = 'Display spell description.'
    )
    parser_what.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_what.set_defaults(func = gaze_what)

    #-------------------------------------------
    #
    # create the parser for the 'short' command
    #
    #-------------------------------------------
    parser_short = subparsers.add_parser('short',
                                         parents = [parent_parser],
                                         help = 'Display spell short description.'
    )
    parser_short.add_argument('spell',
                              nargs = '+',
                              help='Display System Info'
    )
    parser_short.set_defaults(func = gaze_short)

    #-------------------------------------------
    #
    # create the parser for the 'where' command
    #
    #-------------------------------------------
    parser_where = subparsers.add_parser('where',
                                         parents = [parent_parser,
                                                    repo_parent_parser
                                         ],
                                         help = 'Display the section a spell belongs to.'
    )
    parser_where.add_argument('spell',
                              nargs = '+',
                              help = 'Spell(s) to display'
    )
    parser_where.add_argument('-p',
                              '-path',
                              '--path',
                              action = 'store_true',
                              help = 'Display the full path to spell'
    )    
    parser_where.set_defaults(func = gaze_where)

    #-------------------------------------------
    #
    # create the parser for the 'url' command
    #
    #-------------------------------------------
    parser_url = subparsers.add_parser('url',
                                       parents = [parent_parser,
                                                  repo_parent_parser
                                       ],
                                       aliases = ['website'],
                                       help = 'Display spell homepage'
    )
    parser_url.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info'
    )
    parser_url.set_defaults(func = gaze_url)

    #-------------------------------------------
    #
    # create the parser for the 'sources' command
    #
    #-------------------------------------------
    parser_sources = subparsers.add_parser('sources',
                                           parents = [parent_parser,
                                                      repo_parent_parser
                                           ],
                                           help = 'List all source files contained in a spell. (Not Working)'
    )
    parser_sources.add_argument('spell',
                                nargs = '+',
                                help = 'Display System Info'
    )        
    parser_sources.set_defaults(func = gaze_sources)


    #-------------------------------------------
    #
    # create the parser for the 'source_urls' command
    #
    #-------------------------------------------
    parser_source_url = subparsers.add_parser('source_urls',
                                              parents = [parent_parser,
                                                         repo_parent_parser
                                              ],
                                              help = 'Lists the urls to all files contained in a spell.'
    )
    parser_source_url.add_argument('spell',
                                   nargs = '+',
                                   help = 'Spell'
    )
    parser_source_url.set_defaults(func = gaze_source_urls)

    #-------------------------------------------
    #
    # create the parser for the 'maintainer' command
    #
    #-------------------------------------------
    parser_maintainer = subparsers.add_parser('maintainer',
                                              parents = [parent_parser,
                                                         repo_parent_parser
                                              ],
                                              help = 'Display the email address of the person responsible for maintaining a specified spell. (Not Working)'
    )
    parser_maintainer.add_argument('spell',
                                   nargs = '+',
                                   help = 'Spell'
    )    
    parser_maintainer.set_defaults(func = gaze_maintainer)

    #-------------------------------------------
    #
    # create the parser for the 'compile' command
    #
    #-------------------------------------------
    parser_compile = subparsers.add_parser('compile',
                                           parents = [parent_parser,
                                                      repo_parent_parser
                                           ],
                                           help = 'Show the compiler output generated when the spell was built.  If no optional version was given, try the installed version.  If the spell is not installed use the version in the grimoire. (Not Working)'
    )
    parser_compile.add_argument('spell',
                                nargs = 1,
                                help = 'Spell'
    )
    parser_compile.add_argument('version',
                                nargs = '?',
                                help = 'Specifies which Version of spell to view.'
    )        
    parser_compile.set_defaults(func = gaze_log,
                                log = 'compile'
    )

    #-------------------------------------------
    #
    # create the parser for the 'install' command
    #
    #-------------------------------------------
    parser_install = subparsers.add_parser('install',
                                           parents = [parent_parser],
                                           help = 'Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files. If no optional version was given, try the installed version. (Not Working)'
    )
    parser_install.add_argument('spell',
                                nargs = 1,
                                help = 'Spell'
    )
    parser_install.add_argument('version',
                                nargs = 1,
                                help = 'Specifies which version of spell to view'
    )
    parser_install.set_defaults(func = gaze_log,
                                log = 'install')

    #-------------------------------------------
    #
    # create the parser for the 'install-full' command
    #
    #-------------------------------------------
    parser_install_full = subparsers.add_parser('install-full',
                                                parents = [parent_parser],
                                                help = 'Used to determine what files were installed by a spell and where those files are located.  If no optional version was given, try the installed version.  (Not Working)'
    )
    parser_install_full.add_argument('spell',
                                     nargs = 1,
                                     help = 'Spell'
    )
    parser_install_full.add_argument('version',
                                     nargs = 1,
                                     help = 'Specifies which version of the spell to view.'
    )
    parser_install_full.set_defaults(func = gaze_log,
                                     log = 'install_full'
    )

    #-------------------------------------------
    #
    # create the parser for the 'install-spell' command
    #
    #-------------------------------------------
    parser_install_spell = subparsers.add_parser('install-spell',
                                                 parents = [parent_parser],
                                                 help = 'Used to determine what files were installed by a spell and where those files are located, excludes sorcery state files and sorcery log files.  If no optional version was given, try the installed version. (Not Working)'
    )
    parser_install_spell.add_argument('spell',
                                      nargs = 1,
                                      help = 'Spell'
    )
    parser_install_spell.add_argument('version',
                                      nargs = 1,
                                      help = 'Specifies which version of the spell to view'
    )        
    parser_install_spell.set_defaults(func = gaze_log,
                                      log = 'install_spell'
    )

    #-------------------------------------------
    #
    # create the parser for the 'version' command
    #
    #-------------------------------------------
    parser_version = subparsers.add_parser('version',
                                           parents = [parent_parser,
                                                      repo_parent_parser
                                           ],
                                           help = 'Shows the installed version of the spell and the main grimoires version.'
    )
    parser_version.add_argument('spell',
                                nargs = 1,
                                help = 'Display System Info'
    )
    parser_version.set_defaults(func = gaze_version,
                                multi = False
    )

    #-------------------------------------------
    #
    # create the parser for the 'versions' command
    #
    #-------------------------------------------
    parser_versions = subparsers.add_parser('versions',
                                            parents = [parent_parser],
                                            help = 'Shows the installed version of the spell and lists all available versions in all grimoires. If used without a spell name, then lists order of available grimoires.'
    )
    parser_versions.add_argument('spell',
                                 nargs = 1,
                                 help = 'Display System Info'
    )
    parser_versions.set_defaults(func = gaze_version,
                                 multi = True
    )

    #-------------------------------------------
    #
    # create the parser for the 'license' command
    #
    #-------------------------------------------
    parser_license = subparsers.add_parser('license',
                                           parents = [parent_parser,
                                                      repo_parent_parser
                                           ],
                                           help = 'View the license(s) of the given spell(s), or spells in given section(s), or view the information about given license(s) (Not Working)'
    )
    parser_license.add_argument('ssl',
                                nargs = '+',
                                help = 'Spell, Section, or License to view'
    )
    parser_license.set_defaults(func = gaze_license)


    #-------------------------------------------
    #
    # create the parser for the 'versions' command
    #
    #-------------------------------------------
    parser_sum = subparsers.add_parser('sum',
                                       parents = [parent_parser],
                                       help = 'Print CRC checksums for spells(s). If no spell is given it default to all. (Not Working)'
    )
    parser_sum.add_argument('spell',
                            nargs = '?',
                            help = 'Display System Info')
    parser_sum.set_defaults(func = gaze_checksum,
                            check_type = 'CRC'
    )

    #-------------------------------------------
    #
    # create the parser for the 'md5sum' command
    #
    #-------------------------------------------
    parser_md5sum = subparsers.add_parser('md5sum',
                                          parents = [parent_parser,
                                                     repo_parent_parser
                                          ],
                                          help = 'Print spell MD5 message digests (fingerprints). If no spell is given it default to all (Not Working)'
    )
    parser_md5sum.add_argument('spell',
                               nargs = '?',
                               help = 'Display System Info'
    )
    parser_md5sum.set_defaults(func = gaze_checksum,
                               check_type = 'MD5'
    )

    #-------------------------------------------
    #
    # create the parser for the 'size' command
    #
    #-------------------------------------------
    parser_size = subparsers.add_parser('size',
                                        parents = [parent_parser],
                                        help = 'print the sizes and file counts of the passed installed spell(s). (Not Working)'
    )
    parser_size.add_argument('spell',
                             nargs = '+',
                             help = 'Display System Info')
    parser_size.add_argument('-a','-all','--all',
                             action = 'store_true',
                             help = 'Display sizes of all the spells. In addition, this will print the largest spell.')
    parser_size.set_defaults(func = gaze_size)

    #-------------------------------------------
#
    # create the parser for the 'export' command
    #
    #-------------------------------------------
    parser_export = subparsers.add_parser('export',
                                          parents = [parent_parser],
                                          help = 'Take a snapshot of all currently installed spells and their configuration. (Not Working)'
    )
    parser_export.set_defaults(func = gaze_export)

    #-------------------------------------------
    #
    # create the parser for the 'import' command
    #
    #-------------------------------------------
    parser_import = subparsers.add_parser('import',
                                          parents = [parent_parser],
                                          help = "restore the snapshot from a previous 'gaze export' command (see above). (Not Working)")
    parser_import.add_argument('snapshot',
                               nargs = 1,
                               help = 'Display System Info')
    parser_import.add_argument('--depreciated',
                               action = 'store_true',
                               help = 'Use the old behaviour.  An old cache is expected. There is no significant problem if an old cache is restored with the new importer. A few files will be ignored - only the files that the new exporter saves are considered - and the queuing logic wille be slighty more agressive.')
    parser_import.set_defaults(func = gaze_import)


    #-------------------------------------------
    #
    # create the parser for the 'grimoire' command
    #
    #-------------------------------------------
    parser_grimoire = subparsers.add_parser('grimoire',
                                            parents = [parent_parser],
                                            help = "Prints specified grimoire's spells or all grimoires if grimoire-name is omitted (Not Working)")
    parser_grimoire.add_argument('grimoire',
                                 nargs = '*',
                                 help = 'Specify grimoire to view')    
    parser_grimoire.set_defaults(func = gaze_grimoire,
                                 multi = False,
                                 display_format = 'console')

    # create the parser for the 'grimoires' command
    parser_grimoires = subparsers.add_parser('grimoires',
                                             parents = [parent_parser],
                                             help = 'Display installed grimoires by name only. (Not Working)'
    )
    parser_grimoires.set_defaults(func = gaze_grimoire,
                                  multi = True,
                                  display_format = 'console')

    #-------------------------------------------
    #
    # create the parser for the 'html' command
    #
    #-------------------------------------------
    parser_html = subparsers.add_parser('html',
                                        parents = [parent_parser],
                                        help = 'Prints the specified grimoire or all grimoires if grimoire-name is omitted in a nice html format. (Not Working)')
    parser_html.add_argument('grimoire',
                             nargs = '*',
                             help = 'Specified grimoire(s)')
    parser_html.add_argument('-s','--source',
                             action = 'store_true',
                             help = 'Displays links to the source files.')
    parser_html.set_defaults(func = gaze_grimoire,
                             multi = False,
                             display_format = 'html')
    
    #-------------------------------------------
    #
    # create the parser for the 'search' command
    #
    #-------------------------------------------
    parser_search = subparsers.add_parser('search',
                                          parents = [parent_parser,
                                                     repo_parent_parser
                                          ],
                                          help = 'Searches spells name, short description and long description for phrase (Not Working)'
    )
    # Need to make the following mutually exclusive
    parser_search.add_argument('-n','-name','--name',
                             action = 'store_true',
                             help = 'Only search spells name')
    parser_search.add_argument('-s','-short','--short',
                             action = 'store_true',
                             help = 'Only search spells short description')
    parser_search.add_argument('phrase',
                               nargs = 1,
                               help = "Any valid extended regular expression. For optimal results, don't forget to escape any special characters and use quotes to protect the expression."
    )
    parser_search.set_defaults(func = gaze_search)

    #-------------------------------------------
    #
    # create the parser for the 'newer' command
    #
    #-------------------------------------------
    parser_newer = subparsers.add_parser('newer',
                                         parents = [parent_parser],
                                         help = 'Print packages first submitted after a specified date. (Not Working)'
    )
    parser_newer.add_argument('date',
                              nargs = '?',
                              default = 'last_sorcery_update',
                              help = "Specify Date.  The date must be in the 'yyyymmdd' format, where y = year, m = month, and d = day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_newer.set_defaults(func = gaze_newer)


    #-------------------------------------------
    #
    # create the parser for the 'older' command
    #
    #-------------------------------------------
    parser_older = subparsers.add_parser('older',
                                         parents = [parent_parser],
                                         help = 'print packages that were first submitted before a specified date. (Not Working)')
    parser_older.add_argument('date',
                              nargs = '?',
                              help = "Specify Date.  The date must be in the 'yyyymmdd' format, where y = year, m = month, and d = day.  There are two special dates, last_sorcery_update and last_cast.")
    parser_older.set_defaults(func = gaze_older)

    #-------------------------------------------
    #
    # create the parser for the 'from' command
    #
    #-------------------------------------------
    parser_from = subparsers.add_parser('from',
                                        parents = [parent_parser],
                                        help = "find out which spell has installed 'path/file.'  Matching is done literally against the end of the path names in the lists of installed files."
    )
    parser_from.add_argument('filename',
                             nargs = 1,
                             help = 'Display System Info'
    )
    parser_from.add_argument('-r','-regex','--regex',
                             action = 'store_true',
                             help = 'Matching using basic regular expressions against the whole paths in the lists of installed files.'
    )        
    parser_from.set_defaults(func = gaze_from)

    #-------------------------------------------
    #
    # create the parser for the 'installed' command
    #
    #-------------------------------------------
    parser_installed = subparsers.add_parser('installed',
                                             parents = [parent_parser],
                                             help = 'View all installed packages and corresponding version numbers (Not Working)'
    )
    parser_installed.add_argument('spell',
                                  nargs = '*',
                                  help = 'Check to see whether a particular package is installed and if it is installed display its version number'
    )
    parser_installed.set_defaults(func = gaze_installed,
                                  spellstatus=None
    )

    #-------------------------------------------
    #
    # create the parser for the 'section' command
    #
    #-------------------------------------------
    parser_section = subparsers.add_parser('section',
                                           parents = [parent_parser],
                                           help = 'View a list of all sections in the software catalogue or display a list of packages from a specific section. (Not Working)'
    )
    parser_section.add_argument('section',
                                nargs = '?',
                                help = 'Display System Info'
    )
    parser_section.set_defaults(func = gaze_section)

    #-------------------------------------------
    #
    # create the parser for the 'voyeur' command
    #
    #-------------------------------------------
    parser_voyeur = subparsers.add_parser('voyeur',
                                          parents = [parent_parser],
                                          help = 'start looking at what cast is compiling at the moment and outputs its compiler messages. A spell can be optionally specified, or a delay after which to abort when no casts could be found. (Not Working)'
    )
    parser_voyeur.add_argument('spell',
                               nargs = '?',
                               help = 'Display System Info')
    parser_voyeur.set_defaults(func = gaze_voyeur)

    #-------------------------------------------
    #
    # create the parser for the 'history' command
    #
    #-------------------------------------------
    parser_history = subparsers.add_parser('history',
                                           parents = [parent_parser],
                                           help = 'Show history for a spell (alias for gaze HISTORY). (Not Working)'
    )
    parser_history.add_argument('spell',
                                nargs = 1,
                                help = 'Display System Info')
    parser_history.set_defaults(func = gaze_file,
                                filename = 'HISTORY')

    #-------------------------------------------
    #
    # create the parser for the 'checkmd5s' command
    #
    #-------------------------------------------
    parser_checkmd5s = subparsers.add_parser('checkmd5s',
                                             parents = [parent_parser],
                                             help = 'Computes the md5sum on spell sources based on passed spell(s), section(s) or entire grimoire(s) if left blank. (Not Working)'
    )
    parser_checkmd5s.add_argument('spell',
                                  nargs = '*',
                                  help = 'Display System Info')
    parser_checkmd5s.set_defaults(func = gaze_checksum,
                                  filename = 'checksum')


    #-------------------------------------------
    #
    # create the parser for the 'depends' command
    #
    #-------------------------------------------
    parser_depends = subparsers.add_parser('depends',
                                           help = 'shows the spells that explicitly or recursively depend on this installed spell.  Only enabled dependencies are shown. (Not Working)'
    )
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
    parser_depends.set_defaults(func = gaze_depends)

    #-------------------------------------------
    #
    # create the parser for the 'dependencies' command
    #
    #-------------------------------------------
    parser_dependencies = subparsers.add_parser('dependencies',
                                                parents = [parent_parser],
                                                help = 'shows the spells that spell explicitly or recursively depends on. (Not Working)'
    )
    parser_dependencies.add_argument('spell',
                                     nargs = 1,
                                     help = 'Display System Info'
    )
    parser_dependencies.add_argument('level',
                                     nargs = '?',
                                     help = 'Up to level $level if specified.'
    )
    parser_dependencies.add_argument('-c',
                                     action = 'store_true',
                                     help = 'skips trees that have already been shown'
    )
    parser_dependencies.add_argument('--no-optionals',
                                     action = 'store_true',
                                     help = 'skips optional dependencies.'
    )
    parser_dependencies.set_defaults(func = gaze_dependencies)
    
    #-------------------------------------------
    #
    # create the parser for the 'time' command
    #
    #-------------------------------------------
    parser_time = subparsers.add_parser('time',
                                        help = 'Shows the time the spell(s) needed to get cast. By default the last casting time is shown, alternatively the median, mean or weighted mean can be shown.  If more then one spell is specified, also a total time is shown. (Not Working)'
    )
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
    parser_time.set_defaults(func = gaze_time,
                             system = False)

    #-------------------------------------------
    #
    # create the parser for the 'time-system' command
    #
    #-------------------------------------------
    parser_time_system = subparsers.add_parser('time-system',
                                               help = 'Shows the time the whole system needed to get cast. (Not Working)'
    )
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
    parser_time_system.set_defaults(func = gaze_time,
                                    system = True)
                                      
    parser_42 = subparsers.add_parser('42',
                                      parents = [parent_parser])
    parser_42.set_defaults(func = gaze_42)
    

    
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


    
    # Ensure we have root access
    if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra 'sudo' in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
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

        #try:         
        #    real_main(args)
        #except:
        #    logger.critical('You Fucked Up')

        logger.debug('End Application')
        return

if __name__ == '__main__':
    main()
