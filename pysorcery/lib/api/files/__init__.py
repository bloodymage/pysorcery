#! /usr/bin/env python3
#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
import os
import subprocess
import mimetypes

# Other Libraries
# Only Load if module rarfile available.
# If not, error, ask if user wants to install
# import rarfile


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib.util import config
from pysorcery.lib.util import text

# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class BaseFile
# 
#
#-------------------------------------------------------------------------------
class BaseFile():
    def __init__(self,filename):
        logger.debug("Begin Function")
        self.filename = filename
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function pne
    #
    # Path Name Extention
    #
    # input:
    # output:
    # return: Path, Name, and Extention
    #
    #-------------------------------------------------------------------------------
    def pne(self):
        """
        Guess the extension of given filename.
        """
        # Add extra extensions where desired.
        DOUBLE_EXTENSIONS = ['tar.gz','tar.bz2','tar.xz']

        path, filename=os.path.split(self.filename)
        root,ext = os.path.splitext(filename)
        if any([filename.endswith(x) for x in DOUBLE_EXTENSIONS]):
            root, first_ext = os.path.splitext(root)
            ext = first_ext + ext
        return path, root, ext

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_from(self):
        logger.debug("Begin Function")
        
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def remove(self):
        logger.debug("Begin Function")

        logger.debug2("Removing File: " + self.filename)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def read(self):
        logger.debug("Begin Function")
        line_list = []
        
        for line in open(self.filename):
            line_list.append(line[:-1])
            
        logger.debug("End Function")
        return line_list

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def write(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("Begin Function")
        return

#-------------------------------------------------------------------------------
#
# Class SourceFile
# 
#
#-------------------------------------------------------------------------------
class DebianFiles(BaseFile):
    def __init__(self,filename):
        logger.debug("Begin Function")
        BaseFile.__init__(self,filename)
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_from(self):
        logger.debug("Begin Function")
        subprocess.run(["dpkg","-S",self.filename])
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class BaseFile
# 
#
#-------------------------------------------------------------------------------
class ActivityLog(BaseFile):
    def __init__(self):
        if distro.distro_id in distro.distro_dict['deb']:
            filename = '/var/log/apt/history.log'
        elif distro.distro_id in distro.distro_dict['smgl']:
            filename = '/var/log/sorcery/activity'
        else:
            logger.error('Fuck')

        BaseFile.__init__(self,filename)
        
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_activity(self):
        logger.debug('Begin Function')
        
        f = BaseFile(self.filename)
        
        history = f.read()

        for i in history:
            logger.info1(i)

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class File
# 
#
#-------------------------------------------------------------------------------
class Files(DebianFiles,BaseFile):
    def __init__(self,filename):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianFiles.__init__(self,filename)
        else:
            BaseFile.__init__(self,filename)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_from(self):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianFiles.print_from(self)
        else:
            BaseFile.print_from(self)

        logger.debug("End Function")
        return


    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_installed_files(self):
        logger.debug("Begin Function")

        if distro.distro_id in distro.distro_dict['deb']:
            installed_files = DebianFileList.list_installed_files(self)
        else:
            installed_files = BaseFileList.list_installed_files(self)
            
        logger.debug("End Function")
        return installed_files


#-------------------------------------------------------------------------------
#
# Class SourceFile
# 
#
#-------------------------------------------------------------------------------
class SourceFile(BaseFile):
    def set_url(self,url):
        logger.debug("Begin Function")
        self.url = url
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def download(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return


    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def verify(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class BaseDirectories():
    def __init__(self,dirname):
        logger.debug('Begin Function')
        self.dirname = dirname

        logger.debug('End Function')
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_name(self):
        logger.debug("Begin Function")
        logger.info(self.dirname)
        logger.debug("End Function")
        return


#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class DebianDirectories(BaseDirectories):
    def __init__(self,dirname):
        logger.debug("Begin Function")
        BaseDirectories.__init__(self,dirname)
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class Directories(DebianDirectories,BaseDirectories):
    def __init__(self,dirname):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianDirectories.__init__(self,dirname)
        else:
            BaseDirectories.__init__(self,dirname)

        logger.debug("End Function")
        return


#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class BaseFileList():
    def __init__(self,dirname):
        logger.debug("Begin Function")

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
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

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
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

#-------------------------------------------------------------------------------
#
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class FileList(DebianFileList,BaseFileList):
    def __init__(self,dirname):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianFileList.__init__(self)
        else:
            BaseFileList.__init__(self)

        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_installed_files(self):
        logger.debug("Begin Function")

        if distro.distro_id in distro.distro_dict['deb']:
            installed_files = DebianFileList.list_installed_files(self)
        else:
            installed_files = BaseFileList.list_installed_files(self)
            
        logger.debug("End Function")
        return installed_files
