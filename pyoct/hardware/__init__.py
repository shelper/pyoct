# -*- coding: utf-8 -*-

"""
pyoct.hardware
~~~~~~~~

This module contains pyoct hardware controllers:
scanner:
    trigger, pulse, step_ang, step, range_ang, range
    the scanner controller defines the voltage to drive the scanner, this can be
    a 1d, 2d or 3d array that covers B-scan, C-scan and Z-scan,
acquisition:
    from_file, from_camera, from_daq
    trigger, pulse, bit_depth, quant_eff,
modulator:
    mod_phase, mod_pol, mod_

"""
