#! /usr/bin/env python3
#-------------------------------------------------------------------------------
#
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
#
#-------------------------------------------------------------------------------

# System Libraries
import sys
import os
import copy
import tarfile
import socket
import datetime
import time
import platform
import lzma
import gzip
import bz2
import collections

# Other Libraries
import distro
import psutil
import ipgetter
import GeoIP

# Application Libraries
# Application Overrides
from pysorcery.lib import argparse
from pysorcery.lib import logging
# Other Application Libraries
import pysorcery
from pysorcery import __version__

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
# 
# 
#
#-------------------------------------------------------------------------------
class LocalTimezone(datetime.tzinfo):
    def __init__(self):
        self.STDOFFSET = datetime.timedelta(seconds = -time.timezone)
        if time.daylight:
            self.DSTOFFSET = datetime.timedelta(seconds = -time.altzone)
        else:
            self.DSTOFFSET = self.STDOFFSET

        self.DSTDIFF = self.DSTOFFSET - self.STDOFFSET


    def utcoffset(self, dt):
        if self._isdst(dt):
            return self.DSTOFFSET
        else:
            return self.STDOFFSET

    def dst(self, dt):
        if self._isdst(dt):
            return self.DSTDIFF
        else:
            return datetime.timedelta(0)

    def tzname(self, dt):
        return time.tzname[self._isdst(dt)]

    def _isdst(self, dt):
        tt = (dt.year, dt.month, dt.day,
              dt.hour, dt.minute, dt.second,
              dt.weekday(), 0, 0)
        stamp = time.mktime(tt)
        tt = time.localtime(stamp)
        return tt.tm_isdst > 0

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
# Class Backup File
# 
#
#-------------------------------------------------------------------------------
class BackupFile():
    def __init__(self,args):
        Local = LocalTimezone()
        self.hostname = socket.gethostname()
        self.username = os.environ.get('USER')
        if args.date:
            self.datetime = datetime.datetime(int(str(args.date)[0:4]),int(str(args.date)[4:6]),int(str(args.date)[6:8]),0,0,0,0,tzinfo=datetime.timezone.utc)
        else:
            self.datetime = datetime.datetime.now(tz=Local)
#        self.datetime = datetime.datetime.utcnow()
        self.datestring = self.datetime.strftime('%Y%m%d')
        self.no_backups = 12
        self.extention = args.extention
        self.exclude_files = ['README',
                              'INSTALL',
                              '.cvsignore',
                              '~']
        
        self.name = self.hostname + '-' + self.username + '-' + self.datestring + ".tar." + self.extention
        self.user_home = os.path.expanduser("~")
        if args.folder:
            self.backup_dir=args.folder
        else:
            self.backup_dir=self.user_home + '/GDrive/Business/backups/' + self.username


        if args.gfs:
            self.scheme = 'gfs'
        else:
            self.scheme = 'hanoi'



    def pne(self):
        """
        Guess the extension of given filename.
        """
        # Add extra extensions where desired.
        DOUBLE_EXTENSIONS = ['tar.gz','tar.bz2','tar.xz']

        path, filename=os.path.split(self.name)
        root,ext = os.path.splitext(filename)
        if any([filename.endswith(x) for x in DOUBLE_EXTENSIONS]):
            root, first_ext = os.path.splitext(root)
            exgt = first_ext + ext
        return path, root, ext

    def fifo(self):
        logger.debug("Begin Function")

        old_file = self.name
        
        logger.debug("End Function")
        return old_file


    def grandfatherson(self):
        logger.debug("Begin Function")

        old_file = self.name
        
        logger.debug("End Function")
        return old_file

    #-------------------------------------------------------------------------------
    #
    # Func Hanoi
    #
    #
    # Tower of Hanoi Backup script.
    #
    # Bash implementation
    # hanoi_backup v2.3.1 jeremdow@gmail.com
    # modified by jobjol jobjoling@gmail.com
    #
    # This script will archive specified files and folders on the remote host.
    # If run as a daily cron job, archives are rotated on a Tower of Hanoi schedule.
    # Archives from 1, 2, 4, 8, 16... $max days ago are retained depending on the
    # setting.
    #
    # Age of oldest backup file is based on the max days.
    # No Backups       Max Day          Oldest Backup Days Range
    # Infinit (1)      1                infinit
    # 2                2                2
    # 3                4                3-4
    # 4                8                5-8
    # 5                16               9-16
    # 6                32               17-32
    # 7                64               33-64
    # 8                128              65-128
    # ...
    #
    #-------------------------------------------------------------------------------
    def hanoi(self):
        logger.debug("Begin Function")

        origin_date = datetime.datetime(1,1,1,0,0,0,0,tzinfo=datetime.timezone.utc)
        epoch_date = datetime.datetime(1970,1,1,0,0,0,0,tzinfo=datetime.timezone.utc)
        origin_time = epoch_date
        logger.debug2("Origin Time: " + str(origin_time))
        logger.debug3("Origin Date: " + str(origin_date))
        logger.debug3("Epoch Date: " + str(epoch_date))

        logger.debug(self.datetime)

        daysfromorigin = (self.datetime - origin_time).days
