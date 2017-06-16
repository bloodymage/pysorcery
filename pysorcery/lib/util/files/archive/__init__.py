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
import stat

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
    def create(self, filenames, verbosity=0, program=None, interactive=True):
        """Create given archive with given files."""
        util.check_new_filename(self.filename)
        util.check_archive_filelist(filenames)
        if verbosity >= 0:
            logger.info("Creating %s ..." % self.filename)
            res = _create_archive(self.filename, filenames, verbosity=verbosity,
                                  interactive=interactive, program=program)
            if verbosity >= 0:
                logger.info("... %s created." % self.filename)
        return res

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
    def listfiles(self, verbosity=1, program=None, interactive=True):
        """List given archive."""
        # Set default verbosity to 1 since the listing output should be visible.
        util.check_existing_filename(self.filename)
        if verbosity >= 0:
            logger.info("Listing %s ..." % self.filename)
            return _handle_archive(self.filename, 'list', verbosity=verbosity,
                                   interactive=interactive, program=program)

    def recompress_archive(self, verbosity=0, interactive=True):
        """Recompress an archive to hopefully smaller size."""
        util.check_existing_filename(self.filename)
        util.check_writable_filename(self.filename)
        if verbosity >= 0:
            logger.info("Recompressing %s ..." % (self.filename,))
        res = _recompress_archive(self.filename,
                                  verbosity=verbosity,
                                  interactive=interactive)
        if res and verbosity >= 0:
            logger.info(res)
        return 0

    def repack_archive (self, archive_new, verbosity=0, interactive=True):
        """Repack archive to different file and/or format."""
        util.check_existing_filename(self.filename)
        util.check_new_filename(archive_new)
        if verbosity >= 0:
            logger.info("Repacking %s to %s ..." % (self.filename, archive_new))
        res = _repack_archive(self.filename, archive_new, verbosity=verbosity, interactive=interactive)
        if verbosity >= 0:
            logger.info("... repacking successful.")
        return res
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
    def search(self, pattern, verbosity=0, interactive=True):
        """Search pattern in archive members."""
        if not pattern:
            raise Exception("empty search pattern")
        util.check_existing_filename(self.filename)
        if verbosity >= 0:
            logger.info("Searching %r in %s ..." % (pattern, self.filename))
        res = _search_archive(pattern,
                              self.filename,
                              verbosity=verbosity,
                              interactive=interactive)
        if res == 1 and verbosity >= 0:
            logger.info("... %r not found" % pattern)
        return res

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
    def diff(self, verbosity=0, interactive=True):
        logger.debug('Begin Function')

        """Print differences between two archives."""
        util.check_existing_filename(self.files[0])
        util.check_existing_filename(self.files[1])
        if verbosity >= 0:
            logger.info("Comparing %s with %s ..." % (self.files[0], self.files[1]))
            res = _diff_archives(self.files[0],
                                 self.files[1],
                                 verbosity=verbosity,
                                 interactive=interactive)
        if res == 0 and verbosity >= 0:
            logger.info("... no differences found.")
        
        logger.debug('End Function')
        return res

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

def check_archive_format (format, compression):
    """Make sure format and compression is known."""
    if format not in mimetypes.ArchiveFormats:
        raise Exception("unknown archive format `%s'" % format)
    if compression is not None and compression not in mimetypes.ArchiveCompressions:
        raise Exception("unkonwn archive compression `%s'" % compression)

def list_formats ():
    """Print information about available archive formats to stdout."""
    #print("Archive programs of", App)
    print("Archive programs are searched in the following directories:")
    print(util.system_search_path())
    print()
    for format in mimetypes.ArchiveFormats:
        print(format, "files:")
        for command in ArchiveCommands:
            programs = ArchivePrograms[format]
            if command not in programs and None not in programs:
                print("   %8s: - (not supported)" % command)
                continue
            try:
                program = find_archive_program(format, command)
                print("   %8s: %s" % (command, program), end=' ')
                if format == 'tar':
                    encs = [x for x in mimetypes.ArchiveCompressions if util.find_program(x)]
                    if encs:
                        print("(supported compressions: %s)" % ", ".join(encs), end=' ')
                elif format == '7z':
                    if util.p7zip_supports_rar():
                        print("(rar archives supported)", end=' ')
                    else:
                        print("(rar archives not supported)", end=' ')
                print()
            except Exception:
                # display information what programs can handle this archive format
                handlers = programs.get(None, programs.get(command))
                print("   %8s: - (no program found; install %s)" %
                      (command, util.strlist_with_or(handlers)))

#-----------------------------------------------------------------------
#
# Function _extract_archive
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

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
# Function _extract_archive
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
def move_outdir_orphan (outdir):
    """Move a single file or directory inside outdir a level up.
    Never overwrite files.
    Return (True, outfile) if successful, (False, reason) if not."""
    entries = os.listdir(outdir)
    if len(entries) == 1:
        src = os.path.join(outdir, entries[0])
        dst = os.path.join(os.path.dirname(outdir), entries[0])
        if os.path.exists(dst) or os.path.islink(dst):
            return (False, "local file exists")
        shutil.move(src, dst)
        os.rmdir(outdir)
        return (True, entries[0])
    return (False, "multiple files in root")

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def run_archive_cmdlist (archive_cmdlist, verbosity=0):
    """Run archive command."""
    # archive_cmdlist is a command list with optional keyword arguments
    if isinstance(archive_cmdlist, tuple):
        cmdlist, runkwargs = archive_cmdlist
    else:
        cmdlist, runkwargs = archive_cmdlist, {}
    return util.run_checked(cmdlist, verbosity=verbosity, **runkwargs)

