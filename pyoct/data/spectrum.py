# -*- coding: utf-8 -*-

"""
pyoct.spectrum
~~~~~~~~~~~~~~

this module defines the spectrum or interferogram in OCT
it should be the subclass of BaseData
"""

from .basedata import BaseData
from scipy import signal


class Spectrum(BaseData):
    """
    spectrum data based off the BaseData class with additional attributes and memeber functions
    Only supports Gaussian shape in k-space spectrum at this moment

    Attributes:
        wc: center wavelength in unit nm
        range: wavelength range from end to end
    """
    def set_range(self, wc, range):
        self.wc, self.range = wc, range

    @property
    def wavelengths(self):
        """
        return the wavelengths at begein, center and end for the spectrum

        Returns:
            [w0, wc, we]: the 3 wavelength at begin, center and end respectively
        """
        return self.wc - self.range/2, self.wc, self.wc + self.range/2

    @property
    def wavenumbers(self):
        """
        return the wavelengths at begein, center and end for the spectrum

        Returns:
            [k0, kc, ke]: the 3 wavenumber at begin, center and end respectively
        """
        k0, ke = 1E7/(w0 + range/2), 1E7/(w0 - range/2)
        kc = (k0 + ke) / 2
        return k0, kc, ke

    def set_profile(self, fwhm):
        """
        set the envelope shapre of the spectrum in wavenumber domain

        Args:
            fwhm (float): the full width half maxium of the spectrum

        Returns:
            None
        """

        self.profile = signal.gaussian(self.dimension[0], self.fwhm/2.235)
        self.data *= self.shape


    def linearize(self, ref, base='wavenumber', method='cubic'):
        pass







