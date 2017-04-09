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
import os


# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery

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


#-------------------------------------------------------------------------------
#
# Classes
#
# Spell
# 
#
#-------------------------------------------------------------------------------
class BaseGrimoire():
    def __init__(self,args):
        self.name = args.grimoire
        self.description="Ooops!"
        self.url = "www.sm.org"

    def add(self):
        logger.debug('Begin Function')


        logger.debug('End Function')
        return


#-------------------------------------------------------------------------------
#
# Class DebianGrimoire
# 
#
#-------------------------------------------------------------------------------
class DebianGrimoire(BaseGrimoire):
    def __init__(self,args):
        logger.debug('Begin Function')
        BaseGrimoire.__init__(self,args)

        if self.name[0].startswith('ppa://'):
            self.url = self.name

            # force new ppa file to be 644 (LP: #399709)
            #os.umask(0o022)

            # get the line
            #line = args[0]
            #print(line)
            
            # add it
            #sp = SoftwareProperties(options=options)
            #distro = aptsources.distro.get_distro()
            #distro.get_sources(sp.sourceslist)

        logger.debug('End Function')
        return

    def list_spells(self):
        print("Spells")
        return
    
    def add(self):
        logger.debug('Begin Function')

        print(self.url)

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Class DebianGrimoire
# 
#
#-------------------------------------------------------------------------------
class Grimoire(DebianGrimoire,BaseGrimoire):
    def __init__(self,args):
        if distro.distro_id in distro.distro_dict['deb']:
            DebianGrimoire.__init__(self,args)
        else:
            BaseGrimoire.__init__(self,args)

    def list_spells(self):
        print("Spells")
        return

    def add(self):
        if distro.distro_id in distro.distro_dict['deb']:
            DebianGrimoire.add(self)
        elif distro.distro_id in distro.distro_dict['smgl']:
            BaseGrimoire.add(self)
        else:
            # Add except?
            logger.critical("We shouldn't be here")