def rmtree_log_error (func, path, exc):
    """Error function for shutil.rmtree(). Raises a PatoolError."""
    msg = "Error in %s(%s): %s" % (func.__name__, path, str(exc[1]))
    logger.error(msg)

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def make_file_readable (filename):
    """Make file user readable if it is not a link."""
    if not os.path.islink(filename):
        util.set_mode(filename, stat.S_IRUSR)


#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def make_dir_readable (filename):
    """Make directory user readable and executable."""
    util.set_mode(filename, stat.S_IRUSR|stat.S_IXUSR)


#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def make_user_readable (directory):
    """Make all files in given directory user readable. Also recurse into
    subdirectories."""
    for root, dirs, files in os.walk(directory, onerror=logger.error):
        for filename in files:
            make_file_readable(os.path.join(root, filename))
        for dirname in dirs:
            make_dir_readable(os.path.join(root, dirname))

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def cleanup_outdir (outdir, archive):
    """Cleanup outdir after extraction and return target file name and
    result string."""
    make_user_readable(outdir)
    # move single directory or file in outdir
    (success, msg) = move_outdir_orphan(outdir)
    if success:
        # msg is a single directory or filename
        return msg, "`%s'" % msg
    # outdir remains unchanged
    # rename it to something more user-friendly (basically the archive
    # name without extension)
    outdir2 = util.get_single_outfile("", archive)
    os.rename(outdir, outdir2)
    return outdir2, "`%s' (%s)" % (outdir2, msg)

#-----------------------------------------------------------------------
#
# Function _extract_archive
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

    print(program + format_)
    check_program_compression(archive, 'extract', program, compression)
    get_archive_cmdlist = util.get_module_func(scmd='util_archive', program=program, cmd='extract', format_=format_)
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
            logger.info("... %s extracted to %s." % (archive, msg))
        return target
    finally:
        # try to remove an empty temporary output directory
        if do_cleanup_outdir:
            try:
                os.rmdir(outdir)
            except OSError:
                pass

def _handle_archive(archive, command, verbosity=0, interactive=True,
                    program=None, format=None, compression=None):
    """Test and list archives."""
    if format is None:
        format, compression = get_archive_format(archive)
    check_archive_format(format, compression)
    if command not in ('list', 'test'):
        raise Exception("invalid archive command `%s'" % command)
    program = find_archive_program(format, command, program=program)
    check_program_compression(archive, command, program, compression)
    get_archive_cmdlist = util.get_module_func(scmd='util_archive',
                                                   program=program,
                                                   cmd=command,
                                                   format_=format)
    # prepare keyword arguments for command list
    cmdlist = get_archive_cmdlist(archive, compression, program, verbosity, interactive)
    if cmdlist:
        # an empty command list means the get_archive_cmdlist() function
        # already handled the command (eg. when it's a builtin Python
        # function)
        run_archive_cmdlist(cmdlist, verbosity=verbosity)

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def _diff_archives (archive1, archive2, verbosity=0, interactive=True):
    """Show differences between two archives.
    @return 0 if archives are the same, else 1
    @raises: PatoolError on errors
    """
    if util.is_same_file(archive1, archive2):
        return 0
    diff = util.find_program("diff")
    if not diff:
        msg = "The diff(1) program is required for showing archive differences, please install it."
        raise Exception(msg)
    tmpdir1 = util.tmpdir()
    try:
        path1 = _extract_archive(archive1, outdir=tmpdir1, verbosity=-1)
        tmpdir2 = util.tmpdir()
        try:
            path2 = _extract_archive(archive2, outdir=tmpdir2, verbosity=-1)
            return util.run_checked([diff, "-urN", path1, path2], verbosity=1, ret_ok=(0, 1))
        finally:
            shutil.rmtree(tmpdir2, onerror=rmtree_log_error)
    finally:
        shutil.rmtree(tmpdir1, onerror=rmtree_log_error)

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def extract_singlefile_standard (archive, compression, cmd, verbosity, interactive, outdir):
    """Standard routine to extract a singlefile archive (like gzip)."""
    cmdlist = [util.shell_quote(cmd)]
    if verbosity > 1:
        cmdlist.append('-v')
    outfile = util.get_single_outfile(outdir, archive)
    cmdlist.extend(['-c', '-d', '--', util.shell_quote(archive), '>',
        util.shell_quote(outfile)])
    return (cmdlist, {'shell': True})


#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def test_singlefile_standard (archive, compression, cmd, verbosity, interactive):
    """Standard routine to test a singlefile archive (like gzip)."""
    cmdlist = [cmd]
    if verbosity > 1:
        cmdlist.append('-v')
    cmdlist.extend(['-t', '--', archive])
    return cmdlist


