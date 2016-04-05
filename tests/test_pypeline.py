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

from ..pypeline.core import funcwrap, pipeline
from ..pypeline.config import ext_list


# def test_funcwrap():
#     funcwrap.load_ext_funcs()

print(ext_list)

def test_pipeline():
    pline = pipeline.Pipeline(ext_list)

    data_out = pline.process(3)
    # assert next(data_out) == 50
    assert data_out == 50

    # test iterable input
    data_out = pline.process([1, 2, 3, 4])
    assert next(data_out) == 18
    assert next(data_out) == 32
    assert next(data_out) == 50
    assert next(data_out) == 72



# def test_argswrap():
#     pass


def test_pypeline():
    pass
