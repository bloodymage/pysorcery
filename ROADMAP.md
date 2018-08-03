# Roadmap

## 0.0

### 0.0.1
#### Functional Scripts
- pyarchive
  - Functions
    - [X] extract
    - [X] list
    - [X] create
    - [X] test
    - [X] repack
    - [X] search
    - [X] diff
    - [X] formats
    - [X] recompress
  - Archive Formats
    - [X] tar
    - [X] zip
    - [X] gz
    - [X] xz
    - [X] bz2
    - [X] iso
    - [X] others ...
- setup.py

### 0.0.2    
#### Functional Scripts
- pygaze
  - Functions
    - [X] activity
    - [X] alien
    - [ ] checkmd5s
    - [X] compile
    - [X] dependencies
    - [X] depends
    - [ ] export
    - [X] from
    - [ ] grimoire
    - [X] grimoires
    - [X] history
    - [ ] html
    - [ ] import
    - [X] installed
    - [ ] install-full
    - [X] install
    - [X] install-queue
    - [ ] install-spell
    - [X] licenses
    - [X] maintainer
    - [ ] md5sum
    - [ ] newer
    - [ ] older
    - [X] orphans
    - [ ] provides
    - [X] remove-queue - Theoretical, haven't had data to truly test with.
    - [ ] search
    - [X] section
    - [X] short
    - [X] show-exiled
    - [X] show-held
    - [X] size
    - [X] sources
    - [X] source_urls
    - [ ] sum
    - [ ] time
    - [ ] time-system
    - [X] url
    - [X] version
    - [ ] versions
    - [ ] voyeur
    - [X] what
    - [X] where
#### Modified scripts
- pyarchive
  - Functions
    - [X] read (for compressed files, ex. txtfile.gz)
#### Other
- Begin implementation of multiple smgl api versions.
- Pretty print capability

### 0.0.3
#### Functional Scripts
- pysummon
  - URI formats:
    - [ ] http
    - [ ] ftp
    - [ ] git
    - [ ] svn
    - [ ] cvs
    - [ ] rsync
    - [ ] bzr
    - [ ] file (Include Directories)
#### Modified scripts
- pyarchive
  - Functions
    - [ ] add (file)
    
### 0.0.4
#### Functional Scripts
- pyscribe
  - Functions
    - [ ] add
    - [ ] remove
    - [ ] update
    - [ ] localize
    - [ ] unlocalize
    - [ ] set
    - [ ] swap
#### Modified scripts
- pyarchive
  - Functions
    - [ ] append (concatenate two archives, ex. tar1.tar.gz + tar2.tar.gz = tar3.tar.gz)

### 0.0.5
#### Functional Scripts
- pyscribbler
  - Functions
    - [ ] add
    - [ ] remove
    - [ ] add-grimoire

### 0.0.6
#### Functional Scripts
- pycast
#### Modified scripts
- pyarchive
  - Functions
    - [ ] delete (file from archive)
    
### 0.0.7
#### Functional Scripts
- pydispel
#### Modified scripts
- pyarchive
  - Functions
    - [ ] update

### 0.0.8
#### Functional Scripts
- pycleanse

### 0.0.9
#### Functional Scripts
- pysorcery
  - Functions
    - [ ] system-update
    - [ ] update
    - [ ] upgrade
    - [ ] rebuild
    - [ ] queue
    - [ ] queue-security
    - [ ] review-queue
    - [ ] add-queue
    - [ ] remove-queue
    - [ ] hold
    - [ ] unhold
    - [ ] exile
    - [ ] unexile
    - [ ] default ...
  - Menus
    - [ ] Spell
      - [ ] Add
      - [ ] Rebuild (same as 'sorcery rebuild')
      - [ ] Hold
      - [ ] Remove
      - [ ] Select
      - [ ] Update
    - [ ] Option
      - [ ] Sorcery Branch
      - [ ] Color Scheme
      - [ ] Prompt Delay
      - [ ] Download Rate
      - [ ] Nice Level
      - [ ] Umask Value
      - [ ] Email of Sorcerer (SysAdmin)
      - [ ] Feature Menu
      - [ ] Integrity Checking
      - [ ] Parallel / Cached / Distributed Compiling
      - [ ] Dependency Following
      - [ ] Software Mirrors
      - [ ] Optimize Architecture
      - [ ] Compression Type
      - [ ] Sorcery Development
      - [ ] Summon Timeout
      - [ ] Default Download Tool
      - [ ] init.d and xinet.d defaults
      - [ ] Themes
        - [ ] Sound Scheme (only one at a time)
	  - [ ] Star Trek
	  - [ ] Ferris
	  - [ ] Misc
	  - [ ] Simpsons
	  - [ ] Off
	- [ ] Command Theme (multiple allowed)
	  - [ ] Sorcery (only if bash sorcery is not installed)
	  - [ ] Harry Potter
	  - [ ] Lunar (only if bash lunar not installed)
	  - [ ] ...
    - [ ] Log
    - [ ] Queue
    - [ ] Install Root
  - Execute (Menu Options for Execution)
    - [ ] Foreground
    - [ ] Background  

