# -*- coding: utf-8 -*-

"""
pypeline.core
~~~~~~~~~~~~~

this module contains all the processing method, and advanced algorithms for OCT signal processing

calibrate:

disp_comp:

sp2struct:
    @phase, @intensity, @complex

despeckle: (2D, 3D, etc.)

angiograph: (2D, 3D, etc.)
    @speckle_var, @

"""

# register/load all the functions in the settings folder, so can be found and called to form pipeline
# use watchdog to monitor the content change in the settings folder
__all__ = ['pipeline', 'funcwrap', 'argswrap']

