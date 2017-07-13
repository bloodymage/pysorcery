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
# SMGL: BashSpell
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
import mimetypes

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery import lib
from pysorcery.lib.util import files
from pysorcery.lib.util import text

# Other Optional Libraries

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

spellfiles = [ 'BUILD',
               'CONFIGURE',
               'CONFLICTS',
               'DETAILS',
               'DEPENDS',
               'DOWNLOAD',
               'FINAL',
               'HISTORY',
               'INSTALL',
               'INSTALL_EXTRAS',
               'PATCH',
               'POST_BUILD',
               'POST_INSTALL',
               'POST_REMOVE',
               'POST_RESURRECT',
               'PRE_BUILD',
               'PRE_INSTALL',
               'PRE_REMOVE',
               'PRE_RESURRECT',
               'PRE_SUB_DEPENDS',
               'PREPARE',
               'PROVIDES',
               'SECURITY',
               'SUB_DEPENDS',
               'TRANSFER',
               'TRIGGER_CHECK',
               'TRIGGERS',
               'UP_TRIGGERS'
]

#-----------------------------------------------------------------------
#
# Classes
#
# BuildFile
# ConfigureFile
# ConflictsFile
# DetailsFile
# DependsFile
# DownloadFile
# FinalFile
# HistoryFile
# InstallFile
# InstallExtrasFile
# PatchFile
# PostBuildFile
# PostInstallFile
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class BuildFile
# 
# Inputs
# ------
#    @param: name
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
class BuildFile(files.BaseFile):
    pass

#-----------------------------------------------------------------------
#
# Class ConfigureFile
# 
# Inputs
# ------
#    @param: name
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
class ConfigureFile(files.BaseFile):
    pass

#-----------------------------------------------------------------------
#
# Class ConflictsFile
# 
# Inputs
# ------
#    @param: name
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
class ConflictsFile(files.BaseFile):
    pass

#-----------------------------------------------------------------------
#
# Class DetailsFile
# 
# Inputs
# ------
#    @param: name
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
class DetailsFile(files.BaseFile):
    def __init__(self,spell_directory):
        files.BaseFile.__init__(self, spell_directory + '/DETAILS')
        return

    #-------------------------------------------------------------------
    #
    # Function 
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    @param: self
    #
    # Returns
    # -------
    #    @return: description
    #
    # Raises
    # ------
    #    ...
    # Return: description - The description of the package
    #
    #-------------------------------------------------------------------
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
                elif 'LICENSE' in key:
                    details_dict['license'] = value
            else:
                logger.debug('Line: ' + line)

        details_dict['description'] = description

        logger.debug('End Function')
        return details_dict

#-----------------------------------------------------------------------
#
# Class DependsFile
# 
# Inputs
# ------
#    @param: name
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
class DependsFile(files.BaseFile):
    def __init__(self,filename):
        logger.debug('Begin Function')
        
        files.BaseFile.__init__(self,spell_directory + '/DEPENDS')
        
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class DownloadFile
# 
# Inputs
# ------
#    @param: name
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
class DownloadFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class FinalFile
# 
# Inputs
# ------
#    @param: name
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
class FinalFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
# 
# Inputs
# ------
#    @param: name
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
class HistoryFile(files.BaseFile):
    def __init__(self, spell_directory):
        files.BaseFile.__init__(self, spell_directory + '/HISTORY')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
# 
# Inputs
# ------
#    @param: name
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
class InstallFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class InstallExtrasFile
# 
# Inputs
# ------
#    @param: name
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
class InstallExtrasFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
# 
# Inputs
# ------
#    @param: name
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
class PatchFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PostBuildFile
# 
# Inputs
# ------
#    @param: name
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
class PostBuildFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PostInstallFile
# 
# Inputs
# ------
#    @param: name
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
class PostInstallFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PostRemoveFile
# 
# Inputs
# ------
#    @param: name
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
class PostRemoveFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class HistoryFile
# 
# Inputs
# ------
#    @param: name
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
class PostResurrectFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PreBuildFile
# 
# Inputs
# ------
#    @param: name
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
class PreBuildFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PreInstallFile
# 
# Inputs
# ------
#    @param: name
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
class PreInstallFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PreRemoveFile
# 
# Inputs
# ------
#    @param: name
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
class PreRemoveFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PreResurrectFile
# 
# Inputs
# ------
#    @param: name
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
class PreResurrectFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PreSubDependsFile
# 
# Inputs
# ------
#    @param: name
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
class PreSubDependsFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class PrepareFile
# 
# Inputs
# ------
#    @param: name
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
class PrepareFile(files.BaseFile):
    def __init__(self,name):
        logger.debug("Begin Function")
        self.name = name
        logger.debug("End Function")
        return

#-----------------------------------------------------------------------
#
# Class ProvidesFile
# 
# Inputs
# ------
#    @param: name
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
class ProvidesFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class SecurityFile
# 
# Inputs
# ------
#    @param: name
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
class SecurityFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class SubDependsFile
# 
# Inputs
# ------
#    @param: name
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
class SubDependsFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class TransferFile
# 
# Inputs
# ------
#    @param: name
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
class TransferFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class TriggerCheckFile
# 
# Inputs
# ------
#    @param: name
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
class TriggerCheckFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class TriggersFile
# 
# Inputs
# ------
#    @param: name
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
class TriggersFile(files.BaseFile):
    def __init__(self,name):
        logger.debug('Begin Function')
        files.BaseFile.__init__(self,filename)
        logger.debug('End Function')
        return

#-----------------------------------------------------------------------
#
# Class UpTriggersFile
# 
# Inputs
# ------
#    @param: name
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
class UpTriggersFile(files.BaseFile):
    pass
