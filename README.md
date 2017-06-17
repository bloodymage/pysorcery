# Sorcery

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

This is a bonus application.  Sorcery needed to do these various tasks internally.  I simply added a script that calls these functions directly.

### pyledger

Incorporates ledger directly into sorcery

### pyupstream (I need a new Name)

This program checks upstream versions of software.

Alt genurates a new grimoire (Repository) with the latest version on the software.  If using the '--debian' switch will check the version of software in the debian sid repository.

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
Gaze is part of the Sorcery source-based package management suite. It is a
general purpose command-line tool for displaying package logs, version 
information, checking for installed packages, checksums, message
digests, maintainer information, package URL information, removing
obsolete packages, displaying new packages, untracked files, sections,
searching for files that are installed, finding when spells were
created and packages in the software catalogue. It can even take and
retrieve snap shots of currently installed packages for easy
duplication.


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

## Further information:
- [Roadmap](ROADMAP.md)
