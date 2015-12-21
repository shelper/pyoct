# -*- coding: utf-8 -*-

from functools import wraps
import os

from ..data.basedata import BaseData

class PipeLine(object):
    """
    pipeline to connect pipes for streamline data processing.

    example of usage:
    p = PipeLine(functions)
    p.setup_input(input_data)
    p.output2file(output_file)
    p.start()



    """

    def __init__(self, funcs, set_async=True):
        if set_async:
            for func in funcs:

        self.pipes = funcs

    def insert_pipe(self, pipe, position):
        pass

    def pop_pipe(self, position):
        pass

    def get_pipe_list(self):
        pass

    def setup_input(self, input, dimension, dtype):
        if os.path.isfile(input):
            self.input =

        pass

    def start(self):
        # confirm the previous pipe output matches following pipe input format
        pass

class Pipe(object):

    def __init__(self, func):
        self.func =
        pass

