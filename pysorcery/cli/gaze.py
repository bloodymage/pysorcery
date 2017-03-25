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
#
#
# This file is a flat file prototype.  There are several things I flat out do not
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
# create logger
logger = logging.getLogger(__name__)

# Other Optional Libraries
deb_distro_list=['Ubuntu']
distro_id=distro.linux_distribution()[0]

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class Files
# 
#
#-------------------------------------------------------------------------------
class BaseFiles():
    def __init__(self,filename):
        return

    def print_from(self):
        print("Oops")

class DebianFiles(BaseFiles):
    def __init__(self,filename):
        BaseFiles.__init__(self,filename)

    def print_from(self):
        subprocess.run(["dpkg","-S",self.filename])


class Files(DebianFiles,BaseFiles):
    def __init__(self,filename):
        self.filename = filename
        if distro_id in deb_distro_list:
            DebianFiles.__init__(self,filename)
        else:
            BaseFiles.__init__(self,filename)

    def print_from(self):
        if distro_id in deb_distro_list:
            DebianFiles.print_from(self)
        else:
            BaseFiles.print_from(self)
            
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
def gaze_alien(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        colortext = libtext.ConsoleText()
        message = colortext.colorize(spell.name, "bold","white","black")
        print(message)

        message = colortext.colorize(spell.description, "none","white","black")
        print(message)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_orphans(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        colortext = libtext.ConsoleText()
        message = colortext.colorize(spell.name, "bold","white","black")
        print(message)

        message = colortext.colorize(spell.description, "none","white","black")
        print(message)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_activity(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_install_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_remove_queue(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_show_held(args):
    logger.debug("Begin Function")
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
#
#-------------------------------------------------------------------------------
def gaze_show_exiled(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_what
#
#
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
#
#
#-------------------------------------------------------------------------------
def gaze_what(args):
    logger.debug("Begin Function")

    for i in args.spell:
        spell = libspell.Spell(i)

        logger.debug(spell)
        
        colortext = libtext.ConsoleText()
        message = colortext.colorize(spell.name, "bold","white","black")
        print(message)

        message = colortext.colorize(spell.description, "none","white","black")
        print(message)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_short
#
#
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
#
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
        print(name + ": " + section)
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_url
#
#
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
        print(name + ": " + url)

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def gaze_sources(args):
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
def gaze_source_urls(args):
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
def gaze_maintainer(args):
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
def gaze_compile(args):
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
def gaze_install(args):
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
# Functions
#
#
#
#-------------------------------------------------------------------------------
def gaze_license(args):
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
def gaze_checksum(args):
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
def gaze_size(args):
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
def gaze_export(args):
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
def gaze_import(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_grimoire
#
#
#
#-------------------------------------------------------------------------------
def gaze_grimoire(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_html
#
# 
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
# 
#
#-------------------------------------------------------------------------------
def gaze_search(args):
    logger.debug("Begin Function")

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_html
#
# 
#
#-------------------------------------------------------------------------------
def gaze_newer(args):
    logger.debug("Begin Function")

    

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_html
#
# 
#
#-------------------------------------------------------------------------------
def gaze_older(args):
    logger.debug("Begin Function")

    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function gaze_html
#
# 
#
#-------------------------------------------------------------------------------
def gaze_from(args):
    logger.debug("Begin Function")

    spell = Files(args.filename[0])

    spell.print_from()
    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------
def gaze_license(args):
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
def gaze_installed(args):
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
def gaze_section(args):
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
def gaze_voyeur(args):
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
def gaze_file(args):
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
def gaze_history(args):
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

    # create the parser for the "orphans" command
    parser_what = subparsers.add_parser('orphans', help='Display installed spells that do not have any explicit dependencies on them (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_what.set_defaults(func=gaze_orphans)

    # create the parser for the "activity" command
    parser_what = subparsers.add_parser('activity', help='Show the activity log (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_what.set_defaults(func=gaze_activity)


    # create the parser for the "install-queue" command
    parser_what = subparsers.add_parser('install-queue', help='Show spells waiting to be installed (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_install_queue)

    # create the parser for the "remove-queue" command
    parser_what = subparsers.add_parser('remove-queue', help='Show spells to be removed (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_remove_queue)

    # create the parser for the "what" command
    parser_what = subparsers.add_parser('show-held', help='Show all spells in a hold status (Prevents Upgrading) (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_show_held)

    # create the parser for the "what" command
    parser_what = subparsers.add_parser('show-exiled', help='Show all spells in an exiled status (They are not to be installed for any reason) (Not Working)')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_show_exiled)

    # create the parser for the "what" command
    parser_what = subparsers.add_parser('provides', help='List spells that provide a feature (Not Working)')
    parser_what.add_argument('provides',
                             nargs='+',
                             help='Display System Info')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_provides)
    
    # create the parser for the "what" command
    parser_what = subparsers.add_parser('what', help='Display spell description')
    parser_what.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_what)

    # create the parser for the "what" command
    parser_what = subparsers.add_parser('short', help='Display spell short description (Not Working)')
    parser_what.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_what.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_what.set_defaults(func=gaze_short)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('where', help='Display spell section')
    parser_where.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_where)

    # create the parser for the "url" command
    parser_url = subparsers.add_parser('url', help='Display spell homepage')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_url.set_defaults(func=gaze_url)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('sources', help='Display spell sources (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_url.set_defaults(func=gaze_sources)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('source_urls', help='Display spell source file urls (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_url.set_defaults(func=gaze_source_urls)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('maintainer', help='Display spell maintainer (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_url.set_defaults(func=gaze_maintainer)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('compile', help='Display spell compile log (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_url.set_defaults(func=gaze_compile)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('install', help='Display Installed Files (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_url.set_defaults(func=gaze_install,install_display=False)

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('install-full', help='Display Installed Files (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_url.set_defaults(func=gaze_install,install_display='Full')

    # create the parser for the "what" command
    parser_url = subparsers.add_parser('install-spell', help='Display Installed Files (Not Working)')
    parser_url.add_argument('spell',
                             nargs='+',
                             help='Display System Info')
    parser_url.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_url.set_defaults(func=gaze_install,install_display='Spell')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('version', help='Display Spell version')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_version,multi=False)

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('versions', help='Display Spell version across all grimoires')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_version,multi=True)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('license', help='Display Spell License (Not Working)')
    parser_where.add_argument('spell',
                             nargs='+',
                             help='List of spells')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_where.set_defaults(func=gaze_license)

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('sum', help='Display spell CRC checksum (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_checksum,check_type='CRC')

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('md5sum', help='Display spell MD5/SHA sums (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_checksum,check_type='MD5')

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('size', help='Display spell size (Not Working)')
    parser_where.add_argument('spell',
                             nargs='*',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Enable debugging information')
    parser_where.set_defaults(func=gaze_size)

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('export', help='Export a list of installed spells and their config (Not Working)')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_export)

    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('import', help='Import config (Not Working)')
    parser_where.add_argument('snapshot',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--depreciated',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_import)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('grimoire', help='Display grimoire (Not Working)')
    parser_where.add_argument('grimoire',
                             nargs='+',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_grimoire,multi=False,display_format='console')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('grimoires', help='List all grimoires (Not Working)')
    parser_where.add_argument('grimoire',
                             nargs='+',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_grimoire,multi=True,display_format='console')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('html', help='Create an html file with all spells (Not Working)')
    parser_where.add_argument('grimoire',
                             nargs='*',
                             help='Limit spells to specified grimoires')
    parser_where.add_argument('-s','--source',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_grimoire,multi=False,display_format='html')


    # create the parser for the "versions" command
    parser_where = subparsers.add_parser('search', help='Search for ... (Not Working)')
    parser_where.add_argument('-n','--name',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('-s','--short',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('phrase',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_search)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('newer', help='Display spells newer than date (Not Working)')
    parser_where.add_argument('date',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_newer)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('older', help='Display spells older than date (Not Working)')
    parser_where.add_argument('date',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_older)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('from', help='Display spell that installs named file (Not Working)')
    parser_where.add_argument('filename',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_from)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('installed', help='Display installed spells(Not Working)')
    parser_where.add_argument('spell',
                             nargs='*',
                              help='If spell is specified, will print installed version for each spell listed')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_installed)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('section', help='Display grimoire section (Not Working)')
    parser_where.add_argument('section',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_section)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('voyeur', help='Watch spell compilation (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_file,filename='DEPENDS')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('DEPENDS', help='Display DEPENDS script (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_file,filename='DEPENDS')

        # create the parser for the "what" command
    parser_where = subparsers.add_parser('HISTORY', help='Display HISTORY script (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Spell')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_file,filename='HISTORY')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('history', help='Show spell history (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_file,filename='HISTORY')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('checkmd5s', help='Check MD5s (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_checksum,filename='checksum')

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('depends', help='Display spell dependency tree (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('level',
                             nargs='?',
                             help='Display System Info')
    parser_where.add_argument('--fast',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--required',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_depends)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('dependencies', help='Display tree of all spells that depend on spell (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('level',
                             nargs='?',
                             help='Display System Info')
    parser_where.add_argument('-c',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--no-optionals',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_dependencies)

    # create the parser for the "what" command
    parser_where = subparsers.add_parser('time', help='Display spell compile time (Not Working)')
    parser_where.add_argument('spell',
                             nargs=1,
                             help='Display System Info')
    parser_where.add_argument('--last',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--medium',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--mean',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--weight-last',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--full',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_time,system=False)

        # create the parser for the "what" command
    parser_where = subparsers.add_parser('time-system', help='Display time to compile all installed spells (Not Working)')
    parser_where.add_argument('--no-orphans',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--last',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--medium',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--mean',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--weight-last',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--full',
                             action='store_true',
                             help='Display System Info')
    parser_where.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_where.set_defaults(func=gaze_time,system=True)

    args = parser.parse_args()

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
