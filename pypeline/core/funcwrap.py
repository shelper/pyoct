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
import numpy as np


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
    if callable(func):
        return asyncio.coroutine(func)
    elif isinstance(func, str):
        return load_func(func)


def load_func(func_name):
    """
    load function inis file from the ./settings/inis folder

    Args:
        func_name (function): name of the function to be loaded from 'func_name.py' in folder ./settings
    """
    base_func = import_module('.'.join(('settings', func_name, func_name)))
    func_cfg = load_func_cfg(func_name)
    func = functools.partial(base_func, **func_cfg)
    return asyncio.coroutine(func)


def load_func_cfg(func_name):
    try:
        cfg_file = '.'.join((func_name, 'ini'))
        cfg_file = '/'.join(('settings', 'configuration', cfg_file))
        with open(cfg_file, 'r') as f:
            # TODO: load func_name.ini in ./settings/inis
            pass
        func_cfg = {}
    except FileExistsError:
        func_cfg = {}

    return func_cfg


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

def log_scale(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result = 20 * np.log10(abs(result + 1E-6))
        return result
    return wrapper


def partial_return(part='left'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            size = result.shape[0]
            size = size - 1 if size % 2 else size
            if part == 'left':
                return result[:size/2 + 1, :]
            elif part == 'right':
                return result[size/2:, :]
        return wrapper
    return decorator


def proc_along_axis(axis=-1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(data, *args, **kwargs):
            result = np.apply_along_axis(func, axis=axis, *args, **kwargs)
            return result
        return wrapper
    return decorator

