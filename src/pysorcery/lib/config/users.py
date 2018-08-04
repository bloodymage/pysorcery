#!/usr/bin/env python3
# ======================================================================
#
# Sorcery System Tools
#
#    by Geoff S. Derber
#
#
#
#
#
# ======================================================================
ROOTUSER = {
    "uid" : 0,
    "gid" : 0,
    "desc" : "",
    "home" : "/root",
    "shell" : "/bin/bash"
}

DAEMON = {
    "uid" : 1,
    "gid" : 1,
    "desc" : "",
    "home" : "",
    "shell" : ""
}

sysusers = {
    "root" : ROOTUSER,
    "daemon" : DAEMON,
    "bin" : 2,
    "sys" : 3,
x    "sync" : 4,
    "games" : 5,
    "man" : 6,
    "lp" : 7:7:lp:/var/spool/lpd:/usr/sbin/nologin
    "mail" : 8:8:mail:/var/mail:/usr/sbin/nologin
    "news" : 9:9:news:/var/spool/news:/usr/sbin/nologin
    "uucp" : 10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
    "proxy" : 13:13:proxy:/bin:/usr/sbin/nologin
    "www-data" : 33:33:www-data:/var/www:/usr/sbin/nologin
    "backup" : 34:34:backup:/var/backups:/usr/sbin/nologin
    "list" : 38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
    "irc" : 39:39:ircd:/var/run/ircd:/usr/sbin/nologin
    "gnats" : 41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
    "nobody" : 65534:65534:nobody:/nonexistent:/usr/sbin/nologin
    "systemd-network" : 100:102:systemd Network Management,,,:/run/systemd/netif:/usr/sbin/nologin
    "systemd-resolve" : 101:103:systemd Resolver,,,:/run/systemd/resolve:/usr/sbin/nologin
    "syslog" : 102:106::/home/syslog:/usr/sbin/nologin
    "messagebus" : 103
    "_apt" : 104,
    "sshd" : 105,
    "glances" : 106,
    "statd" : 107,
    "ntp" : 108,
    "avahi" : 109,
    "geoclue" : 110,
}

sysgroups = {
    "root" : 0,
    "daemon" : 1,
    "bin" : 2,
    "sys" :3:
    "adm" : 4,
    "tty" : 5,
    "disk" : 6,
    "lp" : 7,
    "mail" : 8,
    "news" : 9,
    "uucp" : 10,
    "man" : 12,
    "proxy" : 13,
    "kmem" : 15,
    "dialout" : 20,
    "fax" : 21,
    "voice" : 22,
    "cdrom" : 24,
    "floppy" : 25,
    "tape" : 26,
    "sudo" : 27,
    "audio" : 29,
    "dip" : 30,
    "www-data" : 33,
    "backup" : 34,
    "operator" : 37,
    "list" : 38,
    "irc" : 39,
    "src" : 40,
    "gnats" : 41,
    "shadow" : 42,
    "utmp" : 43,
    "video" : 44,
    "sasl" : 45,
    "plugdev" : 46,
    "staff" : 50,
    "games" : 60,
    "users" : 100,
    "nogroup" : 65534,
    "systemd-journal" : 101,
    "systemd-network" : 102,
    "systemd-resolve" : 103,
    "input" : 104,
    "crontab" : 105,
    "syslog" : 106,
    "messagebus" : 107,
    "ssh" : 108,
    "netdev" : 109,
    "glances" : 110,
    "rdma" : 111,
    "winbindd_priv" : 112,
    "sambashare" : 113,
    "ntp" : 114,
    "avahi" : 115,
    "geoclue" : 116,
}
