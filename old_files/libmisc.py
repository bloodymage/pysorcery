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
#    along with Sorceory.  If not, see <http://www.gnu.org/licenses/>.
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
import sys
import os
import math

# Other Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib import distro
from pysorcery.lib import logging

# Other Application Libraries


# Other Optional Libraries


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
#-------------------------------------------------------------------------------
            
#-------------------------------------------------------------------------------
#
# Functions
#
#
#
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
#
# Function column_print
#
# Prints input list in columns
#
# Input:
#   list_to_print = List to Print
#   cols          = The number of columns to use
#   columnwise    = To print by row or column
#   gap           = The gap between columns
# Output:
# Return: None
#
#-------------------------------------------------------------------------------
def column_print(obj, cols=4, columnwise=True, gap=4):
    """
    Print the given list in evenly-spaced columns.

    Parameters
    ----------
    obj : list
        The list to be printed.
    cols : int
        The number of columns in which the list should be printed.
    columnwise : bool, default=True
        If True, the items in the list will be printed column-wise.
        If False the items in the list will be printed row-wise.
    gap : int
        The number of spaces that should separate the longest column
        item/s from the next column. This is the effective spacing
        between columns based on the maximum len() of the list items.
    """

    term_height, term_width = os.popen('stty size', 'r').read().split()

    column_width = int(term_width)
    
    sobj = [str(item) for item in obj]
    if cols > len(sobj):
        cols = len(sobj)

    
    imax = max([len(item) for item in sobj])
    cmax = column_width // cols

    max_len = min(imax,cmax - gap)
    
    if columnwise:
        cols = int(math.ceil(float(len(sobj)) / float(cols)))
        
    plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
    
    if columnwise:
        if not len(plist[-1]) == cols:
            plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
        plist = zip(*plist)
    printer = '\n'.join([
        ''.join([c[0:max_len].ljust(max_len + gap) for c in p])
        for p in plist])
    logger.info1(printer)

#    term_height, term_width = os.popen('stty size', 'r').read().split()
#    total_columns = int(term_width) // column_width
#    total_rows = len(list_to_print) // total_columns
#    # ceil
#    total_rows = total_rows + 1 if len(list_to_print) % total_columns != 0 else total_rows

 #   format_string = "".join(["{%d:<%ds}" % (c, column_width) \
#            for c in range(total_columns)])
#    for row in range(total_rows):
#        column_items = []
#        for column in range(total_columns):
#            # top-down order
 #           list_index = row + column*total_rows
#            # left-right order
#            #list_index = row*total_columns + column
#            if list_index < len(list_to_print):
#                column_items.append(list_to_print[list_index])
#            else:
#                column_items.append("")
 #       print(format_string.format(*column_items))