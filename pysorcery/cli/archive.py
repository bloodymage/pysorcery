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
import os
import sys

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
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
def archive_extract(args):
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
                    print(cfile.mimetype)
                    if args.cmd == 'extract':
                        if cfile.mimetype in mimetypes.ArchiveMimetypes:
                            cfile.extract(args.output_dir)
                        else:
                            cfile.decompress(args.output_dir)
                    elif args.cmd == 'create':
                        if cfile.mimetype in mimetypes.ArchiveMimetypes:
                            cfiles.create(args.output_dir)
                        else:
                            cfiles.compress(args.output_dir)
                    elif args.cmd == 'testarchive':
                        cfiles.testarchive()
                    elif args.cmd == 'listfiles':
                        cfiles.listfiles()
                    else:
                        logger.error('Improper Command')
                        logger.error("We Shouldn't be here")

        # Always extract what is explicitly listed
        #logger.info('Archive file: ' + i)
        cfile = lib.Files(i)
        if args.cmd == 'extract':
            if cfile.mimetype in mimetypes.ArchiveMimetypes:
                cfile.extract(args.output_dir)
            else:
                cfile.decompress(args.output_dir)
        elif args.cmd == 'create':
            if cfile.mimetype in mimetypes.ArchiveMimetypes:
                cfile.create(os.getcwd(), args.output_dir)
            else:
                cfile.compress(args.output_dir)
        elif args.cmd == 'testarchive':
            cfile.testarchive()
        elif args.cmd == 'listfiles':
            if cfile.mimetype in mimetypes.ArchiveMimetypes:
                cfile.listfiles()
            else:
                content = cfile.read()
                for line in content:
                    print(line)

        else:
            logger.error('Improper Command')
            logger.error("We Shouldn't be here")

    logger.debug('End Function')
    return

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
def archive_create(args):
    logger.debug('Begin Function')

    for i in args.files:
        cfile = lib.Files(i)
        if cfile.mimetype in mimetypes.ArchiveMimetypes:
            cfile.create(os.getcwd(), args.output_dir)
        else:
            cfile.compress(args.output_dir)

    logger.debug('End Function')
    return

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
def archive_list(args):
    logger.debug('Begin Function')

    for i in args.files:
        cfile = lib.Files(i)
        if cfile.mimetype in mimetypes.ArchiveMimetypes:
            cfile.listfiles()
        else:
            content = cfile.read()
            for line in content:
                print(line)

    logger.debug('End Function')
    return

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
def archive_test(args):
    logger.debug('Begin Function')

    for i in args.files:
        cfile = lib.Files(i)
        cfile.testarchive()

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_create
#
#
# Convert files from one archive or compression format to another
#
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
#         args.srcfile
#         args.dstfile
#
# Return: None
#
#-----------------------------------------------------------------------
def archive_repack(args):
    logger.debug('Begin Function')

    lib.repack(args.srcfile, args.dstfile)
    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_recompress
#
#
# Recompresses a file.
#
# Input:  args
#         args.quiet   - Decrease Output Verbosity
#         args.srcfile - Original File
#         args.dstfile - Destination File
#
# Return: None
#
#-----------------------------------------------------------------------
def archive_recompress(args):
    logger.debug('Begin Function')



    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_diff
