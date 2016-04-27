# -*- coding: utf-8 -*-

import asyncio
import collections


class Pipeline(object):
    """
    pipeline to connect settings for streamline data processing.
    Example:
        p = PipeLine([list of functions])
        p.process(data_in)
        p.close() to close the pipeline
    """

    def __init__(self):
        pass

    def build(self, func_list):
        """

        Args:
            func_list (list): a list of function to run through pipeline
        """
        self.func_list = func_list
        self.func_names = [func.__name__ for func in self.func_list]
        self.pipeline = connect(self.func_list)
        self.run_event = asyncio.get_event_loop()


    def insert(self, position, func):
        """

        Args:
            position (int): the position to inser the function into the pipeline
            func (function/list of function): function to be inserted in to the pipeline
        """
        if isinstance(func, list):
            for f in func:
                self.func_list.insert(position, pipenize(f))
                self.func_names.insert(position, f.__name__)
        elif callable(func):
            self.func_list.insert(position, pipenize(func))
            self.func_names.insert(position, func.__name__)
        self.pipeline = connect(self.func_list)

    def pop_by_name(self, func_name):
        """

        Args:
            func_name (str): name of function to be popped out of the pipeline
        """
        if callable(func_name):
            func_name = func_name.__name__
            idx = self.func_names.index(func_name)
        self.func_list.pop(idx)
        self.func_names.pop(idx)
        self.pipeline = connect(self.func_list)

    def pop_by_idx(self, idx):
        """

        Args:
            func_idx (int): index of function to be popped out of the pipeline
                this is useful when there are functions with same name but idx will be different
        """
        self.func_list.pop(idx)
        self.func_names.pop(idx)
        self.pipeline = connect(self.func_list)

    def swap_by_name(self, func1_name, func2_name):
        """
        Args:
            func1_name: the first name of the function to be swapped
            func2_name: the second name of the function to be swapped
        """
        # TODO: swap two functions in the pipeline by name
        pass

    def swap_by_idx(self, idx1, idx2):
        """
        Args:
            idx1: the first index of the function to be swapped
            idx2: the second index of the function to be swapped
        """
        # TODO: swap two functions in the pipeline by index
        pass

    def process(self, data_in):
        """
        process data or iterable data_source, then yield the result

        Args:
            data_in: input data of the pipeline, this can be data or iterable data source
        """
        print(data_in)
        if isinstance(data_in, collections.Iterable):
            for d in data_in:
                yield self.run_event.run_until_complete(self.pipeline(d))

        else:
            yield self.run_event.run_until_complete(self.pipeline(data_in))

        self.close()

    def close(self):
        """
        close pipeline, stop yielding results, close the async threads
        """
        self.run_event.close()
