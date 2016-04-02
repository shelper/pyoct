# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import numpy as np
from scipy import interpolate
from scipy import signal
# from . import decors


def filter(data, axis=-1, win=[]):
    pass


def resample(x, y, xq, method='cubic'):
    interp = interpolate.interp1d(x, y, kind=method, bounds_error=False, fill_value=0)
    yq = interp(xq)
    return yq


def calibrate_sampling(v, cali_coeff, method='cubic'):
    """
    calibrate the vector to linear wavenumber domain before image reconstruction

    Args:
        v: vector as 1D numpy array
        cali_coeff: polynominal coefficents that maps linear pixel index to its actual wavenumber,
            the linear pixel index and actual wavenumber are both normalized to [0, 1]
        method: the interpolation kind, can be 'linear' or 'cubic', default to 'cubic'

    Returns:
        sp: spectrum as 1D numpy array after calibration

    """
    linear_idx = np.linspace(0, 1, v.shape[-1]).astype(np.float32)
    nonlinear_idx = np.polyval(cali_coeff, linear_idx)
    nonlinear_idx[nonlinear_idx < 0] = 0
    nonlinear_idx[nonlinear_idx > 1] = 1
    v = sig_proc.resample(nonlinear_idx, v, linear_idx, method=method)
    return v


def shift_phase(v, poly_coeff, slope=False):
    """
    shift_phase adds a pixel dependent phase shift to the 1D signal

    Example:
        it can be used to
            1. add/remove physical dispersion mismatch between sample and reference
            2. numerical refocusing, etc.

    Args:
        v: vector as 1D numpy array that phase shift applies to
        poly_coeff: polynominal coefficents for the polyfit of phase shift function
        slope (bool): if False, the linear slope from begin to end will be removed to ensure begin == end
            if True, keep the linear slope from begin to end.

    Returns:
        v: vector as 1D numpy array after phase shifted

    """
    linear_x = np.linspace(0, 1, v.shape[-1]).astype(np.float32)
    if slope:
        poly_coeff = np.append(poly_coeff, [-poly_coeff.sum(), 0])
    phase_shift = np.polyval(poly_coeff, linear_x)
    v = v * np.exp(-1j * phase_shift)
    return v


