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
import sys
import os
import argparse
import copy
import subprocess

# Other Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery import __version__
from pysorcery.lib import libtext
from pysorcery.lib import libconfig

# Other Optional Libraries
if distro.distro_id in distro.distro_dict['deb']:
    import apt

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
        
    def print_from(self):
        logger.debug("Begin Function")
        
        logger.debug("End Function")
        return

    def remove(self):
        logger.debug("Begin Function")

        logger.debug2("Removing File: " + self.filename)

        logger.debug("End Function")
        return

    def read(self):
        logger.debug("Begin Function")
        line_list = []
        for lines in open(self.filename):
            line_list.append(lines)
            
        logger.debug("End Function")
        return line_list

    def write(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("Begin Function")
        return

#-------------------------------------------------------------------------------
#
# Class BuildFile
# 
#
#-------------------------------------------------------------------------------
class BuildFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigureFile
# 
#
#-------------------------------------------------------------------------------
class ConfigureFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConflictsFile
# 
#
#-------------------------------------------------------------------------------
class ConflictsFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class DetailsFile
# 
#
#-------------------------------------------------------------------------------
class DetailsFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class DependsFile
# 
#
#-------------------------------------------------------------------------------
class DependsFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class DownloadFile
# 
#
#-------------------------------------------------------------------------------
class DownloadFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class FinalFile
# 
#
#-------------------------------------------------------------------------------
class FinalFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class HistoryFile
# 
#
#-------------------------------------------------------------------------------
class HistoryFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class HistoryFile
# 
#
#-------------------------------------------------------------------------------
class InstallFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class InstallExtrasFile
# 
#
#-------------------------------------------------------------------------------
class InstallExtrasFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class HistoryFile
# 
#
#-------------------------------------------------------------------------------
class PatchFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PostBuildFile
# 
#
#-------------------------------------------------------------------------------
class PostBuildFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PostInstallFile
# 
#
#-------------------------------------------------------------------------------
class PostInstallFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PostRemoveFile
# 
#
#-------------------------------------------------------------------------------
class PostRemoveFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class HistoryFile
# 
#
#-------------------------------------------------------------------------------
class PostResurrectFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PreBuildFile
# 
#
#-------------------------------------------------------------------------------
class PreBuildFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PreInstallFile
# 
#
#-------------------------------------------------------------------------------
class PreInstallFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PreRemoveFile
# 
#
#-------------------------------------------------------------------------------
class PreRemoveFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PreResurrectFile
# 
#
#-------------------------------------------------------------------------------
class PreResurrectFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PreSubDependsFile
# 
#
#-------------------------------------------------------------------------------
class PreSubDependsFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class PrepareFile
# 
#
#-------------------------------------------------------------------------------
class PrepareFile(BaseFile):
    def __init__(self,name):
        logger.debug("Begin Function")
        self.name = name
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class ProvidesFile
# 
#
#-------------------------------------------------------------------------------
class ProvidesFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class SecurityFile
# 
#
#-------------------------------------------------------------------------------
class SecurityFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class SubDependsFile
# 
#
#-------------------------------------------------------------------------------
class SubDependsFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class TransferFile
# 
#
#-------------------------------------------------------------------------------
class TransferFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class TriggerCheckFile
# 
#
#-------------------------------------------------------------------------------
class TriggerCheckFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class TriggersFile
# 
#
#-------------------------------------------------------------------------------
class TriggersFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class UpTriggersFile
# 
#
#-------------------------------------------------------------------------------
class UpTriggersFile(BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.demug('End Function')
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

    def print_from(self):
        logger.debug("Begin Function")
        subprocess.run(["dpkg","-S",self.filename])
        logger.debug("End Function")
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

    def print_from(self):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianFiles.print_from(self)
        else:
            BaseFile.print_from(self)

        logger.debug("End Function")
        return

class ActivitiesFile(BaseFile):
    def __init__(self):
        if distro.distro_id in distro.distro_dict['deb']:
            filename = '/var/log/apt/history.log'
        elif distro.distro_id in distro.distro_dict['smgl']:
            filename = '/var/log/sorcery/activity'
        else:
            logger.error('Fuck')

        BaseFile.__init__(self,filename)
        
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
# Class Alien
# 
#
#-------------------------------------------------------------------------------
class Alien():
    def __init__(self):
        logger.debug("Begin Function")

        logger.debug("End Function")
        return

    def identify(self):
        logger.debug("Begin Function")
        
        logger.info("In a few minutes I will print files found on this disk")
        logger.info("that were not installed by sorcery.")
        logger.warning("This is not a security feature!")        
        logger.info("Files could still be lurking undetected on this box.")

        if distro.distro_id in distro.distro_dict['deb']:
            # Find a python solution
            subprocess.run(["cruft"])
            
        elif distro.distro_id in distro.distro_dict['smgl']:
            # 1. Find Install Log Files
            # 2. Gather list of installed files
            logger.info("Discovering installed files...")
            installed_files = FileList.list_installed_files(self)
            
            # 3. Find all system files
            logger.info("Discovering ambient files...")
            system_files = FileList.list_system_files(self)
            
            # 4. Print files from step 3 - files from 2            
            alien_files = list(set(system_files) - set(installed_files))

            alien_files.sort()
            
            for i in alien_files:
                logger.info1(i)

        else:
            logger.error("Alien Error")    
            
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class SourceFile
# 
#
#-------------------------------------------------------------------------------
class SourceFile(BaseFile):
    def __init__(self,name):
        logger.debug("Begin Function")
        self.name = name
        self.url = url
        logger.debug("End Function")
        return

    def download(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return

    def unpack(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return

    def verify(self):
        logger.debug("Begin Function")
        self.description="Ooops!"
        logger.debug("End Function")
        return
