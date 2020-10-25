#!/usr/bin/env python

from distutils.core import setup
setup(name='defect',
      version='0.1.0',
      description='Introducing Missing-linker Defects in Metal-Organic Frameworks',
      author='Meiirbek Islamov',
      author_email='mei12@pitt.edu',
      url='https://github.com/meiirbek-islamov/defects',
      packages=['defect'],
      install_requires=[
          'numpy',
          'click',
          'matplotlib',
          'random',
          're',
      ],
      )
