# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

# assert: base assert allowing you to write your own assertions
# assertEqual(a, b): check a and b are equal
# assertNotEqual(a, b): check a and b are not equal
# assertIn(a, b): check that a is in the item b
# assertNotIn(a, b): check that a is not in the item b
# assertFalse(a): check that the value of a is False
# assertTrue(a): check the value of a is True
# assertIsInstance(a, TYPE): check that a is of type "TYPE"
# assertRaises(ERROR, a, args): check that when a is called with args that it raises ERROR


import pytest
import functools
from importlib import import_module
from inspect import getmembers, isfunction

from ..pypeline.core import funcwrap, argswrap, pipeline
from ..pypeline.config import ext_names

# relative import does not work when running script in a python shell
# __name__ is the full name of this file as a module of pypeline, which is 'pypeline.test.test_pypeline'
ext_list = [import_module('.'.join(('...pypeline', 'ext', e)), __name__) for e in ext_names]

func_list = [getattr(ext, ext_name) for ext, ext_name in zip(ext_list, ext_names)]
# print(func_list)
func_list = [functools.partial(f, y=3) for f in func_list]

def test_pipeline():
    pline = pipeline.Pipeline(func_list)
    # test single input
    data_out = pline.process(3)
    assert next(data_out) == 512

    # test iterable input
    data_out = pline.process([1, 2, 3, 4])
    assert next(data_out) == 64
    assert next(data_out) == 216
    assert next(data_out) == 512
    assert next(data_out) == 1000


def test_funcwrap():
    pass


def test_argswrap():
    pass


def test_pypeline():
    pass
