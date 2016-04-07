# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

"""
wrappers
~~~~~~~~~

this module contains the decorators that simplifies some of the common processes.
e.g., return the complex, or real or imag part of the result
run the same process for 1D, 2D, or 3D datasets

"""

import functools
# import numpy as np
import asyncio
import collections
from importlib import import_module
# from ..config import ext_names, ext_files


def load_ext_func(ext_name, cfg_file=None):
    """
    load function inis file from the ./settings/inis folder

    Args:
        ext_name (function): name of the function to be loaded from 'func_name.py' in folder ./settings
        cfg_file:
        async (bool):
    """
    # TODO: load multiple functions from a module, which can be done by:
    # from inspect import getmembers, isfunction
    # module_func_list = [f for f in getmembers(module) if isfunction(f[1])]
    # remember import module executes the top level expressions
    # if that is not desirable, use ast module to parse the source code to get module_func_list


    ext_module = '.'.join(('...ext', ext_name))
    ext_module = import_module(ext_module, __name__)
    func = getattr(ext_module, ext_name)
    if cfg_file:
        func_cfg = load_ext_cfg(cfg_file)
        func = functools.partial(func, **func_cfg)
    else:
        func = functools.partial(func, y=2)
    # if async:
    #     return asyncio.coroutine(ext_func)
    # else:
    #     return func
    return func


def load_ext_cfg(func):
    try:
        cfg_file = '.'.join((func.__name__, 'ini'))
        cfg_file = '/'.join(('settings', 'configuration', cfg_file))
        with open(cfg_file, 'r') as f:
            # TODO: load func_name.ini in ./settings/inis
            pass
        func_cfg = {}
    except FileExistsError:
        func_cfg = {}

    return func_cfg


def load_impl():
    pass


def check_data_in(func):
    """
    check if the input data matches the input requirements, the requirements are defined in
        the configuration file loaded by load_cfg(func)

    Args:
        func (function): function that will process the input data
    """

    def wrapper(*args, **kwargs):
        # TODO: check the input data matches the required format
        data_out = func(*args, **kwargs)
        return data_out
    return wrapper


def connect(func_list):
    """
    connects the functions in the list to form an async pipeline

    Args:
        func_list (list): list of functions in the folder ./settings
    """

    def wrapper(*args, **kwargs):
        for i, func in enumerate(func_list):
            data_in = args[0] if i == 0 else data_out
            data_out = yield from func(data_in, *args[1:], **kwargs)
        return data_out
    return wrapper


def pipenize(func):
    if isinstance(func, collections.Iterable):
        if all(map(callable, func)):
            return [asyncio.coroutine(f) for f in func]
    elif callable(func):
        return asyncio.coroutine(func)
        # elif isinstance(func, str):
        #     return load_func(func)


def m_pipenize(func):
    # TODO: matlab function pipenizer check: http://goo.gl/tMyU2C
    pass


def c_pipenize(func):
    # TODO: c/c++ function pipenizer
    pass


