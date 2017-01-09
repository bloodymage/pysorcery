#!/usr/bin/env python3

from setuputils import setup

setup(name='pySorcery',
      version='0.1.1',
      description='Sorcery',
      author='Geoff S Derber',
      author_email='gd.smlinux@gmail.com',
      url='https://www.github.com/gderber/python-sorcery/',
      license='GPLv3+',
      entry_points={
          'cast_scripts': ['cast=pysorcery.cast.__main__:main'],
          'sorcery_scripts': ['sorcery=pysorcery.sorcery.__main__:main']
      }
     )
