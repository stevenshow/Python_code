import concurrent.futures
import threading
import time

times = [1,2,3,4,5]
def test_func():
    print('You made it to the function')

with concurrent.futures.ThreadPoolExecutor(max_workers=min(10, len(times))) as executor:
    results = executor.map(test_func, times)
