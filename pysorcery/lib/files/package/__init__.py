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
# This implements the packages file classes
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
from pysorcery.lib import files

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
PackageCommands = ('list', 'extract', 'test', 'create', 'read')

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract, ...)
# Programs starting with "py_" are Python modules.
PackagePrograms = {
    'cpio': {
        'extract': ('cpio', 'bsdcpio', '7z'),
        'list': ('cpio', 'bsdcpio', '7z'),
        'test': ('cpio', 'bsdcpio', '7z',),
        'create': ('cpio', 'bsdcpio'),
    },
    'deb': {
        'extract': ('dpkg-deb', '7z'),
        'list': ('dpkg-deb', '7z'),
        'test': ('dpkg-deb', '7z'),
    },
    'rpm': {
        'extract': ('rpm2cpio', '7z'),
        'list': ('rpm', '7z', '7za'),
        'test': ('rpm', '7z'),
    }
}


#-----------------------------------------------------------------------
#
# Classes
#
# Package
# Packages
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Package
#
# This is the Package File Class
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
class PackageFile(files.BaseFile):
    #-------------------------------------------------------------------
    #
    # Function extract
    #
    # Extract archive
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename
    #    @param: verbosity
    #    @param: outdir
    #    @param: program
    #    @param: interactive
    #
    # Returns
    # -------
    #    None
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

        """Verify given archive exists."""
        self.check_existing_filename(self.filename)
        logger.info("Extracting %s ..." % self.filename)
        """Extract given archive."""
        _extract_archive(self.filename,
                         verbosity=verbosity,
                         interactive=interactive,
                         outdir=outdir,
                         program=program)

        logger.debug('End Function')
        return
    
    #-------------------------------------------------------------------
    #
    # Function create
    #
    # Cruate archive
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
    def create(self, filenames, verbosity=0,
               program=None, interactive=True):
        """Create given archive with given files."""
        self.check_new_filename()

        check_names = files.BaseFiles(filelist = filenames)
        check_names.check_filelist()
        if verbosity >= 0:
            logger.info("Creating {self.filename} ...")
            res = _create_archive(self.filename,
                                  filenames,
                                  verbosity=verbosity,
                                  interactive=interactive,
                                  program=program)
            if verbosity >= 0:
                logger.info('... {self.filename} created.')
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
            logger.info('Listing {self.filename} ...')
            return _handle_archive(self.filename,
                                   'list',
                                   verbosity=verbosity,
                                   interactive=interactive,
                                   program=program)

    #-------------------------------------------------------------------
    #
    # Function testarchive
    #
    # Test to ensure the archive is a valid archive
    #
    # Inputs
    # ------
    #     @param: self
    #     @param: verbosity
    #     @param: interactive
    #
    # Returns
    # -------
    #     @return: None (change this to True or False?)
    #
    # Raises
    # ------
    #
    # 
    #-------------------------------------------------------------------
    def recompress_archive(self, verbosity=0, interactive=True):
        """Recompress an archive to hopefully smaller size."""
        util.check_existing_filename(self.filename)
        util.check_writable_filename(self.filename)
        if verbosity >= 0:
            logger.info('Recompressing {self.filename} ...')
        res = _recompress_archive(self.filename,
                                  verbosity=verbosity,
                                  interactive=interactive)
        if res and verbosity >= 0:
            logger.info(res)
        return 0

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
    def repack_archive (self, archive_new, verbosity=0, interactive=True):
        """Repack archive to different file and/or format."""
        util.check_existing_filename(self.filename)
        util.check_new_filename(archive_new)
        if verbosity >= 0:
            logger.info("Repacking %s to %s ..." % (self.filename, archive_new))
        res = _repack_archive(self.filename,
                              archive_new,
                              verbosity=verbosity,
                              interactive=interactive)
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
    def test_archive(self, verbosity=0, program=None, interactive=True):
        """Test given archive."""
        util.check_existing_filename(self.filename)
        if verbosity >= 0:
            logger.info("Testing %s ..." % self.filename)
        res = _handle_archive(self.filename,
                              'test',
                              verbosity=verbosity,
                              interactive=interactive,
                              program=program)
        if verbosity >= 0:
            logger.info("... tested ok.")
        return res

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

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Read the content of a file within an archive
    #
    # Inputs
    # ------
    #     @param: self
    #     @param: filename
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
    def read(self, filename, verbosity=0, interactive=True):
        """Print the content of a file within an archive"""
        content = 'Package Read is not implemented'
        raise NotImplementedError
        return content

