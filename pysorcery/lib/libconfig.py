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
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os

# Other Libraries


# Application Libraries
# System Overrides
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery.lib import libtext

# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)
consolehandler = logging.ColorizingStreamHandler()

# Other Optional Libraries

#-------------------------------------------------------------------------------
#
# Classes
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class ConfigFiles
# 
#
#-------------------------------------------------------------------------------
class ConfigFiles():
    def config_dir():

        # Create List of Paths for Config Files
        path = []
        
        # check if config dir exists
        if os.environ['XDG_CONFIG_DIR']:
            path.append(os.environ['XDG_CONFIG_DIR'])

        if os.path.isdir('~/.config'):
            path.append('~/.config')

        return path

#-------------------------------------------------------------------------------
#
# configure
#
# Load configuration settings in the following order:
# 1. Hard Coded
# 2. {python-dir}/dist-___/pydionysius/dionysius_default.conf
# 3. ~/.config/dionysius/dionysis.conf
# 4. cli switches
#
# As each configuartion is loaded, it will overwrite any previosly set
# configuration option.
#
#-------------------------------------------------------------------------------
def main_configure(args):
    logger.debug("Begin Function")

    # Default Settings
    config = defConfiguration()

    # Congigure Loggings
    configure_logging(args, config)
    
    logger.debug("End Function")
#    logger.debug2("Return variable: Config:\n" + str(config))
    return config

#-------------------------------------------------------------------------------
#
# configure_logging
#
# Configure the logger.
#
#-------------------------------------------------------------------------------
def configure_logging(args,config):
    global logger

    logger.debug("Begin Function")
    
    # Ugly hack to make the changes global
    tempname = __name__.split(":")[0].split(".")[0]
#    print (tempname)
    logger = logging.getLogger(tempname)

    loglevels = {'debug':10,
                 'info': 20,
                 'warning': 30,
                 'error': 40,
                 'critical': 50 }

    if config['verbosity'] == 0:
        config['loglevel'] = loglevels[config['loglevel']]
    else:
        config['loglevel'] = 11 - min(10,config['verbosity'])
    
    
    if args.debug:
        config['loglevel'] = 1
    elif args.loglevel:
        # Bind loglevel to the upper case string value obtained
        # from the command line argument.  This allows the user to
        # specify --log=DEBUG or --log=debug            
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % args.loglevel)
        config['loglevel'] = numeric_level
    elif args.quiet > 0:
        config['loglevel'] = 20 + args.quiet
    elif args.verbosity > 0:
        config['loglevel'] = 11 - args.verbosity
#    else:
#        config['loglevel'] = INFO

    logger.setLevel(config['loglevel'])
    consolehandler.setLevel(config['loglevel'])
        
    # End ugly hack to change logging level globally
    logger = logging.getLogger(__name__)

    # If debugging enabled, log the arguments passed to the program
    logger.debug("Arguments Processed")
#    logger.debug2("Arguments: " + str(args))
    
    logger.debug("End Function")
    return 0

#-------------------------------------------------------------------------------
#
# defPluginList
#
# Gather the default plugins
#
#-------------------------------------------------------------------------------
def defConfiguration():
    config = { "loglevel": "info",
               "verbosity": 0
    }

    return config
