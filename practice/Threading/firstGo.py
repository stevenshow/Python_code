import concurrent.futures
import threading
import time


def tester(seconds):
    print(f'Sleeping for {seconds} second(s) . . .')
    time.sleep(seconds)
    return f'Done sleeping for {seconds} second(s)'


def t_pool_map():
    '''Maps each function and prints them based on submission order'''
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = executor.map(tester, secs)

    for result in results:
        print(result)

    end = time.perf_counter()

    print(f'That took {round(end-start, 2)} second(s) to complete.')


def t_pool_submit():
    '''Manual submission, with the printing being done upon who completed first'''
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        results = [executor.submit(tester, sec) for sec in secs]

    for f in concurrent.futures.as_completed(results):
        print(f.result())

    end = time.perf_counter()

    print(f'That took {round(end-start, 2)} second(s) to complete.')


t_pool_submit()