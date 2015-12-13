# -*- coding: utf-8 -*-

"""

"""
from operator import mul
from functools import reduce
import os
import numpy as np

from numpy import float32, double, uint8, int8, uint16, int16, uint32, int32

class Spectrum(object):

    def __init__(self, dimension, dtype):
        """
        specify the data type and dimension, calculate the basic information of the spectrum object

        :param dimension: list of int, ordered by [spectrum_size, Bscan_num, Cscan_num, time_points]
        :param dtype: string, select from ('float32', 'double64', 'uint8', 'int8', 'int16', 'uint16', 'int32', etc)
        :return: None
        """
        self.dimension = dimension
        self.data = np.array([], dtype=dtype)
        self.dtype = self.data.dtype
        self.dsize = reduce(mul, dimension, 1)

    def load_from_file(self, file, ftype='bin', hdr_size=0):
        if ftype == 'bin':
            with open(file, 'rb') as f:
                f.seek(hdr_size, os.SEEK_SET)
                self.data = np.fromfile(f, dtype=self.dtype, count=self.dsize)
                self.data.shape = self.dimension
        else:
            print('file type not supported:' + ftype)







