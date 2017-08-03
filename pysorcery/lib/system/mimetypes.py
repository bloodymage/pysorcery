#! /usr/bin/env python3
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
# Mimetypes:
#
#    Provides additional functionality to the Mimetypes library from
#    Python.
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
from mimetypes import *

# 3rd Party Libraries

# Application Libraries
# System Library Overrides
from pysorcery.lib.system import logging
# Other Application Libraries

# Other Optional Libraries

#-----------------------------------------------------------------------
#
# Global Variables
#
#-----------------------------------------------------------------------
# Enable Logging
# create logger
logger = logging.getLogger(__name__)

# Map MIME types to file format

filetypedefinitions = {
    ( 'application/gzip',
      'application/java-archive',
      'application/rar',
      'application/vnd.ms-cab-compressed',
      'application/x-7z-compressed',
      'application/x-ace',
      'application/x-adf',
      'application/x-alzip',
      'application/x-archive',
      'application/x-arc',
      'application/x-arj',
      'application/x-bzip2',
      'application/x-cab',
      'application/x-chm',
      'application/x-compress',
      'application/x-cpio',
      'application/x-dms',
      'application/x-gzip',
      'application/x-iso9660-image',
      'application/x-lzop',
      'application/x-lzma',
      'application/x-lzip',
      'application/x-lha',
      'application/x-lrzip',
      'application/x-lzh',
      'application/x-rar',
      'application/x-rzip',
      'application/x-shar',
      'application/x-tar',
      'application/x-vhd',
      'application/x-xz',
      'application/x-zip-compressed',
      'application/x-zoo',
      'application/zip',
      'application/zpaq'
    ): 'archive',
    ( 'application/gzip',    
      'application/x-7z-compressed',
      'application/x-bzip2',
      'application/x-compress',
      'application/x-gzip',    
      'application/x-lzma',
      'application/x-xz',
      'gzip',
      'bzip2',
      'xz'
      ): 'compressed',
    ( 'audio/x-ape',
      'audio/x-shn',
      'audio/flac'
      ): 'audio',
    ( 'application/x-debian-package',
      'application/x-redhat-package-manager',
      'application/x-rpm'
    ): 'package',
    ( 'None' ): 'default'
    }

fileclasstypes = {}
for k, v in filetypedefinitions.items():
    for key in k:
        fileclasstypes[key] = v

# Map MIME types to archive format
ArchiveMimetypes = {
    'application/java-archive': 'zip',
    'application/rar': 'rar',
    'application/vnd.ms-cab-compressed': 'cab',
    'application/x-7z-compressed': '7z',
    'application/x-ace': 'ace',
    'application/x-adf': 'adf',
    'application/x-alzip': 'alzip',
    'application/x-archive': 'ar',
    'application/x-arc': 'arc',
    'application/x-arj': 'arj',
    'application/x-cab': 'cab',
    'application/x-chm': 'chm',
    'application/x-compress': 'compress',
    'application/x-cpio': 'cpio',
    'application/x-dms': 'dms',
    'application/x-iso9660-image': 'iso',
    'application/x-lzop': 'lzop',
    'application/x-lzma': 'lzma',
    'application/x-lzip': 'lzip',
    'application/x-lha': 'lzh',
    'application/x-lrzip': 'lrzip',
    'application/x-lzh': 'lzh',
    'application/x-rar': 'rar',
    'application/x-rzip': 'rzip',
    'application/x-shar': 'shar',
    'application/x-tar': 'tar',
    'application/x-vhd': 'vhd',
    'application/x-zip-compressed': 'zip',
    'application/x-zoo': 'zoo',
    'application/zip': 'zip',
    'application/zpaq': 'zpaq'
}

AudioMimetypes = {
    'audio/x-ape': 'ape',
    'audio/x-shn': 'shn',
    'audio/flac': 'flac'
}

CompressionMimetypes = {
    'application/gzip': 'gzip',    
    'application/x-7z-compressed': '7z',
    'application/x-bzip2': 'bzip2',
    'application/x-compress': 'compress',
    'application/x-gzip': 'gzip',    
    'application/x-lzma': 'lzma',
    'application/x-xz': 'xz',
    'gzip': 'gzip',
    'bzip2': 'bzip2',
    'xz': 'lzma'
}

PackageMimetypes = {
   'application/x-debian-package': 'deb',
    'application/x-redhat-package-manager': 'rpm',
    'application/x-rpm': 'rpm'
}

# Supported archive formats
ArchiveFormats = (
    '7z', 'ace', 'adf', 'alzip', 'ar', 'arc', 'arj',
    'cab', 'chm', 'compress', 'cpio', 'dms',
    'iso', 'lrzip', 'lzh', 'lzip', 'lzma',
    'rar', 'rzip', 'shar', 'tar', 'vhd',
    'zip', 'zoo', 'zpaq')

AudioFormats = ( 'ape', 'flac', 'shn' )

CompressionFormats = ( 'bzip2', 'gzip', 'lzop', 'xz' )

PackageFormats = ( 'rpm', 'deb' )

# Supported compressions (used with tar for example)
# Note that all compressions must also be archive formats
ArchiveCompressions = ('bzip2', 'compress', 'gzip', 'lzip', 'lzma', 'xz')

