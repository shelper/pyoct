# -*- coding: utf-8 -*-

import asyncio
import os

from ..data.basedata import BaseData


class PipeLine(object):
    """
    pipeline to connect pipes for streamline data processing.

    example of usage:
    p = PipeLine(functions)
    p.feed_data(data)
    p.run()

    """

    def __init__(self, funcs=[], data=None):
        self.data_in = data
        self.data_out = None
        self.pipes = [asyncio.coroutine(func) for func in funcs]
        self.pipeline = self.build()
        self.loop = asyncio.get_event_loop()
        # self.pipe_num = len(funcs)

    def build(self):
        def wrapper(*args, **kwargs):
            data_out = yield from self.pipes[0](*args, **kwargs)
            for pipe in self.pipes[1:]:
                data_out = yield from pipe(data_out)
            return data_out
        return wrapper

    def insert_pipe(self, position, func):
        self.pipes.insert(position, asyncio.coroutine(func))
        self.pipeline = self.build()

    def pop_by_name(self, func_name):
        if callable(func_name):
            position = self.pipes.index(func_name)

        self.pipes.pop(position)
        self.pipeline = self.build()

    def pop_by_idx(self, position):
        self.pipes.pop(position)
        self.pipeline = self.build()

    def feed_data(self, data, dimension=None, dtype=None):
        if os.path.isfile(data):
            self.data_in = BaseData(dimension, dtype).load_from_file(data)
        else:
            # TODO add other data handling for :numpy array, and string block
            self.data_in = data

    def run(self):
        self.data_out = self.loop.run_until_complete(self.pipeline(self.data_in))


