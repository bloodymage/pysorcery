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
#
#
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import os
import subprocess

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
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class BaseFile
#
# This is the base File Class
#
#-----------------------------------------------------------------------
class BaseFile():
    def __init__(self,filename):
        logger.debug("Begin Function")
        
        self.filename = filename
        self.mimetype, self.encoding = mimetypes.guess_type(self.filename)
        self.path, self.basename, self.extention = pne(self.filename)

        self.format_class, self.format_ = get_format(self.mimetype,
                                                     self.encoding)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
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
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def remove(self):
        logger.debug("Begin Function")

        logger.debug2("Removing File: " + self.filename)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
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
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def write(self):
        logger.debug("Begin Function")

        self.description="Ooops!"

        logger.debug("Begin Function")
        return


#-----------------------------------------------------------------------
#
# Class Alien
# 
#
#-----------------------------------------------------------------------
class BaseDirectories():
    def __init__(self,dirname):
        logger.debug('Begin Function')

        self.dirname = dirname

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def print_name(self):
        logger.debug("Begin Function")
        logger.info(self.dirname)
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Class Alien
# 
#
#-----------------------------------------------------------------------
class Directories(BaseDirectories):
    pass

#-----------------------------------------------------------------------
#
# Class Alien
# 
#
#-----------------------------------------------------------------------
class BaseFileList():
    def __init__(self,dirname):
        logger.debug("Begin Function")

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
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
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def list_system_files(self):
        logger.debug("Begin Function")

        # List of directories to check        
        sys_dirs = [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                     '/opt', '/sbin', '/share', '/usr','/var' ]

        sys_files = []
        for sys_dir in sys_dirs:
            for root, dirs, files in os.walk(sys_dir):
                for i in dirs:
                    for j in files:
                        system_file = str(os.path.join(root,i,j))
                        sys_files.append(system_file)
        
        logger.debug("End Function")
        return sys_files

#-----------------------------------------------------------------------
#
# Class Alien
# 
#
#-----------------------------------------------------------------------
class DebianFileList(BaseFileList):
    def __init__(self,dirname):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianDirectories.__init__(self)
        else:
            BaseDirectories.__init__(self)

        logger.debug("End Function")
        return

    def list_installed_files(self):
        logger.debug("Begin Function")

        install_files = [ 'Fuck' ]
        
        logger.debug("End Function")
        return install_files

#-----------------------------------------------------------------------
#
# Class Alien
# 
#
#-----------------------------------------------------------------------
class FileList(DebianFileList,BaseFileList):
    def __init__(self,dirname):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianFileList.__init__(self)
        else:
            BaseFileList.__init__(self)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------
    def list_installed_files(self):
        logger.debug("Begin Function")

        if distro.distro_id in distro.distro_dict['deb']:
            installed_files = DebianFileList.list_installed_files(self)
        else:
            installed_files = BaseFileList.list_installed_files(self)
        
        logger.debug("End Function")
        return installed_files


#-------------------------------------------------------------------
#
# Functions
#
# pne
# get_archive_formats
#
#-------------------------------------------------------------------

#-------------------------------------------------------------------
#
# Function pne
#
# Path Name Extention
#
# input:
# output:
# return: Path, Name, and Extention
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

#-------------------------------------------------------------------
#
# Function id_archive_format
#
# Input:  ...
# Output: ...
# Return: archive_format
#         encoding
#
#-------------------------------------------------------------------
def get_format(mimetype=None,encoding=None):
    logger.debug('Begin Function')

    if (mimetype is None and
        encoding is None):
        logger.error('Unknown archive type')
        
    elif (mimetype not in mimetypes.ArchiveMimetypes and
        encoding in mimetypes.encoding_methods):
        archive_class = mimetypes.encoding_methods[encoding]
        
    elif mimetype in mimetypes.ArchiveMimetypes:
        archive_class = mimetypes.ArchiveMimetypes[mimetype]
    else:
        archive_class = mimetype
        logger.error('Unknown archive type for mime:' + str(mimetype))

    if archive_class in shutil.archive_formats:
        archive_format = shutil.archive_formats[archive_class][encoding]
        shutil.init_formats('util_archive')
    elif archive_class in shutil.compressed_formats:
        archive_format = shutil.compressed_formats[archive_class][encoding]
        shutil.init_formats('util_compressed')
    else:
        archive_format = 'Unknown'

    logger.debug('End Function')
    return archive_class, archive_format
