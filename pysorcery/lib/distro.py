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
from distro import *

# Other Libraries


# Application Libraries
# System Library Overrides
# Other Application Libraries


#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Distro Definitions

deb_distro_list=['Ubuntu','linuxmint','debian','Kali']
smgl_distro_list=['Source Mage']
yum_distro_list=['Red Hat', 'Fedora']
pac_distro_list=['Arch']
ebuild_distro_list = [ 'Gentoo' ]
lunar_distro_list = [ 'Lunar' ]

distro_dict = { 'deb': deb_distro_list,
                'smgl': smgl_distro_list,
                'yum': yum_distro_list,
                'pac': pac_distro_list,
                'ebuild': ebuild_distro_list,
                'lunar': lunar_distro_list
                }
distro_id = linux_distribution()[0]