#-----------------------------------------------------------------------
#
# Class Packages
#
# This is the Packages Class for working with multiple archive files.
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
class PackageFiles(files.BaseFiles):
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
            res = _diff_archives(self.files,
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
# program_supports_compression
# find_archive_program
# _extract_archive
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function program_supports_compression
#
# Decide if the given program supports the compression natively.
#
# Inputs
# ------
#    @param:
#
# Returns
# -------
#    @return: True  - if the program supports the given compression
#                     format natively.
#    @return: False - if the program does not support the given
#                     compression.
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def program_supports_compression (program, compression):
    """Decide if the given program supports the compression natively.
    @return: True if the program supports the given compression format
      natively, else False.
    """
    if program in ('tar', 'star', 'bsdtar', 'py_tarfile'):
        return compression in ('gzip', 'bzip2') + py_lzma
    return False

#-----------------------------------------------------------------------
#
# Function check_archive_format
#
# Make sure format and compression is known.
#
# Inputs
# ------
#    @param: format_
#    @param: compression
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
def check_archive_format (format_, compression):
    """Make sure format and compression is known."""
    if format_ not in mimetypes.PackageFormats:
        raise Exception("unknown archive format `%s'" % format)
    if compression is not None and compression not in mimetypes.PackageCompressions:
        raise Exception("unkonwn archive compression `%s'" % compression)

#-----------------------------------------------------------------------
#
# Function list_formats
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
def list_formats ():
    """Print information about available archive formats to stdout."""
    for format_ in mimetypes.PackageFormats:
        print(format_, "files:")
        for command in PackageCommands:
            programs = PackagePrograms[format_]
            if command not in programs and None not in programs:
                print("   %8s: - (not supported)" % command)
                continue
            try:
                program = find_archive_program(format_, command)
                print("   %8s: %s" % (command, program), end=' ')
                print()
            except Exception:
                # display information what programs can handle this archive format
                handlers = programs.get(None, programs.get(command))
                print("   %8s: - (no program found; install %s)" %
                      (command, util.strlist_with_or(handlers)))

#-----------------------------------------------------------------------
#
# Function get_archive_format
#
# This is the base File Class
#
# Inputs
# ------
#    @param: filename
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
    if mime in mimetypes.PackageMimetypes:
        format_ = mimetypes.PackageMimetypes[mime]
    else:
        raise Exception("unknown archive format for file `%s' (mime-type is `%s')" % (filename, mime))
    if format_ == compression:
        # file cannot be in same format compressed
        compression = None
    return format_, compression

#-----------------------------------------------------------------------
#
# function p7zip_supports_rar
#
# Determine if the RAR codec is installed for 7z program.
#
# Inputs
# ------
#    @param: None
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
# Function find_archive_program
#
# ...
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
    commands = PackagePrograms[format_]
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
# Function check_program_compression
#
# Check if a program supports the given compression.
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
# Function move_outdir_orphan
#
# ...
#
# Inputs
# ------
#    @param: outdir
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
# Function run_archive_cmdlist
#
# Run archive command.
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

#-----------------------------------------------------------------------
#
# Function rmtree_log_error
#
# 
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
def rmtree_log_error (func, path, exc):
    """Error function for shutil.rmtree(). Raises a PatoolError."""
    msg = "Error in %s(%s): %s" % (func.__name__, path, str(exc[1]))
    logger.error(msg)


#-----------------------------------------------------------------------
#
# Function cleanup_outdir
#
# 
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
    output_dir = files.BaseDirectory(outdir)
    output_dir.make_user_readable()
    # move single directory or file in outdir
    (success, msg) = move_outdir_orphan(outdir)
    if success:
        # msg is a single directory or filename
        return msg, "`%s'" % msg
    # outdir remains unchanged
    # rename it to something more user-friendly (basically the archive
    # name without extension)
    outdir2 = files.get_single_outfile("", archive)
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
#    @param: archive
#    @param: verbosity
#    @param: interactive
#    @param: outdir
#    @param: program
#    @param: format_
#    @param: compression
#
# Returns
# -------
#    @return: outdir
#    @return: none
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
    get_archive_cmdlist = util.get_module_func(scmd='util_archive',
                                               program=program,
                                               cmd='extract',
                                               format_=format_)
    if outdir is None:
        directory = files.BaseDirectory(".")
        outdir = directory.tmpdir(dir=".")
        do_cleanup_outdir = True
    else:
        do_cleanup_outdir = False
    try:
        cmdlist = get_archive_cmdlist(archive,
                                      compression,
                                      program,
                                      verbosity,
                                      interactive,
                                      outdir)
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

#-----------------------------------------------------------------------
#
# Function _handle_archive
#
# Test and list archives.
#
# Inputs
# ------
#    @param: archive
#    @param: verbosity
#    @param: interactive
#    @param: outdir
#    @param: program
#    @param: format_
#    @param: compression
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
def _diff_archives (archives, verbosity=0, interactive=True):
    """Show differences between two archives.
    @return 0 if archives are the same, else 1
    @raises: PatoolError on errors
    """

    files = files.Files(archives)
    if files.is_same_file():
        return 0
    diff = util.find_program("diff")
    if not diff:
        msg = "The diff(1) program is required for showing archive differences, please install it."
        raise Exception(msg)
    tmpdir1 = files.BaseDirectory.tmpdir()
    try:
        path1 = _extract_archive(archive1, outdir=tmpdir1, verbosity=-1)
        tmpdir2 = files.Basedirectory.tmpdir()
        try:
            path2 = _extract_archive(archive2, outdir=tmpdir2, verbosity=-1)
            return util.run_checked([diff, "-urN", path1, path2], verbosity=1, ret_ok=(0, 1))
        finally:
            shutil.rmtree(tmpdir2, onerror=rmtree_log_error)
    finally:
        shutil.rmtree(tmpdir1, onerror=rmtree_log_error)

#-----------------------------------------------------------------------
#
# Function _recompress_archive
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
    archive2 = files.get_single_outfile(tmpdir2, base, extension=ext)
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
