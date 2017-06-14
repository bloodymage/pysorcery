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
# File: pysorcery/lib/util/__init__.py
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
#
#-----------------------------------------------------------------------
"""
"""
#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import glob
import importlib
import os
import pkg_resources
from shutil import which
import subprocess
import tempfile
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

# Utilities
UTIL_ARCHIVE_PATH = pkg_resources.resource_filename('pysorcery',
                                                    'lib/util/files/archive/')
UTIL_COMPRESSED_PATH = pkg_resources.resource_filename('pysorcery',
                                                       'lib/util/files/compressed/')
UTIL_URL_PATH = pkg_resources.resource_filename('pysorcery', 'lib/util/url/')

# Cemmand Plugins
ARCHIVE_PATH = pkg_resources.resource_filename('pysorcery', 'plugins/archive/')
GAZE_PATH = pkg_resources.resource_filename('pysorcery', 'plugins/gaze/')

# Sorcecy
PACKAGES_PATH = pkg_resources.resource_filename('pysorcery','lib/sorcery/packages')
REPOSITORIES_PATH = pkg_resources.resource_filename('pysorcery',
                                                    'lib/sorcery/packages')

cmd_dir = {
    'util_archive': UTIL_ARCHIVE_PATH,
    'util_compressed': UTIL_COMPRESSED_PATH,
    'util_url': UTIL_URL_PATH,
    'gaze': GAZE_PATH,
    'archive': ARCHIVE_PATH,
    'packages': PACKAGES_PATH,
    'repositories': REPOSITORIES_PATH
}

import_path = {
    'util_archive': 'pysorcery.lib.util.files.archive.',
    'util_compressed': 'pysorcery.lib.util.files.compressed.',
    'util_url': 'pysorcery.lib.util.url.',
    'archive': 'pysorcery.plugins.archive.',
    'gaze': 'pysorcery.plugins.gaze.',
    'packages': 'pysorcery.lib.sorcery.packages.',
    'repositories': 'pysorcery.lib.sorcery.repositories.'
    }

# Used if module names can not be
# the same as the archive format
ArchiveModules = {
    '7z': 'p7zip',
    '7za': 'p7azip',
    '7zr': 'p7rzip',
    'uncompress.real': 'uncompress',
    'dpkg-deb': 'dpkg',
    'extract_chmlib': 'chmlib',
    }

CompressedModules = {
    }

UrlModules = {
}


