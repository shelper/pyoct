# -*- coding: utf-8 -*-

"""
pypeline

the package serves as a toolset for acquiring and processing OCT data
processing and analyzing OCT images, and provides wrappers for OCT impl control

the package tends to use a pipes design to provide a flexible and extensible
way to build customized tools

example1: build a processing pipes to read in raw interferogram data and reconstruct the OCT image
    -> impl initialzation: pypeline.impl.acquisition.init()
    -> acquire data: pypeline.data = pypeline.impl.acquisition.from_file(file_name, data_descriptor)
    -> reconstruct image: pypeline.image = pypeline.core.sp2struct(pypeline.data)
    -> process image: pypeline.core.segmentation(pypeline.image)


"""
__version__ = '1.0.0'
__all__ = ['data', 'core', 'impl', 'tools']

from .data import *

from .core import *

from .impl import *

from .tools import *
