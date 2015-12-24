import functools
import asyncio


@asyncio.coroutine
def add(x, y):
    return x + y


@asyncio.coroutine
def prod(x, y):
    return x * y


@asyncio.coroutine
def power(x, y):
    return x ** y


funcs = [functools.partial(add,
                           y=1), functools.partial(prod,
                                                   y=2),
         functools.partial(power,
                           y=3)]


def connect(pipeline):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            data_out = yield from pipeline(*args, **kw)
            result = yield from func(data_out)
            return result

        return wrapper

    return decorator


pipeline = funcs[0]
for func in funcs[1:]:
    pipeline = connect(pipeline)(func)

for i in range(20):
    data_in = i
    print(asyncio.get_event_loop().run_until_complete(pipeline(data_in)))


def connect(pipeline, func):
    def wrapper(*args, **kwargs):
        data_out = yield from pipeline(*args, **kwargs)
        result = yield from func(data_out)
        return result

    return wrapper


pipeline = funcs[0]
for func in funcs[1:]:
    pipeline = connect(pipeline, func)

for i in range(20):
    data_in = i
    print(asyncio.get_event_loop().run_until_complete(pipeline(data_in)))


@asyncio.coroutine
def sub(x, y):
    return x - y


def insert_pipe(pipeline, func, idx):
    pass


def connect(funcs):
    def wrapper(*args, **kwargs):
        data_out = yield from funcs[0](*args, **kwargs)
        for func in funcs[1:]:
            data_out = yield from func(data_out)
        return data_out

    return wrapper


pipeline = connect(funcs)
for i in range(20):
    data_in = i
    print(asyncio.get_event_loop().run_until_complete(pipeline(data_in)))
