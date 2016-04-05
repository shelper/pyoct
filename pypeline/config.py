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
# import os.path as path
import os
import sys

from .core import funcwrap


# Get the project root dir, which is the parent dir of this
project_root = os.path.dirname(os.path.abspath(__file__))
# print(project_root)
sys.path.insert(0, project_root)

ext_names = ['add', 'power', 'prod', 'subtract']
ext_list = []

# load ext function to the ext_list
for ext in ext_names:
    ext_files = [os.path.basename(f) for f in glob('/'.join((project_root, 'ext', '*.py')))]
    if '__init__.py' in ext_files:
        ext_files.remove('__init__.py')
    file = '.'.join((ext, 'py'))
    if file not in ext_files:
        ext_names.remove(ext)
        print('WARNING: extension {} not found, removed from extension list'.format(ext))
    else:
        ext_list.append(funcwrap.load_ext_func(ext, cfg_file=None))

# load a specific implementation from a folder containing a set of configurations and functions
# funcwrap.load_impl('oct')   # limited to one implementation
