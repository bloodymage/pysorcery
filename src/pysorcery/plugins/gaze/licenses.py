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
# File: pysorcery/plugins/gaze/licenses.py
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
# pyGaze: Licenses
#
#   This plugin displays license information.  If a license is provided
#   as input, the license will be displayed.  If a package is provided
#   as input, the package license will be identified.
#
#-----------------------------------------------------------------------
"""
pyGaze: licenses

This plugin displays license information.  If a license is provided as
input, the license will be displayed.  If a package is provided as 
input, the package license will be identified.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import lib
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
# gaze_licenses
# parser
#
#-----------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function gaze_license
#
# View the license(s) of the given spell(s), or spells in given section(s),
# or view the information about given license(s)
#
# Inputs
# ------
#    @param: args
#            args.spell    - Spell to print compile log.
#                            Maximum 1
#            args.grimoire -
#            args.quiet    - decrease verbosity
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------------------
def gaze_license(args):
    """
Function gaze_license

View the license(s) of the given spell(s), or spells in given section(s),
or view the information about given license(s)

Inputs
------
   @param: args
           args.spell    - Spell to print compile log.
                           Maximum 1
           args.grimoire -
           args.quiet    - decrease verbosity

Returns
-------
   @return: None

Raises
------
   ...
"""

    config_ = config.SorceryConfig()
    license_dir = config_.license_dir

    directory = lib.Directory(license_dir)
    licenses = directory.listfiles()

    if args.ssl[0] in licenses:
        license_ = lib.File(license_dir + '/' + args.ssl[0])
        content = license_.read()
        for line in content:
            print(line)
    else:
        package = lib.Package(args.ssl[0])
        if package.is_package():
            print(package.get_license())
        else:
            raise NotImplementedError

    #logger.debug('End Function')
    return


#-----------------------------------------------------------------------
#
# Function parser
#
# Create subcommand parsing options
#
# Inputs
# ------
#    @param: *args    - tuple of all subparsers and parent parsers
#                       args[0]: the subparser
#                       args[1:] the parent parsers
#    @param: **kwargs - Not used (Future?)
#
# Returns
# -------
#    @return: cmd
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def parser(*args, **kwargs):
    subparsers = args[0]
    parent_parsers = list(args[1:])

    cmd_help = 'View the license(s) of the given spell(s), or spells in given section(s), or view the information about given license(s).'
    cmd = subparsers.add_parser('license',
                                parents = parent_parsers,
                                help = cmd_help
    )
    cmd.add_argument('ssl',
                     nargs = '+',
                     help = 'Spell, Section, or License to view'
    )
    cmd.set_defaults(func = gaze_license,
                     sudo = False)
    return cmd
