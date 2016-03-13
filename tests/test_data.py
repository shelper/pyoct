# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *


import pytest

from .. import pyoct


def test_basedata():
    basedata = pyoct.data.basedata.BaseData([1024, 512], 'uint16')
    basedata.from_file(raw_data_uint16)
    assert 65134 == basedata.data[1023, 511]
    basedata = pyoct.data.basedata.BaseData([1024, 512], 'double')
    basedata.from_file(raw_data_double)
    assert abs(basedata.data[1023, 511] + 0.0061) < 0.001


def test_spectrum():
    spectrum =