class memoized (object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated."""

    def __init__(self, func):
        """Set func and init cache."""
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        """Try to find result for function arguments in local cache or
        execute the function and fill the cache with the result."""
        try:
            return self.cache[args]
        except KeyError:
            self.cache[args] = value = self.func(*args)
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)

    def __repr__(self):
        """Return the function's docstring."""
        return self.func.__doc__

#-----------------------------------------------------------------------
#
# Functions
#
# get_cmd_types
# get_cmd_func
#
#-----------------------------------------------------------------------
def get_single_outfile (directory, archive, extension=""):
    """Get output filename if archive is in a single file format like gzip."""
    outfile = os.path.join(directory, stripext(archive))
    if os.path.exists(outfile + extension):
        # prevent overwriting existing files
        i = 1
        newfile = "%s%d" % (outfile, i)
        while os.path.exists(newfile + extension):
            newfile = "%s%d" % (outfile, i)
            i += 1
        outfile = newfile
    return outfile + extension

def is_same_file (filename1, filename2):
    """Check if filename1 and filename2 point to the same file object.
    There can be false negatives, ie. the result is False, but it is
    the same file anyway. Reason is that network filesystems can create
    different paths to the same physical file.
    """
    if filename1 == filename2:
        return True
    if os.name == 'posix':
        return os.path.samefile(filename1, filename2)
    return is_same_filename(filename1, filename2)


def is_same_filename (filename1, filename2):
    """Check if filename1 and filename2 are the same filename."""
    return os.path.realpath(filename1) == os.path.realpath(filename2)

def strlist_with_or (alist):
    """Return comma separated string, and last entry appended with ' or '."""
    if len(alist) > 1:
        return "%s or %s" % (", ".join(alist[:-1]), alist[-1])
    return ", ".join(alist)

def check_writable_filename(filename):
    """Ensure that the given filename is writable."""
    if not os.access(filename, os.W_OK):
        raise PatoolError("file `%s' is not writable" % filename)

def check_existing_filename (filename, onlyfiles=True):
    """Ensure that given filename is a valid, existing file."""
    if not os.path.exists(filename):
        raise Exception("file `%s' was not found" % filename)
    if not os.access(filename, os.R_OK):
        raise Exception("file `%s' is not readable" % filename)
    if onlyfiles and not os.path.isfile(filename):
        raise Exception("`%s' is not a file" % filename)

def check_new_filename (filename):
    """Check that filename does not already exist."""
    if os.path.exists(filename):
        raise Exception("cannot overwrite existing file `%s'" % filename)

def check_archive_filelist (filenames):
    """Check that file list is not empty and contains only existing files."""
    if not filenames:
        raise Exception("cannot create archive with empty filelist")
    for filename in filenames:
        check_existing_filename(filename, onlyfiles=False)

def set_mode (filename, flags):
    """Set mode flags for given filename if not already set."""
    try:
        mode = os.lstat(filename).st_mode
    except OSError:
        # ignore
        return
    if not (mode & flags):
        try:
            os.chmod(filename, flags | mode)
        except OSError as msg:
            logger.error("could not set mode flags for `%s': %s" % (filename, msg))


def shell_quote (value):
    """Quote all shell metacharacters in given string value with strong
    (ie. single) quotes, handling the single quote especially."""
    if os.name == 'nt':
        return shell_quote_nt(value)
    return "'%s'" % value.replace("'", r"'\''")


def shell_quote_nt (value):
    """Quote argument for Windows system. Modeled after distutils
    _nt_quote_args() function."""
    if " " in value:
        return '"%s"' % value
    return value

def run (cmd, verbosity=0, **kwargs):
    """Run command without error checking.
    @return: command return code"""
    # Note that shell_quote_nt() result is not suitable for copy-paste
    # (especially on Unix systems), but it looks nicer than shell_quote().
    if verbosity >= 0:
        logger.info("running %s" % " ".join(map(shell_quote_nt, cmd)))
    if kwargs:
        if verbosity >= 0:
            logger.info("    with %s" % ", ".join("%s=%s" % (k, shell_quote(str(v)))\
                                           for k, v in kwargs.items()))
        if kwargs.get("shell"):
            # for shell calls the command must be a string
            cmd = " ".join(cmd)
    if verbosity < 1:
        # hide command output on stdout
        with open(os.devnull, 'wb') as devnull:
            kwargs['stdout'] = devnull
            res = subprocess.call(cmd, **kwargs)
    else:
        res = subprocess.call(cmd, **kwargs)
    return res


def run_checked (cmd, ret_ok=(0,), **kwargs):
    """Run command and raise PatoolError on error."""
    retcode = run(cmd, **kwargs)
    if retcode not in ret_ok:
        msg = "Command `%s' returned non-zero exit status %d" % (cmd, retcode)
        raise Exception(msg)
    return retcode


def tmpdir (dir=None):
    """Return a temporary directory for extraction."""
    return tempfile.mkdtemp(suffix='', prefix='Unpack_', dir=dir)

#-------------------------------------------------------------------
#
# Function get_cmd_types
#
#
#
# Inputs
# ------
#     @param: cmd_class - I really need a new name for this...
#         
# Returns
# -------
#     supformats - 'Supported Formats'
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_cmd_types(cmd_class):
    logger.debug('Begin Function')

    # Use [a-z] to allow finding directories, but ignoring
    # '__pycache__', etc
    modules = glob.glob(os.path.dirname(cmd_dir[cmd_class]) + "/[a-z]*")
    logger.debug(modules)

    supformats = []
    for f in modules:
        # Verify f is a real file
        # skip f if f's name is __init__.py
        # skip f if f is an emacs backup
        if (os.path.isfile(f) and
            f.split('/')[-1] != '__init__.py' and
            f.split('.')[-1] != 'py~'):
            supformats.append(os.path.basename(f)[:-3])

    supformats.sort()
    logger.debug('Return: ' + str(supformats))
    logger.debug('End Function')
    return supformats

def stripext (filename):
    """Return the basename without extension of given filename."""
    return os.path.splitext(os.path.basename(filename))[0]

#-------------------------------------------------------------------
#
# Function get_module_func
#
# Inputs
# ------
#    @param: cmd_class
#    @param: cmd_type
#    @param: command
#
# Returns
# -------
#    getattr()
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def get_module_func(*args, **kwargs):
    logger.debug('Begun Function')

    scmd = kwargs['scmd']
    program = kwargs['program']
    command = kwargs['cmd']
    if 'format_' in kwargs:
        format_ = kwargs['format_']
    else:
        format_ = False

    """Get the Python function that executes the given program."""
    # get python module for given archive program
    key = stripext(os.path.basename(program).lower())
    if scmd in import_path:
        basemodname = import_path[scmd]
        if scmd == 'util_archive':
            modulename = basemodname + ArchiveModules.get(key, key)            
        elif scmd == 'util_compressed':
            modulename = basemodname + CompressedModules.get(key, key)
        else:
            modulename = basemodname + program

    # import the module
    try:
        module = importlib.import_module(modulename, __name__)
    except ImportError as msg:
        raise Exception(msg)
    # get archive handler function (eg. patoolib.programs.star.extract_tar)
    try:
        if format_:
            return getattr(module, '%s_%s' % (command, format_))
        else:
            return getattr(module, command)
    except AttributeError as msg:
        raise Exception(msg)

    try:
        logger.debug('Module: ' + str(modulename))
        logger.debug('Command: ' + str(command)) 
        logger.debug('End Function')


    except AttributeError as msg:
        logger.error(msg)
        logger.debug('End Function')
        return

#-------------------------------------------------------------------
#
# Function get_module_func
#
# Inputs
# ------
#    @param: cmd_class
#    @param: cmd_type
#    @param: command
#
# Returns
# -------
#    getattr()
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def system_search_path():
    """Get the list of directories on a system to search for executable programs.
    It is either the PATH environment variable or if PATH is undefined the value
    of os.defpath.
    """
    return os.environ.get("PATH", os.defpath)

@memoized
def find_program (program):
    """Look for program in environment PATH variable."""
    if os.name == 'nt':
        # Add some well-known archiver programs to the search path
        path = os.environ['PATH']
        path = append_to_path(path, get_nt_7z_dir())
        path = append_to_path(path, get_nt_mac_dir())
        path = append_to_path(path, get_nt_winrar_dir())
    else:
        # use default path
        path = None
    return which(program, path=path)

def get_filesize(filename):
    """Return file size in Bytes, or -1 on error."""
    return os.path.getsize(filename)

def strsize(b, grouping=True):
    """Return human representation of bytes b. A negative number of bytes
    raises a value error."""
    if b < 0:
        raise ValueError("Invalid negative byte number")
    if b < 1024:
        return u"%sB" % locale.format("%d", b, grouping)
    if b < 1024 * 10:
        return u"%sKB" % locale.format("%d", (b // 1024), grouping)
    if b < 1024 * 1024:
        return u"%sKB" % locale.format("%.2f", (float(b) / 1024), grouping)
    if b < 1024 * 1024 * 10:
        return u"%sMB" % locale.format("%.2f", (float(b) / (1024*1024)), grouping)
    if b < 1024 * 1024 * 1024:
        return u"%sMB" % locale.format("%.1f", (float(b) / (1024*1024)), grouping)
    if b < 1024 * 1024 * 1024 * 10:
        return u"%sGB" % locale.format("%.2f", (float(b) / (1024*1024*1024)), grouping)
    return u"%sGB" % locale.format("%.1f", (float(b) / (1024*1024*1024)), grouping)
