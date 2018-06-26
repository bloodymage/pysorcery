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
# File: pysorcery/plugins/gaze/from.py
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
# pyGaze: from
#
# ...
#
#-----------------------------------------------------------------------
"""
pyGaze: from

...
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
# gaze_from
# parser
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function gaze_from
#
# find out which spell has installed path/file
#
# Matching is done literally against the end of the path names in the
# lists of installed files. If -regex is passed, the matching is done
# using basic regular expressions against the whole paths in the lists
# of installed files.
#
# Inputs
# ------
#    @param: args
#            args.spell - Spell to print compile log.
#                         Maximum 1
#            args.quiet - decrease verbosity
#
# Returns
# -------
#    @return: None
#
#-----------------------------------------------------------------------
def gaze_from(args):
    logger.debug('Begin Function')

    file_ = lib.File(args.filename[0])
    spells = file_.get_from()

    for spell in spells:
        print(spell)

    logger.debug('End Function')
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

    cmd_help = "find out which spell has installed 'path/file.'  Matching is done literally against the end of the path names in the lists of installed files."
    cmd = subparsers.add_parser('from',
                             parents = parent_parsers,
                             help = cmd_help
    )
    cmd.add_argument('filename',
                     nargs = 1,
                     help = 'Display System Info'
    )
    cmd.add_argument('-r','-regex','--regex',
                     action = 'store_true',
                     help = 'Matching using basic regular expressions against the whole paths in the lists of installed files.'
    )        
    cmd.set_defaults(func = gaze_from,
                     sudo = False)
    return cmd