#        daydiff = datetimediff.days()

        logger.debug4("Datetimediff: " + str(daysfromorigin))

        levels = self.no_backups - 1
        max_days = 2 ** levels

        logger.debug2("Max Days: " + str(max_days))
        logger.debug3("Levels: " + str(levels))

        if levels < 7:
            retain_max_level_backups = True
        else:
            retain_max_level_backups = False

        i = 1

        expired = 1

        while i <= max_days/2:
            rotation = daysfromorigin & i

            daybin = bin(daysfromorigin)
            ibin =bin(i)
            
            logger.debug3("Ibin: " + str(ibin))
            logger.debug3("Daybin: " + str(daybin))
            logger.debug2("Rotation: " + str(rotation))

            if rotation == 0:
                expired = i * 2
                logger.debug4("Breok while loop")
                break
            else:
                if retain_max_level_backups:
                    expired = 4
                else:
                    expired = i * 2

            i=i*2

            logger.debug3("Expired: " + str(expired))
            logger.debug4("I: " + str(i))

        expired_date = self.datetime + datetime.timedelta(days=-expired)
        expired_date_string = expired_date.strftime('%Y%m%d')

        logger.debug2(expired_date_string)

        old_file = '/hanoi/' + self.hostname + '-' + self.username + '-' + expired_date_string + ".tar." + self.extention
        
        logger.debug("End Function")
        return old_file


#-------------------------------------------------------------------------------
#
# Class Backup Home
# 
#
#-------------------------------------------------------------------------------
class BackupHome(BackupFile):
    def filter_function(tarinfo):
        if tarinfo.name in self.exclude_files:
            return None
        else:
            return tarinfo
    
    def compress(self):
        logger.debug("Begin Function")

        backup_dir=self.backup_dir + '/home/'

        backup_file = backup_dir + self.name


        try:
#            tar_file = tarfile.open(self.name)
#            tar_file.add('/home/geoff',arc_name=self.name,filter=filter_function)
            logger.info("Compressing Home files: " + str(backup_file))
        except tar_file.TarError:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")

        logger.debug("End Function")
        return

    def extract(self):
        logger.info("Extracting file: " + str(self.name))

        try:
            tar_file = tarfile.open(self.name)
            for name in tar_file.getnames():
                tar_file.extractall(basename)
            logger.info("Extracted file: " + str(self.name))
        except tar_file.TarError:
            logger.error("Unk Extraction Error")
            pass
        except IOError:
            logger.error("IO Error")
            pass
        except:
            logger.error("Unknown Error")

        return

    def remove_old(self):
        logger.debug("Begin Function")

        if self.scheme == 'gfs':
            expired_file = self.grandfatherson()
        else:
            expired_file = self.hanoi()

        expired_file=self.backup_dir + '/home' + expired_file

        logger.info("Remove Expired File: " + str(expired_file))

        logger.debug("End Function")
        return

    
#-------------------------------------------------------------------------------
#
# Class Backup SQL
# 
#
#-------------------------------------------------------------------------------
class BackupSQL(BackupFile):
    def compress(self):
        logger.info("Compressing SQL file: " + str(self.name))
        return

    def extract(self):
        logger.info("Extracting file: " + str(self.name))
        return

    def remove_old(self):
        logger.debug("Begin Function")

        if self.scheme == 'gfs':
            expired_file = self.grandfatherson()
        else:
            expired_file = self.hanoi()

        expired_file=self.backup_dir + '/sql' + expired_file

        logger.info("Remove Expired File: " + str(expired_file))

        logger.debug("End Function")
        return

