'''Uses futures and processes to concurentlly grab each flag from list of countries.
Then reports the CPU time, script time, and bytes downloaded.
Created by: Steven Schoebinger 04/14/2021'''
# pylint: disable=invalid-name
# [X] Download all flag files into a local directory named flags
# [X] Report the number of bytes downloaded•
# [X] Report the execution time of the script(using time.perf_counter())•
# [X] Report the CPU time of the script (using time.process_time())
import concurrent.futures
import os
from time import perf_counter, process_time

import requests

img_path = os.path.dirname(__file__) + '/flags/'
txt_path = os.path.dirname(__file__) + '/'

with open(txt_path + 'flags.txt', 'r') as f:
    flags = f.read().splitlines()
flags.pop()


def get_flag(country):
    '''Makes get requests for the flag of the country passed.'''
    flag_name = f'{country}.jpg'
    # headers = {
    #     '''User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36
    #         (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'''}
    image = requests.get(
        'https://www.sciencekids.co.nz/images/pictures/flags96/' + flag_name)
    with open(img_path + flag_name, 'wb+') as img:
        img.write(image.content)
    return int(image.headers['Content-Length'])


def p_pool_exec():
    '''Creates processor pool and maps each country to the get_flag() function.
    Reports CPU time, script time, and bytes downloaded'''
    start = perf_counter()
    cpu_start = process_time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(get_flag, flags)
    #print(type(results))
    sum_bytes = sum(results)
    end = perf_counter()
    cpu_end = process_time()
    print(
        f'Multi-Process elapsed CPU Time: {round(cpu_end-cpu_start, 2)} seconds.')
    print(f'Multi-Process elapsed Time: {round(end-start,2)} seconds.')
    # 405.652 Kbs
    print(f'Amount of bytes downloaded: {round(sum_bytes/1024, 3)} Kbs')


p_pool_exec()
