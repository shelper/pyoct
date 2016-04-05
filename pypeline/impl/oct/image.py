# -*- coding: utf-8 -*-

"""
pypeline.image
~~~~~~~~~~~~~~

this module contains misc to manipulate general images, 8bit, 16bit, 24bit, etc.

set_dimension:
set_voxsize:

display:
    display image, default to adjust the image size based on the vox_size

merge: merge2d: merge3d
    merge different color/measurement channels

project:
    min/max intensity projection, mean projection

segmentation:



"""
from .basedata import BaseData

class Image(BaseData):
    def __init__(self, shape, dtype):
        pass