class StatusInfo():
    def __init__(self,args):
        self.lowuse = 50
        self.meduse = 75
        self.highuse = 90
        self.warninguse = 95

        self.distro_id=distro.linux_distribution()[0]
        self.distro_release=distro.linux_distribution()[1]
        self.distro_codename=distro.linux_distribution()[2]

        self.os_name=platform.system()
        self.os_version=platform.release()

        self.hostname=platform.node()

        self.system_time=datetime.datetime.now()

        self.cpu_usage=psutil.cpu_percent()
        self.cpu_cores=psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq()

        self.cpu_freq=[]
        for i in cpu_freq:
            if i < 1000:
                self.cpu_freq.append(str(round(i / 1.0,1)) + "MHz")
            else:
                self.cpu_freq.append(str(round(i / 1000.0,1)) + "GHz")
        
        sensors_temp=psutil.sensors_temperatures()
        sensors_batt=psutil.sensors_battery()

        core_temp=0
        for i in sensors_temp['coretemp']:
            core_temp = i[1] + core_temp
        
        self.cpu_temp = core_temp / 4

        self.battery_per = sensors_batt[0]//1.0
        
        if str(sensors_batt[1]) == "BatteryTime.POWER_TIME_UNLIMITED":
            self.battery_status = "fully-changed"
        else:
            self.battery_status = sensors_batt[1]

        if sensors_batt[2]:
            self.battery_plug = "Plugged In"
        else:
            self.battery_plug = "Discharging"

        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            self.uptime = str(datetime.timedelta(seconds = uptime_seconds))

        self.extip = ipgetter.myip()

        gi = GeoIP.open("/usr/share/GeoIP/GeoIPCity.dat", GeoIP.GEOIP_STANDARD)

        self.location = gi.record_by_addr(self.extip)

        diskinfo = psutil.disk_partitions()

        self.disk_dev=[]
        for i in diskinfo:
            self.disk_dev.append(i[0])

        self.disk_mount=[]
        for i in diskinfo:
            self.disk_mount.append(i[1])

        self.disk_usage=[]
        for i in self.disk_mount:
            usage = psutil.disk_usage(i)
            total = usage[0]//(1024*1024.0)
            used = usage[1]//(1024*1024.0)
            free = usage[2]//(1024*1024.0)
            perc = usage[3]
            j = [ total, used, free, perc]
            self.disk_usage.append(j)

        memory = psutil.virtual_memory()
        self.mem_total=round(memory[0]/(1024*1024*1024),2)
        self.mem_used=round(memory[3]/(1024*1024*1024),2)
        self.mem_free=round(memory[1]/(1024*1024*1024),2)
        self.mem_percent=memory[2]

        memory = psutil.swap_memory()
        self.swap_total=round(memory[0]/(1024*1024*1024),2)
        self.swap_used=round(memory[1]/(1024*1024*1024),2)
        self.swap_free=round(memory[2]/(1024*1024*1024),2)
        self.swap_percent=memory[3]

        users_info = psutil.users()
        logged_in_users=[]
        for i in users_info:
            logged_in_users.append(i[0])

        self.users=list(collections.OrderedDict.fromkeys(logged_in_users))

        

class SystemInfo(StatusInfo):
    def displayinfo(self):
        logger.info("                     System Information")
        logger.info("Distribution:    " + str(self.distro_id) + " " + str(self.distro_release) + " " + str(self.distro_codename))
        logger.info("OS:              " + str(self.os_name) + ' ' + str(self.os_version))
        logger.info("Current Time:    " + str(self.system_time))
        logger.info("Last Login:      ")

        # If Owner of system
        logger.info("Logged in Users: " + str(self.users))

        logger.info("Uptime:          " + str(self.uptime))

        # If uprecords
        logger.info("Uprecords:       ")

        # If laptop
        logger.info("Battery Status:  " + str(self.battery_per) + str("% ") + str(self.battery_status) + " " + str(self.battery_plug))

        logger.info("Load:            ")
        logger.info("Memory:          " + str(self.mem_total) +
                    "GB  " + str(self.mem_used) +
                    "GB/" + str(self.mem_free) +
                    "GB  " + str(self.mem_percent) + "%")
        logger.info("Swap:            " + str(self.swap_total) +
                    "GB  " + str(self.swap_used) +
                    "GB/" + str(self.swap_free) +
                    "GB  " + str(self.swap_percent) + "%")
        logger.info("CPU:")
        logger.info("      CPU Freq: " + str(self.cpu_freq[0]) +
                    "  Min CPU Freq: " + str(self.cpu_freq[1]) +
                    "  Max CPU Freq: " + str(self.cpu_freq[2]))                    
        logger.info("     CPU Cores: " + str(self.cpu_cores) +
                    "     CPU Usage: " + str(self.cpu_usage) + "%")
        logger.info("      CPU Temp: " + str(self.cpu_temp) + "°C")
        logger.info("Disks:")
        logger.info("    Disk Temps:      ")
        logger.info("    Disk Usage:")

        

        x = 0
        for i in self.disk_mount:
            j = self.disk_usage[x]
            logger.info("          " + str(i))
            logger.info("             Total: " + str(j[0]) +
                        " Used: " + str(j[1]) +
                        " Free: " + str(j[2]) +
                        " Percent: " + str(j[3]))
            x = x + 1
        
        logger.info("Location:")
        logger.info("    " + str(self.location['city']) + ", "+ str(self.location['region']) + " " + str(self.location['postal_code']))
        logger.info("    " + str(self.location['country_name']))

        return

