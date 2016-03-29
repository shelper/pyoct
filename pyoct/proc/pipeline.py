# -*- coding: utf-8 -*-

import asyncio
import collections
import functools
from importlib import import_module


# import os
# from ..data.basedata import BaseData


def connect(func_list):
    """
    connects the functions in the list to form an async pipeline

    Args:
        func_list (list): list of functions in the folder ./pipes
    """

    def wrapper(*args, **kwargs):
        for i, func in enumerate(func_list):
            data_in = args[0] if i == 0 else data_out
            data_out = yield from func(data_in, *args[1:], **kwargs)
        return data_out

    return wrapper


def pipenize(func):
    if callable(func):
        return asyncio.coroutine(func)
    elif isinstance(func, str):
        return load_func(func)


def load_func(func_name):
    """
    load function configurations file from the ./pipes/configurations folder

    Args:
        func_name (function): name of the function to be loaded from 'func_name.py' in folder ./pipes
    """
    base_func = import_module('.'.join(('pipes', func_name, func_name)))
    func_cfg = load_func_cfg(func_name)
    func = functools.partial(base_func, **func_cfg)
    return asyncio.coroutine(func)


def load_func_cfg(func_name):
    try:
        cfg_file = '.'.join((func_name, 'cfg'))
        cfg_file = '/'.join(('pipes', 'configuration', cfg_file))
        with open(cfg_file, 'r') as f:
            # TODO: load func_name.cfg in ./pipes/configurations
            pass
        func_cfg = {}
    except FileExistsError:
        func_cfg = {}

    return func_cfg


def check_data_in(func):
    """
    check if the input data matches the input requirements, the requirements are defined in
        the configuration file loaded by load_cfg(func)

    Args:
        func (function): function that will process the input data
    """

    def wrapper(*args, **kwargs):
        # TODO: check the input data matches the required format
        data_out = func(*args, **kwargs)
        return data_out

    return wrapper


class Pipeline(object):
    """
    pipeline to connect pipes for streamline data processing.
    example of usage:
        p = PipeLine([list of functions])
        p.process(data_in)
        p.close() to close the pipeline
    """

    def __init__(self, func_list=[]):
        """

        Args:
            func_list (list): a list of function to run through pipeline,
        """
        if isinstance(func_list, list) and func_list:
            self.func_list = [pipenize(f) for f in func_list]
            self.func_names = [func.__name__ for func in self.func_list]
            self.pipeline = connect(self.func_list)
        else:
            self.pipeline = None
        self.run_event = asyncio.get_event_loop()

    def insert(self, position, func):
        """

        Args:
            position (int): the position to inser the function
            func (function/list of function): function to be inserted in to the pipeline
        """
        if isinstance(func, list):
            for f in func:
                self.func_list.insert(position, asyncio.coroutine(f))
                self.func_names.insert(position, f.__name__)
        elif callable(func):
            self.func_list.insert(position, asyncio.coroutine(func))
            self.func_names.insert(position, func.__name__)
        self.pipeline = connect(self.func_list)

    def pop_by_name(self, func_name):
        """

        Args:
            func_name [str]: name of function to be popped out of the pipeline
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
            func_idx [int]: index of function to be popped out of the pipeline
                this is useful when there are functions with same name
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
        process data or iterable data_source, then yield the results

        Args:
            data_in : input data of the pipeline, this can be data or iterable data source
        """
        if isinstance(data_in, collections.Iterable):
            for d in data_in:
                yield self.run_event.run_until_complete(self.pipeline(d))

        else:
            yield self.run_event.run_until_complete(self.pipeline(data_in))

    def close(self):
        """
        close pipeline, stop yielding results
        """
        self.run_event.close()
