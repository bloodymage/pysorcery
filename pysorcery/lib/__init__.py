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
# File: pysorcery/lib/__init__.py
#
# This file is part of Sorcery.
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
# This file is the pysorcery API.  All files should reference this file.
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries


# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
from pysorcery.lib.system import logging
from pysorcery.lib.system import mimetypes
# Other Application Libraries
#from pysorcery.lib.sorcery import packages
#from pysorcery.lib.sorcery import repositories
#from pysorcery.lib.util import config
from pysorcery.lib.util import files
from pysorcery.lib.util.files import archive
from pysorcery.lib.util.files import compressed
#from pysorcery.lib.util import text
#from pysorcery.lib.util import url

# Other Optional Libraries

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
# Files
# FileList
# Directories
# DirectoryList
# Package
# PackageList
# Repository
# RepositoryList
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class Files
# 
#
#-----------------------------------------------------------------------
class Files(compressed.CompressedFile, archive.Archive, files.BaseFile):
    def read(self):
        if self.format_ != 'Unknown':
            content = compressed.CompressedFile.read(self)
        else:
            content = files.BaseFile.read(self)

        logger.debug('End Function')
        return content


#-----------------------------------------------------------------------
#
# Class FileList
# 
#
#-----------------------------------------------------------------------
class FileList(files.BaseFileList):
    pass

#-------------------------------------------------------------------------------
#
# Class Directories
# 
#
#-------------------------------------------------------------------------------
#class Directories(files.DebianDirectories,files.BaseDirectories):
# pass

#-------------------------------------------------------------------------------
#
# Functions
# 
# Recompress
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Function recompress
#
# Input:  @param: srcfile - the original file
#         @param: dstfile - the new file we are creating with the new
#                           compression method.
# Return: None
#
#-------------------------------------------------------------------------------
def recompress(srcfile, dstfile):
    logger.debug('Begin Function')
    
    source_file = Files(srcfile)
    source_file.decompress(None)
    
    dest_file = Files(dstfile)
    dest_file.compress(source_file.basename)
    
    logger.debug('End Function')
    return

"""
#-------------------------------------------------------------------------------
#
# Class Spell
#
# This is the spell API.
# All spell related actions should go through this class
#
#-------------------------------------------------------------------------------
class Spell(packages.DebianSpell,packages.SMGLBashSpell,packages.BaseSpell):
    def __init__(self,name):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianSpell.__init__(self,name)
        elif distro.distro_id in distro.distro_dict['smgl']:
            SMGLBashSpell.__init__(self,name)
        else:
            BaseSpell.__init__(self,name)

        logger.debug("Begin Function")
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
    def print_version(self,multi=False):
        logger.debug("Begin Function")
        
        if multi:
            grimoires = libcodex.Codex()
            grimoire_list = grimoires.list_grimoires()
            
            m = len(grimoire_list)
        else:
            grimoire_list = [ self.grimoire ]
            m = 1

        if distro.distro_id in distro.distro_dict['deb']:
            print_list = [ "Repository       " ]
        else:
            print_list = [ "Grimoire         " ]
            
        print_list.append("Section          ")

        if distro.distro_id in distro.distro_dict['deb']:
            print_list.append("Package          ")
        else:
            print_list.append("Spell            ")

        if distro.distro_id in distro.distro_dict['deb']:
            print_list.append("Repo version     ")
        else:
            print_list.append("Grimoire Version ")

        print_list.append("Installed version")
        print_list.append("----------       ")
        print_list.append("-------          ")
        print_list.append("-------          ")
        print_list.append("------------     ")
        print_list.append("-----------------")


        for i in grimoire_list:
            print_list.append(i.split('/')[-1])
            print_list.append(self.section)
            print_list.append(self.name)
            print_list.append(self.version)
            print_list.append('-')

        libmisc.column_print(print_list,cols=5,columnwise=False,gap=2)
                
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
    def install(self,args):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianSpell.install(self,args)
        elif distro.distro_id in distro.distro_dict['smgl']:
            SMGLBashSpell.install(self,args)
        else:
            BaseSpell.install(self,args)

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
    def remove(self,args):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianSpell.remove(self,args)
        elif distro.distro_id in distro.distro_dict['smgl']:
            SMGLBashSpell.install(self,args)
        else:
            BaseSpell.remove(self,args)

        logger.debug("End Function")
        return    

#-------------------------------------------------------------------------------
#
# Class SpellList
#
# This is the spell queue API.
# All spell related actions should go through this class
#
#-------------------------------------------------------------------------------
class SpellList(DebianSpellList,BaseSpellList):
    def __init__(self):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianSpellList.__init__(self)
        else:
            BaseSpellList.__init__(self)

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
    def list_queue(self,which_queue):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            queue = DebianSpellList.list_queue(self,which_queue)
        else:
            queue = BaseSpellList.list_queue(self,which_queue)

        logger.debug("End Function")
        return queue

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_installed(self,status=None):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            installed_spells = DebianSpellList.list_installed(self,status)
        else:
            installed_spells = BaseSpellList.list_installed(self,status)

        logger.debug("End Function")
        return installed_spells

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_orphans(self):
        logger.debug('Begin Function')
        if distro.distro_id in distro.distro_dict['deb']:
            orphan_list = DebianSpellList.list_orphans(self)
        else:
            orphan_list = BaseSpellList.list_orphans(self)

        logger.debug('End Function')
        return orphan_list

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def print_list(self, print_list):
        logger.debug("Begin Function")

        for item in print_list:
            logger.info1(item)
            
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
    def print_installed(self):
        logger.debug("Begin Function")

        spell_list = InstalledSpells.list_installed(self)

        print_list = ['Spell','Installed Version', 'Installed Date',
                      '-----','-----------------', '--------------'] + spell_list
        
        text.column_print(print_list,cols=3,columnwise=False,gap=2)
        
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class Repository
# 
#
#-------------------------------------------------------------------------------
class Repository(DebianGrimoire,BaseGrimoire):
    def __init__(self,name = None, grim_dir = None):
        if distro.distro_id in distro.distro_dict['deb']:
            DebianGrimoire.__init__(self,name, grim_dir)
        else:
            BaseGrimoire.__init__(self,name, grim_dir)

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
    def list_spells(self):
        print("Spells")
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
    def add(self):
        if distro.distro_id in distro.distro_dict['deb']:
            DebianGrimoire.add(self)
        else: # distro.distro_id in distro.distro_dict['smgl']:
            BaseGrimoire.add(self)
        #else:
            # Add except?
            #logger.critical("We shouldn't be here")

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def list_sections(self):
        if distro.distro_id in distro.distro_dict['deb']:
            section_list = DebianGrimoire.list_sections(self)
        else: # distro.distro_id in distro.distro_dict['smgl']:
            section_list = BaseGrimoire.list_sections(self)
        #else:
            # Add except?
            #logger.critical("We shouldn't be here")

        return section_list

#-------------------------------------------------------------------------------
#
# Class URI
# 
# The URI API
#
# Currently Supports:
#   HTTP(S)
#
# Planned Support:
#   SFTP
#
#-------------------------------------------------------------------------------
class URI(HTTPUri,
          FTPUri,
          RsyncUri,
          GitUri,
          CVSUri,
          SVNUri,
          TorrentUri,
          BaseURI):
    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # 
    #
    #-------------------------------------------------------------------------------
    def download(self):
        logger.debug('Begin Function')

        if self.uri.startswith('http'):
            HTTPUri.download(self)
        else:
            logger.error('We Fucked Up')
            
        logger.debug('End Function')
        return

"""
