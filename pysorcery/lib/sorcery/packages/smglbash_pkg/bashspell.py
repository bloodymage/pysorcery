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
# Class BuildFile
# 
#
#-------------------------------------------------------------------------------
class BuildFile(BaseFile):
    def __init__(self,filename):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConfigureFile
# 
#
#-------------------------------------------------------------------------------
class ConfigureFile(BaseFile):
    def __init__(self,filename):
        logger.debug('Begin Function')
        BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class ConflictsFile
# 
#
#-------------------------------------------------------------------------------
class ConflictsFile(BaseFile):
    def __init__(self,filename):
        logger.debug('Begin Function')
        
        BaseFile.__init__(self,spell_directory + '/CONFIGURE')
        
        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class DetailsFile
# 
#
#-------------------------------------------------------------------------------
class DetailsFile(BaseFile):
    def __init__(self,spell_directory):
        logger.debug('Begin Function')
        
        BaseFile.__init__(self,spell_directory + '/DETAILS')
        
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
    def parse(self):
        logger.debug('Begin Function')
        
        details_dict = {}

        description_check = False
        case_check = False
        description = ''
        for i in open(self.filename):
            line = i[:-1]


            if (line.startswith('#')):
                logger.debug('Ignoring Line' + line)
            elif ('cat' in line and
                  'EOF' in line):
                description_check = True
            elif 'EOF' in line:
                description_check = False
            elif description_check is True:
                if len(description) == 0:
                    description = line
                else:
                    description += ' ' + line
            elif ('case' in line and
                  'in' in line):
                case_check = True
            elif 'esac' in line:
                case_check = False
            elif case_check is True:
                logger.debug('Ignore Case')
            elif '=' in line:

                key, value = line.split('=')
                if 'VERSION' in key:
                    logger.debug('Line: ' + line)
                    details_dict['version'] = value
                elif 'WEB_SITE' in key:
                    details_dict['website'] = value
                elif key.startswith('SOURCE'):
                    details_dict['source'] = value
                elif 'SHORT' in key:
                    details_dict['short'] = value
            else:
                logger.debug('Line: ' + line)

        details_dict['description'] = description

        logger.debug('End Function')
        return details_dict

#-------------------------------------------------------------------------------
#
# Class DependsFile
# 
#
#-------------------------------------------------------------------------------
class DependsFile(BaseFile):
    def __init__(self,filename):
        logger.debug('Begin Function')
        
        BaseFile.__init__(self,spell_directory + '/DEPENDS')
        
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
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
        logger.debug('End Function')
        return
