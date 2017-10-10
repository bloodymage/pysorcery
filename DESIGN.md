# Sorcery Design Specification

Sorcery is a package management system writen in python.  It is based off of the Sorcery package management system writen in BASH for Source Mage GNU/Linux, which was originally writen by Kyle Sallee for Sorcerer GNU/Linux.  In addition to being able to work with native Sorcery 'spells' which are analygous to Gentoo's ebuilds.  This python version is to be able to work with multiple distributions package managers, such as apt, yum, etc.  This effectively allows a Sysadmin to learn 1 set of commands, and from their no matter which distribution they are using they don't have to learn new commands.

## Programs

All programs have their main name, which in general is 'py___' for example Cast is 'pycast.'  The names also have themes which can be activated through sorcery's menus.  Each theme when active, creates a symlink from the them command to the main program.  The themes include, 'Sorcery' which can only be installed if the BASH version is not also installed.  Other Themes, 'Harry Potter', ...

### Sorcery

This is the menu driven program of the same name.  From the menus, you can set the options, ...

### Cast / Erecto

This program is used to install programs.

On Sourced based distributions, running this program will:
1. Download the source tarball (file?) (If not already downloaded)
2. Extract the package to an appropriate folder.
3. Compile
4. Install

All others:
If compile switch is specified:
1. Download the source package installer (If not alreaded downloaded)
2. Compile
3. Install
Else if the package is not provided by the system's native package manage and is in Sorcery:
1. Download the source tarball
2. Extract the package to an appropriate folder.
3. Compile
4. Create native package per the system package manager (ie. create a *.deb file for Debian based systems).
5. Install the built package.
Else:
1. Interface with the system's native package manager to install the program.

### Gaze / Aparecium

Print requested information.

### Archive (rename?)

Work with files:
Extract,
Compresss,
Read,
...

### Dispel / Deletrius
Uninstall program.

### Alter


### Cabal

### Cleanse

### Confmeld

### Delve

### Resurrect

### Scribe
Manage package manager repositories.
Add/Remove/Update/...

### Scribbler

### Summon / Accio
Download files.

Download source files specified by a spell.
If a URL is provided rather than a spell, download the URL (act like wget, but for ALL url types)
Supported url types:
http(s)
ftp(s)
torrent
git
cvs
svn
rsync
...

### VCast

### XSorcery

### Enchant

### Ledger

### Upstream (New Name)

### Cauldron



## Sorcery file structure

pysorcery/
   __init__.py: Provides top level Sorcery variable definitions, along with Code copywrite information.
   cli/
      __init__.py:
      archive.py:
      gaze.py:
   lib/
      __init__.py: Provides top level Sorcery API.  All applications within the CLI folder should call classes from within this file, no deeper.
      files/
         __init__.py
	 archive/
	    __init__.py
	    ...
	 audio/
	    __init__.py
	    ...
	 compressed/
	    __init__.py
	    ...
	 video/
	    __init__.py
	    ...
      sorcery/
         __init__.py
	 ...
	 smgl/
	    __init__.py
	    ...
	 apt/
	    __init__.py
	    ...
      util/
	 __init__.py
	 ...
   plugins/
      __init__.py
      archive/
         __init__.py: Provides common functions for multiple sub commands.
         add.py:
         create.py:
         extract.py:
         list.py:
         formats.py:
         remove.py:
         concatenate.py:
         ...
      gaze/
         __init__.py:
         ...
      scribe/
         __init__.py:
	 ...
      scribbler/
         __init__.py:
	 ...
      sorcery/
         __init__.py:
	 ...
