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
class SorceryConfig():
    def __init__(self):
        self.logging_config = { "loglevel": "info",
                           "verbosity": 0
        }

        self.config_files = { 'local_config' : '/etc/sorcery/local/config',
                              'local_roots_config' : '/etc/sorcery/local/roots',
                              'local_media_config' : '/etc/sorcery/local/media',
                              'local_url_config' : '/etc/sorcery/local/url',
                              'grimoire_list_file' : '/etc/sorcery/local/grimoire'
        }

        self.theme = { 'sound': 'off',
                  'commands' : []
        }

        self.smgl_library = '/var/lib/sorcery'
        self.directories = { 'smgl_library' : smgl_library,
                        'codex': smgl_library + '/codex',
                        'source_cache': '/var/spool/sorcery',
                        'alien': [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                               '/opt', '/sbin', '/share', '/usr','/var' ]
        }

        self.urls = { 'codex_tarball_url' : 'http://codex.sourcemage.org',
                 'codex_rsync_url' : 'rsync://sourcemage.org::codex',
                 'codex_manifest_url' : 'http://codex.sourcemage.org',
                 'codex_url' : 'codex_tarball_url'
        }

        self.smgl_official_grimoires = [ 'test',
                                    'stable',
                                    'z-rejected',
                                    'games',
                                    'binary' ]

        
        
        self.config = { 'logging': logging_config,
                   'config_files': config_files,
                   'sorcery_branch': 'stable',
                   'directories': directories,
                   'urls': urls,
                   'official_grimoires' : smgl_official_grimoires,
                   'theme': theme
        }
    
    """
                  CAST=${CAST:-cast}
              ARCHIVE=${ARCHIVE:=on}
              AUTOFIX=${AUTOFIX:=on}
            UPDATEFIX=${UPDATEFIX:=off}
            AUTOPRUNE=${AUTOPRUNE:=off}
         MAIL_REPORTS=${MAIL_REPORTS:=off}
                PATCH=${PATCH:=off}
             PRESERVE=${PRESERVE:=on}
                 REAP=${REAP:=on}
       STORE_CONF_LOG=${STORE_CONF_LOG:-off}
             SORCERER=${SORCERER:=root}
              SUSTAIN=${SUSTAIN:=on}
                TMPFS=${TMPFS:=off}
         VIEW_REPORTS=${VIEW_REPORTS:=off}
               VOYEUR=${VOYEUR:=on}
         PROMPT_DELAY=${PROMPT_DELAY:=150}
        PAGER_TIMEOUT=${PAGER_TIMEOUT:=150}
           MAX_CABALS=${MAX_CABALS:=16}
           NET_SELECT=${NET_SELECT:=off}
            MD5SUM_DL=${MD5SUM_DL:=ask_risky}
         CLEAN_SOURCE=${CLEAN_SOURCE:=off}
           ARCHIVEBIN=${ARCHIVEBIN:=tar}
          COMPRESSBIN=${COMPRESSBIN:-bzip2}
            EXTENSION=${EXTENSION:-.bz2}
       SET_TERM_TITLE=${SET_TERM_TITLE:=off}
     PER_SPELL_CFLAGS=${PER_SPELL_CFLAGS:=off}
SHOW_GAZE_SHORT_QUERY=${SHOW_GAZE_SHORT_QUERY:=on}
                COLOR=${COLOR:=on}
           CONFIG_LOC=${CONFIG_LOC:=on}
          GATHER_DOCS=${GATHER_DOCS:=on}
    STRICT_SCM_UPDATE=${STRICT_SCM_UPDATE:=off}
                 NICE=${NICE:=+10}
                UMASK=${UMASK:=0022}
         SORCERY_PATH=${SORCERY_PATH:-"/usr/sbin"}
FORCE_BASESYSTEM_DEPENDS=${FORCE_BASESYSTEM_DEPENDS:-off}

            LDD_CHECK=${LDD_CHECK:=on}
           FIND_CHECK=${FIND_CHECK:=on}
         MD5SUM_CHECK=${MD5SUM_CHECK:=on}
            SYM_CHECK=${SYM_CHECK:=off}

        # menu defined defaults for dependency following
        ORPHAN_MENU_DEFAULT=${ORPHAN_MENU_DEFAULT:-ignore}
     NONORPHAN_MENU_DEFAULT=${NONORPHAN_MENU_DEFAULT:-ignore}
 RECAST_PARENT_MENU_DEFAULT=${RECAST_PARENT_MENU_DEFAULT:-ignore}
 DISPEL_PARENT_MENU_DEFAULT=${DISPEL_PARENT_MENU_DEFAULT:-ignore}

 URL_HTTP_FTP_TIMEOUT=${URL_HTTP_FTP_TIMEOUT:=90}

             FILEPROG=${FILEPROG:=file}
           DIALOGPROG=${DIALOGPROG:=dialog}

                DEBUG=${DEBUG:=/dev/null}

          CROSS_INSTALL=${CROSS_INSTALL:=off}

         ARCHITECTURE=${ARCHITECTURE:=i386}
        OPTIMIZATIONS=${OPTIMIZATIONS:=strip}

        COMPILE_CONFIG=${COMPILE_CONFIG:-/etc/sorcery/compile_config}
          ROOTS_CONFIG=${ROOTS_CONFIG:-/etc/sorcery/roots}
          MEDIA_CONFIG=${MEDIA_CONFIG:-/etc/sorcery/media}
            URL_CONFIG=${URL_CONFIG:-/etc/sorcery/url}
          STATE_CONFIG=${STATE_CONFIG:-/etc/sorcery/state}
         SCREEN_CONFIG=${SCREEN_CONFIG:-/etc/sorcery/screen}

          CONFIG_CACHE=${CONFIG_CACHE:-/etc/sorcery/local}

   SORCERY_INSTALL_LOG=${SORCERY_INSTALL_LOG:-/etc/sorcery/install.log}
       INSTALLWATCH_SO=${INSTALLWATCH_SO:-/usr/lib/installwatch.so}

  SM_LICENSE_DIRECTORY=${SM_LICENSE_DIRECTORY:-/etc/sorcery/licenses}
SM_CONFIG_OPTION_CACHE=${SM_CONFIG_OPTION_CACHE:-/etc/sorcery/local/config_option_cache}
          ACCOUNT_LIST=${ACCOUNT_LIST:-/etc/sorcery/accounts}
            GROUP_LIST=${GROUP_LIST:-/etc/sorcery/groups}

  GRIMOIRE_LIST_BACKUP=${GRIMOIRE_LIST_BACKUP:-/etc/sorcery/local/grimoire.backup}
        RESTORE_SCRIPT=${RESTORE_SCRIPT:-$HOME/sorcery.restore}
       CABAL_DIRECTORY=${CABAL_DIRECTORY:-/etc/sorcery/cabal}
           CABAL_NAMES=${CABAL_NAMES:-$CABAL_DIRECTORY/names}
            CABAL_KEYS=${CABAL_KEYS:-$CABAL_DIRECTORY/keys}
          CABAL_OUTPUT=${CABAL_OUTPUT:-/tmp/cabal.output}

           GPG_KEY_DIR=${GPG_KEY_DIR:-/usr/share/smgl-pubkeys}
           GPG_SIG_EXT=${GPG_SIG_EXT:-asc}
    GPG_VERIFY_SORCERY=${GPG_VERIFY_SORCERY:-no}
   GPG_VERIFY_GRIMOIRE=${GPG_VERIFY_GRIMOIRE:-no}
   
VERIFY_SPELL_LEVELS=${VERIFY_SPELL_LEVELS:-"WORKS_FOR_ME UPSTREAM_HASH UPSTREAM_KEY ESTABLISHED_UPSTREAM_KEY VERIFIED_UPSTREAM_HASH VERIFIED_UPSTREAM_KEY ID_CHECK_UPSTREAM_KEY"}
DEFAULT_SPELL_VRF_LEVEL=${DEFAULT_SPELL_VRF_LEVEL:-"WORKS_FOR_ME"}
    VRF_ALLOWED_LEVELS=${VRF_ALLOWED_LEVELS:-""}
  VRF_ALLOW_NEW_LEVELS=${VRF_ALLOW_NEW_LEVELS:-"on"}
    VRF_ALLOWED_HASHES=${VRF_ALLOWED_HASHES:-""}
  VRF_ALLOW_NEW_HASHES=${VRF_ALLOW_NEW_HASHES:-"on"}
     GPG_GRIMOIRE_LIST=${GPG_GRIMOIRE_LIST:-"test stable-rc stable games z-rejected hardened"}
GRIMOIRE_MANIFEST_ALGORITHM=${GRIMOIRE_MANIFEST_ALGORITHM:-sha1}

      DEF_INSTALL_INIT=${DEF_INSTALL_INIT:-off}
       DEF_ENABLE_INIT=${DEF_ENABLE_INIT:-off}
    DEF_INSTALL_XINETD=${DEF_INSTALL_XINETD:-off}
     DEF_ENABLE_XINETD=${DEF_ENABLE_XINETD:-off}
    DEF_INIT_VS_XINETD=${DEF_INIT_VS_XINETD:-off}

  SGL_LIBRARY_MODULES=${SGL_LIBRARY}/modules
           # system archspecs are still considered part of sorcery
           # and are deliberatly not in INSTALL_ROOT
           ARCH_SPECS=${ARCH_SPECS:-"/usr/share/archspecs"}
             EXCLUDED=${SGL_LIBRARY}/excluded
            PROTECTED=${SGL_LIBRARY}/protected
            VOLATILES=${SGL_LIBRARY}/volatiles
              CONFIGS=${SGL_LIBRARY}/configs
                 SOLO=${SGL_LIBRARY}/solo
          SUBROUTINES=${SGL_LIBRARY}/subroutines
            SUSTAINED=${SGL_LIBRARY}/sustained
        SORCERY_HOOKS=${SORCERY_HOOKS:-/etc/sorcery/hooks}
      SM_LICENSE_LIST=${SM_LICENSE_DIRECTORY}/license_list

         SPELL_INDEX_FILE=${SPELL_INDEX_FILE:-codex.index}
       PROVIDE_INDEX_FILE=${PROVIDE_INDEX_FILE:-provides.index}
       KEYWORD_INDEX_FILE=${KEYWORD_INDEX_FILE:-keyword.index}
       VERSION_INDEX_FILE=${VERSION_INDEX_FILE:-version.index}

             LOCK_DIR=${LOCK_DIR:-/tmp/liblock-$UID}
     LOCK_TRANSACTIONS=${LOCK_TRANSACTIONS:-"$LOCK_DIR/liblock.locklist"}
            MAX_SLEEP=${MAX_SLEEP:-3}

   TABLET_MAX_VERSION=${TABLET_MAX_VERSION:-1}

DEFAULT_CHANGED_CONFIG_ACTION=${DEFAULT_CHANGED_CONFIG_ACTION:-2}

              # SECURITY NOTE: any script running as root must pick a
              # more secure location for temp files that is not accessable
              # by other users and override this variable.
              # mk_tmp_dirs accomplishes this. Scripts run as
              # unpriviledged users are also advised to override this,
              # it is here merely to ensure it is always defined.
              TMP_DIR=${TMP_DIR:-/tmp}

               SCREEN=${SCREEN:-off}

              GAZE_ALIEN_PATHS=${GAZE_ALIEN_PATHS:-
                 DOCS=${DOCS:-'README* FAQ* CHAN* DOC* SETUP LICENSE COPYING NEWS *rc'}
                 DOC_DIRS=${DOC_DIRS:-'doc* conf'}
PROGRESS_SPINNER_CHARS=${PROGRESS_SPINNER_CHARS:-'-\|/'}
       VERBOSE_QUEUING=${VERBOSE_QUEUING:-on}
       HTTP_DL_HANDLER=${HTTP_DL_HANDLER:-wget}

        WHITESPACE_IFS=$' \t\n'
         TAB_ENTER_IFS=$'\t\n'
             ENTER_IFS=$'\n'
          STANDARD_IFS=$WHITESPACE_IFS

. $SUBROUTINES
set_pager

. $MEDIA_CONFIG
. $ROOTS_CONFIG
. $URL_CONFIG
. $STATE_CONFIG
. $COMPILE_CONFIG
. $SCREEN_CONFIG

[  -r  $GRIMOIRE_LIST  ]  &&  .  $GRIMOIRE_LIST

      # no $INSTALL_ROOT, so it stays consistent through INSTALL #15234
      BUILD_DIRECTORY=${BUILD_DIRECTORY:-/usr/src}
   DOCUMENT_DIRECTORY=${INSTALL_ROOT}/usr/share/doc
CONFIG_STAGE_DIRECTORY=${STATE_ROOT}/var/state/sorcery/staged_configs

      # this is passed directly to installwatch so it can't contain
      # shell expansions or regex's
CASTFS_UNSTAGED_PATHS="/dev /proc /tmp /var/tmp /sys ${BUILD_DIRECTORY} ${SGL_LIBRARY} ${INSTALL_ROOT}/${SGL_LIBRARY} ${SOURCE_CACHE} ${CONFIG_CACHE} ${INSTALL_ROOT}/${CONFIG_CACHE} ${STATE_DIRECTORY} ${LOG_DIRECTORY} $DEBUG"
# this value is a mask bits set mean output is done for that particular 
# component of castfs
CASTFS_DEBUG_LEVEL=${CASTFS_DEBUG_LEVEL:=255}
"""


