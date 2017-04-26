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
#    Sorcery is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Sorcery.  If not, see <http://www.gnu.org/licenses/>.
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
#
#-------------------------------------------------------------------------------

# System Libraries

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import distro
# Other Application Libraries
from pysorcery.lib.sorcery import packages
from pysorcery.lib.util import text

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
logger = logging.getLogger(__name__)

#-------------------------------------------------------------------------------
#
# Classes
#
#
# BaseSpell
# DebianSpell
# Spell
#
# BaseSpellQueue
# DebianSpellQueue
# SpellQueue
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class Spell
#
# This is the spell API.
# All spell related actions should go through this class
#
#-------------------------------------------------------------------------------
class Spell(DebianSpell,SMGLBashSpell,BaseSpell):
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
