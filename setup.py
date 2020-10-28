#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='defects',
      version='0.1.0',
      description='Introducing Missing-linker Defects in Metal-Organic Frameworks',
      author='Meiirbek Islamov',
      author_email='mei12@pitt.edu',
      url='https://github.com/meiirbek-islamov/defects',
      packages=find_packages(include=['defects']),
      install_requires=[
          'numpy',
          'matplotlib'
      ],
)
