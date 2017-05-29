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
#
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
#
# Libraries
#
#
#-------------------------------------------------------------------------------

# System Libraries
import logging
from logging import *
import copy

# Other Libraries

# Application Libraries
import pysorcery
from pysorcery.lib.util import text

#-------------------------------------------------------------------------------
#
# Global Variables
#
#-------------------------------------------------------------------------------
# Seethe Roadmap for version information
__version__ = '0.1.1'

#for level in ['DEBUG','INFOV','INFO']:
    
DEBUG2 = 9
DEBUG3 = 8
DEBUG4 = 7
DEBUG5 = 6
DEBUG6 = 5
DEBUG7 = 4
DEBUG8 = 3
DEBUG9 = 2
DEBUG10 = 1

INFO1 = 21
INFO2 = 22
INFO3 = 23
INFO4 = 24
INFO5 = 25
INFO6 = 26
INFO7 = 27
INFO8 = 28
INFO9 = 29

logging.addLevelName(9, "DEBUG2")
logging.addLevelName(8, "DEBUG3")
logging.addLevelName(7, "DEBUG4")
logging.addLevelName(6, "DEBUG5")
logging.addLevelName(5, "DEBUG6")
logging.addLevelName(4, "DEBUG7")
logging.addLevelName(3, "DEBUG8")
logging.addLevelName(2, "DEBUG9")
logging.addLevelName(1, "DEBUG10")

logging.addLevelName(21, "INFO1")
logging.addLevelName(22, "INFO2")
logging.addLevelName(23, "INFO3")
logging.addLevelName(24, "INFO4")
logging.addLevelName(25, "INFO5")
logging.addLevelName(26, "INFO6")
logging.addLevelName(27, "INFO7")
logging.addLevelName(28, "INFO8")
logging.addLevelName(29, "INFO9")

colortext = text.ConsoleText()
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
class LocalLogger(Logger):
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
    # info#
    #
    #-------------------------------------------------------------------------------
    def info1(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(21):
            self._log(21, message, args, **kws)

    #----------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info2(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(22):
            self._log(22, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info3(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(23):
            self._log(23, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info4(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(24):
            self._log(24, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info5(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(25):
            self._log(25, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info6(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(26):
            self._log(26, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info7(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(27):
            self._log(27, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info8(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(28):
            self._log(28, message, args, **kws) 

    #-------------------------------------------------------------------------------
    #
    # info#
    #
    #-------------------------------------------------------------------------------
    def info9(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(29):
            self._log(29, message, args, **kws)

#-------------------------------------------------------------------------------
#
# Class ColorizingStreamHandler
#
# 
#
#-------------------------------------------------------------------------------
class ConsoleLvlFormatter(Formatter):
    def __init__(self, fmt="%(levelno)s: %(message)s"):
        Formatter.__init__(self, fmt)
        self.dbg_fmt  = "%(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s"
        self.info_fmt = "%(message)s"
        self.warn_fmt  = "%(message)s"
        self.err_fmt  = "%(message)s"
        self.crit_fmt  = "%(message)s"
        return

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def format(self, record):        

        # Save the original format configured by the user
        # when the logger formatter was instantiated
        format_orig = self._style._fmt

        # Replace the original format with one customized by logging level
        if record.levelno <= DEBUG:
            self._style._fmt = self.dbg_fmt

        elif record.levelno >= INFO and record.levelno < WARNING:
            self._style._fmt = self.info_fmt

        elif record.levelno == WARNING:
            self._style._fmt = self.warn_fmt

        elif record.levelno == ERROR:
            self._style._fmt = self.err_fmt

        elif record.levelno == CRITICAL:
            self._style._fmt = self.crit_fmt


        # Call the original formatter class to do the grunt work
        result = Formatter.format(self, record)

        # Restore the original format configured by the user
        self._style._fmt = format_orig

        return result

#-------------------------------------------------------------------------------
#
# Class ColorizingStreamHandler
#
# 
#
#-------------------------------------------------------------------------------
class ColorizingStreamHandler(StreamHandler,text.ConsoleText):
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
                        DEBUG: "green",
                        INFO: "white",
                        INFO1: "white",
                        INFO2: "white",
                        INFO3: "white",
                        INFO4: "white",
                        INFO5: "white",
                        INFO6: "white",
                        INFO7: "white",
                        INFO8: "white",
                        INFO9: "white",
                        WARNING: "yellow",
                        ERROR: "red",
                        CRITICAL: "magenta"}
        super(ColorizingStreamHandler, self).__init__(*args, **kwargs)

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def emit(self, record):
        try:
            message = self.format(record)
            stream = self.stream
            if not self.is_tty:
                stream.write(message)
            else:
                message = colortext.colorize(message, "none", self._colors[record.levelno],"black")
                stream.write(message)
            stream.write(getattr(self, 'terminator', '\n'))
            self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except:
            self.handleError(record)

    #-------------------------------------------------------------------------------
    #
    # Function 
    #
    # Input:  ...
    # Output: ...
    # Return: ...
    #
    #-------------------------------------------------------------------------------
    def setLevelColor(self, logging_level, escaped_ansi_code):
        self._colors[logging_level] = escaped_ansi_code


local_manager = copy.copy(Logger.manager)
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
        return Logger.root


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
    debug10("Holy Mothermof Fuck")
    debug9("Holy Fuck")
    debug8("Fubar")
    debug7("snafu")
    debug6("fuck")
    debug5("holy shit")
    debug4("shit")
    debug3("damn")
    debug2("crap")
    debug("Debug Msg")
    info("Info Msg")
    warn("Warn Msg")
    error("Error Msg")
    critical("Crit Msg")
    return 0

