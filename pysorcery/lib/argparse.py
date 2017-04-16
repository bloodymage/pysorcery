#!/usr/bin/env python3
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
#
#
#
#-------------------------------------------------------------------------------

"""Aliases for argparse positional arguments."""

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------
import argparse
from argparse import *

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Classes
#
# AliasedSubParserAction
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class AliasedSubParserAction
#
#-------------------------------------------------------------------------------
class AliasedSubParsersAction(argparse._SubParsersAction):

    #-------------------------------------------------------------------------------
    #
    # Class AliasedPseudoAction
    #
    #-------------------------------------------------------------------------------
    class _AliasedPseudoAction(Action):
        #---------------------------------------------------------------------------
        #
        # Function __init__
        #
        #
        #
        # Input:  ...
        # Output: ...
        # Return: ...
        #
        #-------------------------------------------------------------------------
        def __init__(self, name, aliases, help):
            dest = name
            if aliases:
                dest += ' (%s)' % ','.join(aliases)
            sup = super(AliasedSubParsersAction._AliasedPseudoAction, self)
            sup.__init__(option_strings=[], dest=dest, help=help) 

    #-------------------------------------------------------------------------------
    #
    # Function add_parser
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def add_parser(self, name, **kwargs):
        if 'aliases' in kwargs:
            aliases = kwargs['aliases']
            del kwargs['aliases']
        else:
            aliases = []

        parser = super(AliasedSubParsersAction, self).add_parser(name, **kwargs)

        # Make the aliases work.
        for alias in aliases:
            self._name_parser_map[alias] = parser
        # Make the help text reflect them, first removing old help entry.
        if 'help' in kwargs:
            help = kwargs.pop('help')
            self._choices_actions.pop()
            pseudo_action = self._AliasedPseudoAction(name, aliases, help)
            self._choices_actions.append(pseudo_action)

        return parser

#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# ...
#
#
#
#-------------------------------------------------------------------------------
if __name__ == '__main__':
    # An example parser with subcommands.
    
    parser = ArgumentParser()
    parser.register('action', 'parsers', AliasedSubParsersAction)
    parser.add_argument("--library", metavar="libfile", type=str,
        help="library database filename")
    subparsers = parser.add_subparsers(title="commands", metavar="COMMAND")

    p_import = subparsers.add_parser("import", help="add files to library",
                                     aliases=('imp', 'im'))
    p_import.add_argument("filename", metavar="file", type=str, nargs="+",
        help="the files to import")

    p_remove = subparsers.add_parser("remove", aliases=('rm',),
        help="remove items")
    
    args = parser.parse_args()
    print(args)