class NetworkInfo(StatusInfo):
    def displayinfo(self):
        logger.info("                     Network Information")
        logger.info("External IP: " + str(self.extip))

    
#-------------------------------------------------------------------------------
#
# Function backup
#
#
#
#
#-------------------------------------------------------------------------------
def backup(args):
    logger.debug("Begin Function")
    

    if args.home:
        backup_file=BackupHome(args)
    if args.sql:
        backup_file=BackupSQL(args)
    else:
        backup_file=BackupHome(args)

    backup_file.compress()

    backup_file.remove_old()
    
    logger.info("Backup Files")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def restore(args):
    logger.debug("Begin Function")
        
    logger.info("Restore")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def sync(args):
    logger.debug("Begin Function")
        
    logger.info("Sync")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def cleanup(args):
    logger.debug("Begin Function")
        
    logger.info("Cleanup Junk")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def firewall(args):
    logger.debug("Begin Function")
        
    logger.info("Configure Firewall")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def config_files(args):
    logger.debug("Begin Function")
        
    logger.info("Modify Config Files")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def harden(args):
    logger.debug("Begin Function")
        
    logger.info("Harden System")
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# Function restore
#
#
#
#
#-------------------------------------------------------------------------------
def info(args):
    logger.debug("Begin Function")

    if args.system:
        info = SystemInfo(args)
        info.displayinfo()
    if args.network:
        info = SystemInfo(args)
        info.displayinfo()
    else:
        if not args.system and not args.network:
            info = SystemInfo(args)
            info.displayinfo()
            logger.info("")
            logger.info("")
            info = NetworkInfo(args)
            info.displayinfo()

    
    logger.debug("End Function")
    return

