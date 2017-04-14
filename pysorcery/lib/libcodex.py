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

# Other Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery.lib import libfiles
from pysorcery.lib import libtext

# Other Optional Libraries
if distro.distro_id in distro.distro_dict['deb']:
    import apt
    import aptsources
    import softwareproperties

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------

# Enable Logging
# create logger
logger = logging.getLogger(__name__)

if distro.distro_id in distro.distro_dict['deb']:
    import apt

#-------------------------------------------------------------------------------
#
# Classes
#
# Spell
# 
#
#-------------------------------------------------------------------------------
class BaseCodex():
    def __init__(self):
        self.description="Ooops!"

    def list_grimoires(self):
        logger.debug('Begin Function')

        grimoire_file = libfiles.Files('/etc/sorcery/local/grimoire')
        unedited_grimoire_list = grimoire_file.read()

        grimoire_list = []
        for grimoire in unedited_grimoire_list:
            grimoire_list.append(grimoire.split('=')[1])
        
        logger.debug('End Function')
        return grimoire_list


#-------------------------------------------------------------------------------
#
# Class DebianGrimoire
# 
#
#-------------------------------------------------------------------------------
class DebianCodex(BaseCodex):
    def __init__(self):
        BaseCodex.__init__(self)

    def list_grimoires(self):
        var = subprocess.check_output(['apt-cache', 'policy'])

        repo_list = []
        
        for line in var.splitlines():
            if 'l=' in str(line):                
                line_list=str(line).split(',')

                repo_main=''
                repo_sub=''
                for item in line_list:                    
                    if 'l=' in item:
                        repo_main = item.split('=')[1]
                    if 'c=' in item:
                        repo_sub = item.split('=')[1]

                    if len(repo_main) > 0 and len(repo_sub) > 0:
                        repo = repo_main + ' : ' + repo_sub
                        if repo not in repo_list:
                            repo_list.append(repo)

        return repo_list

    def update(self):
        logger.debug('Begin Function')

        
        subprocess.run(['apt-get', 'update'])

        logger.debug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class Codex
# 
#
#-------------------------------------------------------------------------------
class Codex(DebianCodex, BaseCodex):
    def __init__(self):
        logger.debug("Begin Function")
        if distro.distro_id in distro.distro_dict['deb']:
            DebianCodex.__init__(self)
        else:
            BaseCodex.__init__(self)

        logger.debug("End Function")
        return
        
    def list_grimoires(self):
        if distro.distro_id in distro.distro_dict['deb']:
            grimoire_list = DebianCodex.list_grimoires(self)
        else:
            grimoire_list = BaseCodex.list_grimoires(self)

        return grimoire_list

    def print_grimoires(self):
        grimoires = Codex.list_grimoires(self)
        for grimoire in grimoires:
            logger.info(grimoire.split('/')[-1])

        return

    def update(self):
        if distro.distro_id in distro.distro_dict['deb']:
            grimoire_list = DebianCodex.update(self)
        else:
            grimoire_list = BaseCodex.update(self)

        return grimoire_list

