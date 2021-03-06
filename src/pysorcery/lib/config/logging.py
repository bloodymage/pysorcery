# Libraries
#
#-----------------------------------------------------------------------

# System Libraries
import sys
import os

# 3rd Party Libraries


# Application Libraries
# System Overrides
from pysorcery.lib.system import distro
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
consolehandler = logging.ColorizingStreamHandler()

license_dir = { 'apt': '/usr/share/common-licenses',
                'smgl': '/etc/sorcery/licenses'
}

activity_log = {
    'apt'  : '/var/log/apt/history.log',
    'smgl' : '/var/log/sorcery/activity'
}

log_dirs = {
    'apt': {
        'compile': 'tbd',
        'install': 'tbd',
        'md5': 'tbd',
        },
    'smgl': {
        'compile': '/var/log/sorcery/compile/',
        'install': '/var/log/sorcery/install/',
    },
}

sound_themes = [ 'off', 'ferris', 'star trek' ]

pkg_mgr = distro.distro_group[distro.distro_id]
#-----------------------------------------------------------------------
#
# Classes
#
# SorceryConfig
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# Class SorceryTheme
#
#-----------------------------------------------------------------------
class SorceryTheme():
    def __init__(self):
        self.command_themes = [ 'sorcery', 'harry potter' ]
        return

    def enable(self, theme):
        return

    def disable(self, theme):
        return

#-----------------------------------------------------------------------
#
# Class SorceryConfig
# 
# ...
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
    
        self.sound_theme = 'off'
        self.command_theme = []

        self.smgl_library = '/var/lib/sorcery'
        self.license_dir = license_dir[pkg_mgr]
        self.activity_log = activity_log[pkg_mgr]
        self.codex_dir = self.smgl_library + '/codex'
        self.source_cache = '/var/spool/sorcery'
        self.alien = [ '/bin', '/boot', '/etc', '/lib', '/lib64',
                       '/opt', '/sbin', '/share', '/usr','/var' ]

        self.urls = { 'codex_tarball_url' : 'http://codex.sourcemage.org/',
                      'codex_rsync_url' : 'rsync://sourcemage.org::codex',
                      'codex_manifest_url' : 'http://codex.sourcemage.org',
                      'codex_url' : 'codex_tarball_url'
        }

        self.smgl_official_grimoires = [ 'test',
                                         'stable-rc',
                                         'stable',
                                         'z-rejected',
                                         'games',
                                         'binary' ]
        self.branch = 'stable'
        self.archive = True
        self.autofix = True
        self.updatefix = False
        self.autoprune = False
        self.mail_reports = False
        self.patch = False
        self.preserve = True
        self.reap = True
        self.store_conf_log = False
        self.sorcerer = 'root'
        self.cast = 'cast'
        self.compression = 'lzma'
        self.extension = '.xz'
        self.sustain = True
        self.tmpfs = False
        self.view_reports = False
        self.voyeur = True
        self.prompt_delay = 150
        self.pager_timeout = 150
        self.max_cabals = 16
        self.net_select = False
        self.md5sum_dl = 'ask_risky'
        self.clear_source = False
        self.archivebin = 'tar'
        self.set_term_title = False
        self.per_spell_cflags = False
        self.show_gaze_short_query = True
        self.color = True
        self.config_loc = True
        self.gather_docs = True
        self.strict_scm_update = False
        self.nice = 10
        self.umask = '0022'
        self.force_basesystem_depends = False
        self.ldd_check = True
        self.find_check = True
        self.md5sum_check = True
    """
         SORCERY_PATH=${SORCERY_PATH:-"/usr/sbin"}
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

#-----------------------------------------------------------------------
#
# Functions
#
# configure_logging
# defConfiguration
# main_configuration
#
#-----------------------------------------------------------------------

#-----------------------------------------------------------------------
#
# configure_logging
#
# Configure the logger.
#
# Inputs
# ------
#    @param: args
#    @param: config
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
def configure_logging(args, config):
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
        config['logging']['loglevel'] = 20 - min(20,config['logging']['verbosity'])

    if args.debug:
        config['logging']['loglevel'] = 1
    elif args.quiet > 0:
        config['logging']['loglevel'] = 20 + args.quiet
    elif args.verbosity > 0:
        config['logging']['loglevel'] = 20 - args.verbosity
        print(config['logging']['loglevel'])
    else:
        # Bind loglevel to the upper case string value obtained
        # from the command line argument.  This allows the user to
        # specify --log=DEBUG or --log=debug
        numeric_level = getattr(logging, args.loglevel.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError('Invalid log level: %s' % args.loglevel)
        config['logging']['loglevel'] = numeric_level

    logger.setLevel(config['logging']['loglevel'])
    consolehandler.setLevel(config['logging']['loglevel'])

    # End ugly hack to change logging level globally
    logger = logging.getLogger(__name__)

    # If debugging enabled, log the arguments passed to the program
    logger.debug("Arguments Processed")
#    logger.debug2("Arguments: " + str(args))

    logger.debug("End Function")
    return

#-----------------------------------------------------------------------
#
# defConfiguration
#
# Gather the default plugins
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



    return config

#-----------------------------------------------------------------------
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
def main_configure(args):
    logger.debug("Begin Function")

    # Default Settings
    config = defConfiguration()

    # Congigure Loggings
    configure_logging(args, config)

    logger.debug2("Return variable: Config:\n" + str(config))
    logger.debug("End Function")
    return config
