# -*- coding: utf-8 -*-

from functools import reduce
import numpy as np
import operator
import os


class BaseData(object):
    """
    BaseData as the base class for all common data types: spectrum, interferogram, complex and real array, image. etc.

    Attributes:
        data: the array that contains the actual data
        dimension: list of int that is the shape of the data array
        dtype: the data type for each element in the data array
        dsize: total number of elements in data array

    """

    def __init__(self, dimension, dtype):
        """
        specify the data type and dimension, calculate the basic information of the spectrum object

        Args:
            dimension [int, ]: list of int, which specifies the data as multi dimensional array
            dtype (str): select from ('float32', 'double64', 'uint8', 'int8', 'int16', 'uint16', 'int32', etc)

        Returns:

        """
        self.dimension = dimension
        self.dtype = dtype
        self.dsize = reduce(operator.mul, self.dimension, 1)
        self.data = np.array([], dtype=dtype)

    def from_file(self, file, hdr_size=0):
        """
        read in data from file

        Args:
            file (str): path to the file that coantains the data
            hdr_size (int): file header size in bytes

        Returns:

        """

        with open(file, 'rb') as f:
            try:
                f.seek(hdr_size, os.SEEK_SET)
                self.data = np.fromfile(f, dtype=self.dtype, count=self.dsize)
                if data.size == self.dsize:
                    self.data.shape = self.dimension
                else:
                    raise OSError
            except OSError as e:
                print('cannot load data from file, check file existence and file size')