#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def create_singlefile_standard (archive, compression, cmd, verbosity, interactive, filenames):
    """Standard routine to create a singlefile archive (like gzip)."""
    cmdlist = [util.shell_quote(cmd)]
    if verbosity > 1:
        cmdlist.append('-v')
    cmdlist.extend(['-c', '--'])
    cmdlist.extend([util.shell_quote(x) for x in filenames])
    cmdlist.extend(['>', util.shell_quote(archive)])
    return (cmdlist, {'shell': True})

#-----------------------------------------------------------------------
#
# Function _extract_archive
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
def _recompress_archive(archive, verbosity=0, interactive=True):
    """Try to recompress an archive to smaller size."""
    format, compression = get_archive_format(archive)
    if compression:
        # only recompress the compression itself (eg. for .tar.xz)
        format = compression
    tmpdir = util.tmpdir()
    tmpdir2 = util.tmpdir()
    base, ext = os.path.splitext(os.path.basename(archive))
    archive2 = util.get_single_outfile(tmpdir2, base, extension=ext)
    try:
        # extract
        kwargs = dict(verbosity=verbosity, format_=format, outdir=tmpdir)
        path = _extract_archive(archive, **kwargs)
        # compress to new file
        olddir = os.getcwd()
        os.chdir(path)
        try:
            kwargs = dict(verbosity=verbosity, interactive=interactive, format=format)
            files = tuple(os.listdir(path))
            _create_archive(archive2, files, **kwargs)
        finally:
            os.chdir(olddir)
        # check file sizes and replace if new file is smaller
        filesize = util.get_filesize(archive)
        filesize2 = util.get_filesize(archive2)
        if filesize2 < filesize:
            # replace file
            os.remove(archive)
            shutil.move(archive2, archive)
            diffsize = filesize - filesize2
            return "... recompressed file is now %s smaller." % util.strsize(diffsize)
    finally:
        shutil.rmtree(tmpdir, onerror=rmtree_log_error)
        shutil.rmtree(tmpdir2, onerror=rmtree_log_error)
    return "... recompressed file is not smaller, leaving archive as is."


def _create_archive(archive, filenames, verbosity=0, interactive=True,
                    program=None, format=None, compression=None):
    """Create an archive."""
    if format is None:
        format, compression = get_archive_format(archive)
    check_archive_format(format, compression)
    program = find_archive_program(format, 'create', program=program)
    check_program_compression(archive, 'create', program, compression)
    get_archive_cmdlist = util.get_module_func(scmd='util_archive', program=program, cmd='create', format_=format)
    origarchive = None
    if os.path.basename(program) == 'arc' and \
       ".arc" in archive and not archive.endswith(".arc"):
        # the arc program mangles the archive name if it contains ".arc"
        origarchive = archive
        archive = util.tmpfile(dir=os.path.dirname(archive), suffix=".arc")
    cmdlist = get_archive_cmdlist(archive, compression, program, verbosity, interactive, filenames)
    if cmdlist:
        # an empty command list means the get_archive_cmdlist() function
        # already handled the command (eg. when it's a builtin Python
        # function)
        run_archive_cmdlist(cmdlist, verbosity=verbosity)
    if origarchive:
        shutil.move(archive, origarchive)

def _repack_archive (archive1, archive2, verbosity=0, interactive=True):
    """Repackage an archive to a different format."""
    format1, compression1 = get_archive_format(archive1)
    format2, compression2 = get_archive_format(archive2)
    if format1 == format2 and compression1 == compression2:
        # same format and compression allows to copy the file
        util.link_or_copy(archive1, archive2, verbosity=verbosity)
        return
    tmpdir = util.tmpdir()
    try:
        kwargs = dict(verbosity=verbosity, outdir=tmpdir)
        same_format = (format1 == format2 and compression1 and compression2)
        if same_format:
            # only decompress since the format is the same
            kwargs['format'] = compression1
        path = _extract_archive(archive1, **kwargs)
        archive = os.path.abspath(archive2)
        files = tuple(os.listdir(path))
        olddir = os.getcwd()
        os.chdir(path)
        try:
            kwargs = dict(verbosity=verbosity, interactive=interactive)
            if same_format:
                # only compress since the format is the same
                kwargs['format'] = compression2
            _create_archive(archive, files, **kwargs)
        finally:
            os.chdir(olddir)
    finally:
        shutil.rmtree(tmpdir, onerror=rmtree_log_error)

def _search_archive(pattern, archive, verbosity=0, interactive=True):
    """Search for given pattern in an archive."""
    grep = util.find_program("grep")
    if not grep:
        msg = "The grep(1) program is required for searching archive contents, please install it."
        raise Exception(msg)
    tmpdir = util.tmpdir()
    try:
        path = _extract_archive(archive, outdir=tmpdir, verbosity=-1)
        return util.run_checked([grep, "-r", "-e", pattern, "."], ret_ok=(0, 1), verbosity=1, cwd=path)
    finally:
        shutil.rmtree(tmpdir, onerror=rmtree_log_error)
