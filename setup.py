#! /usr/bin/env python3
#-------------------------------------------------------------------------------
#
# BASH version
# Original version Copyright 2001 by Kyle Sallee
# Additions/corrections Copyright 2002 by the Source Mage Team
#
# Python rewrite
# Copyright 2017 Geoff S Derber
#
# This file is part of Sorcery.
#
# File: Setup.py
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
#-------------------------------------------------------------------------------
from setuputils import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
#with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name='pySorcery',
    version='0.0.1',
    
    description='Sorcery Package Management System',
    long_description='Sorcery Package Management System ...',
    
    url='https://www.github.com/gderber/python-sorcery/',

    author='Geoff S Derber',
    author_email='gd.smlinux@gmail.com',
    
    license='GPLv3+',    

    classifiers=[
        # How mature is this project? Values are:
        #   1 - Planning
        #   2 - Pre-Alpha
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        #   6 - Mature
        #   7 - Inactive
        'Development Status :: 2 - Pre-Alpha',
        
        # Indicate who your project is intended for
        'Intended Audience :: System Administrators',
        'Intended Audience :: System Administrators',

        # Operating Systems
	'Operating System :: POSIX',
        
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',        
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

        'Topic :: System :: Installation/Setup'

        'Environment :: Console'
        'Environment :: Console :: Curses'
    ],

    keywords='blah'
    
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['distro'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'pyalter = pysorcery.cli.alter:main',
            'pycabal = pysorcery.cli.cabal:main',
            'pycast = pysorcery.cli.cast:main',
            'pycleanse = pysorcery.cli.cleanse:main',
            'pydispel = pysorcery.cli.dispel:main',
            'pyresurrect = pysorcery.cli.resurrect:main',
            'pyscribbler = pysorcery.cli.scribbler:main',
            'pyscribe = pysorcery.cli.scribe:main',            
            'pysorcery=pysorcery.cli.sorcery:main',
            'pysummon = pysorcery.cli.summon:main',
            'pyupstream = pysorcery.cli.upstream:main',
            'pyvcast = pysorcery.cli.vcast:main'
        ]
        'gui_scripts': [
            'pyxsorcery = pysorcery.gui.xsorcery'
        ]
    }
)
