# TODO Need to figure out how to properly report bytes downloaded
import os
import requests
from time import perf_counter
from time import process_time
import concurrent.futures

img_path = os.path.dirname(__file__) + '/flags/'
txt_path = os.path.dirname(__file__) + '/'

with open(txt_path + 'flags.txt', 'r') as f:
    flags = f.read().splitlines()

def get_flag(country):
    flag_name = country+ '.jpg'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}
    image = requests.get('https://www.sciencekids.co.nz/images/pictures/flags96/' + flag_name,headers=headers)
    print(len(image.content))
    open(img_path + flag_name, 'wb+').write(image.content)


def t_pool_submit():
    start = perf_counter()
    cpu_start = process_time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = executor.map(get_flag, flags)
    cpu_end = process_time()
    end = perf_counter()
    print(f'Elapsed CPU Time: {round(cpu_end-cpu_start, 2)} seconds.')
    print(f'Elapsed Time: {round(end-start,2)} seconds.')

t_pool_submit()