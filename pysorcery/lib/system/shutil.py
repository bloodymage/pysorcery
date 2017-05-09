#!/usr/bin/env python3
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
#-------------------------------------------------------------------------------

# System Libraries
from shutil import *

# Other Libraries


# Application Libraries
# System Library Overrides
# Other Application Libraries
from pysorcery.lib import util

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
file_format = {
    'xz': 'xztar',
    'gz': 'gztar',
    'bz': 'bztar',
    'tar': 'tar'
    }

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#
# Functions
#
#-------------------------------------------------------------------------------
def init_archive_formats():
    logger.debug('Begin Function')
    available_formats = util.get_archive_formats('archive')

    for i in available_formats:
        if (i != 'tar' or
            i != 'zip'):
            print('Add Module')
        else:
            print('Skipping Module')

    logger.debug('End Function')
    return
