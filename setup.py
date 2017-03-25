#!/usr/bin/env python3

from setuputils import setup

setup(name='pySorcery',
      version='0.1.1',
      description='Sorcery',
      author='Geoff S Derber',
      author_email='gd.smlinux@gmail.com',
      dependencies='distro'
      url='https://www.github.com/gderber/python-sorcery/',
      license='GPLv3+',
      entry_points={
          'sorcery_cast': ['cast=pysorcery.cli.cast:main'],
          'sorcery_sorcery': ['sorcery=pysorcery.cli.sorcery:main']
      }
     )
