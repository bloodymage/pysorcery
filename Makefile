# ----------------------------------------------------------------------
#
# Makefile for pysorcery
#
# By Geoff S Derber
#
#
#
# ---------------------------------------------------------------------
NAME=pysorcery
VERSION=0.0.1a
DESCRIPTION="pySocerery"

# -------
#
# Global Variables
#
# -------
#COLORS
GREEN  := $(shell tput -Txterm setaf 2)
WHITE  := $(shell tput -Txterm setaf 7)
YELLOW := $(shell tput -Txterm setaf 3)
RESET  := $(shell tput -Txterm sgr0)

#
PYTHON_MODULES := pysorcery
PYTHONPATH := .
VENV := .venv
PYTEST := env PYTHONPATH=$(PYTHONPATH) PYTEST=1 $(VENV)/bin/py.test
PYLINT := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pylint --disable=I0011 --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"
PEP8 := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/pep8 --repeat --ignore=E202,E501,E402
PYTHON := env PYTHONPATH=$(PYTHONPATH) $(VENV)/bin/python
PIP := $(VENV)/bin/pip

DEFAULT_PYTHON := /usr/bin/python3
VIRTUALENV := /usr/local/bin/virtualenv

REQUIREMENTS := -r requirements.txt

#
PREFIX=/usr/local
BINDIR=$(PREFIX)/bin
LIBDIR=$(PREFIX)/lib
MANDIR=$(PREFIX)/man
PYDIR=$(LIBDIR)/python3.6/dist-packages/
SORCERYDIR=$(PYDIR)/pysorcery
PKGPYSRCDIR=src/pysorcery

INSTALL_FILES=`find bin -type f 2>/dev/null`
DOC_FILES=*.md

# Packaging
PKG_DIR=pkg
PKG_NAME=$(NAME)-$(VERSION)
PKG=$(PKG_DIR)/$(PKG_NAME).tar.xz
SIG=$(PKG_DIR)/$(PKG_NAME).asc


# Add the following 'help' target to your Makefile
# And add help text after each target name starting with '\#\#'
# A category can be added with @category
HELP_FUN = \
    %help; \
    while(<>) { push @{$$help{$$2 // 'options'}}, [$$1, $$3] if /^([0-9a-zA-Z\-]+)\s*:.*\#\#(?:@([a-zA-Z\-]+))?\s(.*)$$/ }; \
    print "USAGE\n\nmake [target]\n\n"; \
    for (sort keys %help) { \
    print "${WHITE}$$_:${RESET}\n"; \
    for (@{$$help{$$_}}) { \
    $$sep = " " x (16 - length $$_->[0]); \
    print "  ${YELLOW}$$_->[0]${RESET}$$sep${GREEN}$$_->[1]${RESET}\n"; \
    }; \
    print "\n"; }

help: ##@other Show this help.
	@perl -e '$(HELP_FUN)' $(MAKEFILE_LIST)

default: check-coding-style ##@Other: default ...

venv: ##@Setup
	test -d $(VENV) || $(VIRTUALENV) -p $(DEFAULT_PYTHON) -q $(VENV)

requirements: ##@Setup
	@if [ -d wheelhouse ]; then \
	$(PIP) install -q --no-index --find-links=wheelhouse $(REQUIREMENTS); \
	else \
	$(PIP) install -q $(REQUIREMENTS); \
	fi

bootstrap: venv requirements ##@Setup

check-coding-style: bootstrap ##@Debugging
	$(PEP8) $(PYTHON_MODULES)
	$(PYLINT) -E $(PYTHON_MODULES)

pylint-full: check-coding-style
	$(PYLINT) $(PYTHON_MODULES)

test: check-coding-style
	$(PYTEST) $(PYTHON_MODULES)

check:
	$(PYTEST) $(PYTHON_MODULES)

.PHONY: default venv requirements bootstrap check-coding-style pylin

clean-pyc:
	find . -name '*.pyc' -exec rm --force {} +
	find . -name '*.pyo' -exec rm --force {} +
	name '*~' -exec rm --force {}

clean-build:
	rm --force --recursive build/
	rm --force --recursive dist/
	rm --force --recursive *.egg-info

pkg: ##@Packaging
	mkdir -p $(PKG_DIR)

$(PKG): pkg ##@Packaging
	git archive --output=$(PKG) --prefix=$(PKG_NAME)/ HEAD

build: $(PKG) ##@Packaging

$(SIG): $(PKG) ##@Packaging
	gpg --sign --detach-sign --armor $(PKG)

sign: $(SIG) ##@Packaging

clean: ##@Packaging
	rm -f $(PKG) $(SIG)

all: $(PKG) $(SIG)

tag:
	git tag v$(VERSION)
	git push --tags

release: $(PKG) $(SIG) tag

# Ugly hack until setup.py is further developed
install:
	@ln -nsvrf $(PWD)/$(PYSRCDIR) $(SORCERYDIR)
	@for file in $(INSTALL_FILES); do
		ln -nsvrf $$file $(PREFIX)/$$file
	@done
	#mkdir -p $(DOC_DIR)
	#cp -r $(DOC_FILES) $(DOC_DIR)/
