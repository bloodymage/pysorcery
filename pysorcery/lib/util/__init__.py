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
# Util:
#
#  Provides common utilities.
#
#-----------------------------------------------------------------------
"""
Util:

Provides common utilities.
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
# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging

# Other Application Libraries
from pysorcery import lib
#from pysorcery.lib.util import files
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
SORCERY_PATH = pkg_resources.resource_filename('pysorcery','lib/sorcery/')

cmd_dir = {
    'util_archive': UTIL_ARCHIVE_PATH,
    'util_compressed': UTIL_COMPRESSED_PATH,
    'util_url': UTIL_URL_PATH,
    'gaze': GAZE_PATH,
    'archive': ARCHIVE_PATH,
    'sorcery': SORCERY_PATH
}

import_path = {
    'util_archive': 'pysorcery.lib.util.files.archive.',
    'util_compressed': 'pysorcery.lib.util.files.compressed.',
    'util_url': 'pysorcery.lib.util.url.',
    'archive': 'pysorcery.plugins.archive.',
    'gaze': 'pysorcery.plugins.gaze.',
    'sorcery': 'pysorcery.lib.sorcery.'
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


#-----------------------------------------------------------------------
#
# Classes
#
# memoized
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class memoized
#
# Decorator that caches a function's return value each time it is called.
# If called later with the same arguments, the cached value is returned, and
# not re-evaluated.
#
# Inputs
# ------
#     @param: self
#     @param: func
#         
# Returns
# -------
#     @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class memoized (object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated."""

    def __init__(self, func):
        """Set func and init cache."""
        self.func = func
        self.cache = {}
        return

    #-------------------------------------------------------------------
    #
    # Function __call__
    #
    # Try to find result for function arguments in local cache or
    # execute the function and fill the cache with the result.
    #
    # Inputs
    # ------
    #     @param: self -
    #     @param: *args -
    #         
    # Returns
    # -------
    #     @return: self.cache[args]
    #     @return: value
    #     @return: self.func(*args)
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
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

    #-------------------------------------------------------------------
    #
    # Function __repr__
    #
    # Return the function's docstring.
    #
    # Inputs
    # ------
    #     @param: self
    #         
    # Returns
    # -------
    #     @return: self.func.__doc__
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
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

#-----------------------------------------------------------------------
#
# Function strlist_with_or
#
# Return comma separated string, and last entry appended with ' or '.
#
# Inputs
# ------
#     @param: alist
#         
# Returns
# -------
#     @return:
#     @return:
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def strlist_with_or (alist):
    """Return comma separated string, and last entry appended with ' or '."""
    if len(alist) > 1:
        return "%s or %s" % (", ".join(alist[:-1]), alist[-1])
    return ", ".join(alist)

#-----------------------------------------------------------------------
#
# Function get_cmd_types
#
# Quote all shell metacharacters in given string value with strong
# (ie. single) quotes, handling the single quote especially.
#
# Inputs
# ------
#     @param: value
#
# Returns
# -------
#     @return:
#     @return:
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def shell_quote (value):
    """Quote all shell metacharacters in given string value with strong
    (ie. single) quotes, handling the single quote especially."""
    if os.name == 'nt':
        return shell_quote_nt(value)
    return "'%s'" % value.replace("'", r"'\''")


#-----------------------------------------------------------------------
#
# Function shell_quote_nt
#
# Quote argument for Windows system. Modeled after distutils
# _nt_quote_args() function.
#
# Inputs
# ------
#     @param: cmd_class - I really need a new name for this...
#        
# Returns
# -------
#     @return:
#     @return:
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def shell_quote_nt (value):
    """Quote argument for Windows system. Modeled after distutils
    _nt_quote_args() function."""
    if " " in value:
        return '"%s"' % value
    return value

#-----------------------------------------------------------------------
#
# Function run
#
# Run command without error checking
#
# Inputs
# ------
#   @param: cmd -
#           verbosity -
#           **kwargs -
#         
# Returns
# -------
#   @return: res - command return code
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def run (cmd, verbosity=0, **kwargs):
    """Run command without error checking.
    @return: command return code"""
    # Note that shell_quote_nt() result is not suitable for copy-paste
    # (especially on Unix systems), but it looks nicer than shell_quote().
    if verbosity >= 0:
        logger.info("running %s" % " ".join(map(shell_quote_nt, cmd)))
    if kwargs:
        if verbosity >= 0:
            logger.info("    with %s"
                        % ", ".join("%s=%s"
                                    % (k,
                                       shell_quote(str(v))
                                    ) for k, v in kwargs.items()))
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


#-----------------------------------------------------------------------
#
# Function run_checked
#
# Run command and raise PatoolError on error.
#
# Inputs
# ------
#     @param: cmd -
#     @param: ret_ok -
#     @param: **kwargs -
#         
# Returns
# -------
#     @return: retcode
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def run_checked (cmd, ret_ok=(0,), **kwargs):
    """Run command and raise PatoolError on error."""
    retcode = run(cmd, **kwargs)
    if retcode not in ret_ok:
        msg = "Command `%s' returned non-zero exit status %d" % (cmd, retcode)
        raise Exception(msg)
    return retcode

#-----------------------------------------------------------------------
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
#     @return: supformats - 'Supported Formats'
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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
            f.endswith('~') is False):
            supformats.append(os.path.basename(f)[:-3])

    supformats.sort()
    logger.debug('Return: ' + str(supformats))
    logger.debug('End Function')
    return supformats

#-----------------------------------------------------------------------
#
# Function get_module_func
#
# Inputs
# ------
#    @param: *args
#    @param: *kwargs
#
# Returns
# -------
#    getattr()
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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
    key = os.path.splitext(os.path.basename(program).lower())[0]
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

        logger.error(msg)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Function system_search_path
#
# Get the list of directories on a system to search for executable programs.
# It is either the PATH environment variable or if PATH is undefined the value
# of os.defpath.
#
# Inputs
# ------
#    @param: None
#
# Returns
# -------
#    @return: os.environ.get("PATH", os.defpath)
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def system_search_path():
    """Get the list of directories on a system to search for executable programs.
    It is either the PATH environment variable or if PATH is undefined the value
    of os.defpath.
    """
    return os.environ.get("PATH", os.defpath)

#-----------------------------------------------------------------------
#
# Function find_program
#
# Look for program in environment PATH variable.
#
# Inputs
# ------
#    @param: program
#
# Returns
# -------
#    @return: which(program, path=path)
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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

#-----------------------------------------------------------------------
#
# Function strsize
#
# Inputs
# ------
#    @param: b
#    @param: grouping
#
# Returns
# -------
#    @return:
#    @return:
#    @return:
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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
