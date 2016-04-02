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

from ..pypeline.core import funcwrap, argswrap, pipeline


def test_pipeline():
    import functools

    def add(x, y):
        return x + y

    def prod(x, y):
        return x * y

    def power(x, y):
        return x ** y

    funcs = [functools.partial(add, y=1),
             functools.partial(prod, y=2),
             functools.partial(power, y=3)]

    pline = pipeline.Pipeline(funcs)
    pline.feedin_data(3)
    pline.process()
    assert pline.data_out == 512


def test_funcwrap():
    pass


def test_argswrap():
    pass


def test_pypeline():
    pass
