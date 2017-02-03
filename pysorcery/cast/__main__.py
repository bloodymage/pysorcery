#!/usr/bin/env python3
## Original BASH version
## Original version Copyright 2001 by Kyle Sallee
## Additions/corrections Copyright 2002 by the Source Mage Team
##
## Python rewrite
## Copyright 2017 Geoff S Derber
##
##
## This software is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
##
## This software is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this software; if not, see <http://www.gnu.org/licenses/>.
##

#-------------------------------------------------------------------------------
#
# Libraries
#
#-------------------------------------------------------------------------------
# Standard Library
import sys
import argparse
import os

# Related 3rh Party Libraries

# Local application
import pysorcery
#from pysorcery import lib 
#from pysorcery.lib.libmisc import *
#from pysorcery.lib.libdefault import *
from pysorcery import __version__


#------
# Global Vardables
#------
command="cast"


def main():
    """
Main function, processes parameters.  Ensures root access as necessary"


"""
    function="main"

    parser = argparse.ArgumentParser(description='Process parameters')
    parser.add_argument('--cflags',help='Custom CFLAGS',nargs='*')
    parser.add_argument('--cxxflags',help='Custom CXXFLAGS',nargs='*')
    parser.add_argument('--cppflags', help='Custom CPPFLAGS',nargs='*')
    parser.add_argument('--ldflags',  help='Custom LDFLAGS',nargs='*')
    parser.add_argument('--no-opts', help='Turn off setting optimization flags, except for those found in --cflags, --cxxflags, --cppflags and --ldflags.',action='store_true')
    parser.add_argument('-V',help='Override \$VOYEUR setting',nargs='?',choices=['yes','no'])
    parser.add_argument('-d','--download',help='Force download of sources (overwrite existing files).',action='store_true')
    parser.add_argument('-s',help='Download all given spells before compiling',action='store_true')
    parser.add_argument('--deps',help='Configure spells and determine dependencies, only cast dependencies, not spells themselves',action='store_true')
    parser.add_argument('-c','--compile',help="Recompile the spells (don't install from cache).",action='store_true')
    parser.add_argument('-r','--reconfigure',help='Select new dependencies for spells (implies -c)')
    parser.add_argument('-g','--grimoire',nargs='*',help='Use only the specified grimoires for this cast.  NOTE: If there are any cross-grimoire dependencies on unspecified grimoires they will not work. The target spell will not be found. To avoid this, specify all relevant grimoires to the -g parameter in the order you wish them to be searched.')
    parser.add_argument('-R','--recast-down',help='Recursively recast depended-upon spells, even if they are already installed. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.',action='store_true')
    parser.add_argument('-B','--recast-up',help='Recursively recast dependent spells. You probably also want to pass the -c flag to make sure they are recompiled, not resurrected.',action='store_true')
    parser.add_argument('-O','--recast-optional',help='If a spell being built has spells which could optionally depend on it, but those dependencies are disabled, ask to recast the dependee. Optional parameter can be one of: "always", "ask-yes", "ask-no", or "ignore"; it defaults to what is set via the sorcery menu. Implies -c.',nargs='?',choices=['always','ask-yes','ask-no','ignore'])
    parser.add_argument('-Z','--lazy-updates',help='Perform updates on installed spells that need updates. Optional parameter same as above.',nargs='?',choices=['always','ask-yes','ask-no','ignore'])
    parser.add_argument('-b','--force-base-dep',help='Force all spells to depend on basesystem',action='store_true')
    parser.add_argument('--from',help='Specify an alternate directory for $SOURCE_CACHE')
    parser.add_argument('--queue',help='Cast all spells listed in $INSTALL_QUEUE',action='store_true')
    parser.add_argument("-v", "--version", help="Print version information and exit", action='version', version='%(prog)s ' + __version__)
    parser.add_argument('--debug',type=int,help='Specify debugging level',nargs='?')
    parser.add_argument("spells", nargs='+', help='Spells to cast, separated by spaces')
   
    args = parser.parse_args()    

    if args.debug is None:
        debug_level=7
    elif args.debug is not None:
        debug_level=args.debug
    else:
        debug_level=6    
        
    debug (command, function,"Begin Function",0,debug_level)

    #    if not os.geteuid() == 0:
    #        sys.exit("\nOnly Root can run this script\n")

    print(args.spells)
        
    return 0

if __name__ == '__main__':
    main()
