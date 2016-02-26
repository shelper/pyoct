# -*- coding: utf-8 -*-

import pytest

from .. import pyoct


def test_basedata_read():
    basedata = pyoct.data.basedata.BaseData([1024, 512], 'uint16')
    basedata.from_file('/Users/zyuan/develop/pyoct/foo/slope_uint16.raw')


def test_rawdata_calibration():
    rawdata = pyoct.data.basedata.BaseData([1024, 512], 'uint16')
    rawdata.from_file('/Users/zyuan/develop/pyoct/foo/slope_uint16.raw')
    rawdata.

def test_



def test_PipeLine():

    import functools

    def add(x, y):
        return x + y

    def prod(x, y):
        return x * y

    def power(x, y):
        return x**y

    funcs = [functools.partial(add, y=1),
             functools.partial(prod, y=2),
             functools.partial(power, y=3)]

    pline = pyoct.proc.pipeline.Pipeline(funcs)
    pline.feed_data(3)
    pline.run()
    assert pline.data_out == 512

