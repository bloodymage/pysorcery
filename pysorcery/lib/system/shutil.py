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
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
from shutil import *

# 3rd Party Libraries


# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries
from pysorcery.lib import util


#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
logger = logging.getLogger(__name__)

tar_formats = {
    'xz': 'xztar',
    'gzip': 'gztar',
    'bzip2': 'bztar',
    'tar': 'tar'
}

zip_formats = {
    'zip': 'zip'
    }

lzma_formats = {
    'lzma': 'lzma',
    'xz': 'lzma'
    }

gzip_formats = {
    'gzip': 'gzip'
    }

bzip2_formats = {
    'bzip2': 'bzip2'
    }

archive_formats = {
    'tar': tar_formats,
    'zip': zip_formats
    }

compressed_formats = {
    'lzma': lzma_formats,
    'gzip': gzip_formats,
    'bzip2': bzip2_formats
    }

_extensions = {
    'gzip': ['.gz'],
    'bzip2': ['.bz2'],
    'lzma': ['.xz']
    }

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function init_formats
#
#
#
# Input:
# Return:
#
# Exceptions:
#-----------------------------------------------------------------------
def init_formats(format_type):
    logger.debug('Begin Function')
    available_formats = util.get_cmd_types(format_type)

    logger.debug2('Available Formats: ' + str(available_formats))
    
    archive_cmd = ['extract','create']
    compress_cmd = ['decompress','compress']

    cmd = {
        'util_archive': archive_cmd,
        'util_compressed': compress_cmd
        }
    
    for x in cmd[format_type]:
        for i in available_formats:
            if (i == 'tar' or
                i == 'zip'):
                logger.debug2('Skipping Module: ' + str(i))
            else:
                logger.debug2('Adding Module: ' + str(i))
                logger.debug2('Format: ' + str(format_type))
                logger.debug2('Extension: ' + str(_extensions[i]))
                func = util.get_module_func(format_type,
                                            i,
                                            x)

                if x == cmd[format_type][1]:
                    logger.debug2('Adding Archive Format: ' + str(i))
                    logger.debug2('Command: ' + str(x))
                    logger.debug2('Format: ' + str(format_type))
                    logger.debug2('Extension: ' + str(_extensions[i]))
                    description = i + ' File'
                    register_archive_format(i,func, None, description)
                elif x == cmd[format_type][0]:

                    try:
                        description = i + ' File'
                        register_unpack_format(i,
                                               _extensions[i],
                                               func, None,
                                               description)
                        logger.debug2('Adding Unpack Format: ' + str(i))
                        logger.debug3('Command: ' + str(x))
                        logger.debug3('Format: ' + str(format_type))
                        logger.debug3('Extension: ' + str(_extensions[i]))
                    except:
                        logger.error('Error Adding Unpack Format: ' + str(i))
                        logger.error('Command: ' + str(x))
                        logger.error('Format: ' + str(format_type))
                        logger.error('Extension: ' + str(_extensions[i]))

                else:
                    logger.error('Error itializing module functions')

    logger.debug2(get_unpack_formats())
    logger.debug2(get_archive_formats())
    logger.debug('End Function')
    return
