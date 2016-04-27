# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import functools
import os.path as path
import asyncio
import ctypes

class PipeFunc(object):

    def __init__(self, function):
        self.func = function
        self.input_spec = None
        self.output_spec = None

    def set_input_spec(self):
        pass

    def set_output_spec(self):
        pass

    def check_input_spec(self, pend_spec):
        pass

    def check_output_spec(self):
        pass

def wrap_pyfunc(func_file, func_name, input_spec=None, output_spec=None):
    # get the abspath of func_file.
    # import func_name from func_file

    pass

def wrap_cfunc(func_file, func_name, input_spec=None, output_spec=None):
    # converts the input to ctypes based on the input description
    # call the c function using cytpes.byref()
    # converts the result from the c function back to python data
    pass


def check_connectivity(pipefunc_list):
    # for func in pipefunc_list:
    #     if func.input_spec is not None:
    #         check the pipefunc input and output
    #         if input not match:
    #             raise exception of inputMatchError
    #     connect func in async way
    #     if func.output_spec is not None:
    #         pend_spec = func.output_spec
    pass


def connect(pipefunc_list):
    # TODO:
    return [asyncio.coroutine(f) for f in pipefunc_list]


if __name__ == '__main__':

    func_files = ['path-to-dll-files']
    func_list = []

    for file in func_files:
        func = wrap_cfunc(file)
        func = PipeFunc(func)
        func_list.append(func)




