# -*- coding: utf-8 -*-

# import pytest

from .. import pyoct


def test_read_rawdata():
    rawdata = pyoct.data.spectrum.Spectrum([1024, 512], 'int16')
    rawdata.load_from_file('')

def test_PipeLine():
    pyoct.proc.pipeline.
