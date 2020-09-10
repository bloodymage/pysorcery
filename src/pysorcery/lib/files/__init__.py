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
# This file is part of Sorcery.
#
# Additional code from 'patool'
# Copyright (C) 2010-2015 Bastian Kleineidam
#
# File: pysorcery/lib/util/files/__init__.py
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
# Files:
#
#    Library for sorcery that provides for interfacing with
#    files/directories.
#
#-----------------------------------------------------------------------
"""
Files:

Library for sorcery that provides for interfacing with files and
directories.
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------
# System Libraries
import glob
import os
import stat
import subprocess
import tempfile

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
from pysorcery.lib.system import shutil
# Other Application Libraries
from pysorcery.lib import util
from pysorcery.lib.util import config
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

pkg_mgr = distro.distro_group[distro.distro_id]
# Supported package commands
Commands = ('get_alien',
            'get_from')

# List of programs supporting the given archive format and command.
# If command is None, the program supports all commands (list, extract,
# ...)
# Programs starting with "py_" are Python modules.
Programs = {
    'smgl': {
        'basefile': {
            'get_from': ('gaze',),
        },
        'basefiles': {
            'get_installed': ('py_smgl',),
            'get_alien': ('py_smgl',),
        },
        'basedirectory': {
        },
        'basedirectories': {
        },
    },
    'apt': {
        'basefile': {
            'get_from': ('dpkg',),
        },
        'basefiles' : {
            'get_alien': ('cruft',),
        },
        'basedirectory': {
        },
        'basedirectories': {
        },
    }
}

#-----------------------------------------------------------------------
#
# Classes
#
# BaseFile
# BaseFiles
# BaseDirectory
# BaseDirectories
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class NotAFileError
#
# This exception is to be used when a path exists, but is not an
# actual file.
#
# Inputs
# ------
#    @param: message
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class NotAFileException(OSError):
    pass


#-----------------------------------------------------------------------
#
# Class BaseFile
#
# This is the base File Class
#
# Inputs
# ------
#    @param: filename - Defines the filename to be used.
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class BaseFile():
    def __init__(self, filename, *args, **kwargs):
        logger.debug("Begin Function")
        self.filename = filename
        self.mimetype, self.encoding = mimetypes.guess_type(self.filename)
        self.path, self.basename, self.extention = pne(self.filename)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function get_info
    #
    # ...
    #
    # Inputs
    # ------
    #    @param: self
    #    @param: info
    #
    # Returns
    # -------
    #    @return: info
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_info(self, info):
        program = find_program('basefile', info)
        func = util.get_module_func(scmd='util_file',
                                    program=program,
                                    cmd=info)
        info = func(self.filename)
        return info

    #-------------------------------------------------------------------
    #
    # Function get_from
    #
    # List package(s) that provide a file
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @param: packages - list of packages that install filename
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_from(self):
        packages = self.get_info('get_from')
        return packages

    #-------------------------------------------------------------------
    #
    # Function remove
    #
    # Removes a File
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - Filename to remove
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    def remove(self):
        logger.debug("Begin Function")

        try:
            logger.debug2("Removing File: " + self.filename)
            raise NotImplementedError('Remove File not implemented')
        except Exception as msg:
            logger.critical('BaseFile.remove fucked up')

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function check_writable_filename
    #
    # Check that a given file is writable.
    #
    # Inputs
    # ------
    #     @param: self
    #             self.filename - filename to check
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: PermissionError
    #
    #-------------------------------------------------------------------
    def check_writable_filename(self):
        """Ensure that the given filename is writable."""
        if not os.access(self.filename, os.W_OK):
            raise PermissionError("file `%s' is not writable"
                                  % self.filename)
        return

    #-------------------------------------------------------------------
    #
    # Function check_existing_filename
    #
    # Check if a filename exists, and readable.
    #
    # Inputs
    # ------
    #     @param: self
    #             self.filename - Filename to check
    #     @param: onlyfiles - True - Verify filename is an actual file
    #                         False - Verify filename exists regardless of
    #                                 if it is a file, directory, ...
    #
    # Returns
    # -------
    #     @return: None
    #
    # Raises
    # ------
    #    @raises: FileNotFoundError
    #    @raises: PermissionError
    #    @raises: NotAFileError
    #
    #-------------------------------------------------------------------
    def check_existing_filename (self, onlyfiles=True):
        """Ensure that given filename is a valid, existing file."""
        if not os.path.exists(self.filename):
            raise FileNotFoundError("file `%s' was not found"
                                    % self.filename)
        if not os.access(self.filename, os.R_OK):
            raise PermissionError("file `%s' is not readable"
                                  % self.filename)
        if onlyfiles and not os.path.isfile(self.filename):
            raise NotAFileError("`%s' is not a file" % self.filename)
        return

    #-------------------------------------------------------------------
    #
    # Function check_new_filename
    #
    # Check that filename does not already exist.
    #
    # Inputs
    # ------
    #     @param: self
    #             self.filename - Filename to verify
    #
    # Returns
    # -------
    #     @return: None
    #
    # Raises
    # ------
    #     @raises: FileExistsError
    #
    #-------------------------------------------------------------------
    def check_new_filename (self):
        """Check that filename does not already exist."""
        if os.path.exists(self.filename):
            raise FileExistsError("cannot overwrite existing file `%s'"
                                  % self.filename)
        return

    #-------------------------------------------------------------------
    #
    # Function set_mode
    #
    # Set the mode flags (permissions) for given filename if not already
    # set.
    #
    # Inputs
    # ------
    #     @param: self
    #             self.filename - File to set mode on.
    #
    # Returns
    # -------
    #     @return: None
    #
    # Raises
    # ------
    #     @raises: OSError
    #
    #-------------------------------------------------------------------
    def set_mode (self, flags):
        """Set mode flags for given filename if not already set."""
        try:
            mode = os.lstat(self.filename).st_mode
        except OSError:
            # ignore
            return
        if not (mode & flags):
            try:
                os.chmod(self.filename, flags | mode)
            except OSError as msg:
                logger.error("could not set mode flags for `%s': %s"
                             % (self.filename, msg))
        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Read the contents of a file and place each line in a list.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - File to read
    #
    # Returns
    # -------
    #    @return: line_list
    #
    # Raises
    # ------
    #    @raises: FileNotFoundError
    #    @raises: EOFError
    #
    #-------------------------------------------------------------------
    def read(self):
        logger.debug("Begin Function")
        line_list = []

        try:
            for line in open(self.filename):
                line_list.append(line[:-1])
        except FileNotFoundError as msg:
            line_list.append(msg)

        logger.debug("End Function")
        return line_list

    #-------------------------------------------------------------------
    #
    # Function write
    #
    # Write information to a file.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    def write(self):
        logger.debug("Begin Function")

        raise NotImplementedError('BaseFile.write not implemented')

        logger.debug("Begin Function")
        return

    #-------------------------------------------------------------------
    #
    # Function Search
    #
    # ...
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - Filename to search
    #    @param: searchstring
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raisis
    # ------
    #    @raises: NotImplementedError
    #
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug("Begin Function")

        results = "File Search Results"

        raise NotImplementedError('File search not implemented')
        logger.debug("Begin Function")
        return results

    #-------------------------------------------------------------------
    #
    # Function stripext
    #
    # Return the basename without extension of given filename.
    #
    # Inputs
    # ------
    #     @param: self
    #
    # Returns
    # -------
    #     @param: self.basename
    #
    # Raises
    # ------
    #    @raises DepreciationWarning - This function duplicates the 'pne'
    #                                  function.
    #
    #-------------------------------------------------------------------
    def stripext (self):
        """Return the basename without extension of given filename."""
        raise DeprecationWarning('BaseFile.stripext is being depreciated')
        return self.basename

    #-------------------------------------------------------------------
    #
    # Function get_filesize
    #
    # Return file size in Bytes, or -1 on error.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - Filename to get the size of.
    #
    # Returns
    # -------
    #    @return: os.path.getsize()
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_filesize(self):
        """Return file size in Bytes, or -1 on error."""
        return os.path.getsize(self.filename)

    #-------------------------------------------------------------------
    #
    # Function make_file_readable
    #
    # Make a file user readable if it is not a symlink.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def make_file_readable(self):
        """Make file user readable if it is not a link."""
        if not os.path.islink(self.filename):
            self.set_mode(stat.S_IRUSR)
        return

    #-------------------------------------------------------------------
    #
    # Function isfile
    #
    # Check if the provided filename really is a file.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename
    #
    # Returns
    # -------
    #    @return: True
    #    @return: False
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def isfile(self):
        """Make file user readable if it is not a link."""
        if os.path.isfile(self.filename):
            return True
        else:
            return False

    #-------------------------------------------------------------------
    #
    # Function print_name
    #
    # Print the file's name.
    #
    # Note: This may be redundant...
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - name of directory to print.
    #
    # Returns
    # -------
    #    @param: None
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def print_name(self):
        logger.debug("Begin Function")
        logger.info(self.filename)
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Class BaseDirectory
#
# Directories are a specific type of file
#
# Inputs
# ------
#    @param: filename
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class BaseDirectory(BaseFile):
    #-------------------------------------------------------------------
    #
    # Function tmpdir
    #
    # Return a temporary directory for extraction.
    #
    # Inputs
    # ------
    #     @param: self
    #     @param: dir -
    #                 - Default: None
    #
    # Returns
    # -------
    #     @return: tempfilemkdtemp()
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def tmpdir(self, dir=None):
        """Return a temporary directory for extraction."""
        return tempfile.mkdtemp(suffix='', prefix='Unpack_', dir=dir)

    #-------------------------------------------------------------------
    #
    # Function make_dir_readable
    #
    # Makes a directory user readable and executable.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def make_dir_readable (self):
        """Make directory user readable and executable."""
        self.set_mode(stat.S_IRUSR|stat.S_IXUSR)
        return

    #-------------------------------------------------------------------
    #
    # Function make_user_readable
    #
    # Recursively, make all files in a given directory user readable.
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    @return: None
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def make_user_readable(self):
        """
        Make all files in given directory user readable.
        Also recurse into subdirectories.
        """
        for root, dirs, files in os.walk(self.filename,
                                         onerror=logger.error):
            for filename in files:
                file_ = BaseFile(os.path.join(root,
                                              filename))
                file_.make_file_readable()
            for dirname in dirs:
                dir_ = BaseDirectory(os.path.join(root,
                                                  dirname))
                dir_.make_dir_readable()
        return

    #-------------------------------------------------------------------
    #
    # Function isdir
    #
    # Check to see if named "file" is a directory.
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename
    #
    # Returns
    # -------
    #    @return: True
    #    @return: False
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def isdir(self):
        """Make file user readable if it is not a link."""
        if os.path.isdir(self.filename):
            return True
        else:
            return False

    #-------------------------------------------------------------------
    #
    # Function listfiles
    #
    # List the files within a directory.
    #
    #
    # Inputs
    # ------
    #     @param: self
    #
    # Returns
    # -------
    #     @return: dirfiles
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def listfiles(self):
        files = glob.glob(self.filename + "/*")

        dirfiles = []
        for f in files:
            file_ = f.split('/')[-1]
            dirfiles.append(file_)
        return dirfiles

#-----------------------------------------------------------------------
#
# Class BaseFiles
#
# ...
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#            kwargs['filelist'] - list of files
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class BaseFiles():
    def __init__(self, *args, **kwargs):
        logger.debug("Begin Function")

        if 'filelist' in kwargs:
            self.files = kwargs['filelist']
        else:
            self.files = []

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function get_info
    #
    # ...
    #
    # Inputs
    # ------
    #    @param: self
    #    @param: info
    #
    # Returns
    # -------
    #    @return: info
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_info(self, info):
        program = find_program('basefiles', info)
        func = util.get_module_func(scmd='util_file',
                                    program=program,
                                    cmd=info)
        info = func()
        return info

    #-------------------------------------------------------------------
    #
    # Function get_installed
    #
    # ...
    #
    # Inputs
    # ------
    #    @param: self
    #            self.filename - Filename to identify which package(s)
    #                            install that file
    #
    # Returns
    # -------
    #    @param: pkg_list - list of packages that install filename
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_installed(self):
        self.files = self.get_info('get_installed')
        return self.files

    #-------------------------------------------------------------------
    #
    # Function get_alien
    #
    # List files that were not installed by Sorcery.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @param: self.files - List of files that were not installed by
    #                         Sorcery.
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_alien(self):
        self.files = self.get_info('get_alien')
        return self.files

    #-------------------------------------------------------------------
    #
    # Function get_system
    #
    # List all files on the system.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: sys_files - List of files
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def get_system(self):
        logger.debug("Begin Function")

        # List of directories to check
        sys_dirs = [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                     '/opt', '/sbin', '/share', '/usr','/var' ]
        ignore_dirs = ['/home']

        self.files = []
        for sys_dir in sys_dirs:
            for root, dirs, files in os.walk(sys_dir):
                for i in dirs:
                    for j in files:
                        system_file = str(os.path.join(root,i,j))
                        self.files.append(system_file)

        logger.debug("End Function")
        return self.files

    #-------------------------------------------------------------------
    #
    # Function is_same_file
    #
    # Check if filename1 and filename2 point to the same file object.
    # There can be false negatives, ie. the result is False, but it is
    # the same file anyway. Reason is that network filesystems can create
    # different paths to the same physical file.
    #
    # Inputs
    # ------
    #     @param: self
    #             self.files - list of 2 files to check
    #
    # Returns
    # -------
    #     @return: True
    #     @return: os.path.samefile
    #     @return: self.is_same_filename
    #
    # Raises
    # ------
    #    @raises: ...
    #
    #-------------------------------------------------------------------
    def is_same_file (self):
        """Check if filename1 and filename2 point to the same file
        object.  There can be false negatives, ie. the result is False,
        but it is the same file anyway. Reason is that network
        filesystems can create different paths to the same physical
        file.
        """
        if self.files[0] == self.files[1]:
            return True
        if os.name == 'posix':
            return os.path.samefile(self.files[0], self.files[1])
        return self.is_same_filename(self.files[0], self.files[1])

    #-------------------------------------------------------------------
    #
    # Function is_same_filename
    #
    # Check if filename1 and filename2 are the same filename.
    #
    # Inputs
    # ------
    #     @param: self
    #
    # Returns
    # -------
    #     @return: True/False
    #
    # Raises
    # ------
    #     @raises: ...
    #
    #-------------------------------------------------------------------
    def is_same_filename(self):
        """Check if filename1 and filename2 are the same filename."""
        return os.path.realpath(self.files[0]) == os.path.realpath(self.files[1])

    #-------------------------------------------------------------------
    #
    # Function check_filelist
    #
    # Check that file list is not empty and contains only existing files.
    #
    # Inputs
    # ------
    #     @param: self
    #
    # Returns
    # -------
    #     @return: None
    #
    # Raises
    # ------
    #     @raises: ...
    #
    #-------------------------------------------------------------------
    def check_filelist (self):
        """
        Check that file list is not empty and contains only existing
        files.
        """
        if not self.files:
            raise Exception("cannot create archive with empty filelist")
        for filename in self.files:
            file_ = BaseFile(filename)
            file_.check_existing_filename(onlyfiles=False)
        return

#-----------------------------------------------------------------------
#
# Class BaseDirectories
#
# ...
#
# Inputs
# ------
#    @param: *args
#    @param: **kwargs
#            kwargs['filelist'] - list of files
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
class BaseDirectories(BaseFiles):
    #-------------------------------------------------------------------
    #
    # Function stripbackup
    #
    # Check that file list is not empty and contains only existing files.
    #
    # Inputs
    # ------
    #     @param: self
    #
    # Returns
    # -------
    #     @return: None
    #
    # Raises
    # ------
    #     @raises: ...
    #
    #-------------------------------------------------------------------
    def stripbackup(self):
        newfiles = []
        for f in self.files:
            # Verify f is a real file
            # skip f if f is an emacs backup
            if (os.path.isfile(f) and
                f.endswith('~') is False):
                supformats.append(os.path.basename(f)[:-3])

        newfiles.sort()
        self.files = newfiles
        return self.files

#-------------------------------------------------------------------
#
# Functions
#
# pne
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function pne
#
# Get the Path, Name, and Extention of a file.
#
# Inputs
# ------
#    @param: ifilename - input filename
#
# Returns
# -------
#    @return: Path
#    @return: Name
#    @return: Extention
#
# Raises
# ------
#    @raises: ...
#
#-------------------------------------------------------------------
def pne(ifilename):
    """
    Get the path, name, and extension of given filename.
    """
    # Add extra extensions where desired.
    DOUBLE_EXTENSIONS = ['tar.gz','tar.bz2','tar.xz']

    path, filename=os.path.split(ifilename)
    root,ext = os.path.splitext(filename)
    if any([filename.endswith(x) for x in DOUBLE_EXTENSIONS]):
        root, first_ext = os.path.splitext(root)
        ext = first_ext + ext
    return path, root, ext

#-----------------------------------------------------------------------
#
# Function get_single_outfile
#
# Get output filename if archive is in a single file format like gzip.
#
# Inputs
# ------
#     @param: directory
#     @param: archive
#     @param: extention
#
# Returns
# -------
#     @return: outfile + extention
#
# Raises
# ------
#     @raises: ...
#
#-----------------------------------------------------------------------
def get_single_outfile (directory, archive, extension=""):
    """
    Get output filename if archive is in a single file format
    like gzip.
    """
    archname = BaseFile(archive)
    outfile = os.path.join(directory, archname.basename)
    if os.path.exists(outfile + extension):
        # prevent overwriting existing files
        i = 1
        newfile = "%s%d" % (outfile, i)
        while os.path.exists(newfile + extension):
            newfile = "%s%d" % (outfile, i)
            i += 1
        outfile = newfile
    return outfile + extension

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
#    @return: program
#    @return: exe
#
# Raises
# ------
#    @raises: ...
#
#-----------------------------------------------------------------------
def find_program(class_, command, program=None):
    """Find suitable archive program for given format and mode."""
    commands = Programs[pkg_mgr][class_]
    programs = []
    if program is not None:
        # try a specific program first
        programs.append(program)
    # first try the universal programs with key None
    for key in (None, command):
        if key in commands:
            programs.extend(commands[key])
    if not programs:
        raise Exception("%s program class `%s' is not supported"
                        % (command, class_))
    # return the first existing program
    for program in programs:
        if program.startswith('py_'):
            # it's a Python module and therefore always supported
            return program
        exe = util.find_program(program)
        return exe
