#! /usr/bin/env python3
#-------------------------------------------------------------------------------
#
# Copyright 2017 Geoff S Derber
#
# This file is part of Dionysius.
#
#    Dionysius is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Dionysius is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Dionysius.  If not, see <http://www.gnu.org/licenses/>.
#
#
#
#
# This file is a flat file prototype.  There are several things I flat out do not
# know how to do.  This allows me to try out the parts I do know.
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
import argparse
import logging
import copy

# Other Libraries

# Application Libraries

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Seethe Roadmap for version information
__version__ = '0.1.1'

DEBUG2 = 9
DEBUG3 = 8
DEBUG4 = 7
DEBUG5 = 6
DEBUG6 = 5
DEBUG7 = 4
DEBUG8 = 3
DEBUG9 = 2
DEBUG10 = 1

logging.addLevelName(9, "DEBUG2")
logging.addLevelName(8, "DEBUG3")
logging.addLevelName(7, "DEBUG4")
logging.addLevelName(6, "DEBUG5")
logging.addLevelName(5, "DEBUG6")
logging.addLevelName(4, "DEBUG7")
logging.addLevelName(3, "DEBUG8")
logging.addLevelName(2, "DEBUG9")
logging.addLevelName(1, "DEBUG10")

#-------------------------------------------------------------------------------
#
# Classes part 1
#
# 
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Class LocalLogger
#
# 
#
#-------------------------------------------------------------------------------
class LocalLogger(logging.Logger):
    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug2(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(9):
            self._log(9, message, args, **kws)

    #----------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug3(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(8):
            self._log(8, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug4(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(7):
            self._log(7, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug5(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(6):
            self._log(6, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug6(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(5):
            self._log(5, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug7(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(4):
            self._log(4, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug8(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(3):
            self._log(3, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug9(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(2):
            self._log(2, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # debug#
    #
    #-------------------------------------------------------------------------------
    def debug10(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(1):
            self._log(1, message, args, **kws)

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

#        logger.debug("Text: " + str(text) + "\nAttribute: " + str(attribute) + "\nFgColor: " + str(fgcolor) + "\nBgColor: " + str(bgcolor))
        if attribute in attributes:
            begincolor=escape + str(attributes[attribute])
        else:
#            logger.debug("Attribute: " + attribute + " is not a valid attribute")
            begincolor=escape + str(attributes['none'])

        if fgcolor in fgcolors:
            begincolor=begincolor + ";" + str(fgcolors[fgcolor])
        else:
#            logger.debug("Foreground Color: " + fgcolor + " is not a valid color")
            begincolor=begincolor + ";" + str(fgcolors['white'])
    
        if bgcolor in bgcolors:
            begincolor=begincolor + ";" + str(bgcolors[bgcolor]) + "m"
        else:
            print("bgcolor")
#            logger.debug("Background Color: " + fgcolor + " is not a valid color")
            begincolor=begincolor + ";" + str(bgcolors['black']) + "m"

        resetcolor=escape + str(attributes['none']) + ";" + str(fgcolors['white']) + ";" + str(bgcolors['black']) + "m"

        textstring = begincolor + text + resetcolor
#        logger.debug("Textstring: " + textstring)
    
        return textstring

#-------------------------------------------------------------------------------
#
# Class ColorizingStreamHandler
#
# 
#
#-------------------------------------------------------------------------------
class ColorizingStreamHandler(logging.StreamHandler,ConsoleText):
    def __init__(self, *args, **kwargs):
        self._colors = {DEBUG10: "green",
                        DEBUG9: "green",
                        DEBUG8: "green",
                        DEBUG7: "green",
                        DEBUG6: "green",
                        DEBUG5: "green",
                        DEBUG4: "green",
                        DEBUG3: "green",
                        DEBUG2: "green",
                        logging.DEBUG: "green",
                        logging.INFO: "cyan",
                        logging.WARNING: "yellow",
                        logging.ERROR: "red",
                        logging.CRITICAL: "magenta"}
        super(ColorizingStreamHandler, self).__init__(*args, **kwargs)

    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream
            if not self.is_tty:
                stream.write(message)
            else:
                colortext = ConsoleText()
                message = colortext.colorize(message, "none", self._colors[record.levelno],"black")
                stream.write(message)
            stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    def setLevelColor(self, logging_level, escaped_ansi_code):
        self._colors[logging_level] = escaped_ansi_code


local_manager = copy.copy(logging.Logger.manager)
local_manager.loggerClass = LocalLogger

#-------------------------------------------------------------------------------
#
# func getLogger
#
# Local implementation of 'logging.getLogger'
# This ensures we have the added logging names, debug2..debug10
#
#-------------------------------------------------------------------------------
def getLogger(name=None):  # noqa
    if name:
        return local_manager.getLogger(name)
    else:
        return logging.Logger.root


# Enable Logging
# create logger
logger = getLogger(__name__)
logger.setLevel(DEBUG10)

# Define Handlers
consolehandler = ColorizingStreamHandler()

# Define Formatters
consoleformatter = logging.Formatter('%(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s')

# Set handler ...
consolehandler.setLevel(DEBUG10)
consolehandler.setFormatter(consoleformatter)

# Add handlers to logger
logger.addHandler(consolehandler)

#-------------------------------------------------------------------------------
#
# Classes
#
# 
# 
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Classes ConfigFiles
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
# Functions
#
#
#
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# func verifydebuglevels
#
# Remove before final
#
# This is for testing to ensure all debug levels display as expected.
#
#-------------------------------------------------------------------------------
def verifydebuglevels():
    logger.debug10("Holy Mothermof Fuck")
    logger.debug9("Holy Fuck")
    logger.debug8("Fubar")
    logger.debug7("snafu")
    logger.debug6("fuck")
    logger.debug5("holy shit")
    logger.debug4("shit")
    logger.debug3("damn")
    logger.debug2("crap")
    logger.debug("Debug Msg")
    logger.info("Info Msg")
    logger.warn("Warn Msg")
    logger.error("Error Msg")
    logger.critical("Crit Msg")
    return 0


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
    logger = getLogger('pydionysius')

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
                raise ValueError('Invalid log level: %s' % loglevel)
            config['loglevel'] = numeric_level
    elif args.verbosity > 0:
        config['loglevel'] = 11 - args.verbosity
#    else:
#        config['loglevel'] = INFO

    logger.setLevel(config['loglevel'])
    consolehandler.setLevel(config['loglevel'])
        
    # End ugly hack to change logging level globally
    logger = getLogger(__name__)

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
def defPluginList():
    defPluginPath = plugins.__path__
    filelist = fileops.listFiles(defPluginPath,0)

    if '__init__.py' in filelist:
        filelist.remove('__init__.py')

    for item in filelist:
        filelist[filelist.index(item)] = item.replace(".py","")
        
    return filelist

#-------------------------------------------------------------------------------
#
# defPluginList
#
# Gather the default plugins
#
#-------------------------------------------------------------------------------
def defConfiguration():
    config = { "loglevel": "debug",
               "verbosity": 10
    }

    return config

#-------------------------------------------------------------------------------
#
# Real_Main
#
# 
#
#-------------------------------------------------------------------------------
def real_main(args):    
    logger.debug("Entered Function")

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description="Dionysius creates, and compresses media files from CDs/DVDs/Blu-Rays")
    parser.add_argument("--config",
                        nargs=1,
                    help="Use specified config file")
    parser.add_argument("-v", "--verbosity",
                        action="count",
                        default=0,
                    help="increase output verbosity")
    parser.add_argument("--loglevel",
                        help="Set minimum logging level",
                        choices=["debug","info","warning","error","critical","DEBUG","INFO","WARNING","ERROR","CRITICAL"])
    parser.add_argument("-V", "--version",
                        help="Print version information and exit",
                        action="version",
                        version="%(prog)s " + __version__)
    parser.add_argument("--debug",
                        help="Enable Debugging",
                        action="store_true")

    args = parser.parse_args()

    config = main_configure(args)
    logger.debug("Configuration set")
#    logger.debug2("Configuration Settings: " + str(config))
    
    # "application" code
    colortext = ConsoleText()
    print(colortext.colorize("Let's Have fun!","none","blue","yellow"))
    
    verifydebuglevels()
    logger.debug("End Function")
    return 0


#-------------------------------------------------------------------------------
#
# Main
#
# The First function, initalizes everything else.
#
# Inputs come from command line argument
#
# This is ugly code
#
#
# Reads configuration files in the following order:
# 1. ~/.config/dionysius/dionysis.conf
# 2. /etc/dionysius/dionysius.conf
# 3. {python-dir}/dist-___/pydionysius/dionysius.conf
#
# Conf files are in yaml format
#
# Note: Any cli switches will override the settings in the config files
#
#-------------------------------------------------------------------------------
def main(args=None):
        """Run the main command-line interface for dionysius. Includes top-level
    exception handlers that print friendly error messages.
        """

        logger.debug("Begin Application")
#        try:         
#            real_main(args)
        real_main(args)        
#        except:
#            logger.critical("You Fucked Up")

        logger.debug("End Application")
        return 0


main()
