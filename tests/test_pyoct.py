# -*- coding: utf-8 -*-

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

from .. import pyoct


# def test_data_generator():
#     pyoct.tools.data_generator.gen_spectrum()
#     pyoct.tools.data_generator.gen_basedata()

def test_rawdata_calibration():
    rawdata = pyoct.data.basedata.BaseData([1024, 512], 'uint16')
    rawdata.from_file('/Users/zyuan/develop/pyoct/foo/slope_uint16.raw')



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
    pline.feedin_data(3)
    pline.run()
    assert pline.data_out == 512

