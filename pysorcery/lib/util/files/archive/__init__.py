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
# Additional code from 'patool'
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# File: pysorcery/lib/util/files/archive/__init__.py
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
# This implements the archive classes
#
# ...
#
#-----------------------------------------------------------------------
"""
Impliments classes for working with archive files.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import os

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
from pysorcery.lib.system import shutil
# Other Application Libraries
from pysorcery.lib import util
from pysorcery.lib.util import files

# Condiional Libraries
try:
    # use Python 3 lzma module if available
    import lzma
    py_lzma = ('py_lzma',)
except ImportError:
    py_lzma = ()


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

# Supported archive commands
ArchiveCommands = ('list', 'extract', 'test', 'create')

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract, ...)
# Programs starting with "py_" are Python modules.
ArchivePrograms = {
    'ace': {
        'extract': ('unace',),
        'test': ('unace',),
        'list': ('unace',),
    },
    'adf': {
        'extract': ('unadf',),
        'test': ('unadf',),
        'list': ('unadf',),
    },
    'alzip': {
        'extract': ('unalz',),
        'test': ('unalz',),
        'list': ('unalz',),
    },
    'ape': {
        'create': ('mac',),
        'extract': ('mac',),
        'list': ('py_echo',),
        'test': ('mac',),
    },
    'ar': {
        None: ('ar',),
    },
    'arc': {
        None: ('arc',),
        'extract': ('nomarch',),
        'test': ('nomarch',),
        'list': ('nomarch',),
    },
    'bzip2': {
        None: ('7z', '7za'),
        'extract': ('pbzip2', 'lbzip2', 'bzip2', 'py_bz2'),
        'test': ('pbzip2', 'lbzip2', 'bzip2'),
        'create': ('pbzip2', 'lbzip2', 'bzip2', 'py_bz2'),
        'list': ('py_echo'),
    },
    'cab': {
        'extract': ('cabextract', '7z'),
        'create': ('lcab',),
        'list': ('cabextract', '7z'),
        'test': ('cabextract', '7z'),
    },
    'chm': {
        'extract': ('archmage', 'extract_chmLib'),
        'test': ('archmage',),
    },
    'flac': {
        'extract': ('flac',),
        'test': ('flac',),
        'create': ('flac',),
        'list': ('py_echo',),
    },
    'tar': {
        None: ('tar', 'star', 'bsdtar', 'py_tarfile'),
    },
    'zip': {
        None: ('7z', '7za', 'py_zipfile'),
        'extract': ('unzip',),
        'list': ('unzip',),
        'test': ('zip', 'unzip',),
        'create': ('zip',),
    },
    'gzip': {
        None: ('7z', '7za', 'pigz', 'gzip'),
        'extract': ('py_gzip',),
        'create': ('zopfli', 'py_gzip'),
    },
    'iso': {
        'extract': ('7z',),
        'list': ('7z', 'isoinfo'),
        'test': ('7z',),
        'create': ('genisoimage',),
    },
    'lzh': {
        None: ('lha',),
        'extract': ('lhasa',),
    },
    'lzip': {
        'extract': ('plzip', 'lzip', 'clzip', 'pdlzip'),
        'list': ('py_echo',),
        'test': ('plzip', 'lzip', 'clzip', 'pdlzip'),
        'create': ('plzip', 'lzip', 'clzip', 'pdlzip'),
    },
    'lrzip': {
        'extract': ('lrzip',),
        'list': ('py_echo',),
        'test': ('lrzip',),
        'create': ('lrzip',),
    },
    'compress': {
        'extract': ('gzip', '7z', '7za', 'uncompress.real'),
        'list': ('7z', '7za', 'py_echo',),
        'test': ('gzip', '7z', '7za'),
        'create': ('compress',),
    },
    '7z': {
        None: ('7z', '7za', '7zr'),
    },
    'rar': {
        None: ('rar',),
        'extract': ('unrar', '7z'),
        'list': ('unrar', '7z'),
        'test': ('unrar', '7z'),
    },
    'arj': {
        None: ('arj',),
        'extract': ('7z',),
        'list': ('7z',),
        'test': ('7z',),
    },
    'cpio': {
        'extract': ('cpio', 'bsdcpio', '7z'),
        'list': ('cpio', 'bsdcpio', '7z'),
        'test': ('cpio', 'bsdcpio', '7z',),
        'create': ('cpio', 'bsdcpio'),
    },
    'rpm': {
        'extract': ('rpm2cpio', '7z'),
        'list': ('rpm', '7z', '7za'),
        'test': ('rpm', '7z'),
    },
    'deb': {
        'extract': ('dpkg-deb', '7z'),
        'list': ('dpkg-deb', '7z'),
        'test': ('dpkg-deb', '7z'),
    },
    'dms': {
        'extract': ('xdms',),
        'list': ('xdms',),
        'test': ('xdms',),
    },
    'lzop': {
        None: ('lzop',),
    },
    'lzma': {
        'extract': ('7z', 'lzma', 'xz') + py_lzma,
        'list': ('7z', 'py_echo'),
        'test': ('7z', 'lzma', 'xz'),
        'create': ('lzma', 'xz') + py_lzma,
    },
    'rzip': {
        'extract': ('rzip',),
        'list': ('py_echo',),
        'create': ('rzip',),
    },
    'shar': {
        'create': ('shar',),
        'extract': ('unshar',),
    },
    'shn': {
        'extract': ('shorten',),
        'list': ('py_echo',),
        'create': ('shorten',),
    },
    'vhd': {
        'extract': ('7z',),
        'list': ('7z',),
        'test': ('7z',),
    },
    'xz': {
        None: ('xz', '7z'),
        'extract': py_lzma,
        'create': py_lzma,
    },
    'zoo': {
        None: ('zoo',),
    },
    'zpaq': {
        None: ('zpaq',),
    },
}

# List those programs that have different python module names because of
# Python module naming restrictions.
ProgramModules = {
    '7z': 'p7zip',
    '7za': 'p7azip',
    '7zr': 'p7rzip',
    'uncompress.real': 'uncompress',
    'dpkg-deb': 'dpkg',
    'extract_chmlib': 'chmlib',
}

#-----------------------------------------------------------------------
#
# Classes
#
# Archive
# Archives
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Archive(files.BaseFile):        
    #-------------------------------------------------------------------
    #
    # Function extract
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def extract(self,
                verbosity=0,
                outdir=None,
                program=None,
                interactive=True):
        logger.debug('Begin Function')

        """Extract given archive."""
        #util.check_existing_filename(archive)
        logger.info("Extracting %s ..." % self.filename)
        _extract_archive(self.filename, verbosity=verbosity, interactive=interactive, outdir=outdir, program=program)

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function create
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def create(self, root_dir=None, base_dir=None, compression_lvl=9):
        logger.debug('Begin Function')
        
        shutil.make_archive(self.basename,
                            self.format_,
                            root_dir,
                            base_dir)

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function listfiles
    #
    # This is the base File Class
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def listfiles(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'listfiles')
        # We know what the format is, initialize that format's class
        file_content = archive_func(self.filename)
        
        logger.debug('End Function')
        return file_content

    #-------------------------------------------------------------------
    #
    # Function testarchive
    #
    # Test to ensure the archive is a valid archive
    #
    # Inputs
    # ------
    #     self:
    #
    # Returns
    # -------
    #     None (change this to True or False?)
    #
    # Raises
    # ------
    #
    # 
    #-------------------------------------------------------------------
    def testarchive(self):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'testarchive')
        # We know what the format is, initialize that format's class
        if archive_func(self.filename):
            logger.info(str(self.filename) + ' is a valid, readable archive')
        else:
            logger.error(str(self.filename) + ' is not a valid, readable archive')
            
        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function search
    #
    # Searches archive files
    #
    # Inputs
    # ------
    #     self:
    #     searchstring:
    #
    # Returns
    # -------
    #     result
    #
    # Raises
    # ------
    #
    #
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug('Begin Function')

        archive_func = util.get_module_func('util_archive',
                                            self.format_class,
                                            'search')

        results = archive_func(self.filename, searchstring)
        
        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class Archives(files.BaseFiles):
    #-------------------------------------------------------------------
    #
    # Function search
    #
    # Searches archive files
    #
    # Inputs
    # ------
    #     self:
    #     searchstring:
    #
    # Returns
    # -------
    #     result
    #
    # Raises
    # ------
    #
    #-------------------------------------------------------------------
    def diff(self):
        logger.debug('Begin Function')

        results = "A + B"
        
        logger.debug('End Function')
        return results

#-----------------------------------------------------------------------
#
# Functions
#
# find_archive_program
# _extract_archive
#
#-----------------------------------------------------------------------
def program_supports_compression (program, compression):
    """Decide if the given program supports the compression natively.
    @return: True iff the program supports the given compression format
      natively, else False.
    """
    if program in ('tar', 'star', 'bsdtar', 'py_tarfile'):
        return compression in ('gzip', 'bzip2') + py_lzma
    return False


def get_archive_format (filename):
    """Detect filename archive format and optional compression."""
    mime, compression = mimetypes.guess_type(filename)
    if not (mime or compression):
        raise Exception("unknown archive format for file `%s'" % filename)
    if mime in mimetypes.ArchiveMimetypes:
        format = mimetypes.ArchiveMimetypes[mime]
    else:
        raise Exception("unknown archive format for file `%s' (mime-type is `%s')" % (filename, mime))
    if format == compression:
        # file cannot be in same format compressed
        compression = None
    return format, compression

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def p7zip_supports_rar():
    """Determine if the RAR codec is installed for 7z program."""
    if os.name == 'nt':
        # Assume RAR support is compiled into the binary.
        return True
    # the subdirectory and codec name
    codecname = 'p7zip/Codecs/Rar29.so'
    # search canonical user library dirs
    for libdir in ('/usr/lib', '/usr/local/lib', '/usr/lib64', '/usr/local/lib64', '/usr/lib/i386-linux-gnu', '/usr/lib/x86_64-linux-gnu'):
        fname = os.path.join(libdir, codecname)
        if os.path.exists(fname):
            return True
    return False

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def find_archive_program (format_, command, program=None):
    """Find suitable archive program for given format and mode."""
    commands = ArchivePrograms[format_]
    programs = []
    if program is not None:
        # try a specific program first
        programs.append(program)
    # first try the universal programs with key None
    for key in (None, command):
        if key in commands:
            programs.extend(commands[key])
    if not programs:
        raise Exception("%s archive format `%s' is not supported" % (command, format))
    # return the first existing program
    for program in programs:
        if program.startswith('py_'):
            # it's a Python module and therefore always supported
            return program
        exe = util.find_program(program)
        if exe:
            if program == '7z' and format == 'rar' and not p7zip_supports_rar():
                continue
            return exe
    # no programs found
    raise Exception("could not find an executable program to %s format %s; candidates are (%s)," % (command, format, ",".join(programs)))

def check_program_compression(archive, command, program, compression):
    """Check if a program supports the given compression."""
    program = os.path.basename(program)
    if compression:
        # check if compression is supported
        if not program_supports_compression(program, compression):
            if command == 'create':
                comp_command = command
            else:
                comp_command = 'extract'
            comp_prog = find_archive_program(compression, comp_command)
            if not comp_prog:
                msg = "cannot %s archive `%s': compression `%s' not supported"
                raise util.PatoolError(msg % (command, archive, compression))

#-----------------------------------------------------------------------
#
# Class Archive
#
# This is the base File Class
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def _extract_archive(archive, verbosity=0, interactive=True, outdir=None,
                     program=None, format_=None, compression=None):
    """Extract an archive.
    @return: output directory if command is 'extract', else None
    """
    if format_ is None:
        format_, compression = get_archive_format(archive)
    mimetypes.check_type(format_, compression)
    program = find_archive_program(format_, 'extract', program=program)
    check_program_compression(archive, 'extract', program, compression)
    get_archive_cmdlist = util.get_module_func(program, 'extract', format_)
    if outdir is None:
        outdir = util.tmpdir(dir=".")
        do_cleanup_outdir = True
    else:
        do_cleanup_outdir = False
    try:
        cmdlist = get_archive_cmdlist(archive, compression, program, verbosity, interactive, outdir)
        if cmdlist:
            # an empty command list means the get_archive_cmdlist() function
            # already handled the command (eg. when it's a builtin Python
            # function)
            run_archive_cmdlist(cmdlist, verbosity=verbosity)
        if do_cleanup_outdir:
            target, msg = cleanup_outdir(outdir, archive)
        else:
            target, msg = outdir, "`%s'" % outdir
        if verbosity >= 0:
            util.log_info("... %s extracted to %s." % (archive, msg))
        return target
    finally:
        # try to remove an empty temporary output directory
        if do_cleanup_outdir:
            try:
                os.rmdir(outdir)
            except OSError:
                pass
