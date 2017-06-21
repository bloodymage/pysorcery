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
import os
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
# Class BaseFile
#
# This is the base File Class
#
# Inputs
# ------
#    @param: filename - 
#
# Returns
# -------
#    None
#
# Raises
# ------
#    ...
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
    # Function list_from
    #
    # ...
    #
    # Inputs
    # ------
    #    @param:
    #
    # Returns
    # -------
    #    pkg_list - list of ..
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def list_from(self):
        logger.debug("Begin Function")

        id_from = { 'deb' : subprocess.check_output(["dpkg",
                                                     "-S",
                                                     self.filename]),
                    'smgl': 'Fix Me'
        }
        var = id_from[distro.distro_pkg[distro.distro_id]]

        pkg_list = []
        for line in var.splitlines():
            line_list = str(line).split(',')
            item = line_list[0].split("'")[1]
            pkg_list.append(item)

        logger.debug("End Function")
        return pkg_list

    #-------------------------------------------------------------------
    #
    # Function remove
    #
    # ...
    #
    # Inputs
    # ------
    #    @param: ...
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
    def remove(self):
        logger.debug("Begin Function")

        logger.debug2("Removing File: " + self.filename)

        logger.debug("End Function")
        return

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
    #    @return: None
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
    def check_writable_filename(self):
        """Ensure that the given filename is writable."""
        if not os.access(self.filename, os.W_OK):
            raise PatoolError("file `%s' is not writable" % self.filename)
        return
    
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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
    def check_existing_filename (self, onlyfiles=True):
        """Ensure that given filename is a valid, existing file."""
        if not os.path.exists(self.filename):
            raise Exception("file `%s' was not found" % self.filename)
        if not os.access(self.filename, os.R_OK):
            raise Exception("file `%s' is not readable" % self.filename)
        if onlyfiles and not os.path.isfile(self.filename):
            raise Exception("`%s' is not a file" % self.filename)
        return

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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    
    #
    #-----------------------------------------------------------------------
    def check_new_filename (self):
        """Check that filename does not already exist."""
        if os.path.exists(self.filename):
            raise FileExistsError("cannot overwrite existing file `%s'"
                                  % self.filename)
        return

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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
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
    #-------------------------------------------------------------------
    def read(self):
        logger.debug("Begin Function")
        line_list = []
        
        for line in open(self.filename):
            line_list.append(line[:-1])
            
        logger.debug("End Function")
        return line_list

    #-------------------------------------------------------------------
    #
    # Function write
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
    #-------------------------------------------------------------------
    def write(self):
        logger.debug("Begin Function")

        self.description="Ooops!"

        logger.debug("Begin Function")
        return

    #-------------------------------------------------------------------
    #
    # Function search
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
    #-------------------------------------------------------------------
    def search(self, searchstring):
        logger.debug("Begin Function")

        results = "File Search Results"

        logger.debug("Begin Function")
        return results

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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
    def stripext (self):
        """Return the basename without extension of given filename."""
        return os.path.splitext(os.path.basename(self.filename))[0]
    
    #-----------------------------------------------------------------------
    #
    # Function get_filesize
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
    #-----------------------------------------------------------------------
    def get_filesize(self):
        """Return file size in Bytes, or -1 on error."""
        return os.path.getsize(self.filename)

#-----------------------------------------------------------------------
#
# Class BaseDirectory
#
# Directories are a specific type of file
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
class BaseDirectory(BaseFile):
    #-------------------------------------------------------------------
    #
    # Function 
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
    #-------------------------------------------------------------------
    def print_name(self):
        logger.debug("Begin Function")
        logger.info(self.filename)
        logger.debug("End Function")
        return

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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
    def tmpdir(self, dir=None):
        """Return a temporary directory for extraction."""
        return tempfile.mkdtemp(suffix='', prefix='Unpack_', dir=dir)

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
class BaseFiles():
    def __init__(self, *args, **kwargs):
        logger.debug("Begin Function")

        self.files = kwargs['filelist']

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
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
    #-------------------------------------------------------------------
    def list_installed_files(self):
        logger.debug("Begin Function")

        install_log_dir = '/var/log/sorcery/install'
        install_files = []
        for root, dirs, files  in os.walk(install_log_dir):
            for i in files:
                install_log = install_log_dir + '/'+ i
                f = Files(install_log)
                install_files = install_files + f.read()
        
        logger.debug("End Function")
        return install_files

    #-------------------------------------------------------------------
    #
    # Function list_system_files
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
    #-------------------------------------------------------------------
    def list_system_files(self):
        logger.debug("Begin Function")

        # List of directories to check        
        sys_dirs = [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                     '/opt', '/sbin', '/share', '/usr','/var' ]
        ignore_dirs = ['/home']

        sys_files = []
        for sys_dir in sys_dirs:
            for root, dirs, files in os.walk(sys_dir):
                for i in dirs:
                    for j in files:
                        system_file = str(os.path.join(root,i,j))
                        sys_files.append(system_file)
        
        logger.debug("End Function")
        return sys_files

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
    def is_same_file (self):
        """Check if filename1 and filename2 point to the same file object.
        There can be false negatives, ie. the result is False, but it is
        the same file anyway. Reason is that network filesystems can create
        different paths to the same physical file.
        """
        if self.files[0] == self.files[1]:
            return True
        if os.name == 'posix':
            return os.path.samefile(self.files[0], self.files[1])
        return self.is_same_filename(self.files[0], self.files[1])

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
    def is_same_filename(self):
        """Check if filename1 and filename2 are the same filename."""
        return os.path.realpath(self.files[0]) == os.path.realpath(self.files[1])

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
    #     supformats - 'Supported Formats'
    #
    # Raises
    # ------
    #    ...
    #
    #-----------------------------------------------------------------------
    def check_archive_filelist (self):
        """Check that file list is not empty and contains only existing files."""
        if not self.files:
            raise Exception("cannot create archive with empty filelist")
        for filename in self.files:
            file_ = BaseFile(filename)
            file_.check_existing_filename(filename, onlyfiles=False)
        return

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
# Path Name Extention
#
# ...
#
# Inputs
# ------
#    @param: ifilename
#
# Returns
# -------
#    Path
#    Name
#    Extention
#
# Raises
# ------
#    ...
#
#-------------------------------------------------------------------
def pne(ifilename):
    """
    Guess the extension of given filename.
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
#-----------------------------------------------------------------------
def get_single_outfile (directory, archive, extension=""):
    """Get output filename if archive is in a single file format like gzip."""
    archname = BaseFile(archive)
    outfile = os.path.join(directory, archname.stripext())
    if os.path.exists(outfile + extension):
        # prevent overwriting existing files
        i = 1
        newfile = "%s%d" % (outfile, i)
        while os.path.exists(newfile + extension):
            newfile = "%s%d" % (outfile, i)
            i += 1
        outfile = newfile
    return outfile + extension