# internal MIME database
mimedb = None

#-----------------------------------------------------------------------
#
# Classes
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Functions
#
# init_mimedb
# add_mimedb_data
# add_mimetypes
# check_types
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Function init_mimedb
#
# Initialize the internal MIME database.
#
# Inputs
# ------
#    @param: None
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def init_mimedb():
    """Initialize the internal MIME database."""
    global mimedb
    try:
        mimedb = mimetypes.MimeTypes(strict=False)
    except Exception as msg:
        log_error("could not initialize MIME database: %s" % msg)
        return
    add_mimedb_data(mimedb)
    return

#-----------------------------------------------------------------------
#
# Function add_mimedb_data
#
# Initialize the internal MIME database.
#
# Inputs
# ------
#    @param: mimedb
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def add_mimedb_data(mimedb):
    """Add missing encodings and mimetypes to MIME database."""
    mimedb.encodings_map['.bz2'] = 'bzip2'
    mimedb.encodings_map['.lzma'] = 'lzma'
    mimedb.encodings_map['.xz'] = 'xz'
    mimedb.encodings_map['.lz'] = 'lzip'
    mimedb.suffix_map['.tbz2'] = '.tar.bz2'
    add_mimetype(mimedb, 'application/x-lzop', '.lzo')
    add_mimetype(mimedb, 'application/x-adf', '.adf')
    add_mimetype(mimedb, 'application/x-arj', '.arj')
    add_mimetype(mimedb, 'application/x-lzma', '.lzma')
    add_mimetype(mimedb, 'application/x-xz', '.xz')
    add_mimetype(mimedb, 'application/java-archive', '.jar')
    add_mimetype(mimedb, 'application/x-rar', '.rar')
    add_mimetype(mimedb, 'application/x-rar', '.cbr')
    add_mimetype(mimedb, 'application/x-7z-compressed', '.7z')
    add_mimetype(mimedb, 'application/x-7z-compressed', '.cb7')
    add_mimetype(mimedb, 'application/x-cab', '.cab')
    add_mimetype(mimedb, 'application/x-rpm', '.rpm')
    add_mimetype(mimedb, 'application/x-debian-package', '.deb')
    add_mimetype(mimedb, 'application/x-ace', '.ace')
    add_mimetype(mimedb, 'application/x-ace', '.cba')
    add_mimetype(mimedb, 'application/x-archive', '.a')
    add_mimetype(mimedb, 'application/x-alzip', '.alz')
    add_mimetype(mimedb, 'application/x-arc', '.arc')
    add_mimetype(mimedb, 'application/x-lrzip', '.lrz')
    add_mimetype(mimedb, 'application/x-lha', '.lha')
    add_mimetype(mimedb, 'application/x-lzh', '.lzh')
    add_mimetype(mimedb, 'application/x-rzip', '.rz')
    add_mimetype(mimedb, 'application/x-zoo', '.zoo')
    add_mimetype(mimedb, 'application/x-dms', '.dms')
    add_mimetype(mimedb, 'application/x-zip-compressed', '.crx')
    add_mimetype(mimedb, 'application/x-shar', '.shar')
    add_mimetype(mimedb, 'application/x-tar', '.cbt')
    add_mimetype(mimedb, 'application/x-vhd', '.vhd')
    add_mimetype(mimedb, 'audio/x-ape', '.ape')
    add_mimetype(mimedb, 'audio/x-shn', '.shn')
    add_mimetype(mimedb, 'audio/flac', '.flac')
    add_mimetype(mimedb, 'application/x-chm', '.chm')
    add_mimetype(mimedb, 'application/x-iso9660-image', '.iso')
    add_mimetype(mimedb, 'application/zip', '.cbz')
    add_mimetype(mimedb, 'application/zip', '.epub')
    add_mimetype(mimedb, 'application/zip', '.apk')
    add_mimetype(mimedb, 'application/zpaq', '.zpaq')
    return

#-----------------------------------------------------------------------
#
# Function add_mimetype
#
# Initialize the internal MIME database.
#
# Inputs
# ------
#    @param: mimedb
#    @param: mimetype
#    @param: extention
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def add_mimetype(mimedb, mimetype, extension):
    """Add or replace a mimetype to be used with the given extension."""
    # If extension is already a common type, strict=True must be used.
    strict = extension in mimedb.types_map[True]
    mimedb.add_type(mimetype, extension, strict=strict)
    return

#-----------------------------------------------------------------------
#
# Function check_type
#
# Initialize the internal MIME database.
#
# Inputs
# ------
#    @param: format_
#    @param: encoding
#
# Returns
# -------
#    @return: None
#
# Raises
# ------
#    ...
#
#-----------------------------------------------------------------------
def check_type(format_, encoding):
    """Make sure format and compression is known."""

    if not (format_ in ArchiveFormats
        or format_ in CompressionFormats
        or format_ in AudioFormats
        or format_ in PackageFormats):
        raise Exception("Unknown file format `%s'" % format_)
    if encoding is not None and encoding not in ArchiveCompressions:
        raise Exception("Unkonwn archive compression `%s'" % encoding)
    return
