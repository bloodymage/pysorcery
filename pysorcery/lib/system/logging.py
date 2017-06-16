#!/usr/bin/env python3
#-----------------------------------------------------------------------
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
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#
#-----------------------------------------------------------------------

# System Libraries
import logging
from logging import *
import copy

# 3rd Party Libraries

# Application Libraries
from pysorcery import __version__
from pysorcery.lib.util import text

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------

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

VINFO1 = 19
VINFO2 = 18
VINFO3 = 17
VINFO4 = 16
VINFO5 = 15
VINFO6 = 14
VINFO7 = 13
VINFO8 = 12
VINFO9 = 11

logging.addLevelName(9, "DEBUG2")
logging.addLevelName(8, "DEBUG3")
logging.addLevelName(7, "DEBUG4")
logging.addLevelName(6, "DEBUG5")
logging.addLevelName(5, "DEBUG6")
logging.addLevelName(4, "DEBUG7")
logging.addLevelName(3, "DEBUG8")
logging.addLevelName(2, "DEBUG9")
logging.addLevelName(1, "DEBUG10")

logging.addLevelName(19, "VINFO1")
logging.addLevelName(18, "VINFO2")
logging.addLevelName(17, "VINFO3")
logging.addLevelName(16, "VINFO4")
logging.addLevelName(15, "VINFO5")
logging.addLevelName(14, "VINFO6")
logging.addLevelName(13, "VINFO7")
logging.addLevelName(12, "VINFO8")
logging.addLevelName(11, "VINFO9")

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
#-----------------------------------------------------------------------
#
# Classes
#
# LocalLogger
# ConsoleLvlFormatter
# ColorizingStreamHandler
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class LocalLogger
#
# Calls the read function based on the file format.
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class LocalLogger(Logger):
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug2(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(9):
            self._log(9, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug3(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(8):
            self._log(8, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug4(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(7):
            self._log(7, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug5(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(6):
            self._log(6, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug6(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(5):
            self._log(5, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug7(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(4):
            self._log(4, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug8(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(3):
            self._log(3, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug9(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(2):
            self._log(2, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def debug10(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(1):
            self._log(1, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo1(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(19):
            self._log(19, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo2(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(18):
            self._log(18, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo3(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(17):
            self._log(17, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo4(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(16):
            self._log(16, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo5(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(15):
            self._log(15, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo6(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(14):
            self._log(14, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo7(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(13):
            self._log(13, message, args, **kws)

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo8(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(12):
            self._log(12, message, args, **kws) 

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def vinfo9(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(11):
            self._log(11, message, args, **kws)

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info1(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(21):
            self._log(21, message, args, **kws)

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info2(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(22):
            self._log(22, message, args, **kws) 

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info3(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(23):
            self._log(23, message, args, **kws) 

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info4(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(24):
            self._log(24, message, args, **kws) 

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info5(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(25):
            self._log(25, message, args, **kws) 

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info6(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(26):
            self._log(26, message, args, **kws) 

        return
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info7(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(27):
            self._log(27, message, args, **kws) 

        return
    
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info8(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(28):
            self._log(28, message, args, **kws) 

        return
    
    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def info9(self, message, *args, **kws):
        # Yes, logger takes its '*args' as 'args'.
        if self.isEnabledFor(29):
            self._log(29, message, args, **kws)

        return

#-----------------------------------------------------------------------
#
# Class ConsoleLvlFormatter
#
# Adds further functionality for the console to change the
# format based on the logging lewel
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
class ConsoleLvlFormatter(Formatter):
    def __init__(self, fmt="%(levelno)s: %(message)s"):
        Formatter.__init__(self, fmt)
        self.dbg_fmt  = "%(name)s:%(funcName)s:%(lineno)d - %(levelname)s - %(message)s"
        self.info_fmt = "%(message)s"
        self.warn_fmt  = "%(message)s"
        self.err_fmt  = "%(message)s"
        self.crit_fmt  = "%(message)s"
        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
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

#-----------------------------------------------------------------------
#
# Class ColorizingStreamHandler
#
# Calls the read function based on the file format.
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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
                        VINFO1: "white",
                        VINFO2: "white",
                        VINFO3: "white",
                        VINFO4: "white",
                        VINFO5: "white",
                        VINFO6: "white",
                        VINFO7: "white",
                        VINFO8: "white",
                        VINFO9: "white",
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
        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    @property
    def is_tty(self):
        isatty = getattr(self.stream, 'isatty', None)
        return isatty and isatty()

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
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

        return

    #-------------------------------------------------------------------
    #
    # Function read
    #
    # Calls the read function based on the file format.
    #
    # Inputs
    # ------
    #    ...
    #
    # Returns
    # -------
    #    none
    #
    # Raises
    # ------
    #    ...
    #
    #-------------------------------------------------------------------
    def setLevelColor(self, logging_level, escaped_ansi_code):
        self._colors[logging_level] = escaped_ansi_code
        return


local_manager = copy.copy(Logger.manager)
local_manager.loggerClass = LocalLogger


#-----------------------------------------------------------------------
#
# Functions
#
# getLogger
# verifydebuglevels
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function getLogger
#
# Calls the read function based on the file format.
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def getLogger(name=None):  # noqa
    if name:
        return local_manager.getLogger(name)
    else:
        return Logger.root

#-----------------------------------------------------------------------
#
# func verifydebuglevels
#
# Remove before final
#
# This is for testing to ensure all debug levels display as expected.
#
# Inputs
# ------
#    ...
#
# Returns
# -------
#    none
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
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
    return

