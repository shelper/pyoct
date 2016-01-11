# -*- coding: utf-8 -*-

"""
wrappers
~~~~~~~~~

this module contains the decorators that simplifies some of the common processes.
e.g., return the complex, or real or imag part of the result
run the same process for 1D, 2D, or 3D datasets

"""

import functools

def complex(): #wrapper to return complex data
    pass

def real(): #wrapper to return real data
    pass

def imag(): #wrapper to return imaginary data
    pass

def amplitude(): #wrapper to return amplitude/intensity data
    pass

def phase(): #wrapper to return phase data
    pass

# TODO before perform this, the input array needs to be transposed so that func runs on axis=-1
def proc_2d(func):
    @functools.wraps(func)
    def wrapper(data, *args, **kwargs):
        for i in data[]
    pass

def proc_3d():
    pass
