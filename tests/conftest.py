# -*- coding: utf-8 -*-

# below imports enables python 2 and 3 compatible codes
# requires python-future, install by `pip install future`
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import pytest
import os

# _test_data_dir = '/'.join((os.path.dirname(__file__), 'foo_data'))
#
# @pytest.fixture(autouse=True)
# def test_global_vars(request):
#     request.function.__globals__['raw_data_uint16'] = '/'.join((_test_data_dir, 'slope_uint16.raw'))
#     request.function.__globals__['raw_data_double'] = '/'.join((_test_data_dir, 'slope_double.raw'))
