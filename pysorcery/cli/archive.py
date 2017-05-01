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
import argparse
import sys

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import *
from pysorcery import lib
from pysorcery.lib.util import config
from pysorcery.lib.util.files import archive
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

#-----------------------------------------------------------------------
#
# Function archive_extract
#
# Extract files listed.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.files - List of files to extract
#         args.recursive - Extract all files in all subfolders
#         args.depth (Add me) - if recursive, limit to depth #
#         args.output_dir - Directory to extract to
# Return: None
#
#-----------------------------------------------------------------------
def archive_file(args):
    logger.debug('Begin Function')

    for i in args.files:
        # Check for recursive extraction
        if args.recursive:
            # If True, extract all compressed files within a directory and
            # its sub directories
            #
            # Fix me! Add max depth option
            for root, dirs, files in os.walk(i):
                for sfile in files:
                    cfile = lib.Files(sfile)
                    cfile.archive(args.cmd, args.output_dir)
        # Always extract what is explicitly listed
        logger.info('Extracting file: ' + i)
        cfile = lib.Files(i)
        cfile.archive(args.cmd, args.output_dir)

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Function archive_list
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_list(args):
    logger.debug('Begin Function')

    for i in args.files:
        if args.recursive:
            for root, dirs, files in os.walk(i):
                for sfile in files:
                    cfile = lib.CompressedFile(sfile)
                    cfile.list_files()
                    
        print('Extracting file: ' + i)
        cfile = lib.CompressedFile(i)
        cfile.list_files()

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_create(args):
    logger.debug('Begin Function')

    newarchive = lib.CompressedFile(args.archive)

    for i in args.source:
        newarchive.compress(i)
    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_test(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_repack(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_recompress(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_diff(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_search(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None
#
#-----------------------------------------------------------------------
def archive_formats(args):
    logger.debug('Begin Function')

    formats = archive.get_archive_formats()

    cmd = 'archive_support'
    
    for i in formats:
        logger.info(i + ' files:')

        archive_func = archive.get_archive_cmd_func(i,
                                                    cmd)
        # We know what the format is, initialize that format's class
        archive_func()

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Real_Main
#
#
# Find and display all files which are not currently tracked by the
# sorcery package management system
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Output: Prints list of alien files
# Return: None 
#
#-----------------------------------------------------------------------
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
    epilog_text = """
See man pyarchive() for more information.\n
\n
Report bugs to ...
"""

    # Parse Command Line Arguments
    parser = argparse.ArgumentParser(
        description = 'Universal archive extractor. creator, etc...',
        epilog = epilog_text
    )
    parser.add_argument('-V',
                        '--version',
                        action = 'version',
                        help = 'Print version information and exit',
                        version = '%(prog)s ' + __version__
    )
    parent_parser = argparse.ArgumentParser(add_help=False)
    # Parser Groups
    logging_opts = parent_parser.add_argument_group('Logging Options')
    logging_opts.add_argument('-q',
                              '--quiet',
                              action = 'count',
                              default = 0,
                              help = quiet_help
    )
    if DEBUG:
        logging_opts.add_argument('-v',
                                  '--verbosity',
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
    parent_parser.add_argument('-V',
                        '--version',
                        action = 'version',
                        help = 'Print version information and exit',
                        version = '%(prog)s ' + __version__
    )

    # Create subcommands
    subparsers = parser.add_subparsers(title = 'commands',
                                       metavar = 'Command',
                                       help = 'Description'
    )
    #-----------------------------------------------------------------
    #
    # create the parser for the 'extract' command
    #
    #-----------------------------------------------------------------
    parser_extract = subparsers.add_parser('extract',
                                           parents = [parent_parser],
                                           help = 'Extract files'
    )
    parser_extract.add_argument('files',
                                nargs = '+',
                                help = 'Extract files'
    )
    parser_extract.add_argument('-o',
                                '--output-dir',
                                metavar = 'DIRECTORY',
                                help = 'Output Directory'
    )
    parser_extract.add_argument('-r', '--recursive',
                                action = 'store_true',
                                help = 'Recursive'
    )
    parser_extract.set_defaults(func=archive_file,
                                cmd='extract')
    #-----------------------------------------------------------------
    #
    # create the parser for the 'list' command
    #
    #-----------------------------------------------------------------
    parser_list = subparsers.add_parser('list',
                                        parents = [parent_parser],
                                        help = 'List files')
    parser_list.add_argument('files',
                             nargs = '+',
                             help = 'List files')
    parser_list.add_argument('-r', '--recursive',
                                action = 'store_true',
                                help = 'Recursive')
    parser_list.set_defaults(func = archive_file,
                             cmd='listfiles')

    #-----------------------------------------------------------------
    #
    # create the parser for the 'create' command
    #
    #-----------------------------------------------------------------
    parser_create = subparsers.add_parser('create',
                                          parents = [parent_parser],
                                          help = 'Create files')
    parser_create.add_argument('archive',
                               nargs = 1,
                               help = 'Create files')
    parser_create.add_argument('source',
                               nargs = '+',
                               help = 'Files / Directories to add to the archive')
    parser_create.set_defaults(func = archive_file,
                               cmd = 'create')
    #-----------------------------------------------------------------
    #
    # create the test command
    #
    #-----------------------------------------------------------------
    parser_test = subparsers.add_parser('test',
                                        aliases = ['verify'],
                                        help = 'Test files')
    parser_test.add_argument('archive',
                             nargs = 1,
                             help = 'Create files')
    parser_test.add_argument('source',
                             nargs = '+',
                             help = 'Files / Directories to add to the archive')
    parser_test.set_defaults(func = archive_file,
                             cmd = 'testarchive')

    #-----------------------------------------------------------------
    #
    # create the parser for the 'repack' command
    #
    #-----------------------------------------------------------------
    parser_repack = subparsers.add_parser('repack',
                                          parents = [parent_parser],
                                          help = 'Repack files')
    parser_repack.add_argument('file',
                               nargs = '+',
                               help = 'Repack files')
    parser_repack.set_defaults(func = archive_file,
                               cmd = 'repack')

    #-----------------------------------------------------------------
    #
    # create the parser for the 'recompress' command
    #
    #-----------------------------------------------------------------
    parser_recompress = subparsers.add_parser('recompress',
                                              parents = [parent_parser],
                                              help = 'Recompress files'
    )
    parser_recompress.add_argument('file',
                             nargs = '+',
                             help = 'Recompress files')
    parser_recompress.set_defaults(func = archive_file,
                                   cmd = 'recompress')

    #-----------------------------------------------------------------
    #
    # create the parser for the 'diff' command
    #
    #-----------------------------------------------------------------
    parser_diff = subparsers.add_parser('diff',
                                        parents = [parent_parser],
                                        help = 'Diff files')
    parser_diff.add_argument('file',
                             nargs = 2,
                             help = 'Diff files')
    parser_diff.set_defaults(func = archive_diff)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'search' command
    #
    #-----------------------------------------------------------------
    parser_search = subparsers.add_parser('search',
                                          parents = [parent_parser],
                                          help = 'Search files')
    parser_search.add_argument('file',
                             nargs = '+',
                             help = 'Search files')
    parser_search.set_defaults(func = archive_search)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'formats' command
    #
    #-----------------------------------------------------------------
    parser_formats = subparsers.add_parser('formats',
                                           parents = [parent_parser],
                                           help = 'Formats files')
    parser_formats.set_defaults(func = archive_formats)

    # With version, help description must be before version declaration
    parser.set_defaults(func = False,
                        quiet = 0,
                        verbosity = 0,
                        debug = False,
                        loglevel = 'INFO')
    
    args = parser.parse_args()

    # Set configuration
    config_ = config.main_configure(args)

    logger.debug('Configuration set')
    logger.debug2('Configuration Settings: ' + str(config_))
    logger.debug3('Arguments: ' + str(args))

    # 'application' code
    if args.func:
        args.func(args)
    else:
        parser.print_help()
        logger.error('No command was given')

    #logging.verifydebuglevels()
    logger.debug('End Function')
    return


#-----------------------------------------------------------------------#
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
#-----------------------------------------------------------------------
def main(args=None):
    """Run the main command-line interface for pyarchive. Includes 
    top-level exception handlers that print friendly error messages.
    """

    logger.debug('Begin Application')
    #try:         
        #real_main(args)
    real_main(args)        
    #except:
    #    logger.critical('You Fucked Up')

    logger.debug('End Application')
    return

#-----------------------------------------------------------------------
#
#
#
#-----------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(main())
