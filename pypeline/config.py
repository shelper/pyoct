# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""
Config the package pypeline

the pypeline package aims to provide an async frame work for data processing in scientific research.
for instance, Optical coherence tomography (OCT) users can config the package to run for OCT by using the
processing functions in the the folder impl/oct/*

"""
from glob import glob
import os.path as path

pypeline_path = path.dirname(path.abspath(__file__))
ext_files = [path.basename(f) for f in glob('/'.join((pypeline_path, 'ext', '*.py')))]
if '__init__.py' in ext_files:
    ext_files.remove('__init__.py')

ext_names = ['add', 'power', 'prod', 'subtract']

for ext in ext_names:
    file = '.'.join((ext, 'py'))
    if file not in ext_files:
        ext_names.remove(ext)
        print('extension {} not found, removed from extension list'.format(ext))