#-------------------------------------------------------------------------------
#
# configure
#
# Load configuration settings in the following order:
# 1. Hard Coded
# 2. {python-dir}/dist-___/pyaegis/aegis_default.conf
# 3. ~/.config/aegis/aegis.conf
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
#    logger = getLogger('pyaegis')

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
    config = { "loglevel": "info",
               "verbosity": 0
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

    parser = argparse.ArgumentParser(description="Aegis helps with system security.")
    parser.add_argument("--config",
                        nargs=1,
                    help="Use specified config file")
    parser.add_argument("-q", "--quiet",
                        action="count",
                        default=0,
                    help="Decrease output verbosity")
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

    subparsers = parser.add_subparsers(help='Sub commands')

    # create the parser for the "backup" command
    parser_backup = subparsers.add_parser('backup', help='backup help')
    backup_group_main = parser_backup.add_argument_group("Action")
    backup_group_main.add_argument('--apps',
                                   help='Create/Update installed applications list',
                                   action='store_true')
    backup_group_main.add_argument('--home',
                                   help='Create Home Backup',
                                   action='store_true')
    backup_group_main.add_argument('--sql',
                                   help='Create Database Backup',
                                   action='store_true')
    backup_group_scheme = parser_backup.add_argument_group('Scheme')
    backup_group_scheme.add_argument('--gfs',
                                     action='store_true',
                                     help='Use the "Grandfather/Father/Son" backup schedule')
    backup_group_scheme.add_argument('--hanoi',
                                     action='store_true',
                                     help='Use the "Tower of Hanoi" backup schedule')
    parser_backup.add_argument('--folder',
                               help='Specify Folder for backup file')
    parser_backup.add_argument('--extention',
                               choices=["gz","bz2", "xz"],
                               default='xz',
                               help='Specify Extention for backup file (changes compression method)')
    parser_backup.add_argument('--date',
                               type=int,
                               help='Create (late) backup for specified date')
    parser_backup.add_argument("--debug",
                    help="Enable Debugging",
                    action="store_true")
    parser_backup.set_defaults(func=backup)

    # create the parser for the "restore" command
    parser_restore = subparsers.add_parser('restore', help='restore help')
    restore_group_main = parser_restore.add_argument_group('action')
    restore_group_main.add_argument('--apps',
                                    action='store_true',
                                    help='Restore installed applications list')
    restore_group_main.add_argument('--gdrive',
                                    action='store_true',
                                    help='bar help')
    restore_group_main.add_argument('--git',
                                    action='store_true',
                                    help='bar help')
    restore_group_main.add_argument('--home',
                                    action='store_true',
                                    help='bar help')
    restore_group_main.add_argument('--sql',
                                    action='store_true',
                                    help='bar help')
    parser_restore.set_defaults(func=restore)

    # create the parser for the "sync" command    
    parser_sync = subparsers.add_parser('sync', help='sync help')
    sync_group_main = parser_sync.add_argument_group('action')
    sync_group_main.add_argument('--gdrive',
                                 action='store_true',
                                 help='bar help')
    sync_group_main.add_argument('--git',
                                 action='store_true',
                                 help='bar help')
    sync_group_main.add_argument('--network',
                                 action='store_true',
                                 help='bar help')
    parser_restore.set_defaults(func=sync)

    # create the parser for the "cleanup" command
    parser_cleanup = subparsers.add_parser('cleanup', help='sync help')
    cleanup_group_main = parser_cleanup.add_argument_group('action')
    cleanup_group_main.add_argument('--files',
                                    action='store_true',
                                    help='bar help')
    cleanup_group_main.add_argument('--kernels',
                                    action='store_true',
                                    help='bar help')
    parser_restore.set_defaults(func=cleanup)
    
    # create the parser for the "restore" command    
    parser_firewall = subparsers.add_parser('firewall',
                                            help='sync help')
    parser_firewall.add_argument('--profile',
                                 help='Use Named Profile')
    parser_firewall.add_argument('-d',
                                 '--disable_service',
                                 help='Disable Service')
    parser_firewall.add_argument('-e',
                                 '--enable_service',
                                 help='Enable Service')
    parser_firewall.add_argument('--panic',
                                 help='Enable Panic Mode.  Same as "--profile panic"')
    parser_firewall.add_argument('-s',
                                 '--stop',
                                 help='Stop the firewall.  WARNING this will allow all incoming and outgoing traffic')
    parser_firewall.add_argument('--status',
                                 help='Display Current Firewall Status')
    parser_firewall.add_argument('--wait',
                                 help='For testing purposes')
    parser_restore.set_defaults(func=firewall)

    # create the parser for the "restore" command
    parser_harden = subparsers.add_parser('harden', help='Harden the System')
    parser_harden.add_argument('bar',
                               type=int,
                               help='bar help')
    parser_restore.set_defaults(func=harden)

    # create the parser for the "restore" command
    parser_info = subparsers.add_parser('info', help='Display Status Information')
    parser_info.add_argument('--system',
                             action='store_true',
                             help='Display System Info')
    parser_info.add_argument('--network',
                             action='store_true',
                             help='Display System Info')
    parser_info.add_argument('--weather',
                             action='store_true',
                             help='Display System Info')
    parser_info.add_argument('--debug',
                             action='store_true',
                             help='Display System Info')
    parser_info.set_defaults(func=info)
    
    args = parser.parse_args()

    config = main_configure(args)
    logger.debug2("Configuration set")
    logger.debug3("Configuration Settings: " + str(config))
    logger.debug4("Arguments: " + str(args))
    
    # "application" code
    args.func(args)

    
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
# 1. ~/.config/aegis/aegis.conf
# 2. /etc/aegis/aegis.conf
# 3. {python-dir}/dist-___/aegis/aegis.conf
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
#            logger.critical(str(args))

        logger.debug("End Application")
        return 0


main()
