"""
Demonstration of the asyncio module in Python 3.5

This simulation is composed of three layers, each of which will split up the
data into some different subsets, pass the subsets off to the next layer, wait
for results, and then do some non-trivial processing to return to the previous
layer (in this case, sleeping for a few seconds). The expensive operations are
offloaded to a ThreadPoolExecutor, which maintains a pool of processing
threads, allowing for the utilization of multiple cores (hypothetically).
"""
import asyncio
import logging
import time
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(format="[%(thread)-5d]%(asctime)s: %(message)s")
logger = logging.getLogger('async')
logger.setLevel(logging.INFO)

executor = ThreadPoolExecutor(max_workers=10)
loop = asyncio.get_event_loop()

def cpu_bound_op(exec_time, *data):
    """
    Simulation of a long-running CPU-bound operation
    :param exec_time: how long this operation will take
    :param data: data to "process" (sum it up)
    :return: the processed result
    """
    logger.info("Running cpu-bound op on {} for {} seconds".format(data, exec_time))
    time.sleep(exec_time)
    return sum(data)

@asyncio.coroutine
def process_pipeline(data):
    # just pass the data along to level_a and return the results
    results = yield from level_a(data)
    return results

@asyncio.coroutine
def level_a(data):
    # tweak the data a few different ways and pass them each to level b.
    level_b_inputs = data, 2*data, 3*data
    results = yield from asyncio.gather(*[level_b(val) for val in level_b_inputs])
    # we've now effectively called level_b(...) three times with three inputs,
    # and (once the yield from returns) they've all finished, so now we'll take
    # the results and pass them along to our own long-running CPU-bound
    # process via the thread pool.
    # Note the signature of run_in_executor: (executor, func, *args)
    # The third argument and beyond will be passed to cpu_bound_op when it is called.
    print(results)
    result = yield from loop.run_in_executor(executor, cpu_bound_op, 3, *results)
    # level_a processing is now done, pass back the results
    return result

@asyncio.coroutine
def level_b(data):
    # similar to level a
    level_c_inputs = data/2, data/4, data/7
    results = yield from asyncio.gather(*[level_c(val) for val in level_c_inputs])
    print(results)
    result = yield from loop.run_in_executor(executor, cpu_bound_op, 2, *results)
    return result

@asyncio.coroutine
def level_c(data):
    # final level - queue up the long-running CPU-bound process in the
    # thread pool immediately
    result = yield from loop.run_in_executor(executor, cpu_bound_op, 1, data)
    print(result)
    return result

def main():
    start_time = time.time()
    result = loop.run_until_complete(process_pipeline(2.5))
    logger.info("Completed ({}) in {} seconds".format(result, time.time() - start_time))

if __name__ == '__main__':
    main()
