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
import sys
import subprocess
import os

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery.lib import libcodex
from pysorcery.lib import libfiles
from pysorcery.lib import libmisc
from pysorcery.lib import libmisc
from pysorcery.lib import libtext

# Other Optional Libraries
if distro.distro_id in distro.distro_dict['deb']:
    import apt

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
# Class BaseSpell
# 
#
#-------------------------------------------------------------------------------
class BaseSpell():
    def __init__(self,name):
        logger.debug("Begin Function")
        
        self.name = name

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
    def set_details(self):
        logger.debug('Begin Function')
        
        codex = libcodex.Codex()
        grimoire_list = codex.list_grimoires()

        for i in grimoire_list:
            spell_list_file = libfiles.Files(i + '/codex.index')
            spell_list = spell_list_file.read()

            for item in spell_list:
                spell, section_dir = item.split(' ')

                if self.name == spell:
                    self.section_dir = section_dir
                    break

            if self.name == spell:
                self.grimoire = i.split('/')[-1]
                break

        self.section = self.section_dir.split('/')[-1]
        self.spell_directory = self.section_dir + '/' + self.name

        details_file = libfiles.DetailsFile(self.spell_directory)
        details = details_file.read()
        
        self.description = details['description']
        self.version = details['version']
        self.url = details['website']
        self.short = details['short']
        
        self.source_files = {}

        #file_name = url.split('/')[-1]

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
        print("Installing: " + self.name)
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class BaseSpell
# 
#
#-------------------------------------------------------------------------------
class SMGLBashSpell():
    def __init__(self,name):
        logger.debug("Begin Function")
        BaseSpell.__init__(self,name)
        
        codex = libcodex.Codex()
        grimoire_list = codex.list_grimoires()

        for i in grimoire_list:
            spell_list_file = libfiles.Files(i + '/codex.index')
            spell_list = spell_list_file.read()

            for item in spell_list:
                spell, section_dir = item.split(' ')

                if self.name == spell:
                    self.section_dir = section_dir
                    break

            if self.name == spell:
                self.grimoire = i.split('/')[-1]
                break

        self.section = self.section_dir.split('/')[-1]
        self.spell_directory = self.section_dir + '/' + self.name

        details_file = libfiles.DetailsFile(self.spell_directory)
        details = details_file.read()
        
        self.description = details['description']
        self.version = details['version']
        self.url = details['website']
        self.short = details['short']
        
        self.source_files = {}

        #file_name = url.split('/')[-1]

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
        print("Installing: " + self.name)
        logger.debug("End Function")
        return

#-------------------------------------------------------------------------------
#
# Class DebianSpell
# 
#
#-------------------------------------------------------------------------------
class DebianSpell(BaseSpell):
    def __init__(self,name):
        logger.debug("Begin Function")
        BaseSpell.__init__(self,name)

        self.cache    = apt.cache.Cache()
