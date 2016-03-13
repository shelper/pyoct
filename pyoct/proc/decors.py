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
from .. import data


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

