# -*- coding: utf-8 -*-

import asyncio
import os
import functools

from ..data.basedata import BaseData

# def pipehead(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         yield func(*args, **kwargs)
#     return wrapper


def piperize(prev_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            input =  yield from prev_func
            return func(input)
        return wrapper
    return decorator


class PipeLine(object):
    """
    pipeline to connect pipes for streamline data processing.

    example of usage:
    p = PipeLine(functions)
    p.setup_input(input_data)
    p.output2file(output_file)
    p.start()

    """

    def __init__(self, funcs=[], data_in=None):
        self.data_in = data_in
        # self.funcs = funcs
        self.pipe_num = len(funcs)
        self.pipes = []
        if len(funcs) >= 2:
            for i, func in reversed(funcs)[:-1]:
                prev_func = funcs[self.pipe_num - (i + 2)]
                self.pipes.append(piperize(prev_func)(func))
            self.pipes.append(asyncio.coroutine(func))
        self.

    def insert_pipe(self, func, position):
        pass

    def pop_pipe(self, position):
        pass

    def get_pipe_list(self):
        pass

    def setup_input(self, input, dimension, dtype):
        if os.path.isfile(input):
            self.input = BaseData([1024, 512]).load_from_file('~/develop/pyoct/foo/foodata.raw')
        pass

    def start(self):
        # confirm the previous pipe output matches following pipe input format
        pass


