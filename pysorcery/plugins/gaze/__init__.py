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
# File: pysorcery/cli/archive.py
#
# This file is part of Sorcery.
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
This is a bonus application for pysorcery.  PySorcery for multiple
reasons to internally extract, create, list the contents, etc.
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
from pysorcery.lib.util.files import archive
# Conditional Libraries


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
# archive_extract
# archive_list
# archive_create
# archive_test
# archive_repack
# archive_recompress
# archive_diff
# archive_search
# archive_formats
#
#-----------------------------------------------------------------------

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
def checksum(args):
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
def queue(args):
    logger.debug('Begin Function')

    # 
    queue = libspell.SpellList()
    spell_queue = queue.list_queue(args.queue)

    queue.print_list(spell_queue)
    
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
        spell = lib.Package(i)
        version = spell.get_version()

        logger.debug(spell)

        if args.multi:
            logger.critical('Fix Me')
        else:
            if args.verbose > 0:
                logger.critical('Fix Me')
            else:
                message = colortext.colorize(spell.name, 'bold','white','black')
                logger.info1(message)

                message = colortext.colorize(version, 'none','white','black')
                logger.info2(message)

                print()
    
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
def log(args):
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
def grimoire(args):
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
def file(args):
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
def time(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return