### 0.0.10
#### Functional Scripts
- Guru tools
  - [ ] Spider
    - [ ] Check for Broken Links
    - [ ] Validate URIs
    - [ ] Watch URLs for Changes
  - [ ] Dependencies
        - [ ] list cast order of list of spells based on dependencies
	- [ ] Check for circular dependencies
	- [ ] Find missing dependencies
	- [ ] Check duplicate dependencies
  - [ ] MD5unpack - Obtain MD5/SHA256/SHA512 for a tarball

### 0.0.11
#### Functional Scripts
- pyupstream
  - Check Debian Upstream
  - Create Spell From Debian Upstream
#### Sorcery Spell API 3

### 0.0.12
#### Script Modifications
- pygaze
  - Add Upstream information

### 0.0.13
#### Functional Scripts
- pyresurrect

### 0.0.14
#### Functional Scripts
- pyalter

### 0.0.15
#### Functional Scripts
- pyvcast

### 0.0.16
#### Functional Scripts
- pycabal

### 0.0.17
#### Functional Scripts
- pyconfmeld

### 0.0.18
#### Functional Scripts
- pydelve

### 0.0.19
#### Modified Scripts
- pyupdate
  - Add Homepage upstream


## 0.1

~- Sorcery CLI functional replacement for BASH version
#### Supported Distributions
- [ ] Source Mage
- [ ] Xubuntu

### 0.1.1
####
- API Funtionally complete

### 0.1.2
####
- Maximize native python code (minimize calls to outside programs).
- If sorcery needs outside program for a feature, create option to install.

### 0.1.3
- Ensure proper exception handling

### 0.1.4
#### Functional Scripts
- pyenchant
 
### 0.1.5
#### Functional Scripts
- pycauldron


## 0.2
- Framework functionally complete

### 0.2.1
#### Functional Scripts
- pyxsorcery


## 0.3
- GUI functionally complete


## 0.4

### 0.4.1
#### Modified Scripts
- Guru tools
  - [ ] Fix History
  - [ ] Report
    - [ ] Grimoire Image
    - [ ] Compare Images
  - [ ] Rebuild packages (Repairs /var/state/sorcery/packages
  - [ ] Cherry-pick

### 0.4.2
#### Functional Scripts
- pysmgl-ledger


## 0.5
- Base Code Functional
- Open to the public?

### 0.5.1
#### Supported Distributions
- Kali

### 0.5.2
#### Supported Distributions
- Debian


## 0.6
- Sorcery Pockage Management Complete
- Debian APT complete

### 0.6.1
#### New Package Manager
- Add support for Lunar Linux '...'
  - Ensure commands are compatible with Lunar Linux commands
  - Add Lunar 'Theme' for commands.

### 0.6.2
#### New Package Manager
- Add support for Arch 'pacman'

### 0.6.3
#### New Package Manager
-  Add support for Fedora 'yum'

### 0.6.4
#### New Package Manager
- Add support for Gentoo 'portage'


## 0.7
- Major Linux distributions package managers supported


## 0.8
- Add support for 'pip' package manager

### 0.8.1


## 0.9
- Initial System Functionally complete

### 0.9.1
Debug, debug, debug



## 1.0
- Release 1


### 1.1.0
#### New Package Manager
- Add support for MacOS 'Homebrew'



## 2.0
- Release 2


### 2.1.0


## 3.0
####
