# -*- coding: utf-8 -*-

"""
pyoct.spectrum
~~~~~~~~~~~~~~

this module defines the spectrum or interferogram in OCT
it should be the subclass of BaseData
"""

from.basedata import BaseData

class Spectrum(BaseData):
    def __init__(self):
        pass

    def linearize(self, ref, base='wavenumber', method='cubic'):
        pass







