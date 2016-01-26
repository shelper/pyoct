# -*- coding: utf-8 -*-

"""
wrappers
~~~~~~~~~

this module contains the decorators that simplifies some of the common processes.
e.g., return the complex, or real or imag part of the result
run the same process for 1D, 2D, or 3D datasets

"""

import functools
import numpy as np


def partial_return(part):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            size = result.shape[0]
            if part == 'cplx':
                return result
            elif part == 'real':
                return result.real
            elif part == 'imag':
                return result.imag
            elif part == 'l_half':
                return result[:size/2+1, :]
            elif part == 'r_half':
                return result[size/2:, :]
            elif part == 'amplitude':
                return abs(result)
            elif part == 'phase':
                return np.angle(result)
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