#-------------------------------------------------------------------------------
#
# configure_logging
#
# Configure the logger.
#
#-------------------------------------------------------------------------------
def configure_logging(args,config):
    global logger
    global consolhandler

    logger.debug("Begin Function")
    
    # Ugly hack to make the changes global
    tempname = __name__.split(":")[0].split(".")[0]
    logger = logging.getLogger(tempname)

    loglevels = {'debug':10,
                 'info': 20,
                 'warning': 30,
                 'error': 40,
                 'critical': 50 }

    if config['logging']['verbosity'] == 0:
        config['logging']['loglevel'] = loglevels[config['logging']['loglevel']]
    else:
        config['logging']['loglevel'] = 11 - min(10,config['logging']['verbosity'])
    
    
    if args.debug:
        config['logging']['loglevel'] = 1
    elif args.loglevel:
        # Bind loglevel to the upper case string value obtained
        # from the command line argument.  This allows the user to
        # specify --log=DEBUG or --log=debug            
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % args.loglevel)
        config['logging']['loglevel'] = numeric_level
    elif args.quiet > 0:
        config['logging']['loglevel'] = 20 + args.quiet
    elif args.verbosity > 0:
        config['logging']['loglevel'] = 11 - args.verbosity
#    else:
#        config['loglevel'] = INFO

    logger.setLevel(config['logging']['loglevel'])
    consolehandler.setLevel(config['logging']['loglevel'])
        
    # End ugly hack to change logging level globally
    logger = logging.getLogger(__name__)

    # If debugging enabled, log the arguments passed to the program
    logger.debug("Arguments Processed")
