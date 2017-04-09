# Sorcery

This is a complete re-write of Sorcery used by Source Mage GNU/Linux.  The original code was done in BASH, this will be in python.  This intended to be a functional dropin replacement, that will work side-by-side with the original sorcery code.  To do so, the commands have been named py<command>.  This version is designed to be flexible enough to work on non-sorcery systems such as Debian/Ubuntu.

## New Commands

### pyupstream (I need a new Name)

This program checks upstream versions of software.

Alt genurates a new grimoire (Repository) with the latest version on the software.  If using the '--debian' switch will check the version of software in the debian sid repository.

### pyaegis

Originally intended to be a stand-alone application.  I found my coding efforts had enough overlap that I added this to sorcery.

This program works on hardening your system, setting up firewalls...

## The Commands

### pyalter

### pycabal

### pycast
    is part of the sorcery package management suite. It is a command-line
    tool for automatically retrieving, unpacking, compiling, installing,
    and tracking software installations.


### pycleanse

### pydispel

### pygaze

Major changes: Removed prune (This was depreciated sometime between 2001-2005)

### pyressurect

### pyscribbler

### pyscribe

### pysorcery

### pysummon

### pyvcast

### pyxsorcery

## Supported Distros
- Source Mage (Tested using python 3.6.1)
- Ubuntu (Tested on X-Ubuntu 16.04 LTS using python 3.5)
