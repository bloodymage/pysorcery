# Sorcery

Sorcery is a suite of applications for managing system packages...

This is a complete re-write of Sorcery used by Source Mage GNU/Linux.  The original code was done in BASH, this will be in python.  This intended to be a functional dropin replacement, that will work side-by-side with the original sorcery code.  To do so, the commands have been named py<command>.  This version is designed to be flexible enough to work on non-sorcery systems such as Debian/Ubuntu.


## New Commands

### pyarchive
A Universal Compressed File manager.
- Extracts
- Compresses
- List Contents
- Test
- Repack
- Recompress
- Diff
- Search
- Formats
- Add
- Read (compressed File)
This is a bonus application.  Sorcery needed to do these various tasks internally.  I simply added a script that calls these functions directly.

### pyledger
Incorporates ledger directly into sorcery

### pyupstream (I need a new Name)
This program checks upstream versions of software.  Alt generates a new grimoire (Repository) with the latest version on the software.  If using the '--debian' switch will check the version of software in the debian sid repository.

### pycauldron
Create Custom Install Disks

### pyenchant
SMGL installation program


## The Commands

### pyalter
Changes spells after they have been installed

### pycabal

### pycast
    is part of the sorcery package management suite. It is a command-line
    tool for automatically retrieving, unpacking, compiling, installing,
    and tracking software installations.

### pycleanse
cleanse is part of the sorcery source-code package management suite. It
       is a command-line tool for fixing and cleaning files maintained by sor‐
       cery.

### pyconfmeld
...

### pydelve
...

### pydispel
Remove Software Packages.

### pygaze
Gaze is part of the Sorcery source-based package management suite. It is a
general purpose command-line tool for displaying package logs, version 
information, checking for installed packages, checksums, message
digests, maintainer information, package URL information, removing
obsolete packages, displaying new packages, untracked files, sections,
searching for files that are installed, finding when spells were
created and packages in the software catalogue. It can even take and
retrieve snap shots of currently installed packages for easy
duplication.


Major changes:
- Removed prune (This was depreciated sometime between 2001-2005)
- 'gaze grimoire' and 'gaze html' includes a switch '--...' that will put the different grimoires in columns for comparing spell versions that exist in multiple grimoires.
- 

### pyressurect
Installs software packages from cache tarballs.

### pyscribbler
A utility for controlling spells within your grimoires

### pyscribe
Tracks, adds, and removes grimoires

### pysorcery
Menu-driven software package management utility

### pysummon
Downloads spell source files.

### pyvcast

### pyxsorcery
Menu-driven software package management utility


## Supported Package Managers
- Sorcery
- Apt
- Yum
- Pacman
- Ebuild
- Lunar (name?)


## Supported Distros
- Source Mage (Tested using python 3.6.1)
- Ubuntu (Tested on X-Ubuntu 16.04 LTS using python 3.5)
- Kali (Tested ...)
- 

## Themes
Themes allows alternate names for commands on the cli
- Sorcery (remove 'py' from names, this conflicts with Source Mage's sorcery)
- Harry Potter
  - pysummon = achio
  - ...
- Lunar (An attempt to try and unify lunar and sorcery development, with themes for each distribution).
  - ...

## Further information:
- [Roadmap](ROADMAP.md)
- [Wiki] (https://github.com/gderber/python-sorcery/wiki)