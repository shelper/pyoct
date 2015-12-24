# -*- coding: utf-8 -*-

# import pytest

from .. import pyoct


def test_read_rawdata():
    rawdata = pyoct.data.basedata.BaseData([1024, 512], 'int16')
    rawdata.load_from_file('/Users/zyuan/develop/pyoct/foo/foodata.raw')


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

    pline = pyoct.proc.pipeline.PipeLine(funcs)
    pline.feed_data(3)
    pline.run()
    assert pline.data_out == 512

