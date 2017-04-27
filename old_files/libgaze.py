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
import os
import sys

# Other Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging
# Other Application Libraries
from pysorcery.lib import libcodex
from pysorcery.lib import libfiles
from pysorcery.lib import libgrimoire
from pysorcery.lib import libtext

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
# Function print_base_codex
# 
#
#-------------------------------------------------------------------------------
def print_base_codex():
    logger.debug('Begin Function')

    codex = libcodex.Codex()
    grimoire_list = codex.list_grimoires()

    grimoire_dict = {}
    for i in grimoire_list:
        grimoire = libgrimoire.Grimoire(grim_dir = i)
        section_list = grimoire.list_sections()
                    
        section_dict = {}
        for section in section_list:
            section_dict[section] = []
            
        spell_list_file = libfiles.Files(i + '/codex.index')
        spell_list = spell_list_file.read()

        for item in spell_list:
            spell, section = item.split(' ')
            section_dict[section.split('/')[-1]].append(spell)

        grimoire_dict[i] = section_dict

        for key in grimoire_dict:
            logger.info('-----------------------------')
            logger.info('Grimoire: ' + key.split('/')[-1])
            logger.info('-----------------------------')

            for sec_key in grimoire_dict[key]:
                logger.info('-----------------------------')
                logger.info('Section: ' + key.split('/')[-1] + ' / ' + sec_key)
                logger.info('-----------------------------')

                for item in grimoire_dict[key][sec_key]:
                    logger.info(item)

        logger.debug('End Function')
        return

#-------------------------------------------------------------------------------
#
# Function print_debian_codex
# 
#
#-------------------------------------------------------------------------------
def print_debian_codex(self):
    logger.debug('Begin Function')

    logger.debug('End Function')
    return

#-------------------------------------------------------------------------------
#
# Function print_codex
# 
#
#-------------------------------------------------------------------------------
def print_codex():
    if distro.distro_id in distro.distro_dict['deb']:
        print_debian_codex()
    else:
        print_base_codex()

    return
