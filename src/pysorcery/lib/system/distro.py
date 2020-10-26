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
# Distro:
#
#    Provides additional functionality to the Distro library from
#    Python.
#
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------

# System Libraries
from distro import *

# 3rd Party Libraries


# Application Libraries
# System Library Overrides

# Other Application Libraries


#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------

# Distro Definitions
distro_definitions = {
    ('Ubuntu',
     'Linux Mint',
     'Debian',
     'Kali GNU/Linux',
     'Debian GNU/Linux',
     'Rasbian GNU/Linux
    ): 'apt',
    ('Source Mage',
     'SMGL'
    ): 'smgl',
    ('Red Hat',
     'Fedora'
    ): 'yum',
    ('Arch',
     'Black Arch'
    ): 'pacman',
    ('Gentoo',
     'Funtoo'
    ): 'ebuild',
    ('Lunar'): 'module'
    }

distro_group = {}
for k, v in distro_definitions.items():
    for key in k:
        distro_group[key] = v

distro_id = linux_distribution()[0]
