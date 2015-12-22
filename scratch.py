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
    return x**y


def connect(next_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            data_out = yield from func(*args, **kw)
            result = yield from next_func(data_out)
            return result
        return wrapper
    return decorator


funcs = [functools.partial(add, 1),
         functools.partial(prod, 2),
         functools.partial(power, 3)]

pipeline = funcs[-1]
for i, func in enumerate(reversed(funcs[:-1])):
    pipeline = connect(pipeline)(func)

# while True:
for i in range(20):
    result = asyncio.get_event_loop().run_until_complete(pipeline(i))
    print(result)