#    logger.debug2("Arguments: " + str(args))
    
    logger.debug("End Function")
    return 0

#-------------------------------------------------------------------------------
#
# defConfiguration
#
# Gather the default plugins
#
#-------------------------------------------------------------------------------
def defConfiguration():
    logging_config = { "loglevel": "info",
                       "verbosity": 0
    }

    config_files = { 'local_config' : '/etc/sorcery/local/config',
                     'local_roots_config' : '/etc/sorcery/local/roots',
                     'local_media_config' : '/etc/sorcery/local/media',
                     'local_url_config' : '/etc/sorcery/local/url',
                     'grimoire_list_file' : '/etc/sorcery/local/grimoire'
    }

    theme = { 'sound': 'off',
              'commands' : []
              }

    smgl_library = '/var/lib/sorcery'
    directories = { 'smgl_library' : smgl_library,
                    'codex': smgl_library + '/codex',
                    'source_cache': '/var/spool/sorcery',
                    'alien': [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                               '/opt', '/sbin', '/share', '/usr','/var' ]
                    }

    urls = { 'codex_tarball_url' : 'http://codex.sourcemage.org',
             'codex_rsync_url' : 'rsync://sourcemage.org::codex',
             'codex_manifest_url' : 'http://codex.sourcemage.org',
             'codex_url' : 'codex_tarball_url'
             }

    smgl_official_grimoires = [ 'test',
                                'stable',
                                'z-rejected',
                                'games',
                                'binary' ]

    config = { 'logging': logging_config,
               'config_files': config_files,
               'sorcery_branch': 'stable',
               'directories': directories,
               'urls': urls,
               'official_grimoires' : smgl_official_grimoires,
               'theme': theme
               }
    
    """
                  CAST=${CAST:-cast}
              ARCHIVE=${ARCHIVE:=on}
              AUTOFIX=${AUTOFIX:=on}
            UPDATEFIX=${UPDATEFIX:=off}
            AUTOPRUNE=${AUTOPRUNE:=off}
         MAIL_REPORTS=${MAIL_REPORTS:=off}
                PATCH=${PATCH:=off}
             PRESERVE=${PRESERVE:=on}
                 REAP=${REAP:=on}
       STORE_CONF_LOG=${STORE_CONF_LOG:-off}
             SORCERER=${SORCERER:=root}
              SUSTAIN=${SUSTAIN:=on}
                TMPFS=${TMPFS:=off}
         VIEW_REPORTS=${VIEW_REPORTS:=off}
               VOYEUR=${VOYEUR:=on}
         PROMPT_DELAY=${PROMPT_DELAY:=150}
        PAGER_TIMEOUT=${PAGER_TIMEOUT:=150}
           MAX_CABALS=${MAX_CABALS:=16}
           NET_SELECT=${NET_SELECT:=off}
            MD5SUM_DL=${MD5SUM_DL:=ask_risky}
         CLEAN_SOURCE=${CLEAN_SOURCE:=off}
           ARCHIVEBIN=${ARCHIVEBIN:=tar}
          COMPRESSBIN=${COMPRESSBIN:-bzip2}
            EXTENSION=${EXTENSION:-.bz2}
       SET_TERM_TITLE=${SET_TERM_TITLE:=off}
     PER_SPELL_CFLAGS=${PER_SPELL_CFLAGS:=off}
SHOW_GAZE_SHORT_QUERY=${SHOW_GAZE_SHORT_QUERY:=on}
                COLOR=${COLOR:=on}
           CONFIG_LOC=${CONFIG_LOC:=on}
          GATHER_DOCS=${GATHER_DOCS:=on}
    STRICT_SCM_UPDATE=${STRICT_SCM_UPDATE:=off}
                 NICE=${NICE:=+10}
                UMASK=${UMASK:=0022}
         SORCERY_PATH=${SORCERY_PATH:-"/usr/sbin"}
FORCE_BASESYSTEM_DEPENDS=${FORCE_BASESYSTEM_DEPENDS:-off}

            LDD_CHECK=${LDD_CHECK:=on}
           FIND_CHECK=${FIND_CHECK:=on}
         MD5SUM_CHECK=${MD5SUM_CHECK:=on}
            SYM_CHECK=${SYM_CHECK:=off}

        # menu defined defaults for dependency following
        ORPHAN_MENU_DEFAULT=${ORPHAN_MENU_DEFAULT:-ignore}
     NONORPHAN_MENU_DEFAULT=${NONORPHAN_MENU_DEFAULT:-ignore}
 RECAST_PARENT_MENU_DEFAULT=${RECAST_PARENT_MENU_DEFAULT:-ignore}
 DISPEL_PARENT_MENU_DEFAULT=${DISPEL_PARENT_MENU_DEFAULT:-ignore}

 URL_HTTP_FTP_TIMEOUT=${URL_HTTP_FTP_TIMEOUT:=90}

             FILEPROG=${FILEPROG:=file}
           DIALOGPROG=${DIALOGPROG:=dialog}

                DEBUG=${DEBUG:=/dev/null}

          CROSS_INSTALL=${CROSS_INSTALL:=off}

         ARCHITECTURE=${ARCHITECTURE:=i386}
        OPTIMIZATIONS=${OPTIMIZATIONS:=strip}

        COMPILE_CONFIG=${COMPILE_CONFIG:-/etc/sorcery/compile_config}
          ROOTS_CONFIG=${ROOTS_CONFIG:-/etc/sorcery/roots}
          MEDIA_CONFIG=${MEDIA_CONFIG:-/etc/sorcery/media}
            URL_CONFIG=${URL_CONFIG:-/etc/sorcery/url}
          STATE_CONFIG=${STATE_CONFIG:-/etc/sorcery/state}
         SCREEN_CONFIG=${SCREEN_CONFIG:-/etc/sorcery/screen}

          CONFIG_CACHE=${CONFIG_CACHE:-/etc/sorcery/local}

   SORCERY_INSTALL_LOG=${SORCERY_INSTALL_LOG:-/etc/sorcery/install.log}
       INSTALLWATCH_SO=${INSTALLWATCH_SO:-/usr/lib/installwatch.so}

  SM_LICENSE_DIRECTORY=${SM_LICENSE_DIRECTORY:-/etc/sorcery/licenses}
SM_CONFIG_OPTION_CACHE=${SM_CONFIG_OPTION_CACHE:-/etc/sorcery/local/config_option_cache}
          ACCOUNT_LIST=${ACCOUNT_LIST:-/etc/sorcery/accounts}
            GROUP_LIST=${GROUP_LIST:-/etc/sorcery/groups}
         GRIMOIRE_LIST=${GRIMOIRE_LIST:-/etc/sorcery/local/grimoire}
  GRIMOIRE_LIST_BACKUP=${GRIMOIRE_LIST_BACKUP:-/etc/sorcery/local/grimoire.backup}
        RESTORE_SCRIPT=${RESTORE_SCRIPT:-$HOME/sorcery.restore}
       CABAL_DIRECTORY=${CABAL_DIRECTORY:-/etc/sorcery/cabal}
           CABAL_NAMES=${CABAL_NAMES:-$CABAL_DIRECTORY/names}
            CABAL_KEYS=${CABAL_KEYS:-$CABAL_DIRECTORY/keys}
          CABAL_OUTPUT=${CABAL_OUTPUT:-/tmp/cabal.output}

           GPG_KEY_DIR=${GPG_KEY_DIR:-/usr/share/smgl-pubkeys}
           GPG_SIG_EXT=${GPG_SIG_EXT:-asc}
    GPG_VERIFY_SORCERY=${GPG_VERIFY_SORCERY:-no}
   GPG_VERIFY_GRIMOIRE=${GPG_VERIFY_GRIMOIRE:-no}
   
VERIFY_SPELL_LEVELS=${VERIFY_SPELL_LEVELS:-"WORKS_FOR_ME UPSTREAM_HASH UPSTREAM_KEY ESTABLISHED_UPSTREAM_KEY VERIFIED_UPSTREAM_HASH VERIFIED_UPSTREAM_KEY ID_CHECK_UPSTREAM_KEY"}
DEFAULT_SPELL_VRF_LEVEL=${DEFAULT_SPELL_VRF_LEVEL:-"WORKS_FOR_ME"}
    VRF_ALLOWED_LEVELS=${VRF_ALLOWED_LEVELS:-""}
  VRF_ALLOW_NEW_LEVELS=${VRF_ALLOW_NEW_LEVELS:-"on"}
    VRF_ALLOWED_HASHES=${VRF_ALLOWED_HASHES:-""}
  VRF_ALLOW_NEW_HASHES=${VRF_ALLOW_NEW_HASHES:-"on"}
     GPG_GRIMOIRE_LIST=${GPG_GRIMOIRE_LIST:-"test stable-rc stable games z-rejected hardened"}
GRIMOIRE_MANIFEST_ALGORITHM=${GRIMOIRE_MANIFEST_ALGORITHM:-sha1}

      DEF_INSTALL_INIT=${DEF_INSTALL_INIT:-off}
       DEF_ENABLE_INIT=${DEF_ENABLE_INIT:-off}
    DEF_INSTALL_XINETD=${DEF_INSTALL_XINETD:-off}
     DEF_ENABLE_XINETD=${DEF_ENABLE_XINETD:-off}
    DEF_INIT_VS_XINETD=${DEF_INIT_VS_XINETD:-off}

  SGL_LIBRARY_MODULES=${SGL_LIBRARY}/modules
           # system archspecs are still considered part of sorcery
           # and are deliberatly not in INSTALL_ROOT
           ARCH_SPECS=${ARCH_SPECS:-"/usr/share/archspecs"}
             EXCLUDED=${SGL_LIBRARY}/excluded
            PROTECTED=${SGL_LIBRARY}/protected
            VOLATILES=${SGL_LIBRARY}/volatiles
              CONFIGS=${SGL_LIBRARY}/configs
                 SOLO=${SGL_LIBRARY}/solo
          SUBROUTINES=${SGL_LIBRARY}/subroutines
            SUSTAINED=${SGL_LIBRARY}/sustained
        SORCERY_HOOKS=${SORCERY_HOOKS:-/etc/sorcery/hooks}
      SM_LICENSE_LIST=${SM_LICENSE_DIRECTORY}/license_list

         SPELL_INDEX_FILE=${SPELL_INDEX_FILE:-codex.index}
       PROVIDE_INDEX_FILE=${PROVIDE_INDEX_FILE:-provides.index}
       KEYWORD_INDEX_FILE=${KEYWORD_INDEX_FILE:-keyword.index}
       VERSION_INDEX_FILE=${VERSION_INDEX_FILE:-version.index}

             LOCK_DIR=${LOCK_DIR:-/tmp/liblock-$UID}
     LOCK_TRANSACTIONS=${LOCK_TRANSACTIONS:-"$LOCK_DIR/liblock.locklist"}
            MAX_SLEEP=${MAX_SLEEP:-3}

   TABLET_MAX_VERSION=${TABLET_MAX_VERSION:-1}

DEFAULT_CHANGED_CONFIG_ACTION=${DEFAULT_CHANGED_CONFIG_ACTION:-2}

              # SECURITY NOTE: any script running as root must pick a
              # more secure location for temp files that is not accessable
              # by other users and override this variable.
              # mk_tmp_dirs accomplishes this. Scripts run as
              # unpriviledged users are also advised to override this,
              # it is here merely to ensure it is always defined.
              TMP_DIR=${TMP_DIR:-/tmp}

               SCREEN=${SCREEN:-off}

              GAZE_ALIEN_PATHS=${GAZE_ALIEN_PATHS:-
                 DOCS=${DOCS:-'README* FAQ* CHAN* DOC* SETUP LICENSE COPYING NEWS *rc'}
                 DOC_DIRS=${DOC_DIRS:-'doc* conf'}
PROGRESS_SPINNER_CHARS=${PROGRESS_SPINNER_CHARS:-'-\|/'}
       VERBOSE_QUEUING=${VERBOSE_QUEUING:-on}
       HTTP_DL_HANDLER=${HTTP_DL_HANDLER:-wget}

        WHITESPACE_IFS=$' \t\n'
         TAB_ENTER_IFS=$'\t\n'
             ENTER_IFS=$'\n'
          STANDARD_IFS=$WHITESPACE_IFS

. $SUBROUTINES
set_pager

. $MEDIA_CONFIG
. $ROOTS_CONFIG
. $URL_CONFIG
. $STATE_CONFIG
. $COMPILE_CONFIG
. $SCREEN_CONFIG

[  -r  $GRIMOIRE_LIST  ]  &&  .  $GRIMOIRE_LIST

      # no $INSTALL_ROOT, so it stays consistent through INSTALL #15234
      BUILD_DIRECTORY=${BUILD_DIRECTORY:-/usr/src}
   DOCUMENT_DIRECTORY=${INSTALL_ROOT}/usr/share/doc
CONFIG_STAGE_DIRECTORY=${STATE_ROOT}/var/state/sorcery/staged_configs

      # this is passed directly to installwatch so it can't contain
      # shell expansions or regex's
CASTFS_UNSTAGED_PATHS="/dev /proc /tmp /var/tmp /sys ${BUILD_DIRECTORY} ${SGL_LIBRARY} ${INSTALL_ROOT}/${SGL_LIBRARY} ${SOURCE_CACHE} ${CONFIG_CACHE} ${INSTALL_ROOT}/${CONFIG_CACHE} ${STATE_DIRECTORY} ${LOG_DIRECTORY} $DEBUG"
# this value is a mask bits set mean output is done for that particular 
# component of castfs
CASTFS_DEBUG_LEVEL=${CASTFS_DEBUG_LEVEL:=255}
"""


    return config

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
