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
#
#-------------------------------------------------------------------------------

# System Libraries
import sys

# Other Libraries

# Application Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Seethe Roadmap for version information

#-------------------------------------------------------------------------------
#
# Class ConsoleText
#
# 
#
#-------------------------------------------------------------------------------
class ConsoleText():
    def __init__(self):
        self.escape = "\x1b["

        self.attributes = {
            "none": 0,
            "bold":1,
            "unk_a":2,
            "unk_b":3,
            "underline":4,
            "blink":5,
            "unk_c":6,
            "reverse": 7
        }

        self.fgcolors = {
            "black" : 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "fuchsia": 35,
            "magenta": 35,
            "turquoise": 36,
            "cyan": 36,
            "white": 37
        }

        self.bgcolors = {
            "black" : 40,
            "red": 41,
            "green": 42,
            "yellow": 43,
            "blue": 44,
            "fuchsia": 45,
            "magenta": 45,
            "turquoise": 46,
            "cyan": 46,
            "white": 47    
        }

    #-------------------------------------------------------------------------------
    #
    # function ConsoleText.colorize
    #
    # 
    #
    #-------------------------------------------------------------------------------
    def colorize(self,text,attribute="none",fgcolor="white",bgcolor="black"):

        escape = "\x1b["

        attributes = {
            "none": 0,
            "bold":1,
            "unk_a":2,
            "unk_b":3,
            "underline":4,
            "blink":5,
            "unk_c":6,
            "reverse": 7
        }

        fgcolors = {
            "black" : 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "fuchsia": 35,
            "magenta": 35,
            "turquoise": 36,
            "cyan": 36,
            "white": 37
        }

        bgcolors = {
            "black" : 40,
            "red": 41,
            "green": 42,
            "yellow": 43,
            "blue": 44,
            "fuchsia": 45,
            "magenta": 45,
            "turquoise": 46,
            "cyan": 46,
            "white": 47    
        }

        if attribute in attributes:
            begincolor=escape + str(attributes[attribute])
        else:
            begincolor=escape + str(attributes['none'])

        if fgcolor in fgcolors:
            begincolor=begincolor + ";" + str(fgcolors[fgcolor])
        else:
            begincolor=begincolor + ";" + str(fgcolors['white'])
    
        if bgcolor in bgcolors:
            begincolor=begincolor + ";" + str(bgcolors[bgcolor]) + "m"
        else:
            begincolor=begincolor + ";" + str(bgcolors['black']) + "m"

        resetcolor=escape + str(attributes['none']) + ";" + str(fgcolors['white']) + ";" + str(bgcolors['black']) + "m"

        textstring = begincolor + text + resetcolor
    
        return textstring
