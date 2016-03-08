# -*- coding: utf-8 -*-

"""
pyoct
~~~

the package serves as a toolset for acquiring and processing OCT data
processing and analyzing OCT images, and provides wrappers for OCT system control

the package tends to use a pipes design to provide a flexible and extensible
way to build customized tools

example1: build a processing pipes to read in raw interferogram data and reconstruct the OCT image
    -> system initialzation: pyoct.system.acquisition.init()
    -> acquire data: pyoct.data = pyoct.system.acquisition.from_file(file_name, data_descriptor)
    -> reconstruct image: pyoct.image = pyoct.proc.sp2struct(pyoct.data)
    -> process image: pyoct.proc.segmentation(pyoct.image)


"""
__version__ = 1.0.0
__all__ = ['data', 'proc', 'system', 'tools']

from .data import *

from .proc import *

from .system import *

from .tools import *