#        self.cache.update()
        self.cache.open()
        
        self.pkg      = self.cache[self.name]

        versions = self.pkg.versions

        self.version = versions[0].version

        self.architecture = versions[0].architecture
        self.description  = versions[0].description
        self.url = versions[0].homepage
        self.short = self.description

        pkg_section = versions[0].section

        if 'universe' in pkg_section or 'multiverse' in pkg_section:
            self.section = str(pkg_section).split('/')[1]
        else:
            self.section = str(pkg_section)            

        self.grimoire = 'Fix Me'            
        self.dependencies = versions[0].dependencies
        self.optional_dependencies = versions[0].suggests
        self.size = versions[0].installed_size
        
        logger.debug("End Function")
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ....x
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def install(self, args):
        logger.debug("Begin Function")

        if args.reconfigure:
            subprocess.run(['dpkg-reconfigure', self.name])

            
        if args.compile:
            subprocess.run(['apt-build', 'install', self.name])
        else:
            subprocess.run(['apt-get', 'install', self.name])
                    
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
    def remove(self, args):
        logger.debug("Begin Function")

        #subprocess.run(['apt-get', 'remove', self.name])

        cache = apt.cache.Cache()
        cache.open(None)
        pkg = cache[pkg_name]
        cache.update()
        pkg.mark_delete(True, purge=True)
        resolver = apt.cache.ProblemResolver(cache)
        
        if pkg.is_installed is False:
            logger.error(pkg_name + " not installed so not removed")
        else:
            for pkg in cache.get_changes():
                if pkg.mark_delete:
                    logger.info(pkg_name + " is installed and will be removed")
                    logger.info(" %d package(s) will be removed" % cache.delete_count)
                    resolver.remove(pkg)
                    
        try:
            cache.commit()
            cache.close()
        except Exception:
            logger.error("Sorry, package removal failed.")
                    
        logger.debug("End Function")
        return

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
# Class BaseSpellQueue
#
# This is the spell API.
# All spell related actions should go through this class
#
#-------------------------------------------------------------------------------
class BaseSpellList():
    def __init__(self):
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
    def list_queue(self,which_queue):
        logger.debug("Begin Function")
        queue_file = libfiles.Files('/var/log/sorcery/queue/' + which_queue)

        queue = queue_file.read()

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

        spell_list = []

        for line in open('/var/state/sorcery/packages'):
            spell = line.split(':')

            name = spell[0]
            date = spell[1]
            spellstatus = spell[2]
            version = spell[3]

            if not status and spellstatus != 'exiled':
                spell_list.append(name)
                spell_list.append(date)
                spell_list.append(version)
            elif status == spellstatus:
                spell_list.append(name)
                spell_list.append(date)
                spell_list.append(version)
            else:
                logger.error('We fucked up')

        logger.debug('End Function')
        return spell_list


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

        var = subprocess.check_output(['gaze','orphans'])

        orphan_list = []
        for line in var.splitlines():
            line_list = str(line).split(',')
            item = line_list[0].split("'")[1]
            orphan_list.append(item)

        logger.debug2(orphan_list)
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
    def list_provides(self, feature):
        logger.debug('Begin Function')

        grimoires =  libcodex.Codex()

        providers = []
        for grimoire in grimoires.list_grimoires():
            for line in open(grimoire + '/provides.index'):
                if feature.upper() == line.split(' ')[0]:
                    providers.append(line.split('/')[-1][:-1])

        logger.debug('End Function')
        return providers


#-------------------------------------------------------------------------------
#
# Class DebianSpellQueue
#
# This is the spell API.
# All spell related actions should go through this class
#
#-------------------------------------------------------------------------------
class DebianSpellList(BaseSpellList):
    def __init__(self):
        logger.debug("Begin Function")
        BaseSpellList.__init__(self)

        #self.cache = apt.Cache()
        #self.cache.update()
        #self.cache.open(None)

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

        if which_queue == 'install':
            cache = apt.cache.Cache()
            cache.open(None)
            cache.upgrade()
            queue = cache.get_changes()
        elif which_queue == 'remove':
            queue = []
            logger.error('Not Implimented')
        else:
            queue = []
            logger.critical('We Fucked Up')
            

        logger.debug2(queue)
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
        var = subprocess.check_output(['apt', 'list','--installed'])

        spell_list = []
        
        for line in var.splitlines():
            tmpline = str(line).split("'")[1]
            
            name = tmpline.split('/')[0]
            
            if 'Listi' not in name:
                spell_list.append(name)
                spell_list.append('-')
                spell_list.append('-')

        logger.debug2(spell_list)
        logger.debug("End Function")
        return spell_list        
        
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

        var = subprocess.check_output(['deborphan'])

        orphan_list = []
        for line in var.splitlines():
            line_list = str(line).split(',')
            item = line_list[0].split("'")[1]
            print(item)

        logger.debug(orphan_list)
        logger.debug('End Function')
        return orphan_list

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
        
        libmisc.column_print(print_list,cols=3,columnwise=False,gap=2)
        
        logger.debug("End Function")
        return
