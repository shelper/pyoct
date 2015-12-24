# -*- coding: utf-8 -*-

from functools import reduce
import numpy as np
import operator
import os

class BaseData(object):

    def __init__(self, dimension, dtype):
        """
        specify the data type and dimension, calculate the basic information of the spectrum object

        :param dimension: list of int, ordered by [spectrum_size, Bscan_num, Cscan_num, time_points]
        :param dtype: string, select from ('float32', 'double64', 'uint8', 'int8', 'int16', 'uint16', 'int32', etc)
        :return: None
        """
        self.dimension = dimension
        self.dtype = dtype
        self.data = np.array([], dtype=dtype)
        self.dsize = reduce(operator.mul, dimension, 1)

    def load_from_file(self, file, ftype='bin', hdr_size=0):
        if ftype == 'bin':
            with open(file, 'rb') as f:
                f.seek(hdr_size, os.SEEK_SET)
                self.data = np.fromfile(f, dtype=self.dtype, count=self.dsize)
                self.data.shape = self.dimension
        else:
            print('file type not supported:' + ftype)

