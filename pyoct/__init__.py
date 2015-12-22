# -*- coding: utf-8 -*-

"""
pyoct
~~~

the package serves as a toolset for acquiring and processing OCT data
processing and analyzing OCT images, and provides wrappers for OCT hardware control

the package tends to use a pipes design to provide a flexible and extensible
way to build customized tools

example1: build a processing pipes to read in raw interferogram data and reconstruct the OCT image
    -> hardware initialzation: pyoct.hardware.acquisition.init()
    -> acquire data: pyoct.data = pyoct.hardware.acquisition.from_file(file_name, data_descriptor)
    -> reconstruct image: pyoct.image = pyoct.proc.sp2struct(pyoct.data)
    -> process image: pyoct.proc.segmentation(pyoct.image)


"""

from .data import *

from .proc import *

