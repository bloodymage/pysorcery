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

from pysorcery import __version__, DEBUG
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
class CommonParser(ArgumentParser):
    def __init__(self, *args, **kwargs):
        super(CommonParser, self).__init__(*args, **kwargs)

        return

    def add_version_option(self):
        self.add_argument('-V',
                          '--version',
                          action = 'version',
                          help = 'Print version information and exit',
                          version = '%(prog)s ' + __version__
        )
        return

    def add_logging_option(self):
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

        # Create Parent Parsur
        self.parent = argparse.ArgumentParser(add_help=False)
    
        # Parser Groups
        # Logging Group
        self.logging = self.parent.add_argument_group('Logging Options')

        # Quiet Settings
        self.logging.add_argument('-q',
                                  '--quiet',
                                  action = 'count',
                                  default = 0,
                                  help = quiet_help
        )

        # If debugging is enabled
        if DEBUG:
            # Verbose Options
            self.logging.add_argument('-v',
                                      '--verbosity',
                                      action = 'count',
                                      default = 0,
                                      help = verbose_help
            )
            # Set Loglevel
            self.logging.add_argument('--loglevel',
                                      choices = loglevel_choices,
                                      default = 'INFO',
                                      help = loglevel_help
            )

            # Maximize logging
            self.logging.add_argument('--debug',
                                      action = 'store_true',
                                      help = debug_help
            )

        return self.parent
        