#
#
# Find and display all differences between two archive filesxs
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Return: None
#
#-----------------------------------------------------------------------
def archive_diff(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_search
#
#
# Search archive for search term.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Return: None
#
#-----------------------------------------------------------------------
def archive_search(args):
    logger.debug('Begin Function')

    
    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Functions archive_formats
#
#
# List all archive and compression formats supported.
#
# Input:  args
#         args.quiet - Decrease Output Verbosity
# Return: None
#
#-----------------------------------------------------------------------
def archive_formats(args):
    logger.debug('Begin Function')

    format_groups = ['util_archive', 'util_compressed']

    cmd = 'archive_support'

    for x in format_groups:
        # Obtain list of all supported formats of type 'x'
        formats = util.get_cmd_types(x)

        # 
        for i in formats:
            logger.info(i + ' files:')

            # Identify function that displays formats support
            archive_func = util.get_module_func(x,
                                                i,
                                                cmd)
            
            # Execute the identified function
            archive_func()

    logger.debug('End Function')
    return

#-----------------------------------------------------------------------
#
# Real_Main
#
# 1. Creates the argument parser
# 2. Eshablishes configuration
# 3. Runs the function specified by the arguments
#
# Input:  args
# 
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

    # Parser for printing cmd version information
    parser.add_argument('-V',
                        '--version',
                        action = 'version',
                        help = 'Print version information and exit',
                        version = '%(prog)s ' + __version__
    )

    # Create Parent Parsur
    parent_parser = argparse.ArgumentParser(add_help=False)
    
    # Parser Groups
    # Logging Group
    logging_opts = parent_parser.add_argument_group('Logging Options')

    # Quiet Settings
    logging_opts.add_argument('-q',
                              '--quiet',
                              action = 'count',
                              default = 0,
                              help = quiet_help
    )

    # If debugging is enabled
    if DEBUG:
        # Verbose Options
        logging_opts.add_argument('-v',
                                  '--verbosity',
                                  action = 'count',
                                  default = 0,
                                  help = verbose_help
        )
        # Set Loglevel
        logging_opts.add_argument('--loglevel',
                                  choices = loglevel_choices,
                                  default = 'INFO',
                                  help = loglevel_help
        )

        # Maximize logging
        logging_opts.add_argument('--debug',
                                  action = 'store_true',
                                  help = debug_help
        )

    # Enable version in child parsers
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
    parser_extract.set_defaults(func=archive_extract)
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
    parser_list.set_defaults(func = archive_list) 

    #-----------------------------------------------------------------
    #
    # create the parser for the 'create' command
    #
    #-----------------------------------------------------------------
    parser_create = subparsers.add_parser('create',
                                          parents = [parent_parser],
                                          help = 'Create files')
    parser_create.add_argument('files',
                               nargs = 1,
                               metavar = 'archive',
                               help = 'Archive file to create')
    parser_create.add_argument('output_dir',
                               metavar = 'source',
                               help = 'Files / Directories to add to the archive')
    parser_create.set_defaults(func = archive_create)
    
    #-----------------------------------------------------------------
    #
    # create the test command
    #
    #-----------------------------------------------------------------
    parser_test = subparsers.add_parser('test',
                                        aliases = ['verify'],
                                        help = 'Test files')
    parser_test.add_argument('files',
                             nargs = 1,
                             metavar = 'archive',
                             help = 'Create files')
    parser_test.set_defaults(func = archive_test)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'repack' command
    #
    #-----------------------------------------------------------------
    parser_repack = subparsers.add_parser('repack',
                                          parents = [parent_parser],
                                          help = 'Repack files')
    parser_repack.add_argument('srcfile',
                               help = 'Original File')
    parser_repack.add_argument('dstfile',
                               help = 'Destination File')
    parser_repack.set_defaults(func = archive_repack)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'recompress' command
    #
    #-----------------------------------------------------------------
    parser_recompress = subparsers.add_parser('recompress',
                                              parents = [parent_parser],
                                              help = 'Recompress files'
    )
    parser_recompress.add_argument('srcfile',
                                   help = 'Source file')
    parser_recompress.add_argument('dstfile',
                                   help = 'Destination file')
    parser_recompress.set_defaults(func = archive_recompress)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'diff' command
    #
    #-----------------------------------------------------------------
    parser_diff = subparsers.add_parser('diff',
                                        parents = [parent_parser],
                                        help = 'Compare Archive Files')
    parser_diff.add_argument('archive1',
                             help = 'Archives to compare')
    parser_diff.add_argument('archive2',
                             help = 'Archives to compare')
    parser_diff.set_defaults(func = archive_diff)

    #-----------------------------------------------------------------
    #
    # create the parser for the 'search' command
    #
    #-----------------------------------------------------------------
    parser_search = subparsers.add_parser('search',
                                          parents = [parent_parser],
                                          help = 'Search archive')
    parser_search.add_argument('archive',
                             help = 'Archive to search')
    parser_search.add_argument('searchterm',
                             nargs = '+',
                             help = 'Term to search for')
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


#-----------------------------------------------------------------------
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
#
#
# Note: Any cli switches will override the settings in the config files
#
#-----------------------------------------------------------------------
def main(args=None):
    """Run the main command-line interface for pyarchive. Includes 
    top-level exception handlers that print friendly error messages.
    """

    logger.debug('Begin Application')
    try:         
        real_main(args)
    except:
        logger.critical('You Fucked Up')

    logger.debug('End Application')
    return

#-----------------------------------------------------------------------
#
#
#
#-----------------------------------------------------------------------
if __name__ == '__main__':
    sys.exit(main())
