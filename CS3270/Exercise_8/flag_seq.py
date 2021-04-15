'''Sequentially goes to website and downloads each flag based on the country name in
list of countries provided.  Reports CPU time, script time, and bytes downloaded
Created by: Steven Schoebinger 04/14/2021'''
#pylint: disable=invalid-name
# [X] Download all flag files into a local directory named flags
# [X] Report the number of bytes downloaded•
# [X] Report the execution time of the script(using time.perf_counter())•
# [X] Report the CPU time of the script (using time.process_time())

import os
from time import perf_counter, process_time

import requests

img_path = os.path.dirname(__file__) + '/flags/'
txt_path = os.path.dirname(__file__) + '/'

# Populate flags list with all flag names
with open(txt_path + 'flags.txt', 'r') as f:
    flags = f.read().splitlines()
flags.pop()


def get_flags():
    '''Processes each country name in list and requests that jpg from site sequentially.'''
    start = perf_counter()
    cpu_start = process_time()
    sum_filesizes = 0
    for country in flags:
        flag_name = country + '.jpg'
        # headers = {
        #     '''User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36\
        #         (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'''}
        image = requests.get(
            'https://www.sciencekids.co.nz/images/pictures/flags96/' + flag_name)
        #print(image.headers['Content-Length'])
        sum_filesizes += int(image.headers["Content-Length"])
        open(img_path + flag_name, 'wb+').write(image.content)
    end = perf_counter()
    cpu_end = process_time()
    print(
        f'Sequential elapsed CPU Time: {round(cpu_end-cpu_start, 2)} seconds.')
    print(f'Sequential elapsed Script Time: {round(end-start,2)} seconds.')
    # 405.652 Kbs
    print(f'Amount of bytes downloaded: {round(sum_filesizes/1024, 3)} Kbs')


get_flags()
