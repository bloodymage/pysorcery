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
#
#
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
from pysorcery import __version__, enable_debugging_mode
from pysorcery.lib import libtext
from pysorcery.lib import libconfig
from pysorcery.lib import libfiles
# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
# Allow Color text on console
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
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function archive_extract
#
#
#
#-------------------------------------------------------------------------------
def archive_extract(args):
    logger.debug('Begin Function')

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function archive_list
#
#
#
#-------------------------------------------------------------------------------
def archive_list(args):
    logger.debug('Begin Function')

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_create(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_test(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_repack(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_recompress(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_diff(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_search(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Functions archive_create
#
#
#
#-------------------------------------------------------------------------------
def archive_formats(args):
    logger.debug('Begin Function')

    logger.info('Tar:')
    
    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Real_Main
#
# 
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


    # Create subcommands
    subparsers = parser.add_subparsers(title = 'commands',
                                       metavar = 'Command',
                                       help = 'Description')
    # Enable aliases for subcommands
    parser.register('action',
                    'parsers',
                    argparse.AliasedSubParsersAction)

    # create the parser for the 'extract' command
    parser_extract = subparsers.add_parser('extract',
                                        help = 'Extract files')
    parser_extract.add_argument('file',
                             nargs = '+',
                             help = 'Extract files')
    parser_extract.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_extract.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_extract.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_extract.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_extract.set_defaults(func = archive_extract)

    # create the parser for the 'list' command
    parser_list = subparsers.add_parser('list',
                                        help = 'List files')
    parser_list.add_argument('file',
                             nargs = '+',
                             help = 'List files')
    parser_list.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_list.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_list.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_list.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_list.set_defaults(func = archive_list)

    # create the parser for the 'create' command
    parser_create = subparsers.add_parser('create',
                                        help = 'Create files')
    parser_create.add_argument('file',
                             nargs = '+',
                             help = 'Create files')
    parser_create.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_create.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_create.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_create.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_create.set_defaults(func = archive_create)

    # create the parser for the 'test' command
    parser_test = subparsers.add_parser('test',
                                        help = 'Test files')
    parser_test.add_argument('file',
                             nargs = '+',
                             help = 'Test files')
    parser_test.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_test.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_test.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_test.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_test.set_defaults(func = archive_test)

    # create the parser for the 'repack' command
    parser_repack = subparsers.add_parser('repack',
                                        help = 'Repack files')
    parser_repack.add_argument('file',
                             nargs = '+',
                             help = 'Repack files')
    parser_repack.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_repack.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_repack.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_repack.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_repack.set_defaults(func = archive_repack)

    # create the parser for the 'recompress' command
    parser_recompress = subparsers.add_parser('recompress',
                                        help = 'Recompress files')
    parser_recompress.add_argument('file',
                             nargs = '+',
                             help = 'Recompress files')
    parser_recompress.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_recompress.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_recompress.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_recompress.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_recompress.set_defaults(func = archive_recompress)

    # create the parser for the 'diff' command
    parser_diff = subparsers.add_parser('diff',
                                        help = 'Diff files')
    parser_diff.add_argument('file',
                             nargs = '+',
                             help = 'Diff files')
    parser_diff.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_diff.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_diff.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_diff.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_diff.set_defaults(func = archive_diff)


    # create the parser for the 'search' command
    parser_search = subparsers.add_parser('search',
                                        help = 'Search files')
    parser_search.add_argument('file',
                             nargs = '+',
                             help = 'Search files')
    parser_search.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_search.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_search.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_search.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_search.set_defaults(func = archive_search)


    # create the parser for the 'formats' command
    parser_formats = subparsers.add_parser('formats',
                                        help = 'Formats files')
    parser_formats.add_argument('-q', '--quiet',
                                 action = 'count',
                                 default = 0,
                                 help = quiet_help)

    if enable_debugging_mode:
        parser_formats.add_argument('-v', '--verbosity',
                                action = 'count',
                                default = 0,
                                help = verbose_help)
        parser_formats.add_argument('--loglevel',
                                choices = loglevel_choices,
                                help = loglevel_help)
        parser_formats.add_argument('--debug',
                                action = 'store_true',
                                help = debug_help)

    parser_formats.set_defaults(func = archive_formats)

    # Parser Groups
    logging_opts = parser.add_argument_group('Logging Options')

    logging_opts.add_argument('-q', '--quiet',
                              action = 'count',
                              default = 0,
                              help = quiet_help)

    if enable_debugging_mode is True:
        logging_opts.add_argument('-v', '--verbosity',
                                  action = 'count',
                                  default = 0,
                                  help = verbose_help)
        logging_opts.add_argument('--loglevel',
                                  choices = ['debug','info','warning',
                                           'error','critical',
                                           'DEBUG','INFO','WARNING',
                                           'ERROR','CRITICAL'],
                                  help = loglevel_help)
        logging_opts.add_argument('--debug',
                                  action = 'store_true',
                                  help = debug_help)

    # With version, help description must be before version declaration
    parser.add_argument('-V', '--version',
                        action = 'version',
                        help = 'Print version information and exit',
                        version = '%(prog)s ' + __version__)
    parser.set_defaults(func = False,
                        debug = False,
                        verbosity = 0,
                        loglevel = 'INFO')

    args = parser.parse_args()

    #if os.geteuid() != 0:
        # os.execvp() replaces the running process, rather than launching a child
        # process, so there's no need to exit afterwards. The extra 'sudo' in the
        # second parameter is required because Python doesn't automatically set $0
        # in the new process.
    #    os.execvp('sudo', ['sudo'] + sys.argv)

    config = libconfig.main_configure(args)

    logger.debug('Configuration set')
    logger.debug2('Configuration Settings: ' + str(config))
    logger.debug3('Arguments: ' + str(args))

    # 'application' code
    args.func(args)
    
#    logging.verifydebuglevels()
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

        logger.debug('Begin Application')
#        try:         
#            real_main(args)
        real_main(args)        
#        except:
#            logger.critical('You Fucked Up')

        logger.debug('End Application')
        return 0

if __name__ == '__main__':
    main()
