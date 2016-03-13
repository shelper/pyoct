# -*- coding: utf-8 -*-

from functools import reduce
import numpy as np
import operator
import os


class BaseData(object):
    """
    Base class for all common data types: spectrum, interferogram, complex and real array, image. etc.

    Attributes:
        data: the array that contains the actual data
        shape: list of int that is the shape of the data array
        dtype: the data type for each element in the data array
        dsize: total number of elements in data array

    """

    def __init__(self, shape, dtype):
        """
        specify the data type and dimension, calculate the basic information of the spectrum object

        Args:
            dimension [int, ]: list of int, which specifies the data as multi dimensional array
            dtype (str): select from ('float32', 'double64', 'uint8', 'int8', 'int16', 'uint16', 'int32', etc)

        Returns:

        """
        self.shape = shape
        self.dtype = dtype
        self.data = np.array([], dtype=dtype)

    def from_file(self, file, hdr_size=0):
        """
        read in data from file

        Args:
            file (str): path to the file that coantains the data, file should be binary
            hdr_size (int): file header size in bytes

        Returns:

        """

        with open(file, 'rb') as f:
            try:
                f.seek(hdr_size, os.SEEK_SET)
                data_size = np.prod(self.shape)
                self.data = np.fromfile(f, dtype=self.dtype, count=data_size)
                if self.data.size != data_size:
                    raise Exception()
                self.data.shape = self.shape
            except:
                print('cannot load data correctly from file, check file existence and file size')


